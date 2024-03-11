#!/usr/bin/python3
"""This module contains all the test cases for the console.py file."""
import unittest
import os
import sys
from io import StringIO
from console import HBNBCommand
from unittest.mock import patch
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):
    """Test cases for the console module."""
    def setUp(self):
        """Set up the test environment."""
        self.console = HBNBCommand()
        self.mock_stdin = patch('sys.stdin', StringIO())
        self.mock_stdin.start()
        self.mock_stdout = patch('sys.stdout', StringIO())
        self.mock_stdout.start()

    def tearDown(self):
        """Tear down the test environment."""
        self.mock_stdin.stop()
        self.mock_stdout.stop()
    
    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(f.getvalue(), "")
    
    def test_EOF(self):
        """Test the EOF command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(f.getvalue(), "")
    
    def test_help(self):
        """Test the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help quit"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help EOF"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help create"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help show"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help destroy"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help all"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help update"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help count"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help show BaseModel"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help show User"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help show State"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help show City"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help show Place"))
        with patch('sys.stdout', new=StringIO()):
            self.assertFalse(self.console.onecmd("help show Amenity"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help show Review"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help destroy BaseModel"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help destroy User"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help destroy State"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help destroy City"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help destroy Place"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help destroy Amenity"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help destroy Review"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help all BaseModel"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help all User"))

    def test_emptyline(self):
        """Test the emptyline command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("\n"))
            self.assertEqual(f.getvalue(), "")

    def test_create(self):
        """Test the create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Review")
            self.assertTrue(f.getvalue() != "")
    
    def create_edge_cases(self):
        """Test the create command with edge cases."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create MyModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_show(self):
        """Test the show command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show State")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show City")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Place")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Amenity")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Review")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        createe= self.console.onecmd("create BaseModel")
        #get id of the created from the output
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {createe}")
            self.assertTrue(f.getvalue() != "")
    
    def test_destroy(self):
        """Test the destroy command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy State")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy City")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy Place")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy Amenity")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy Review")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        createe= self.console.onecmd("create BaseModel")
        #get id of the created from the output
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {createe}")
            self.assertEqual(f.getvalue(), "** no instance found **\n")
    
    def test_all(self):
        """Test the all command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all State")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all City")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all Place")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all Amenity")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all Review")
            self.assertEqual(f.getvalue(), "[]\n")
        createe= self.console.onecmd("create BaseModel")
        #get id of the created from the output
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"all BaseModel")
            self.assertTrue(f.getvalue() != "[]\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"all")
            self.assertTrue(f.getvalue() != "[]\n")
    
    def test_update(self):
        """Test the update command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update State")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update City")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update Place")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update Amenity")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update Review")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        createe= self.console.onecmd("create BaseModel")
        #get id of the created from the output
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {createe}")
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {createe} name")
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        new_instance = BaseModel()
        new_instance.save()
        createe= new_instance.id
        #missing value and attribute
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {createe}")
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {createe} name")
            self.assertEqual(f.getvalue(), "** value missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {createe} name 'Betty'")
            self.assertEqual(f.getvalue(), "")
        #delete the created instance
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {createe}")
            self.assertEqual(f.getvalue(), "")
    
    def test_class_name_with_all(self):
        """This method tests the all command with class name.
        like BaseModel.all()"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.all()")
            self.assertNotEqual(f.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.all()")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State.all()")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.all()")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Place.all()")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Amenity.all()")
            self.assertEqual(f.getvalue(), "[]\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Review.all()")
            self.assertEqual(f.getvalue(), "[]\n")
        # wrong class name
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Bas.all()")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
    
    def test_count(self):
        """This method tests the count command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.count()")
            self.assertNotEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.count()")
            self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State.count()")
            self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.count()")
            self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Place.count()")
            self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Amenity.count()")
            self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Review.count()")
            self.assertEqual(f.getvalue(), "0\n")
        # wrong class name
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Bas.count()")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
    
    def test_show_with_class_name(self):
        """This method tests the show command with class name.
        like BaseModel.show()"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.show()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.show()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State.show()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.show()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Place.show()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Amenity.show()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Review.show()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        # wrong class name
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Bas.show()")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        
        # create a new instance of each class and try show of them
        
        # BaseModel
        new_instance = BaseModel()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"BaseModel.show({createe})")
            self.assertTrue(f.getvalue() != "")
        # User
        new_instance = User()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"User.show({createe})")
            self.assertTrue(f.getvalue() != "")
        # State
        new_instance = State()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"State.show({createe})")
            self.assertTrue(f.getvalue() != "")
        # City
        new_instance = City()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"City.show({createe})")
            self.assertTrue(f.getvalue() != "")
        # Place
        new_instance = Place()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"Place.show({createe})")
            self.assertTrue(f.getvalue() != "")
        # Amenity
        new_instance = Amenity()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"Amenity.show({createe})")
            self.assertTrue(f.getvalue() != "")
        # Review
        new_instance = Review()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"Review.show({createe})")
            self.assertTrue(f.getvalue() != "")
        
    def test_destroy_with_class_name(self):
        """This method tests the destroy command with class name.
        like BaseModel.destroy()"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.destroy()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.destroy()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State.destroy()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.destroy()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Place.destroy()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Amenity.destroy()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Review.destroy()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        # wrong class name
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Bas.destroy()")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        
        # create a new instance of each class and try destroy of them
        
        # BaseModel
        new_instance = BaseModel()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"BaseModel.destroy({createe})")
            self.assertNotEqual(f.getvalue(), "")
        # User
        new_instance = User()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"User.destroy({createe})")
            self.assertNotEqual(f.getvalue(), "")
        # State
        new_instance = State()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new= StringIO()) as f:
            self.console.onecmd(f"State.destroy({createe})")
            self.assertNotEqual(f.getvalue(), "")
        # City
        new_instance = City()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"City.destroy({createe})")
            self.assertNotEqual(f.getvalue(), "")
        # Place
        new_instance = Place()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"Place.destroy({createe})")
            self.assertNotEqual(f.getvalue(), "")
        # Amenity
        new_instance = Amenity()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"Amenity.destroy({createe})")
            self.assertNotEqual(f.getvalue(), "")
        # Review
        new_instance = Review()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"Review.destroy({createe})")
            self.assertNotEqual(f.getvalue(), "")
        
        # wrong id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"BaseModel.destroy('123456')")
            self.assertEqual(f.getvalue(), "** no instance found **\n")
    
    def test_update_with_class_name(self):
        """This method tests the update command with class name.
        like BaseModel.update()"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.update()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.update()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State.update()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.update()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Place.update()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Amenity.update()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Review.update()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        # wrong class name
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Bas.update()")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        
        # create a new instance of each class and try update of them
        
        # BaseModel
        new_instance = BaseModel()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'BaseModel.update("{createe}")')
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'BaseModel.update("{createe}")')
            #attribute name missing
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'BaseModel.update("{createe}", "name")')
            self.assertEqual(f.getvalue(), "** value missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'BaseModel.update("{createe}", "name", "Betty")')
            self.assertEqual(f.getvalue(), "")
        #woth wrong id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'BaseModel.update("123456", "name", "Betty")')
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        # User
        new_instance = User()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'User.update("{createe}")')
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'User.update("{createe}", "name")')
            self.assertEqual(f.getvalue(), "** value missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'User.update("{createe}", "name", "Betty")')
            self.assertEqual(f.getvalue(), "")
        # State
        new_instance = State()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'State.update("{createe}")')
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'State.update("{createe}", "name")')
            self.assertEqual(f.getvalue(), "** value missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'State.update("{createe}", "name", "Betty")')
            self.assertEqual(f.getvalue(), "")
        # City
        new_instance = City()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'City.update("{createe}")')
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'City.update("{createe}", "name")')
            self.assertEqual(f.getvalue(), "** value missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'City.update("{createe}", "name", "Betty")')
            self.assertEqual(f.getvalue(), "")
        # Place
        new_instance = Place()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'Place.update("{createe}")')
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'Place.update("{createe}", "name")')
            self.assertEqual(f.getvalue(), "** value missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'Place.update("{createe}", "name", "Betty")')
            self.assertEqual(f.getvalue(), "")
        # Amenity
        new_instance = Amenity()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'Amenity.update("{createe}")')
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'Amenity.update("{createe}", "name")')
            self.assertEqual(f.getvalue(), "** value missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'Amenity.update("{createe}", "name", "Betty")')
            self.assertEqual(f.getvalue(), "")
        # Review
        new_instance = Review()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'Review.update("{createe}")')
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'Review.update("{createe}", "name")')
            self.assertEqual(f.getvalue(), "** value missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'Review.update("{createe}", "name", "Betty")')
            self.assertEqual(f.getvalue(), "")
    
    def test_update_with_class_name_and_dictonary(self):
        """This method tests the update command with class name and dictionary.
        like BaseModel.update()"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.update()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.update()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State.update()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.update()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Place.update()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Amenity.update()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Review.update()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        # wrong class name
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Bas.update()")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        
        # create a new instance of each class and try update of them
        
        # BaseModel
        new_instance = BaseModel()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'BaseModel.update("{createe}", "name", "Betty")')
            self.assertEqual(f.getvalue(), "")
        # User
        new_instance = User()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'User.update("{createe}", "name", "Betty")')
            self.assertEqual(f.getvalue(), "")
        # State
        new_instance = State()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'State.update("{createe}", "name", "Betty")')
            self.assertEqual(f.getvalue(), "")
        # City
        new_instance = City()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'City.update("{createe}", "name", "Betty")')
            self.assertEqual(f.getvalue(), "")
        # Place
        new_instance = Place()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'Place.update("{createe}", "name", "Betty")')
            self.assertEqual(f.getvalue(), "")
        # Amenity
        new_instance = Amenity()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'Amenity.update("{createe}", "name", "Betty")')
            self.assertEqual(f.getvalue(), "")
        # Review
        new_instance = Review()
        new_instance.save()
        createe= new_instance.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'Review.update("{createe}", "name", "Betty")')
            self.assertEqual(f.getvalue(), "")
        
        # wrong id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'BaseModel.update("123456", "name", "Betty")')
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        

if __name__ == "__main__":
    unittest.main()
