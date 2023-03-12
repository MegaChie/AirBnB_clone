#!/usr/bin/python3


from models.base_model import BaseModel
class User(BaseModel):
    """ First User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
