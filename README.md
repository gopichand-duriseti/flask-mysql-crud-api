# Flask User CRUD API  
A simple Flask server that performs Create, Read, Update, Delete (CRUD) operations on users.  
User data is stored in a MySQL database.

## Features
- Create a new user  
- Get all users  
- Get a single user by ID  
- Update user details  
- Delete a user  
- Data stored in a MySQL table  

## How to Run the Server
python3 app.py  
Server runs at: http://127.0.0.1:5000

## Database Setup
Run these SQL commands:

CREATE DATABASE usersdb;

CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    mobileNumber VARCHAR(15),
    password VARCHAR(100)
);

## API Endpoints

### 1. Create User  
POST /users  
Body:
{
    "id": 5,
    "name": "NewUser",
    "email": "new@example.com",
    "mobileNumber": "9000000005",
    "password": "pass5"
}

### 2. Get All Users  
GET /users

### 3. Get Single User  
GET /users/<id>  
Example:
/users/3

### 4. Update User  
PUT /users/<id>  
Body:
{
    "name": "Updated Name",
    "email": "updated@example.com"
}

### 5. Delete User  
DELETE /users/<id>  
Example:
/users/2

## Notes
- All operations modify MySQL database rows  
- Server connects automatically to MySQL  
- Ensure MySQL is running before starting the server
