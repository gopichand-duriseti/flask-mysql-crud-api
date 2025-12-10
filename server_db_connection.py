from flask import Flask,request,jsonify
import mysql.connector

app=Flask(__name__)

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gopi@0371",
    database="usersdb")

cursor=db.cursor()

#Adding/Creating a User
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    query = "INSERT INTO users (id, name, email, mobileNumber, password) VALUES (%s, %s, %s, %s, %s)"
    values = (data["id"], data["name"], data["email"], data["mobileNumber"], data["password"])
    cursor.execute(query, values)
    db.commit()
    return jsonify({"message": "User created successfully"}), 201

#To Get all users details
@app.route("/users", methods=["GET"])
def get_all_users():
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    if not users:
        return jsonify({"message": "No users found"}), 404
    return jsonify(users)

#Getting User Details
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
    
#UPDATING User
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    # Fetch existing user
    cursor.execute("SELECT name, email, mobileNumber, password FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()

    if not user:
        return jsonify({"error": "User not found"}), 404
    existing_name, existing_email, existing_mobile, existing_password = user
    data = request.get_json()

    # Use new value if given or else keep existing
    new_name = data.get("name", existing_name)
    new_email = data.get("email", existing_email)
    new_mobile = data.get("mobileNumber", existing_mobile)
    new_password = data.get("password", existing_password)

    query = """UPDATE users SET name = %s, email = %s, mobileNumber = %s, password = %s WHERE id = %s """

    values = (new_name, new_email, new_mobile, new_password, user_id)
    cursor.execute(query, values)
    db.commit()
    return jsonify({"message": "User updated successfully"})

#DELETING User
@app.route("/users/<int:user_id>",methods=['DELETE'])
def delete_user(user_id):
    query="SELECT * FROM users WHERE id=%s"  
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    if not user:
        return {"error": "User not found"}, 404
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    db.commit()
    return jsonify({"message": "User deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)