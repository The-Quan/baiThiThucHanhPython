from database import connect_to_database

def add_member(name, dob, address):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "INSERT INTO members (name, dob, address) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, dob, address))
    connection.commit()
    cursor.close()
    connection.close()
    print("Member added successfully")
