#!/usr/bin/python3
"""
Module for the Base Class
- Public instance attributes
    - id
    - created_at
    - updated_at
- Public instance methods
    - save(self) - updates the updated_at attribute
    - to_dict(self) - returns dictionary
- __str__ method to print
"""
import sys
import uuid
from datetime import datetime


class BaseModel:
    """
    This is the main class in the program
    """
    def __init__(self, *args, **kwargs):
        """
        Initialiazes new instance of BaseModel.

        Args:
            *args: Unused positional arguments
            **kwargs: Dictionary representation of an instance.

        If kwargs is not empty:
            Each key has an attribute name
            Each value is the value of the corresponding attr name
            Convert datetime to datetime objects

        Otherwise:
            Create id and created_at values as initially done
        """
        if kwargs:
            if '__class__' in kwargs:
                # Remove '__class__' from the dictionary
                del kwargs['__class__']
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
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

