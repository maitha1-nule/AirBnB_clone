#!/usr/bin/python3
"""
This is the parent class of the program.
Public Instance Atr:
     id(str)
     created_at(datetime)
    updated_at(datetime)

Public Instance methods:
    __str__: which returns [<class name>]
    (<self.id>) <self.__dict__>
    _to__dict__: whic returns a dict repsentation
    of the created and updated at instances
    save: which updates the instance created at.
"""
import uuid
import datetime


class BaseModel:
    """
    This is the parent class of the entire program
    """

    def __init__(self, *args, **kwargs):
        """Dunder init constructor for all the functions"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """
        This method is used to more like declare how values are
        returned
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
        This method will be used to serialize our values
        after they have been entered by a user, implemented
        """
        inst_dict = self.__dict__.copy()
        inst_dict['__class__'] = self.__clas__.__main__
        inst_dict['created_at'] = self.created_at.isoformat()
        inst_dict['updated_at'] = self.updated_at.isoformat()
        return inst_dict
