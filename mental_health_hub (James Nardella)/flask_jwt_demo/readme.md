# Flask JWT Authentication Demo

## Overview
This project demonstrates a **token-based authentication system** using **Flask** and **JWT (JSON Web Tokens)**.  
It includes:

- **User Registration** - securely hashes and stores passwords with `bcrypt`  
- **User Login** - verifies credentials and returns a signed JWT  
- **Protected Routes** - accessible only with a valid token in the `Authorization` header  
- **Logout** - client-side token invalidation concept  
- **API Test Script** - demonstrates how to interact with the Flask app using `requests`

---

## Requirements
- Python 3.8+  

Install dependencies with:

pip install flask bcrypt pyjwt requests


## Running the Application

1. Start the Flask app:
python "Token-Based Authentication (JWT).py"

This will start the server at:
http://127.0.0.1:5000


2. Test the API using the provided script:
python test_api.py


## Files

Token-Based Authentication (JWT).py - Flask app with JWT authentication system
test_api.py - Example script to register, login, and access protected routes


## Example API Flow

1. Register a user:
POST /register → { "username": "alice", "password": "mypassword" }

2. Login to receive JWT:
POST /login → returns { "token": "<JWT_TOKEN>" }

3. Access protected route with token:
GET /protected + header → Authorization: Bearer <JWT_TOKEN>

4. Logout:
POST /logout → instructs client to delete token


## Notes

Tokens expire after 30 minutes.

Passwords are never stored in plaintext - they are hashed with bcrypt.

The demo uses an in-memory dictionary (users_db) as a mock database (resets when the server restarts).


