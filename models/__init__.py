#!/usr/bin/python3
"""This is to make a singletos instance of the FileStorage
class and reload the objects from the file to storage automatically
when the module is imported"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
