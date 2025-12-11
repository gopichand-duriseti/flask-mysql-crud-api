# Flask User CRUD API

A simple Flask server that performs Create, Read, Update, Delete (CRUD) operations on users.
User data is stored in a MySQL database.

---

## Features

- Create a new user
- Get all users
- Get a single user by ID
- Update user details
- Delete a user
- Data stored in a MySQL table

---

## Prerequisites

- Python 3.8+ installed
- MySQL server installed and running
- Git (optional)

---

## Recommended project setup (Linux / macOS)

```bash
# 1. Clone the repo (if you haven't already)
git clone https://github.com/gopichand-duriseti/flask-mysql-crud-api.git
cd flask-mysql-crud-api

# 2. Install dependencies directly (virtual environment optional)
pip install --upgrade pip
pip install -r requirements.txt
```

On Windows (PowerShell):

```powershell
# Install dependencies directly (venv optional)
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Environment & configuration

It's best practice to keep credentials out of source control. Create a `.env` file at the project root with the following values (example):

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_db_password
DB_NAME=usersdb
```

The project expects a module named `database.py` (or an equivalent configuration) that reads these environment variables and exposes a `db` connection and `cursor`. Example minimal `database.py`:

```py
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "usersdb")

db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    port=DB_PORT
)

cursor = db.cursor()
```

> Make sure you have `python-dotenv` installed (included in `requirements.txt`).

---

## Database setup

Run these SQL commands to create the database and table (example):

```sql
CREATE DATABASE usersdb;

USE usersdb;

CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    mobileNumber VARCHAR(15),
    password VARCHAR(255)
);
```

Notes:

- `password` should store a hashed value, not plain text. Use a secure hashing routine (e.g. `werkzeug.security.generate_password_hash`).
- Pick a suitable `id` strategy for production (auto-increment or UUID) instead of manually assigning `id`.

---

## Installing dependencies

Create `requirements.txt` (if not present) with the libraries you need. Example:

```
Flask>=2.0
mysql-connector-python>=8.0
python-dotenv
Werkzeug
```

Install with:

```bash
pip install -r requirements.txt
```

---

## Running the server

```bash
# Run the Flask app directly (virtual environment optional)
python3 app.py
```
bash
# Activate virtualenv if not already active
source venv/bin/activate

# Run the Flask app
python3 app.py
```

Server runs at: `http://127.0.0.1:5000` by default.

If `app.py` uses `debug=True`, only use that in development. Do not enable debug mode in production.

---

## API Endpoints

1. **Create User**
   - `POST /users`
   - Body example:

```json
{
  "id": 5,
  "name": "NewUser",
  "email": "new@example.com",
  "mobileNumber": "9000000005",
  "password": "pass5"
}
```

> The server should hash the `password` before inserting into the DB.

2. **Get All Users**

   - `GET /users`

3. **Get Single User**

   - `GET /users/<id>`
   - Example: `/users/3`

4. **Update User**

   - `PUT /users/<id>`
   - Body: include only fields to update, e.g. `{ "name": "Updated Name", "email": "updated@example.com" }`

5. **Delete User**

   - `DELETE /users/<id>`
   - Example: `/users/2`

---

## Example `curl` requests

Create user:

```bash
curl -X POST http://127.0.0.1:5000/users \
  -H "Content-Type: application/json" \
  -d '{"id": 5, "name": "NewUser", "email": "new@example.com", "mobileNumber": "9000000005", "password": "pass5"}'
```

Get user:

```bash
curl http://127.0.0.1:5000/users/5
```

Update user:

```bash
curl -X PUT http://127.0.0.1:5000/users/5 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated"}'
```

Delete user:

```bash
curl -X DELETE http://127.0.0.1:5000/users/5
```

---

## Security Guidelines (Not Required for Basic Usage)

These are optional improvements if you plan to extend this project:

- Do not expose sensitive fields such as passwords.
- Store hashed passwords for better security.
- Store credentials safely using environment variables.

---

## Tests

You can test endpoints via `curl`, Postman, or automated tests (pytest + requests). Add tests under a `tests/` directory if desired.

---

## Common commands

```bash
# See current branch / status
git status

# Add and commit
git add -A
git commit -m "Add requirements.txt and update README"

# Push
git push origin main
```

---

## Contribution

Feel free to open issues or PRs. Keep changes small and document them in the PR description.

---

## License

Choose a license (e.g. MIT) and add a `LICENSE` file if this repo will be public.
