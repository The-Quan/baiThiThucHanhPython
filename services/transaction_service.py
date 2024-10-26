from database import connect_to_database

def borrow_book(member_id, book_id, borrow_date):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "INSERT INTO borrow_transactions (member_id, book_id, borrow_date, status) VALUES (%s, %s, %s, 'Borrowed')"
    cursor.execute(query, (member_id, book_id, borrow_date))
    connection.commit()
    cursor.close()
    connection.close()
    print("Book borrowed successfully")

def return_book(member_id, book_id):
    connection = connect_to_database()
    cursor = connection.cursor()

    update_query = """
    UPDATE borrow_transactions
    SET status = 'Returned'
    WHERE member_id = %s AND book_id = %s AND status = 'Borrowed'
    """
    cursor.execute(update_query, (member_id, book_id))
    connection.commit()
    print("Book returned successfully")
    
    cursor.close()
    connection.close()

def generate_report():
    connection = connect_to_database()
    cursor = connection.cursor()
    query = """
    SELECT m.id, m.name, m.dob, m.address, b.title, bt.borrow_date, bt.status
    FROM borrow_transactions bt
    JOIN members m ON bt.member_id = m.id
    JOIN books b ON bt.book_id = b.id
    """
    cursor.execute(query)
    transactions = cursor.fetchall()
    print("Report:")
    print("ID | Member Name | DOB       | Address | Book Title    | Borrow Date | Status")
    for i, row in enumerate(transactions, start=1):
        print(f"{i} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]}")
    cursor.close()
    connection.close()

def display_today_transactions():
    from datetime import date
    today = date.today().strftime('%Y-%m-%d')
    connection = connect_to_database()
    transactions_list = []
    try:
        cursor = connection.cursor()
        query = """
        SELECT id, member_id, book_id, borrow_date, status
        FROM borrow_transactions
        WHERE borrow_date = %s AND (status = 'Borrowed' OR status = 'Returned')
        """
        cursor.execute(query, (today,))
        transactions = cursor.fetchall()
        
        for transaction in transactions:
            transactions_list.append({
                "id": transaction[0],
                "member_id": transaction[1],
                "book_id": transaction[2],
                "borrow_date": transaction[3].strftime('%Y-%m-%d'),
                "status": transaction[4]
            })
    except Exception as e:
        print(f"Error displaying today's transactions: {e}")
    finally:
        cursor.close()
        connection.close()
    return transactions_list


