#!/usr/bin/python3
""" __init__ to connect the engine with other classes"""
from models.engine.file_storage import FileStorage

eng = FileStorage()
eng.reload()
