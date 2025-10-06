from django.shortcuts import render
from django.http import JsonResponse
from .mongo_utils import get_collection
from bson import ObjectId
import json


def index(request):
    """
    Index view with MongoDB practice examples.
    """
    context = {
        'title': 'MongoDB Practice with Django',
        'description': 'This app demonstrates basic MongoDB operations'
    }
    return render(request, 'practice/index.html', context)


def list_users(request):
    """
    List all users from MongoDB.
    
    Returns:
        JsonResponse: List of users
    """
    try:
        collection = get_collection('users')
        users = list(collection.find())
        
        # Convert ObjectId to string for JSON serialization
        for user in users:
            user['_id'] = str(user['_id'])
        
        return JsonResponse({'users': users, 'count': len(users)})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def create_user(request):
    """
    Create a new user in MongoDB.
    
    Expects POST request with JSON body containing user data.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            collection = get_collection('users')
            result = collection.insert_one(data)
            
            return JsonResponse({
                'message': 'User created successfully',
                'id': str(result.inserted_id)
            }, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


def get_user(request, user_id):
    """
    Get a specific user by ID.
    
    Args:
        user_id (str): MongoDB ObjectId as string
    """
    try:
        collection = get_collection('users')
        user = collection.find_one({'_id': ObjectId(user_id)})
        
        if user:
            user['_id'] = str(user['_id'])
            return JsonResponse({'user': user})
        else:
            return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def update_user(request, user_id):
    """
    Update a user in MongoDB.
    
    Expects PUT/PATCH request with JSON body containing updated data.
    """
    if request.method in ['PUT', 'PATCH']:
        try:
            data = json.loads(request.body)
            collection = get_collection('users')
            result = collection.update_one(
                {'_id': ObjectId(user_id)},
                {'$set': data}
            )
            
            if result.matched_count:
                return JsonResponse({'message': 'User updated successfully'})
            else:
                return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Only PUT/PATCH methods are allowed'}, status=405)


def delete_user(request, user_id):
    """
    Delete a user from MongoDB.
    """
    if request.method == 'DELETE':
        try:
            collection = get_collection('users')
            result = collection.delete_one({'_id': ObjectId(user_id)})
            
            if result.deleted_count:
                return JsonResponse({'message': 'User deleted successfully'})
            else:
                return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Only DELETE method is allowed'}, status=405)

