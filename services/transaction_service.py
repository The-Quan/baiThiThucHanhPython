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
    cursor = connection.cursor()
    
    query = """
    SELECT * FROM borrow_transactions
    WHERE borrow_date = %s 
    """
    cursor.execute(query, (today,))
    transactions = cursor.fetchall()
    
    print("Today's Transactions (Borrowed or Returned):")
    for transaction in transactions:
        print(transaction)
    
    cursor.close()
    connection.close()

