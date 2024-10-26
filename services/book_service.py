from database import connect_to_database

def add_book(title, author):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "INSERT INTO books (title, author) VALUES (%s, %s)"
    cursor.execute(query, (title, author))
    connection.commit()
    cursor.close()
    connection.close()
    print("Book added successfully")
