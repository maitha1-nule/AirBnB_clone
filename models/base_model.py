#!/usr/bin/python3
"""
this is the parent clas for the whole program
"""
import sys
import uuid
from datetime import datetime


class BaseModel:
    """
    This is the main class in the program
    """
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def save(self):
        """
        used to save the updated instance
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        used to serialize the objects after being entered
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict

    def __str__(self):
        """
        usedd to decaire how the output is going to be like after printing
        """
        class_name = self.__class__.__name__
        return (f"{class_name}, {self.id}, {self.__dict__}")

if __name__ == '__main__':
    my_model = BaseModel()

