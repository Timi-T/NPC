#!/usr/bin/python3
"""
App for National population commision
"""

from flask import Flask, request
from flask_login import LoginManager, login_user
from bcrypt import Bcrypt
from models.citizens import Citizen
from models.lga import LGA
from models.users import User
from models.states import State
from models.wards import Ward

app = Flask(__name__)

loginmanager = LoginManager(app)
app.secret_key = "secretkey"
bcrypt = Bcrypt()


@app.route('api/v1/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Function to create a user"""
    from models import storage
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
    from models import storage
    st_info = request.get_json()
    name = st_info.get('name')

    if name:
        new_state = State(name)
        storage.new(new_state)
        storage.save()
    else:
        return "Invalid credentials"

@app.route('api/v1/lgas', methods=['POST'], strict_slashes=False)
def create_lga():
    """Function to create a Local govt. area"""
    from models import storage

    lga_info = request.get_json()
    name = lga_info.get('name')
    state_id = lga_info.get('state_id')

    if name and state_id:
        new_lga = LGA(name)
        storage.new(new_lga)
        storage.save()
    else:
        return "Invalid credentials"

@app.route('api/v1/wards', methods=['POST'], strict_slashes=False)
def create_ward():
    """Function to create a ward in a Local govt. area"""
    from models import storage

    lga_info = request.get_json()
    name = lga_info.get('name')
    lga_id = lga_info.get('lga_id')

    if name and lga_id:
        new_ward = Ward(name, lga_id)
        storage.new(new_ward)
        storage.save()
    else:
        return "Invalid credentials"

@app.route('api/v1/citizens', methods=['POST'], strict_slashes=False)
def create_citizen():
    """Function to create a Local govt. area"""
    from models import storage

    citi_info = request.get_json()
    name = citi_info.get('name')
    gender = citi_info.get('gender')
    address = citi_info.get('address')
    phone = citi_info.get('phone')
    if isinstance(phone, int) == False:
        return "Phone number must be an integer"
    ward_id = citi_info.get('ward_id')
    if name and gender and address and phone and ward_id:
        new_citi = Citizen(name)
        storage.new(new_citi)
        storage.save()
    else:
        return "Invalid credentials"


@app.route('api/v1/login', strict_slashes=False)
def login():
    """Log a user into the application"""
    from models import storage

    user_info = request.get_json()
    email = user_info.get('email')
    pwd = user_info.get('password')
    if email and pwd:
        """
            Filter the users in the database by email
            get the user object
        """
        login_user("user_object")


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")