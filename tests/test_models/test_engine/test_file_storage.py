#!/usr/bin/python3
"""This module contains the test for the file storage class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
import os
import json


class TestFileStorage(unittest.TestCase):
    """This class contains the tests for the file storage class"""

    @classmethod
    def setUpClass(cls):
        """This method sets up the tests"""
        cls.storage = FileStorage()
        cls.storage.reload()
        cls.model = BaseModel()
        cls.model.save()

    @classmethod
    def tearDownClass(cls):
        """This method tears down the tests"""
        os.remove("file.json")

    def test_all(self):
        """This method tests the all method of the file storage class"""
        self.assertIsInstance(self.storage.all(), dict)
        self.assertIn(f"BaseModel.{self.model.id}", self.storage.all())
        # test key and value of the dictionary
        key = f"BaseModel.{self.model.id}"
        value = self.storage.all()[key]
        self.assertIsInstance(value, BaseModel)
        self.assertDictEqual(value.to_dict(), self.model.to_dict())

    def test_new(self):
        """This method tests the new method of the file storage class"""
        model = BaseModel()
        self.storage.new(model)
        key = f"BaseModel.{model.id}"
        self.assertIn(key, self.storage.all())
        self.assertIs(self.storage.all()[key], model)
        # check if the object is saved to the file
        self.storage.save()
        with open("file.json", "r") as file:
            obj_dict = json.load(file)
            self.assertIn(key, obj_dict)
            self.assertDictEqual(obj_dict[key], model.to_dict())

        # check length of the file
        self.assertEqual(len(obj_dict), len(self.storage.all()))

    def test_save(self):
        """This method tests the save method of the file storage class"""
        model = BaseModel()
        self.storage.new(model)
        key = f"BaseModel.{model.id}"
        self.storage.save()
        with open("file.json", "r") as file:
            obj_dict = json.load(file)
            self.assertIn(key, obj_dict)
            self.assertDictEqual(obj_dict[key], model.to_dict())

        # check length of the file
        self.assertEqual(len(obj_dict), len(self.storage.all()))

    def test_reload(self):
        """This method tests the reload method of the file storage class"""
        model = BaseModel()
        model.save()
        key = f"BaseModel.{model.id}"
        self.storage.save()
        self.storage.reload()
        self.assertIn(key, self.storage.all())
        self.assertDictEqual(self.storage.all()[
                             key].to_dict(), model.to_dict())

    def test_save_reload(self):
        """This method tests the save and reload methods of the file storage class"""
        model = BaseModel()
        model.save()
        key = f"BaseModel.{model.id}"
        self.storage.save()
        self.storage.reload()
        self.assertIn(key, self.storage.all())
        self.assertDictEqual(self.storage.all()[
                             key].to_dict(), model.to_dict())

    def reolad_from_non_existent_file(self):
        """This method tests the reload method of the file storage class when the file does not exist"""
        os.remove("file.json")
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_the_class_after_adding_new_attr_to_a_model(self):
        """This method tests the class after adding new attribute to a model"""
        model = BaseModel()
        model.name = "model"
        model.save()
        key = f"BaseModel.{model.id}"
        self.storage.save()
        self.storage.reload()
        self.assertIn(key, self.storage.all())
        self.assertDictEqual(self.storage.all()[
                             key].to_dict(), model.to_dict())
    
    def testReoladingAfterEachImport(self):
        """This method tests the reloading of the storage after each import"""
        from models import storage
        storage.reload()
        self.assertIsInstance(storage.all(), dict)
        self.assertIn(f"BaseModel.{self.model.id}", storage.all())
        # test key and value of the dictionary
        key = f"BaseModel.{self.model.id}"
        value = storage.all()[key]
        self.assertIsInstance(value, BaseModel)
        self.assertDictEqual(value.to_dict(), self.model.to_dict())
    
    def testInvokingSaveAfterEachImport(self):
        """This method tests the invoking of the save method after each import"""
        from models import storage
        storage.save()
        with open("file.json", "r") as file:
            obj_dict = json.load(file)
            self.assertIn(f"BaseModel.{self.model.id}", obj_dict)
            self.assertDictEqual(obj_dict[f"BaseModel.{self.model.id}"], self.model.to_dict())
    
    def testCallingNewSelfIfNotInstanciatingFromDictionary(self):
        """This method tests the calling of new method if not instanciating from dictionary"""
        model = BaseModel()
        model.save()
        key = f"BaseModel.{model.id}"
        self.storage.save()
        self.storage.reload()
        self.assertIn(key, self.storage.all())
        self.assertDictEqual(self.storage.all()[
                             key].to_dict(), model.to_dict())
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        self.assertIn(key, self.storage.all())
        self.assertDictEqual(self.storage.all()[
                             key].to_dict(), model.to_dict())

    # Test calling the 'new' method for a model instance that was not instantiated from a dictionary
    def test_call_new_method_for_non_dict_model_instance(self):
        """This method tests calling the 'new' method for a model instance that was not instantiated from a dictionary"""
        model = BaseModel()
        self.storage.new(model)
        key = f"BaseModel.{model.id}"
        self.assertIn(key, self.storage.all())
        self.assertIs(self.storage.all()[key], model)
        # check if the object is saved to the file
        self.storage.save()
        with open("file.json", "r") as file:
            obj_dict = json.load(file)
            self.assertIn(key, obj_dict)
            self.assertDictEqual(obj_dict[key], model.to_dict())

        # check length of the file
        self.assertEqual(len(obj_dict), len(self.storage.all()))

        # Test saving a model instance with additional attributes and reloading the storage
    def test_save_model_with_additional_attributes_and_reload(self):
        """This method tests saving a model instance with additional attributes and reloading the storage"""
        model = BaseModel()
        model.name = "model"
        self.storage.new(model)
        key = f"BaseModel.{model.id}"
        self.assertIn(key, self.storage.all())
        self.assertIs(self.storage.all()[key], model)
        # check if the object is saved to the file
        self.storage.save()
        self.storage.reload()
        self.assertIn(key, self.storage.all())
        self.assertDictEqual(self.storage.all()[key].to_dict(), model.to_dict())


if __name__ == "__main__":
    unittest.main()
