# Library Management System - Project Requirements

## 1. Project Overview

You are tasked with implementing a **Library Management System API** using FastAPI. The system should manage physical books through a digital interface, providing comprehensive book and member management capabilities.

## 2. Core Entities

### 2.1 Book Entity

**Attributes:**

* `id` (str): Unique identifier (UUID format)
* `title` (str): Book title (required, max 200 characters)
* `author` (str): Author name (required, max 100 characters)
* `isbn` (str): International Standard Book Number (required, validate format)
* `publication_year` (int): Year of publication (1900-2024)
* `genre` (str): Book genre/category (required, max 50 characters)
* `total_copies` (int): Total number of copies (minimum 1)
* `available_copies` (int): Number of available copies
* `status` (str): Book status - "available", "out_of_stock", "discontinued"
* `created_at` (datetime): Record creation timestamp
* `updated_at` (datetime): Last update timestamp

**Business Rules:**

* ISBN must be valid (10 or 13 digits, with proper checksum)
* `available_copies` cannot exceed `total_copies`
* `available_copies` cannot be negative
* Book status automatically updates based on available copies

### 2.2 Member Entity

**Attributes:**

* `id` (str): Unique identifier (UUID format)
* `first_name` (str): First name (required, max 50 characters)
* `last_name` (str): Last name (required, max 50 characters)
* `email` (str): Email address (required, unique, validate format)
* `phone` (str): Phone number (optional, validate format)
* `membership_date` (date): Date of membership (default: current date)
* `status` (str): Member status - "active", "suspended", "expired"
* `max_books_allowed` (int): Maximum books member can borrow (default: 5)
* `created_at` (datetime): Record creation timestamp
* `updated_at` (datetime): Last update timestamp

**Business Rules:**

* Email must be unique across all members
* Phone number must be valid format (if provided)
* Member status affects borrowing privileges

### 2.3 Transaction Entity

**Attributes:**

* `id` (str): Unique identifier (UUID format)
* `book_id` (str): Reference to book (required)
* `member_id` (str): Reference to member (required)
* `transaction_type` (str): "checkout" or "return"
* `transaction_date` (datetime): Date and time of transaction
* `due_date` (datetime): Due date for returns (calculated automatically)
* `return_date` (datetime): Actual return date (null for checkouts)
* `fine_amount` (float): Fine amount if overdue (default: 0.0)
* `status` (str): Transaction status - "active", "returned", "overdue"

**Business Rules:**

* Checkout period is 14 days by default
* Fine calculation: Rs.50 per day after due date
* Member cannot borrow more than `max_books_allowed`
* Book must be available for checkout

## 3. API Endpoints

### 3.1 Book Management

#### GET /books

* **Purpose**: Retrieve all books with optional filtering
* **Query Parameters**:
  * `title` (optional): Filter by title (partial match)
  * `author` (optional): Filter by author (partial match)
  * `genre` (optional): Filter by genre
  * `status` (optional): Filter by status
* **Response**: List of books

#### GET /books/{book_id}

* **Purpose**: Retrieve a specific book by ID
* **Response**: Book details or 404 if not found

#### POST /books

* **Purpose**: Add a new book
* **Request Body**: Book creation data
* **Response**: Created book with generated ID

#### PUT /books/{book_id}

* **Purpose**: Update an existing book
* **Request Body**: Book update data
* **Response**: Updated book or 404 if not found

#### DELETE /books/{book_id}

* **Purpose**: Delete a book (soft delete - set status to discontinued)
* **Response**: Success message or 404 if not found

### 3.2 Member Management

#### GET /members

* **Purpose**: Retrieve all members with optional filtering
* **Query Parameters**:
  * `name` (optional): Filter by first or last name (partial match)
  * `email` (optional): Filter by email (exact match)
  * `status` (optional): Filter by status
* **Response**: List of members

#### GET /members/{member_id}

* **Purpose**: Retrieve a specific member by ID
* **Response**: Member details or 404 if not found

