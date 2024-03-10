#!/usr/bin/python3
"""This module is for testing the base model class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import json
import os


class TestBaseModel(unittest.TestCase):
    """This class is for testing the base model class"""

    def setUp(self) -> None:
        """This method sets up the test environment"""
        self.base_model1 = BaseModel()
        self.base_model2 = BaseModel()

    def tearDown(self) -> None:
        """This method tears down the test environment"""
        del self.base_model1
        del self.base_model2

    def test_base_model_id(self):
        """This method tests the id attribute of the base model"""
        self.assertIsInstance(self.base_model1.id, str)
        self.assertNotEqual(self.base_model1.id, self.base_model2.id)

    def test_base_model_created_at(self):
        """This method tests the created_at attribute of the base model"""
        self.assertIsInstance(self.base_model1.created_at, datetime)
        self.assertIsInstance(self.base_model2.created_at, datetime)

    def test_base_model_updated_at_created_at_save_method(self):
        """This method tests the updated_at attribute of the base model"""
        self.assertIsInstance(self.base_model1.updated_at, datetime)
        self.assertIsInstance(self.base_model2.updated_at, datetime)
        base_model1_created_at = self.base_model1.created_at
        base_model2_created_at = self.base_model2.created_at
        self.assertEqual(self.base_model1.updated_at, self.base_model1.created_at)
        self.assertEqual(self.base_model2.updated_at, self.base_model2.created_at)
        sleep(1)
        self.base_model1.save()
        self.base_model2.save()
        self.assertNotEqual(self.base_model1.updated_at,
                base_model1_created_at)
        self.assertNotEqual(self.base_model2.updated_at,
                base_model2_created_at)

        def test_base_model_str(self):
            """This method tests the __str__ method of the base model"""
        self.assertIsInstance(str(self.base_model1), str)
        self.assertIsInstance(str(self.base_model2), str)
        self.assertEqual(str(
            self.base_model1), f"[BaseModel] ({self.base_model1.id}) {self.base_model1.__dict__}")
        self.assertEqual(str(
            self.base_model2), f"[BaseModel] ({self.base_model2.id}) {self.base_model2.__dict__}")

        def test_base_model_to_dict(self):
            """This method tests the to_dict method of the base model"""
        self.assertIsInstance(self.base_model1.to_dict(), dict)
        self.assertIsInstance(self.base_model2.to_dict(), dict)
        base_model1_dict = self.base_model1.to_dict()
        base_model2_dict = self.base_model2.to_dict()
        self.assertIsInstance(base_model1_dict["created_at"], str)
        self.assertIsInstance(base_model1_dict["updated_at"], str)
        self.assertIsInstance(base_model2_dict["created_at"], str)
        self.assertIsInstance(base_model2_dict["updated_at"], str)
        self.assertEqual(base_model1_dict["__class__"], "BaseModel")
        self.assertEqual(base_model2_dict["__class__"], "BaseModel")
        # test the type of the created_at and updated_at attributes
        self.assertEqual(
                base_model1_dict["created_at"], self.base_model1.created_at.isoformat())
        self.assertEqual(
                base_model1_dict["updated_at"], self.base_model1.updated_at.isoformat())
        self.assertEqual(
                base_model2_dict["created_at"], self.base_model2.created_at.isoformat())
        self.assertEqual(
                base_model2_dict["updated_at"], self.base_model2.updated_at.isoformat())

        self.assertDictEqual(base_model1_dict, self.base_model1.to_dict())
        self.assertDictEqual(base_model2_dict, self.base_model2.to_dict())

    def test_base_model_to_dict_with_adding_attributes(self):
        """This method tests the to_dict method of the base model"""
        self.base_model1.name = "John"
        self.base_model1.age = 20
        base_model1_dict = self.base_model1.to_dict()
        self.assertEqual(base_model1_dict["name"], "John")
        self.assertEqual(base_model1_dict["age"], 20)
        self.assertEqual(base_model1_dict["__class__"], "BaseModel")
        self.assertEqual(
                base_model1_dict["created_at"], self.base_model1.created_at.isoformat())
        self.assertEqual(
                base_model1_dict["updated_at"], self.base_model1.updated_at.isoformat())
        # test tat the __dict__ contains the new attributes
        self.assertEqual(self.base_model1.__dict__["name"], "John")
        self.assertEqual(self.base_model1.__dict__["age"], 20)

        # update the updated_at attribute
        self.base_model1.save()

        my_dict = self.base_model1.to_dict()
        self.assertEqual(my_dict["updated_at"],
                self.base_model1.updated_at.isoformat())

        def test_base_model_init_with_kwargs(self):
            """This method tests the __init__ method of the base model"""
        my_id = str(self.base_model1.id)
        my_created_at = self.base_model1.created_at
        my_updated_at = self.base_model1.updated_at
        model_json_dict = self.base_model1.to_dict()

        # create a new instance of the base model with the json dict
        my_new_model = BaseModel(**model_json_dict)

        self.assertEqual(my_id, my_new_model.id)
        self.assertEqual(type(my_id), type(my_new_model.id))
        self.assertEqual(my_created_at, my_new_model.created_at)
        self.assertEqual(type(my_created_at), type(my_new_model.created_at))
        self.assertEqual(my_updated_at, my_new_model.updated_at)
        self.assertEqual(type(my_updated_at), type(my_new_model.updated_at))
        self.assertDictEqual(self.base_model1.to_dict(),
                my_new_model.to_dict())
        self.assertEqual(self.base_model1.__str__(), my_new_model.__str__())
        self.assertEqual(self.base_model1.__class__, my_new_model.__class__)

    def test_base_model_init_with_kwargs(self):
        """This method tests the __init__ method of the base model"""
        my_id = str(self.base_model1.id)
        my_created_at = self.base_model1.created_at
        my_updated_at = self.base_model1.updated_at
        model_json_dict = self.base_model1.to_dict()

        # create a new instance of the base model with the json dict
        my_new_model = BaseModel(**model_json_dict)

        self.assertEqual(my_id, my_new_model.id)
        self.assertEqual(type(my_id), type(my_new_model.id))
        self.assertEqual(my_created_at, my_new_model.created_at)
        self.assertEqual(type(my_created_at), type(my_new_model.created_at))
        self.assertEqual(my_updated_at, my_new_model.updated_at)
        self.assertEqual(type(my_updated_at), type(my_new_model.updated_at))
        self.assertDictEqual(self.base_model1.to_dict(),
                my_new_model.to_dict())
        self.assertEqual(self.base_model1.__str__(), my_new_model.__str__())
        self.assertEqual(self.base_model1.__class__, my_new_model.__class__)

    def test_base_model_init_with_kwargs_with_new_attributes(self):
        """This method tests the __init__ method of the base model"""
        self.base_model1.name = "John"
        self.base_model1.age = 20
        model_json_dict = self.base_model1.to_dict()

        # create a new instance of the base model with the json dict
        my_new_model = BaseModel(**model_json_dict)

        self.assertEqual(self.base_model1.id, my_new_model.id)
        self.assertEqual(self.base_model1.created_at, my_new_model.created_at)
        self.assertEqual(self.base_model1.updated_at, my_new_model.updated_at)
        self.assertEqual(self.base_model1.name, my_new_model.name)
        self.assertEqual(self.base_model1.age, my_new_model.age)
        self.assertDictEqual(self.base_model1.to_dict(),
                my_new_model.to_dict())
        self.assertEqual(self.base_model1.__str__(), my_new_model.__str__())
        self.assertEqual(self.base_model1.__class__, my_new_model.__class__)

    def test_init_with_args_and_keyargs_and_args_are_ignore(self):
        """This method tests the __init__ method of the base model"""

        my_new_model = BaseModel("John", **self.base_model1.to_dict())
        self.assertNotIn("John", my_new_model.__dict__.values())
        self.assertNotIn("John", my_new_model.__dict__.keys())
        self.assertNotIn("John", my_new_model.__dict__.items())
        self.assertEqual(self.base_model1.id, my_new_model.id)
        self.assertEqual(self.base_model1.created_at, my_new_model.created_at)
        self.assertEqual(self.base_model1.updated_at, my_new_model.updated_at)
        self.assertDictEqual(self.base_model1.to_dict(),
                my_new_model.to_dict())
        self.assertEqual(self.base_model1.__str__(), my_new_model.__str__())
        self.assertEqual(self.base_model1.__class__, my_new_model.__class__)
