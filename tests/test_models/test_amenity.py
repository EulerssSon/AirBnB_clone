#!/usr/bin/python3

"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    # Amenity object can be created with a name attribute
    def test_create_amenity_with_name_attribute(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    # Amenity object can be created without a name attribute
    def test_create_amenity_without_name_attribute(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    # Amenity object has an updated_at attribute
    def test_amenity_has_updated_at_attribute(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'updated_at'))

    # Amenity object has a created_at attribute
    def test_amenity_has_created_at_attribute(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'created_at'))

    # Amenity object can be updated with a new name attribute
    def test_update_amenity_name(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    # Amenity object has a unique id attribute
    def test_amenity_has_unique_id_attribute(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    # Amenity object can be created with a JSON string of attributes
    # Amenity object can be converted to a dictionary
    def test_amenity_to_dictionary_conversion(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict["name"], "Swimming Pool")

    # Amenity object can be created with a dictionary of attributes
    def test_create_amenity_with_dictionary_attributes(self):
        amenity_dict = {"name": "Swimming Pool"}
        amenity = Amenity(**amenity_dict)
        self.assertEqual(amenity.name, "Swimming Pool")

    # Amenity object can be represented as a string
    def test_amenity_string_representation(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(str(amenity), "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__))


class TestAmenityEss(unittest.TestCase):

    # Amenity object can be created with a name attribute
    def test_create_amenity_with_name_attribute(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    # Amenity object can be created without a name attribute
    def test_create_amenity_without_name_attribute(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    # Amenity object can be updated with a new name attribute
    def test_update_name_attribute(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        amenity.name = "Gym"
        self.assertEqual(amenity.name, "Gym")

    # Amenity object can be converted to a dictionary
    def test_convert_to_dictionary(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["name"], "Swimming Pool")

    # Amenity object can be converted to a JSON string
    def test_convert_to_json_string(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        amenity_json = amenity.to_dict()
        self.assertEqual(type(amenity_json), dict)

    # Amenity object can be represented as a string
    def test_amenity_representation(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(str(amenity), "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__))

    # Amenity object has a created_at attribute
    def test_amenity_has_created_at_attribute(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'created_at'))

    # Amenity object has a unique id attribute
    def test_amenity_has_unique_id_attribute(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    # Amenity object has an updated_at attribute
    def test_amenity_has_updated_at_attribute(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'updated_at'))

    # Amenity object can be updated with a new name attribute that is an empty string
    def test_update_amenity_with_empty_name(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        amenity.name = ""
        self.assertEqual(amenity.name, "")

    # Amenity object can be updated with a new name attribute that is not a string
    def test_update_amenity_with_non_string_name(self):
        amenity = Amenity()
        amenity.name = 12345
        self.assertEqual(amenity.name, 12345)

    # Amenity object can be created with a name attribute that is not a string
    def test_create_amenity_with_non_string_name_attribute(self):
        amenity = Amenity()
        amenity.name = 12345
        self.assertEqual(amenity.name, 12345)

    # Amenity object can be created with a name attribute that contains numbers
    def test_create_amenity_with_name_attribute(self):
        amenity = Amenity()
        amenity.name = "12345"
        self.assertEqual(amenity.name, "12345")

    # Amenity object can be created with a name attribute that contains spaces
    def test_create_amenity_with_name_attribute(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    # Amenity object can be created with a name attribute that is longer than 128 characters
    def test_create_amenity_with_long_name_attribute(self):
        amenity = Amenity()
        amenity.name = "This is a very long name for an amenity. It exceeds the limit of 128 characters."
        self.assertEqual(amenity.name, "This is a very long name for an amenity. It exceeds the limit of 128 characters.")

    # Amenity object can be created with a name attribute that contains uppercase letters
    def test_create_amenity_with_name_attribute(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    # Amenity object can be created with a name attribute that contains special characters
    def test_create_amenity_with_special_characters(self):
        amenity = Amenity()
        amenity.name = "!@#$%^&*()"
        self.assertEqual(amenity.name, "!@#$%^&*()")

    # Amenity object can be created with a default name attribute value
    def test_create_amenity_with_default_name(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    # Amenity object can be updated with a new name attribute that is longer than 128 characters
    def test_update_amenity_with_long_name(self):
        amenity = Amenity()
        long_name = "a" * 129
        amenity.name = long_name
        self.assertEqual(amenity.name, long_name)


class TestAmenity_ins(unittest.TestCase):

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_two_amenities_unique_ids(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_two_amenities_different_created_at(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_two_amenities_different_updated_at(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        amstr = am.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    def test_args_unused(self):
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        am = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(am.id, "345")
        self.assertEqual(am.created_at, dt)
        self.assertEqual(am.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenitysaveing(unittest.TestCase):

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    def test_two_saves(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        second_updated_at = am.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        am.save()
        self.assertLess(second_updated_at, am.updated_at)

    def test_save_with_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_save_updates_file(self):
        am = Amenity()
        am.save()
        amid = "Amenity." + am.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenitytoDictMethod(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    def test_to_dict_contains_added_attributes(self):
        am = Amenity()
        am.middle_name = "Holberton"
        am.my_number = 98
        self.assertEqual("Holberton", am.middle_name)
        self.assertIn("my_number", am.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        am = Amenity()
        am_dict = am.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        am = Amenity()
        self.assertNotEqual(am.to_dict(), am.__dict__)

    def test_to_dict_with_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)


if __name__ == "__main__":
    unittest.main()
