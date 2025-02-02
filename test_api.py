import requests

BASE_URL = "http://127.0.0.1:8000/api"

# Dummy user credentials
USER_DATA = {
    "username": "Islam",
    "email": "islam@user.com",
    "password": "12345"
}

# Function to test registration functionality.
def register():
    """Register a new user."""
    response = requests.post(f"{BASE_URL}/register/", json=USER_DATA)
    print("Register Response:", response.json())

# Function to test login functionality.
def login():
    """Login and get JWT token."""
    response = requests.post(f"{BASE_URL}/login/", json={
        "username": USER_DATA["username"],
        "password": USER_DATA["password"]
    })
    data = response.json()
    if "access" in data:
        return data["access"]
    else:
        print("Login Failed:", data)
        return None
    
# Function to test inserting a book to a database table.
def add_book(token):
    """Add a new book."""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/books/", headers=headers, json={
        "title": "Django Basics",
        "author": "John Doe",
        "description": "A book on Django for beginners."
    })
    print("Add Book Response:", response.json())
    return response.json().get("id")

# Function to test editing  book details in a database table.
def edit_book(token, book_id):
    """Edit an existing book."""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.put(f"{BASE_URL}/books/{book_id}/", headers=headers, json={
        "title": "Advanced Django",
        "author": "John Doe",
        "description": "An advanced book on Django."
    })
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        data = {"error": "Invalid JSON response"}
    print("Edit Book Response:", data)


def delete_book(token, book_id):
    """Delete a book."""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{BASE_URL}/books/{book_id}/", headers=headers)
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        data = {"message": "Book deleted successfully"}
    print("Delete Book Response:", data)



def list_books_with_pagination(token, page=1):
    """List all books with pagination."""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/books/?page={page}", headers=headers)
    
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        data = {"error": "Invalid JSON response"}
    
    print(f"Books (Page {page}):", data)




def post_review(token, book_id):
    """Post a review for a book."""
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/books/{book_id}/reviews/", headers=headers, json={
        "content": "This book is amazing!"
    })
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        data = {"error": "Invalid JSON response"}
    print("Post Review Response:", data)
    return data.get("id")



def edit_review(token, review_id):
    """Edit a review."""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.put(f"{BASE_URL}/reviews/{review_id}/", headers=headers, json={
        "content": "This book is fantastic!"
    })
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        data = {"error": "Invalid JSON response"}
    print("Edit Review Response:", data)



def delete_review(token, review_id):
    """Delete a review."""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{BASE_URL}/reviews/{review_id}/", headers=headers)
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        data = {"message": "Review deleted successfully"}
    print("Delete Review Response:", data)



def view_reviews(book_id):
    """View all reviews for a specific book."""
    response = requests.get(f"{BASE_URL}/books/{book_id}/reviews/")
    
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        data = {"error": "Invalid JSON response"}
    
    print(f"Reviews for Book {book_id}:", data)



if __name__ == "__main__":
    register()  # Register test user
    token = login()  # Login as the same user
    
    if token:
        book_id = add_book(token)  # User adds a book
        if book_id:
            edit_book(token, book_id)
            list_books_with_pagination(token, page=1)

            review_id = post_review(token, book_id)  # User posts a review, in this case the system will refuse the comment because the user is the book owner. Try changing the 'book_id' parameter to a book of another user, the review will be accepted.
            print("Review ID:", review_id)
            
            if review_id:
                edit_review(token, review_id)
                view_reviews(book_id)  # Ensure the same user retrieves the reviews
                delete_review(token, review_id)

            delete_book(token, book_id)

