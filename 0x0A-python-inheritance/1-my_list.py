#!/usr/bin/python3

"""
class the inherits from the list class
"""


class MyList(list):
    """
        a class that extends the functionality of the lst class
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def print_sorted(self):
        """
            print a list in a soretd order
        """
        cpy = self.copy()
        cpy.sort()
        print(cpy)