#### GET /members/{member_id}/can-borrow

* **Purpose**: Check if a member can borrow a book
* **Response**: Borrowing status with reason

#### GET /members/{member_id}/borrowed-count

* **Purpose**: Get the number of books currently borrowed by a member
* **Response**: Count of borrowed books

#### GET /members/{member_id}/borrowed-books

* **Purpose**: Get the list of books currently borrowed by a member
* **Response**: List of borrowed books with details

#### GET /members/with-borrowed-counts/

* **Purpose**: Get all members with their currently borrowed book counts
* **Response**: List of members with borrowed counts

#### POST /members

* **Purpose**: Register a new member
* **Request Body**: Member registration data
* **Response**: Created member with generated ID

#### PUT /members/{member_id}

* **Purpose**: Update member information
* **Request Body**: Member update data
* **Response**: Updated member or 404 if not found

#### DELETE /members/{member_id}

* **Purpose**: Deactivate a member (soft delete - set status to expired)
* **Response**: Success message or 404 if not found

### 3.3 Transaction Management

#### GET /transactions

* **Purpose**: Retrieve all transactions with optional filtering
* **Query Parameters**:
  * `book_id` (optional): Filter by book ID
  * `member_id` (optional): Filter by member ID
  * `transaction_type` (optional): Filter by type (checkout/return)
  * `status` (optional): Filter by status
* **Response**: List of transactions

#### GET /transactions/{transaction_id}

* **Purpose**: Retrieve a specific transaction by ID
* **Response**: Transaction details or 404 if not found

#### POST /transactions/checkout

* **Purpose**: Check out a book to a member
* **Request Body**: Checkout data (book_id, member_id)
* **Response**: Created transaction or error if rules violated

#### POST /transactions/return

* **Purpose**: Return a book from a member
* **Request Body**: Return data (book_id, member_id)
* **Response**: Updated transaction with fine calculation

#### GET /transactions/overdue

* **Purpose**: Get all overdue transactions
* **Response**: List of overdue transactions

## 4. Data Validation Requirements

### 4.1 Input Validation

* All required fields must be present
* String lengths must be within specified limits
* Email format validation using regex
* Phone number format validation (if provided)
* ISBN validation (10 or 13 digits with checksum)
* Date range validation (publication year: 1900-2024)

### 4.2 Business Rule Validation

* Member cannot borrow more than `max_books_allowed`
* Book must be available for checkout
* Member must be active to borrow books
* Transaction dates must be logical (return date after checkout date)

## 5. Error Handling

### 5.1 HTTP Status Codes

* `200 OK`: Successful GET, PUT operations
* `201 Created`: Successful POST operations
* `400 Bad Request`: Invalid input data
* `404 Not Found`: Resource not found
* `409 Conflict`: Business rule violation
* `422 Unprocessable Entity`: Validation errors
* `500 Internal Server Error`: Server errors

### 5.2 Error Response Format

```json
{
  "error": "Error message",
  "details": "Additional error details",
  "timestamp": "2024-01-01T12:00:00Z"
}
```

## 6. Data Storage

### 6.1 File-based Storage

* Use JSON files for data persistence
* Implement proper file locking for concurrent access
* Handle file corruption gracefully
* Implement backup and recovery mechanisms

### 6.2 File Structure

* `data/books.json`: Book records
* `data/members.json`: Member records
* `data/transactions.json`: Transaction records

## 7. Additional Requirements

### 7.1 Code Organization

* Use proper OOP principles (inheritance, encapsulation, polymorphism)
* Implement service layer for business logic
* Separate data models from API routes
* Use utility functions for common operations

### 7.2 Documentation

* Comprehensive docstrings for all functions and classes
* API documentation using FastAPI's automatic generation
* README with setup and usage instructions

### 7.3 Testing

* Unit tests for all business logic
* Integration tests for API endpoints
* Test data validation and error scenarios

## 8. Evaluation Criteria

