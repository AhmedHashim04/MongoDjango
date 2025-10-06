# MongoDjango

This repo saves my steps while practicing MongoDB with Django.

## Overview

This is a Django project configured to work with MongoDB using PyMongo. It provides a REST API for basic CRUD operations on a users collection, serving as a learning platform for MongoDB operations in Django.

## Features

- ✅ Django 4.2 project structure
- ✅ MongoDB integration using PyMongo
- ✅ RESTful API endpoints for user management
- ✅ Clean separation of MongoDB utilities
- ✅ Example views and URL routing
- ✅ Simple web interface with API documentation

## Prerequisites

- Python 3.8 or higher
- MongoDB installed and running locally (or accessible remotely)
- pip (Python package manager)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AhmedHashim04/MongoDjango.git
   cd MongoDjango
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure MongoDB connection:**
   
   Edit `mongoproject/settings.py` and uncomment/configure the MongoDB settings:
   ```python
   MONGODB_SETTINGS = {
       'HOST': 'mongodb://localhost:27017/',
       'DATABASE': 'mongodjango_db',
   }
   ```

4. **Run Django migrations (for default SQLite tables):**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   
   Open your browser and navigate to: `http://localhost:8000`

## Project Structure

```
MongoDjango/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── mongoproject/             # Main project directory
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   └── ...
└── practice/                 # MongoDB practice app
    ├── mongo_utils.py       # MongoDB connection utilities
    ├── views.py             # API views for CRUD operations
    ├── urls.py              # App URL configuration
    └── templates/           # HTML templates
```

## API Endpoints

### List all users
```bash
GET /api/users/
```

### Create a new user
```bash
POST /api/users/create/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 30
}
```

### Get a specific user
```bash
GET /api/users/<user_id>/
```

### Update a user
```bash
PUT /api/users/<user_id>/update/
Content-Type: application/json

{
  "age": 31
}
```

### Delete a user
```bash
DELETE /api/users/<user_id>/delete/
```

## Example Usage

### Using curl:

**Create a user:**
```bash
curl -X POST http://localhost:8000/api/users/create/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Smith", "email": "jane@example.com", "age": 25}'
```

**Get all users:**
```bash
curl http://localhost:8000/api/users/
```

**Get a specific user:**
```bash
curl http://localhost:8000/api/users/507f1f77bcf86cd799439011/
```

**Update a user:**
```bash
curl -X PUT http://localhost:8000/api/users/507f1f77bcf86cd799439011/update/ \
  -H "Content-Type: application/json" \
  -d '{"age": 26}'
```

**Delete a user:**
```bash
curl -X DELETE http://localhost:8000/api/users/507f1f77bcf86cd799439011/delete/
```

### Using Python requests:

```python
import requests
import json

# Create a user
response = requests.post(
    'http://localhost:8000/api/users/create/',
    json={"name": "John Doe", "email": "john@example.com", "age": 30}
)
print(response.json())

# Get all users
response = requests.get('http://localhost:8000/api/users/')
print(response.json())
```

## MongoDB Operations

The `practice/mongo_utils.py` module provides helper functions for MongoDB operations:

- `get_mongo_client()` - Get MongoDB client connection
- `get_mongo_db()` - Get database instance
- `get_collection(collection_name)` - Get a specific collection

You can use these utilities in your own views to perform MongoDB operations.

## Learning Resources

- [MongoDB Official Documentation](https://docs.mongodb.com/)
- [PyMongo Documentation](https://pymongo.readthedocs.io/)
- [Django Documentation](https://docs.djangoproject.com/)

## Notes

- This project uses SQLite for Django's internal tables (sessions, auth, etc.) and MongoDB for application data
- The MongoDB connection is configured in `settings.py` under `MONGODB_SETTINGS`
- All user data is stored in MongoDB's `users` collection
- Make sure MongoDB is running before starting the Django server

## Contributing

Feel free to fork this repository and submit pull requests for any improvements!

## License

This is a learning project and is open for anyone to use and learn from.

