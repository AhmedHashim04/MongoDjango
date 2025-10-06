"""
MongoDB connection utility module.

This module provides a simple interface to connect to MongoDB
and perform basic operations.
"""

from pymongo import MongoClient
from django.conf import settings


def get_mongo_client():
    """
    Get MongoDB client instance.
    
    Returns:
        MongoClient: MongoDB client connection
    """
    mongodb_settings = getattr(settings, 'MONGODB_SETTINGS', {})
    host = mongodb_settings.get('HOST', 'mongodb://localhost:27017/')
    return MongoClient(host)


def get_mongo_db():
    """
    Get MongoDB database instance.
    
    Returns:
        Database: MongoDB database
    """
    mongodb_settings = getattr(settings, 'MONGODB_SETTINGS', {})
    db_name = mongodb_settings.get('DATABASE', 'mongodjango_db')
    client = get_mongo_client()
    return client[db_name]


def get_collection(collection_name):
    """
    Get MongoDB collection instance.
    
    Args:
        collection_name (str): Name of the collection
        
    Returns:
        Collection: MongoDB collection
    """
    db = get_mongo_db()
    return db[collection_name]
