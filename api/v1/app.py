#!/usr/bin/python3
"""
App for National population commision
"""

from flask import Flask, request
from flask_login import LoginManager
from bcrypt import Bcrypt
from models.users import User
from models.states import State
from models import storage

app = Flask(__name__)

loginmanager = LoginManager(app)
app.secret_key = "secretkey"
bcrypt = Bcrypt()


@app.route('api/v1/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Function to create a user"""
    user_info = request.get_json()
    name = user_info.get('name')
    email = user_info.get('email')
    password = user_info.get('password')
    if name and email and password:
        pwd = bcrypt.generate_password_hash(password)
        new_user = User(name, email, pwd)
        storage.new(new_user)
        storage.save()
    else:
        return "Invalid credentials"

@app.route('api/v1/states', methods=['POST'], strict_slashes=False)
def create_state():
    """function to create a state"""
    st_info = request.get_json()
    name = st_info.get('name')

    if name:
        new_state = State(name)
        storage.new(new_state)
        storage.save()
    else:
        return "Invalid credentials"


@app.route('api/v1/login', strict_slashes=False)
def login():
    """Log a user into the application"""


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")