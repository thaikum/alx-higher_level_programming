#!/usr/bin/python3
"""
jasdkfjalj
"""
class LockedClass:
    """
    askldfjla
    """
    def __setattr__(self, name, value):
        if hasattr(self, name) or name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError("object has no attribute 'last_name'")
