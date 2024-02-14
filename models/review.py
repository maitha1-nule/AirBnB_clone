#!/usr/bin/python3
"""
This is the review class, it will 
also inherit from the BAsemodel class
"""
from base_model import BaseModel


class Review(BaseModel):
    """Inherits from the basemodel"""
    def __init__(self):
        """Dunder init method"""
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