Your implementation will be evaluated using a combination of automated testing and manual assessment:

### Automated Testing (80 points)

#### Functional Requirements (80 points)

* **Server Health (5 points)**: API server starts and responds
* **API Documentation (5 points)**: Swagger UI accessible
* **Books Endpoints (25 points)**:
  * GET /books (10 points)
  * POST /books (10 points)
  * GET /books/{id} (5 points)
* **Members Endpoints (25 points)**:
  * GET /members (10 points)
  * POST /members (10 points)
  * GET /members/{id}/borrowed-books (5 points)
* **Transactions Endpoints (25 points)**:
  * GET /transactions (10 points)
  * POST /transactions/checkout (15 points)
* **Data Validation (10 points)**:
  * ISBN validation (5 points)
  * Email validation (5 points)
* **Error Handling (5 points)**:
  * 404 error handling (5 points)

### Manual Assessment (20 points)

* **Code Quality (10 points)**: OOP design, modularity, documentation
* **Client Integration (10 points)**: Visual verification using client application

### Scoring System

* **Percentage Calculation**: (Total Points / Max Points) × 100
* **Grade Assignment**: A (90%+), B (80-89%), C (70-79%), D (60-69%), F (<60%)

### Evaluation Process

1. **Automated Testing**: Your API will be tested against predefined criteria
2. **Client Application Testing**: Your API will be tested with the provided client application
3. **Code Review**: Manual assessment of code quality and OOP implementation
4. **Final Score**: Combined automated and manual assessment scores

## 9. Submission Requirements

### Repository Structure

Your submission should follow this structure:

```
candidate-branch/
└── api_server/          # Only API server code
    ├── main.py          # FastAPI application entry point
    ├── models/          # Pydantic models
    ├── services/        # Business logic
    ├── routes/          # API endpoints
    ├── utils/           # Utility functions
    └── requirements.txt # Dependencies
```

### Implementation Requirements

1. **Complete FastAPI application** with all required endpoints
2. **All data models and business logic** implemented
3. **Proper error handling and validation**
4. **Comprehensive documentation** and docstrings
5. **Working with provided client application** for testing
6. **Server must start** with `uvicorn main:app --reload`

### Testing Requirements

* **Self-testing**: Use the provided client application to test your API
* **API Documentation**: Ensure Swagger UI is accessible
* **All Endpoints**: Verify all required endpoints work correctly
* **Data Validation**: Test ISBN and email validation
* **Error Handling**: Verify proper HTTP status codes and error messages

## 10. Timeline

* **Day 11 (Day-end)**: Requirements discussion and design session
* **Day 12-13-14**: Implementation and self-testing
* **Day 15**: Final testing and submission

## 11. Testing and Validation

### Self-Testing with Client Application

You will receive a Flask client application (`client_app/`) that you can use to test your API implementation:

#### Setup Instructions

1. **Create virtual environment for API server**:
   ```bash
   cd api_server
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Create virtual environment for client application**:
   ```bash
   cd client_app
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

#### Testing Workflow

1. **Start your API server** (in API server virtual environment):
   ```bash
   cd api_server
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   uvicorn main:app --reload
   ```

2. **Start the client application** (in client virtual environment):
   ```bash
   cd client_app
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   python main.py
   ```

3. **Test all features**:
   * Add and view books
   * Add and view members
   * Checkout and return books
   * View borrowed books and member details
   * Test validation and error handling

### API Testing Tools

You can also test your API using:

* **FastAPI Swagger UI**: `http://localhost:8000/docs`
* **Postman**: Import API endpoints for testing
* **curl**: Command-line API testing
* **Python requests**: Script-based testing

### Validation Checklist

Before submission, ensure:

* [ ] All endpoints respond correctly
* [ ] Data validation works (ISBN, email, etc.)
* [ ] Business rules are enforced
* [ ] Error handling is proper
* [ ] Client application works with your API
* [ ] API documentation is accessible

Good luck with your implementation!
