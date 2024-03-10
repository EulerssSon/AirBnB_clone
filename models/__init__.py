#!/usr/bin/python3
""" __init__ to connect the engine with other classes"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
