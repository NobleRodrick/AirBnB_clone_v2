#!/usr/bin/python3
"""
Here comes the state class
"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """
    class to test the test class
    """

    def __init__(self, *args, **kwargs):
        """
        initialize the class vars
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
