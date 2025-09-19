# Library Management System - Client Application

This is a Flask-based web client for the Library Management System API.

## Setup

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the FastAPI Server:**
   Make sure the FastAPI server is running on `http://localhost:8000`
   ```bash
   # From the api_server directory
   cd ../api_server
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Start the Client Application:**
   ```bash
   # From the client_app directory
   python main.py
   ```

4. **Access the Application:**
   - Client: http://localhost:5000
   - API Documentation: http://localhost:8000/docs

## Features

- **Dashboard**: Overview of library statistics
- **Books Management**: View, add, and manage books
- **Members Management**: View, add, and manage members with borrowed book details
- **Transactions**: View transactions, checkout books, and return books
- **Member Borrowed Books**: Click on borrowed count to view detailed list of books borrowed by each member
- **Real-time API Integration**: Direct communication with FastAPI backend

## Dependencies

- **Flask**: Web framework for the client application
- **requests**: HTTP library for API communication

## Project Structure

```
client_app/
├── main.py              # Flask application
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── templates/          # HTML templates
│   ├── index.html      # Main dashboard template
│   ├── books.html      # Books management page
│   ├── members.html    # Members management page
│   ├── transactions.html # Transactions management page
│   ├── add_book.html   # Add book form
│   ├── add_member.html # Add member form
│   ├── checkout.html   # Book checkout form
│   ├── return.html     # Book return form
│   ├── member_borrowed_books.html # Member's borrowed books detail page
│   └── error.html      # Error page template
└── static/             # Static files (CSS, JS, images)
```

## Usage

1. Navigate to http://localhost:5000
2. Use the navigation menu to access different sections
3. The client will automatically communicate with the FastAPI server
4. All data operations are performed through the API

## Troubleshooting

- **Connection Error**: Make sure the FastAPI server is running on port 8000
- **Import Errors**: Ensure all dependencies are installed using `pip install -r requirements.txt`
- **Port Already in Use**: Change the port in `main.py` if port 5000 is occupied
