from flask import Flask, jsonify, request, render_template
from services.book_service import add_book
from services.member_service import add_member
from services.transaction_service import borrow_book, return_book, generate_report, display_today_transactions
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Route này sẽ hiển thị trang index.html
    return render_template('index.html')

@app.route('/api/add_book', methods=['POST'])
def api_add_book():
    data = request.json
    title = data.get('title')
    author = data.get('author')
    add_book(title, author)
    return jsonify({"message": "Book added successfully"})

@app.route('/api/add_member', methods=['POST'])
def api_add_member():
    data = request.json
    name = data.get('name')
    dob = data.get('dob')
    address = data.get('address')
    add_member(name, dob, address)
    return jsonify({"message": "Member added successfully"})

@app.route('/api/borrow_book', methods=['POST'])
def api_borrow_book():
    data = request.json
    member_id = data.get('member_id')
    book_id = data.get('book_id')
    borrow_date = data.get('borrow_date')
    borrow_book(member_id, book_id, borrow_date)
    return jsonify({"message": "Book borrowed successfully"})

@app.route('/api/return_book', methods=['POST'])
def api_return_book():
    data = request.json
    member_id = data.get('member_id')
    book_id = data.get('book_id')
    return_book(member_id, book_id)
    return jsonify({"message": "Book returned successfully"})

@app.route('/api/today_transactions', methods=['GET'])
def api_today_transactions():
    today_transactions = display_today_transactions()
    return jsonify(today_transactions)

if __name__ == '__main__':
    app.run(debug=True)
