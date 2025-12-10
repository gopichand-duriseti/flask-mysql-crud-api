from flask import Flask,request,jsonify
import json,os
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
    query = "select * from users"
    cursor.execute(query)
    users = cursor.fetchall()
    if not users:
        return jsonify({"message": "No users found"}), 404
    return jsonify(users)

#Getting User Details
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    query = "select * from users where id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
    
#Updating User
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    query="select * from users where id=%s"  
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    if not user:
        return {"error": "User not found"}, 404
    data = request.get_json()
    query = "UPDATE users SET name = %s, email = %s, mobileNumber = %s, password = %s WHERE id = %s"
    values = (data.get("name"), data.get("email"), data.get("mobileNumber"), data.get("password"), user_id)
    cursor.execute(query, values)
    db.commit()
    
#Deleting a user
@app.route("/users/<int:user_id>",methods=['DELETE'])
def delete_user(user_id):
    query="select * from users where id=%s"  
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    if not user:
        return {"error": "User not found"}, 404
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    db.commit()

if __name__ == "__main__":
    app.run(debug=True)