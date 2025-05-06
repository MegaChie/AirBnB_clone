#!/usr/bin/python3
"""
Logic for the user model.
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    User class for AirBnB clone project.

    Attributes:
        email (str): Unique email for each user.
        password (str): Unique password for each user.
        first_name (str): First name of each user.
        last_name (str): Last name of each user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

