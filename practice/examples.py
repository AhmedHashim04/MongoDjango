"""
Example MongoDB operations for practice.

This file demonstrates various MongoDB operations using PyMongo.
Uncomment and run these examples in Django shell or create views for them.
"""

from practice.mongo_utils import get_collection
from bson import ObjectId


def example_insert_one():
    """Insert a single document."""
    collection = get_collection('users')
    user = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'age': 30,
        'city': 'New York'
    }
    result = collection.insert_one(user)
    print(f"Inserted user with ID: {result.inserted_id}")
    return result.inserted_id


def example_insert_many():
    """Insert multiple documents."""
    collection = get_collection('users')
    users = [
        {'name': 'Jane Smith', 'email': 'jane@example.com', 'age': 25},
        {'name': 'Bob Johnson', 'email': 'bob@example.com', 'age': 35},
        {'name': 'Alice Brown', 'email': 'alice@example.com', 'age': 28}
    ]
    result = collection.insert_many(users)
    print(f"Inserted {len(result.inserted_ids)} users")
    return result.inserted_ids


def example_find_all():
    """Find all documents."""
    collection = get_collection('users')
    users = list(collection.find())
    for user in users:
        print(f"{user['name']} - {user['email']}")
    return users


def example_find_one():
    """Find a single document."""
    collection = get_collection('users')
    user = collection.find_one({'name': 'John Doe'})
    if user:
        print(f"Found: {user['name']} - {user['email']}")
    return user


def example_find_with_filter():
    """Find documents with filter."""
    collection = get_collection('users')
    # Find users older than 25
    users = list(collection.find({'age': {'$gt': 25}}))
    print(f"Found {len(users)} users older than 25")
    return users


def example_update_one():
    """Update a single document."""
    collection = get_collection('users')
    result = collection.update_one(
        {'name': 'John Doe'},
        {'$set': {'age': 31, 'city': 'Boston'}}
    )
    print(f"Modified {result.modified_count} document(s)")
    return result


def example_update_many():
    """Update multiple documents."""
    collection = get_collection('users')
    result = collection.update_many(
        {'age': {'$lt': 30}},
        {'$set': {'status': 'young'}}
    )
    print(f"Modified {result.modified_count} document(s)")
    return result


def example_delete_one():
    """Delete a single document."""
    collection = get_collection('users')
    result = collection.delete_one({'name': 'John Doe'})
    print(f"Deleted {result.deleted_count} document(s)")
    return result


def example_delete_many():
    """Delete multiple documents."""
    collection = get_collection('users')
    result = collection.delete_many({'age': {'$gt': 30}})
    print(f"Deleted {result.deleted_count} document(s)")
    return result


def example_count_documents():
    """Count documents."""
    collection = get_collection('users')
    total = collection.count_documents({})
    print(f"Total users: {total}")
    
    young_users = collection.count_documents({'age': {'$lt': 30}})
    print(f"Users under 30: {young_users}")
    
    return {'total': total, 'young': young_users}


def example_aggregation():
    """Aggregation pipeline example."""
    collection = get_collection('users')
    
    pipeline = [
        {'$match': {'age': {'$gte': 25}}},
        {'$group': {
            '_id': None,
            'average_age': {'$avg': '$age'},
            'count': {'$sum': 1}
        }}
    ]
    
    results = list(collection.aggregate(pipeline))
    if results:
        print(f"Average age: {results[0]['average_age']}")
        print(f"Count: {results[0]['count']}")
    return results


def example_sorting():
    """Sort documents."""
    collection = get_collection('users')
    
    # Sort by age descending
    users = list(collection.find().sort('age', -1))
    print("Users sorted by age (descending):")
    for user in users:
        print(f"{user['name']} - Age: {user['age']}")
    return users


def example_projection():
    """Use projection to select specific fields."""
    collection = get_collection('users')
    
    # Only get name and email fields
    users = list(collection.find({}, {'name': 1, 'email': 1, '_id': 0}))
    for user in users:
        print(f"{user['name']} - {user['email']}")
    return users


# To run these examples in Django shell:
# python manage.py shell
# from practice.examples import *
# example_insert_one()
# example_find_all()
# etc.
