#!/usr/bin/python3
"""
Reload storage everytime package is initialized
"""

from models.engine.storage import DB_storage

storage = DB_storage()
storage.reload()