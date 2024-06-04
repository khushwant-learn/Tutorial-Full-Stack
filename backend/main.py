# CRUD App
# create
# - first name
# - last name
# - email

# localhost:5000/create_contact

# Request
# type: GET or POST or PUT or PATCH or DELETE

from flask import request, jsonify
from config import app, db
from models import Contact

