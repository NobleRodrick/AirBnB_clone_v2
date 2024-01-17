#!/usr/bin/python3
"""
this also acts as the engine for the db engine format
Contains the TestDBStorageDocs and TestDBStorage classes
"""
from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
import unittest
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pycodestyle
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity,
           "City": City,
           "Place": Place,
           "Review": Review,
           "State": State,
           "User": User
           }
storage_t = os.getenv("HBNB_TYPE_STORAGE")


class TestDBStorageDocs(unittest.TestCase):
    """
    class to test documentation and style of the db
    Tests to check the documentation and style of DBStorage class
    """
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_test_db_storage(self):
        """  function tests tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8_check = pycodestyle.StyleGuide(quiet=True)
        result = pep8_check.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    
    def test_pep8_conformance_db_storage(self):
        """
        Does this conform to the PEP* format
        """
        pep8_check = pycodestyle.StyleGuide(quiet=True)
        result = pep8_check.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


# class TestFileStorage(unittest.TestCase):
#     """Test the FileStorage class"""
#     @unittest.skipIf(storage_t != 'db', "not testing db storage")
#     def test_all_returns_dict(self):
#         """Test that all returns a dictionary"""
#         self.assertIs(type(models.storage.all()), dict)

#     @unittest.skipIf(storage_t != 'db', "not testing db storage")
#     def test_all_no_class(self):
#         """Test that all returns all rows when no class is passed"""

#     @unittest.skipIf(storage_t != 'db', "not testing db storage")
#     def test_new(self):
#         """test that new adds an object to the database"""

#     @unittest.skipIf(storage_t != 'db', "not testing db storage")
#     def test_save(self):
#         """Test that save properly saves objects to file.json"""

class TestDBStorageDocs(unittest.TestCase):
    """
    Tests to check the documentation and style of DBStorage class
    """
    @classmethod
    def setUpClass(cls):
        """
        function to help Set-up for the doc tests
        """
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_test_db_storage(self):
        """
         function Test tests/test_models/test_db_storage.py conforms to PEP8.
        """
        pep8_check = pycodestyle.StyleGuide(quiet=True)
        result = pep8_check.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_db_storage(self):
        """
        function Test that models/engine/db_storage.py conforms to PEP8.
        """
        pep8_check = pycodestyle.StyleGuide(quiet=True)
        result = pep8_check.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
        
    def test_dbs_func_docstrings(self):
        """
        function Tests for the presence of doc strings in DBStorage methods
        """
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_db_storage_module_docstring(self):
        """
        function Tests for the db_storage.py module docstring
        """
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """
        function Tests for the DBStorage class docstring
        """
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")


class TestFileStorage(unittest.TestCase):
    """
    CLASS contains functions that will Test the FileStorage
    """
    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """
        function Test that all returns of a dictionary object
        """
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_new(self):
        """
        function test that new adds an object to the database
        """

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """
        function Test that all returns all rows when no class is passed
        """

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_save(self):
        """
        function Test that save properly saves objects to file.json
        """
