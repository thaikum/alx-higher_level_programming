#!/usr/bin/python3

"""
Student class
"""


class Student:
    """
    student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            new_obj = {}
            for key in attrs:
                if self.__dict__.get(key):
                    new_obj[key] = self.__dict__.get(key)

            return new_obj

    def reload_from_json(self, json):
        self.first_name = json.get("first_name")
        self.last_name = json.get("last_name")
        self.age = json.get("age")
