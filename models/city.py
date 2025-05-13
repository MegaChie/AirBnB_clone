#!/usr/bin/python3
"""
Logic for the city model.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class for the AirBnB clone project.

    Attributes:
        name (str): The name of the city.
        state_id (str): The ID of the state the city belongs to.
    """
    name = ""
    state_id = ""
