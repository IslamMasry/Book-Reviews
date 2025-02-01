# Book Review Application with Django REST Framework (DRF)


The **Book Review Application** is a REST API built using Django and Django REST Framework (DRF). This app allows users to register, log in, publish books, and leave reviews on books published by other users. The application uses JWT (JSON Web Tokens) for authentication and enforces rules such as preventing users from reviewing their own books.

---

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [API Documentation](#api-documentation)
5. [Testing the API](#testing-the-api)
6. [Contributing](#contributing)
7. [License](#license)

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

