# Bookish

Bookish is an online bookstore application that allows users to browse, search, and purchase books. It also provides features for managing authors, publishers, and user accounts.

## API Endpoints

All endpoints expect and return data in JSON format.

### Books

- **List Books**
  - **Description:** Get a list of all books.
  - **Method:** `GET`
  - **Endpoint:** `/books`
  - **Query Parameters:**
    - `search` (string): Search by title or author.
    - `publisher` (string): Filter by publisher.
    - `genre` (string): Filter by genre.
    - `sort` (string): Sort by `price_asc`, `price_desc`, `popularity`, `genre`.
  - **Response Status:** `200 OK`
  - **Response Body:**
    ```json
    [
      {
        "id": 1,
        "title": "The Lord of the Rings",
        "author_id": 1,
        "publisher_id": 1,
        "genre": "Fantasy",
        "price": 25.99,
        "popularity": 100
      }
    ]
    ```

- **Get Book**
  - **Description:** Get details for a specific book.
  - **Method:** `GET`
  - **Endpoint:** `/books/{id}`
  - **Response Status:** `200 OK`
  - **Response Body:**
    ```json
    {
      "id": 1,
      "title": "The Lord of the Rings",
      "author": { "id": 1, "name": "J.R.R. Tolkien" },
      "publisher": { "id": 1, "name": "Allen & Unwin" },
      "genre": "Fantasy",
      "price": 25.99,
      "description": "A high-fantasy novel."
    }
    ```

- **Create Book**
  - **Description:** Add a new book.
  - **Method:** `POST`
  - **Endpoint:** `/books`
  - **Request Body:**
    ```json
    {
      "title": "The Hobbit",
      "author_id": 1,
      "publisher_id": 1,
      "genre": "Fantasy",
      "price": 15.99,
      "description": "A fantasy novel."
    }
    ```
  - **Response Status:** `201 Created`

- **Update Book**
  - **Description:** Update an existing book.
  - **Method:** `PUT`
  - **Endpoint:** `/books/{id}`
  - **Request Body:**
    ```json
    {
      "price": 17.99
    }
    ```
  - **Response Status:** `200 OK`

- **Delete Book**
  - **Description:** Delete a book.
  - **Method:** `DELETE`
  - **Endpoint:** `/books/{id}`
  - **Response Status:** `204 No Content`

### Authors

- **List Authors**
  - **Description:** Get a list of all authors.
  - **Method:** `GET`
  - **Endpoint:** `/authors`
  - **Response Status:** `200 OK`

- **Get Author**
  - **Description:** Get details for a specific author and their books.
  - **Method:** `GET`
  - **Endpoint:** `/authors/{id}`
  - **Response Status:** `200 OK`

- **Create Author**
  - **Description:** Add a new author.
  - **Method:** `POST`
  - **Endpoint:** `/authors`
  - **Request Body:**
    ```json
    {
      "name": "J.K. Rowling"
    }
    ```
  - **Response Status:** `201 Created`

- **Update Author**
  - **Description:** Update an existing author.
  - **Method:** `PUT`
  - **Endpoint:** `/authors/{id}`
  - **Request Body:**
    ```json
    {
      "name": "Joanne Rowling"
    }
    ```
  - **Response Status:** `200 OK`

- **Delete Author**
  - **Description:** Delete an author.
  - **Method:** `DELETE`
  - **Endpoint:** `/authors/{id}`
  - **Response Status:** `204 No Content`

### Publishers

- **List Publishers**
  - **Description:** Get a list of all publishers.
  - **Method:** `GET`
  - **Endpoint:** `/publishers`
  - **Response Status:** `200 OK`

- **Get Publisher**
  - **Description:** Get details for a specific publisher and their books.
  - **Method:** `GET`
  - **Endpoint:** `/publishers/{id}`
  - **Response Status:** `200 OK`

- **Create Publisher**
  - **Description:** Add a new publisher.
  - **Method:** `POST`
  - **Endpoint:** `/publishers`
  - **Request Body:**
    ```json
    {
      "name": "Bloomsbury Publishing"
    }
    ```
  - **Response Status:** `201 Created`

- **Update Publisher**
  - **Description:** Update an existing publisher.
  - **Method:** `PUT`
  - **Endpoint:** `/publishers/{id}`
  - **Request Body:**
    ```json
    {
      "name": "Bloomsbury"
    }
    ```
  - **Response Status:** `200 OK`

- **Delete Publisher**
  - **Description:** Delete a publisher.
  - **Method:** `DELETE`
  - **Endpoint:** `/publishers/{id}`
  - **Response Status:** `204 No Content`

### Auth

- **Register**
  - **Description:** Register a new user.
  - **Method:** `POST`
  - **Endpoint:** `/auth/register`
  - **Request Body:**
    ```json
    {
      "username": "testuser",
      "email": "test@example.com",
      "password": "password123"
    }
    ```
  - **Response Status:** `201 Created`

- **Login**
  - **Description:** Log in a user.
  - **Method:** `POST`
  - **Endpoint:** `/auth/login`
  - **Request Body:**
    ```json
    {
      "email": "test@example.com",
      "password": "password123"
    }
    ```
  - **Response Status:** `200 OK`
  - **Response Body:**
    ```json
    {
      "token": "your_jwt_token"
    }
    ```

### Profile

- **Get Profile**
  - **Description:** Get the current user's profile.
  - **Method:** `GET`
  - **Endpoint:** `/profile`
  - **Response Status:** `200 OK`

- **Update Profile**
  - **Description:** Update the current user's profile.
  - **Method:** `PUT`
  - **Endpoint:** `/profile`
  - **Request Body:**
    ```json
    {
      "username": "new_username"
    }
    ```
  - **Response Status:** `200 OK`

### Orders

- **List Orders**
  - **Description:** Get the current user's order history.
  - **Method:** `GET`
  - **Endpoint:** `/orders`
  - **Response Status:** `200 OK`

- **Create Order**
  - **Description:** Create a new order from the user's cart.
  - **Method:** `POST`
  - **Endpoint:** `/orders`
  - **Response Status:** `201 Created`

### Cart

- **Get Cart**
  - **Description:** Get the current user's shopping cart.
  - **Method:** `GET`
  - **Endpoint:** `/cart`
  - **Response Status:** `200 OK`

- **Add to Cart**
  - **Description:** Add a book to the user's shopping cart.
  - **Method:** `POST`
  - **Endpoint:** `/cart`
  - **Request Body:**
    ```json
    {
      "book_id": 1,
      "quantity": 1
    }
    ```
  - **Response Status:** `200 OK`

## Database Schema

Here is a textual representation of the database schema. A diagram should be created and added here.

- **users**
  - `id` (PK)
  - `username`
  - `email`
  - `password_hash`
  - `created_at`
  - `updated_at`

- **books**
  - `id` (PK)
  - `title`
  - `description`
  - `author_id` (FK to authors.id)
  - `publisher_id` (FK to publishers.id)
  - `genre`
  - `price`
  - `popularity`
  - `created_at`
  - `updated_at`

- **authors**
  - `id` (PK)
  - `name`
  - `created_at`
  - `updated_at`

- **publishers**
  - `id` (PK)
  - `name`
  - `created_at`
  - `updated_at`

- **orders**
  - `id` (PK)
  - `user_id` (FK to users.id)
  - `total_price`
  - `created_at`

- **order_items**
  - `id` (PK)
  - `order_id` (FK to orders.id)
  - `book_id` (FK to books.id)
  - `quantity`
  - `price`

- **cart_items**
  - `id` (PK)
  - `user_id` (FK to users.id)
  - `book_id` (FK to books.id)
  - `quantity`
