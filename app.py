from services.book_service import add_book
from services.member_service import add_member
from services.transaction_service import borrow_book, return_book, generate_report, display_today_transactions

def show_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Generate Report")
    print("6. Display Today's Transactions")
    print("7. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)
        
        elif choice == '2':
            name = input("Enter member name: ")
            dob = input("Enter member date of birth (YYYY-MM-DD): ")
            address = input("Enter member address: ")
            add_member(name, dob, address)
        
        elif choice == '3':
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
            borrow_book(member_id, book_id, borrow_date)
        
        elif choice == '4':
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            return_book(member_id, book_id)
        
        elif choice == '5':
            generate_report()
        
        elif choice == '6':
            display_today_transactions()
        
        elif choice == '7':
            print("Exiting the Library Management System. Goodbye!")
            break
        
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
