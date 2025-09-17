# Library Management System - Capstone Project

## Project Overview

This capstone project implements a digital Library Management System using FastAPI. The system manages physical books through a digital interface, providing comprehensive book and member management capabilities.

## Learning Objectives

This project will help you demonstrate proficiency in:
- **FastAPI** framework and RESTful API design
- **Object-Oriented Programming** concepts and implementation
- **Pydantic models** for data validation
- **File I/O operations** with JSON data
- **Exception handling** and error management
- **Regular expressions** for data validation
- **Modular code organization** and best practices

## Project Structure

```
Library_Mgmt/
├── README.md                     # This file
├── PROJECT_REQUIREMENTS.md       # Detailed project specifications
├── IMPLEMENTATION_GUIDE.md       # Step-by-step implementation guide
├── data/                         # Sample data files
│   ├── books.json
│   ├── members.json
│   └── transactions.json
├── api_server/                   # FastAPI backend implementation
│   ├── main.py
│   ├── requirements.txt         # API server dependencies
│   ├── README.md               # API server documentation
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── book.py
│   │   ├── member.py
│   │   └── transaction.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── books.py
│   │   ├── members.py
│   │   └── transactions.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── book_service.py
│   │   ├── member_service.py
│   │   └── transaction_service.py
│   └── utils/
│       ├── __init__.py
│       └── file_handler.py
├── client_app/                   # Flask client application
│   ├── main.py
│   ├── requirements.txt         # Client dependencies
│   ├── README.md               # Client documentation
│   ├── templates/
│   │   └── index.html
│   └── static/
└── tests/                        # Evaluation tests (instructor use only)
    ├── test_basic.py
    └── README.md
```

## Quick Start

### API Server Setup

1. **Setup Environment**:
   ```bash
   cd api_server
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Run the API Server**:
   ```bash
   uvicorn main:app --reload
   ```

### Client Application Setup

1. **Setup Client Environment**:
   ```bash
   cd client_app
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Run the Client Application**:
   ```bash
   python main.py
   ```

4. **Access API Documentation**:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Core Features

- **Book Management**: Add, update, delete, and search books
- **Member Management**: Register and manage library members with borrowing tracking
- **Transaction Management**: Check-out and check-in books with fine calculation
- **Member Borrowing Tracking**: View borrowed books count and detailed borrowing history
- **Search & Filter**: Find books by various criteria
- **Status Tracking**: Monitor book availability and member status
- **Data Validation**: Ensure data integrity and business rules
- **Enhanced Member Features**: Borrowing status checks, borrowed book lists, and member history

## Evaluation Criteria

Your implementation will be evaluated on:
- **Functionality**: All required features working correctly
- **Code Quality**: Clean, readable, and well-documented code
- **OOP Design**: Proper use of classes, inheritance, and encapsulation
- **Error Handling**: Comprehensive exception management
- **API Design**: RESTful principles and proper HTTP status codes
- **Data Validation**: Input validation and business rule enforcement

## Getting Started

1. Read `PROJECT_REQUIREMENTS.md` for detailed specifications
2. Follow `IMPLEMENTATION_GUIDE.md` for step-by-step instructions
3. Start with the basic models and gradually build functionality
4. Test your implementation using the provided client application

Good luck with your implementation!
