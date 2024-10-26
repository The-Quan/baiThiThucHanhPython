async function fetchTodayTransactions() {
    try {
        const response = await fetch('/api/today_transactions');
        const transactions = await response.json();

        const tableBody = document.getElementById('transactions-table');
        tableBody.innerHTML = '';  // Xóa nội dung cũ nếu có

        transactions.forEach(transaction => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${transaction.id}</td>
                <td>${transaction.member_id}</td>
                <td>${transaction.book_id}</td>
                <td>${transaction.borrow_date}</td>
                <td>${transaction.status}</td>
            `;
            tableBody.appendChild(row);
        });
    } catch (error) {
        console.error('Error fetching transactions:', error);
    }
}

// Hàm thêm sách
async function addBook() {
    const title = document.getElementById('book-title').value;
    const author = document.getElementById('book-author').value;

    try {
        const response = await fetch('/api/add_book', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, author })
        });
        const result = await response.json();
        alert(result.message);
    } catch (error) {
        console.error('Error adding book:', error);
    }
}

// Hàm thêm thành viên
async function addMember() {
    const name = document.getElementById('member-name').value;
    const dob = document.getElementById('member-dob').value;
    const address = document.getElementById('member-address').value;

    try {
        const response = await fetch('/api/add_member', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, dob, address })
        });
        const result = await response.json();
        alert(result.message);
    } catch (error) {
        console.error('Error adding member:', error);
    }
}

// Hàm mượn sách
async function borrowBook() {
    const member_id = document.getElementById('borrow-member-id').value;
    const book_id = document.getElementById('borrow-book-id').value;
    const borrow_date = document.getElementById('borrow-date').value;

    try {
        const response = await fetch('/api/borrow_book', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ member_id, book_id, borrow_date })
        });
        const result = await response.json();
        fetchTodayTransactions()
        alert(result.message);
    } catch (error) {
        console.error('Error borrowing book:', error);
    }
}

// Hàm trả sách
async function returnBook() {
    const member_id = document.getElementById('return-member-id').value;
    const book_id = document.getElementById('return-book-id').value;

    try {
        const response = await fetch('/api/return_book', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ member_id, book_id })
        });
        const result = await response.json();
        alert(result.message);
    } catch (error) {
        console.error('Error returning book:', error);
    }
}

// Tự động gọi khi tải trang
window.onload = fetchTodayTransactions;
