#!/usr/bin/python3
"""
tests basemodel
"""
import unittest
import os
from datetime import datetime
from unittest.mock import MagicMock
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """
    class with test cases
    """
    def test_init(self):
        """
        tests initializers
        """
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_save(self):
        """
        tests the saving mod
        """
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, initial_updated_at)

    def test_to_dict(self):
        """
        tests the dict mod
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()

        expected_keys = {'id', 'created_at', 'updated_at', '__class__'}
        self.assertEqual(set(obj_dict.keys()), expected_keys)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_str(self):
        """
        test the str mod
        """
        obj = BaseModel()
        expected_str = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_str)

    def test_created_at(self):
        """
        tests the created_at mod
        """
        custom_created_at = datetime(2023, 11, 8, 12, 0, 0)
        with unittest.mock.patch('models.base_model.datetime') as mock_datetime:
            mock_datetime.now.return_value = custom_created_at
            obj = BaseModel()
            self.assertEqual(obj.created_at, custom_created_at)

    def test_updated_at(self):
        """
        tests the update_at mod after a save
        """
        obj = BaseModel()
        custom_updated_at = datetime(2023, 11, 8, 12, 0, 0)
        with unittest.mock.patch('models.base_model.datetime') as mock_datetime:
            mock_datetime.now.return_value = custom_updated_at
            obj.save()
            self.assertEqual(obj.updated_at, custom_updated_at)

if __name__ == '__main__':
    unittest.main()
