# Book Review Application with Django REST Framework (DRF)


The **Book Review Application** is a REST API built using Django and Django REST Framework (DRF). This app allows users to register, log in, publish books, and leave reviews on books published by other users. The application uses JWT (JSON Web Tokens) for authentication and enforces rules such as preventing users from reviewing their own books.

---

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [API Documentation](#api-documentation)
5. [Testing the API](#testing-the-api)

---

## Features

- **User Authentication**:
  - User registration and login using JWT.
  - Secured endpoints for authenticated users.

- **Book Management**:
  - Authenticated users can publish books with details like title, author, description, and cover image.
  - Users can list all books, retrieve a specific book, update and delete their own books.

- **Review and Comment System**:
  - Users can post reviews on books published by other users.
  - Users can edit or delete only their own reviews.
  - Users cannot review on their own books.

- **Pagination**:
  - Pagination is implemented for listing books and reviews to handle large datasets efficiently.

---

## Technologies Used

- **Backend**:
  - Django
  - Django REST Framework
  - JWT for authentication
  - SQLite (default database for development)

- **Frontend**:
  - This project is a backend-only application. You can use any frontend framework (e.g., React, Angular, Vue.js) to consume the API.

- **Other Tools**:
  - Postman (for API testing)
  - Python `requests` library for automated testing (attached a sample module for testing the API without using Postman or cURL)

---

## Setup Instructions

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.8 or higher
- Pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/IslamMasry/Book-Reviews.git
cd book-reviews
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # For Linux users, use `source venv/bin/activate`
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Apply Migrations

```bash
python manage.py migrate
```

### Step 5: Create a Superuser (Optional)

Create a superuser to access the Django admin panel:

```bash
python manage.py createsuperuser
```

### Step 6: Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

---

## API Documentation

### Base URL

```
http://127.0.0.1:8000/api/
```

### Authentication

All endpoints (except registration and login) require JWT authentication. Include the JWT token in the `Authorization` header:

```
Authorization: Bearer <your-access-token>
```

### Endpoints

#### 1. **User Registration**
- **URL**: `/api/register/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "testpassword123"
  }
  ```

#### 2. **User Login**
- **URL**: `/api/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "testuser",
    "password": "testpassword123"
  }
  ```
- **Response**:
  ```json
  {
    "refresh": "your-refresh-token",
    "access": "your-access-token"
  }
  ```

#### 3. **Add a Book**
- **URL**: `/api/books/`
- **Method**: `POST`
- **Headers**:
  ```
  Authorization: Bearer <your-access-token>
  ```
- **Request Body**:
  ```json
  {
    "title": "Bayesian Reasoning and Machine Learning",
    "author": "David Barber",
    "description": "This book provides a knowledge about the probabilistic approach in Machine Learning."
  }
  ```

#### 4. **List All Books**
- **URL**: `/api/books/`
- **Method**: `GET`
- **Query Parameters**:
  - `page`: Page number for pagination (default: 1)

#### 5. **Add a Review**
- **URL**: `/api/books/<book_id>/reviews/`
- **Method**: `POST`
- **Headers**:
  ```
  Authorization: Bearer <your-access-token>
  ```
- **Request Body**:
  ```json
  {
    "content": "This is a great book!"
  }
  ```

#### 6. **Edit a Review**
- **URL**: `/api/reviews/<review_id>/`
- **Method**: `PUT`
- **Headers**:
  ```
  Authorization: Bearer <your-access-token>
  ```
- **Request Body**:
  ```json
  {
    "content": "This is an updated review!"
  }
  ```

#### 7. **Delete a Review**
- **URL**: `/api/reviews/<review_id>/`
- **Method**: `DELETE`
- **Headers**:
  ```
  Authorization: Bearer <your-access-token>
  ```

---

## Testing the API

You can test the API using:
- **Postman**: Manually test each endpoint.
- **Python Script**: Use the provided `test_api.py` script to automate testing.

### Running the Python Test Script

1. Install the `requests` library:
   ```bash
   pip install requests
   ```

2. Run the script:
   ```bash
   python test_api.py
   ```

---




## Contributors

[Islam Elmasry](#Islam-Elmasry) - Software Engineer

- **Email**: dr.egy2009@hotmail.com
- **GitHub**: [IslamMasry](https://github.com/IslamMasry)

---

Thank you for checking out!

