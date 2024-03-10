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
        self.assertEqual(self.base_model1.updated_at, base_model1_created_at)
        self.assertEqual(self.base_model2.updated_at, base_model2_created_at)
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
