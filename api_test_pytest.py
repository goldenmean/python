
import requests
import pytest
import json


# Base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

def get_post(post_id):
    """Helper function to get a post by its ID"""
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    return response

def test_get_post_success():
    """Test successful retrieval of a post"""
    response = get_post(1)
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1
    assert 'title' in data
    assert 'body' in data

def test_get_post_not_found():
    """Test retrieval of a non-existent post"""
    response = get_post(999999)  # This ID doesn't exist
    assert response.status_code == 404

def test_create_post():
    """Test creation of a new post"""
    new_post = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    data = response.json()
    assert data['title'] == 'foo'
    assert data['body'] == 'bar'
    assert data['userId'] == 1
    assert 'id' in data

def test_update_post():
    """Test updating an existing post"""
    updated_post = {
        'id': 1,
        'title': 'updated title',
        'body': 'updated body',
        'userId': 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=updated_post)
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == 'updated title'
    assert data['body'] == 'updated body'

def test_delete_post():
    """Test deleting a post"""
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

@pytest.mark.parametrize("post_id, expected_keys", [
    (1, ['userId', 'id', 'title', 'body']),
    (2, ['userId', 'id', 'title', 'body']),
    (3, ['userId', 'id', 'title', 'body']),
])
def test_post_structure(post_id, expected_keys):
    """Test the structure of posts"""
    response = get_post(post_id)
    assert response.status_code == 200
    data = response.json()
    assert all(key in data for key in expected_keys)

def test_response_headers():
    """Test the response headers"""
    response = get_post(1)
    assert 'application/json' in response.headers['Content-Type']
    assert 'charset=utf-8' in response.headers['Content-Type']

def test_response_time():
    """Test the response time"""
    response = get_post(1)
    assert response.elapsed.total_seconds() < 1  # Assuming response should be under 1 second

# Execute this pytests as 
# pytest -vv --log-cli-level=DEBUG/INFO/WARNING/ERROR 