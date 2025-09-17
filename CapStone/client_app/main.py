from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# API base URL
API_BASE_URL = "http://localhost:8000"

@app.route('/')
def index():
    """Main dashboard page."""
    return render_template('index.html')

@app.route('/books')
def books():
    """Books management page."""
    try:
        response = requests.get(f"{API_BASE_URL}/books")
        books_data = response.json()
        return render_template('books.html', books=books_data)
    except Exception as e:
        return render_template('books.html', books=[], error=str(e))

@app.route('/books/add', methods=['GET', 'POST'])
def add_book():
    """Add a new book."""
    if request.method == 'POST':
        try:
            book_data = {
                'title': request.form['title'],
                'author': request.form['author'],
                'isbn': request.form['isbn'],
                'publication_year': int(request.form['publication_year']),
                'genre': request.form['genre'],
                'total_copies': int(request.form['total_copies']),
                'available_copies': int(request.form['available_copies'])
            }
            
            response = requests.post(f"{API_BASE_URL}/books", json=book_data)
            if response.status_code == 201:
                return redirect(url_for('books'))
            else:
                return render_template('add_book.html', error=response.json().get('detail', 'Error adding book'))
        except Exception as e:
            return render_template('add_book.html', error=str(e))
    
    return render_template('add_book.html')

@app.route('/members')
def members():
    """Members management page."""
    try:
        response = requests.get(f"{API_BASE_URL}/members/with-borrowed-counts/")
        members_data = response.json()
        return render_template('members.html', members=members_data)
    except Exception as e:
        return render_template('members.html', members=[], error=str(e))

@app.route('/members/add', methods=['GET', 'POST'])
def add_member():
    """Add a new member."""
    if request.method == 'POST':
        try:
            member_data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'phone': request.form['phone'] if request.form['phone'] else None,
                'max_books_allowed': int(request.form['max_books_allowed'])
            }
            
            response = requests.post(f"{API_BASE_URL}/members", json=member_data)
            if response.status_code == 201:
                return redirect(url_for('members'))
            else:
                return render_template('add_member.html', error=response.json().get('detail', 'Error adding member'))
        except Exception as e:
            return render_template('add_member.html', error=str(e))
    
    return render_template('add_member.html')

@app.route('/transactions')
def transactions():
    """Transactions management page."""
    try:
        response = requests.get(f"{API_BASE_URL}/transactions")
        transactions_data = response.json()
        return render_template('transactions.html', transactions=transactions_data)
    except Exception as e:
        return render_template('transactions.html', transactions=[], error=str(e))

@app.route('/transactions/checkout', methods=['GET', 'POST'])
def checkout_book():
    """Checkout a book."""
    if request.method == 'POST':
        try:
            checkout_data = {
                'book_id': request.form['book_id'],
                'member_id': request.form['member_id']
            }
            
            response = requests.post(f"{API_BASE_URL}/transactions/checkout", json=checkout_data)
            if response.status_code == 201:
                return redirect(url_for('transactions'))
            else:
                return render_template('checkout.html', error=response.json().get('detail', 'Error checking out book'))
        except Exception as e:
            return render_template('checkout.html', error=str(e))
    
    # Get books and members for the form
    try:
        books_response = requests.get(f"{API_BASE_URL}/books")
        members_response = requests.get(f"{API_BASE_URL}/members")
        
        books = books_response.json()
        members = members_response.json()
        
        return render_template('checkout.html', books=books, members=members)
    except Exception as e:
        return render_template('checkout.html', books=[], members=[], error=str(e))

@app.route('/transactions/return', methods=['GET', 'POST'])
def return_book():
    """Return a book."""
    if request.method == 'POST':
        try:
            return_data = {
                'book_id': request.form['book_id'],
                'member_id': request.form['member_id']
            }
            
            response = requests.post(f"{API_BASE_URL}/transactions/return", json=return_data)
            if response.status_code == 200:
                return redirect(url_for('transactions'))
            else:
                return render_template('return.html', error=response.json().get('detail', 'Error returning book'))
        except Exception as e:
            return render_template('return.html', error=str(e))
    
    # Get active transactions for the form
    try:
        transactions_response = requests.get(f"{API_BASE_URL}/transactions?status=active")
        transactions = transactions_response.json()
        
        return render_template('return.html', transactions=transactions)
    except Exception as e:
        return render_template('return.html', transactions=[], error=str(e))

@app.route('/api/books')
def api_books():
    """API endpoint to get books."""
    try:
        response = requests.get(f"{API_BASE_URL}/books")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/members')
def api_members():
    """API endpoint to get members."""
    try:
        response = requests.get(f"{API_BASE_URL}/members")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/members/<member_id>/borrowed-books')
def member_borrowed_books(member_id):
    """Display borrowed books for a specific member."""
    try:
        # Get member details
        member_response = requests.get(f"{API_BASE_URL}/members/{member_id}")
        if member_response.status_code != 200:
            return render_template('error.html', error="Member not found")
        
        member = member_response.json()
        
        # Get borrowed books
        books_response = requests.get(f"{API_BASE_URL}/members/{member_id}/borrowed-books")
        if books_response.status_code == 200:
            borrowed_books = books_response.json()
        else:
            borrowed_books = []
        
        return render_template('member_borrowed_books.html', member=member, borrowed_books=borrowed_books)
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/api/transactions')
def api_transactions():
    """API endpoint to get transactions."""
    try:
        response = requests.get(f"{API_BASE_URL}/transactions")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting Library Management Client...")
    print("Make sure the FastAPI server is running on http://localhost:8000")
    print("Access the client at http://localhost:5000")
    app.run(debug=True, port=5000)
