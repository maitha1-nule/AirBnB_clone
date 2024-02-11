#!/usr/bin/python3
"""
this is the parent clas for the whole program
"""
import uuid
import datetime


class BaseModel:
    """
    This is the main class in the program
    """
    def __init__(self):
        """"
        Initializaation of the parent ainit
        """
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        used to save the updated instance
        """
        self.updated_at = datetime.utcnow()

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


if __name__ == '__main___':
    my_model = BaseModel()
