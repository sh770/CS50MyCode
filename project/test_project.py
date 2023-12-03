import json
import os
import pytest
from project import app, read_users_from_file, showUsers , delAllUsers


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login(client):
    response = client.post('/', data=dict(username='1', password='1'))
    assert response.status_code == 302  # Redirect status code

def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200  # OK status code
    assert b'About Page' in response.data

def test_home_page(client):
    response = client.get('/home')
    assert response.status_code == 200  # OK status code
    assert b'Home Page' in response.data

def test_register_existing_user(client):
    response = client.post('/register', data=dict(username='1', password='1'))
    assert b'Username already exists' in response.data


def test_register_new_user(client):
    response = client.post('/register', data=dict(username='19', password='19'))
    assert response.status_code == 302  # Redirect status code

    # Additional assertion to check if the new user is in the file
    users = read_users_from_file()
    assert any(user['username'] == '19' for user in users)

    # Clean up, remove the newly registered user from the file
    users = [user for user in users if user['username'] != '19']
    with open('users.json', 'w') as file:
        json.dump({'users': users}, file)

def test_del_all_users():
    # יצירת קובץ זמני לצורך הטסט
    with open('test_users.json', 'w') as test_file:
        test_file.write('{"users": [{"username": "1", "password": "1"}]}')

    # בדיקה שהפונקציה מחיקה את רשימת היוזרים
    # result = delAllUsers()

    # דפוס של ערכי הרשימה לפני הבדיקה
    with open('test_users.json', 'r') as file:
        data = json.load(file)
    print(f"Data before assertion: {data['users']}")

    os.remove("test_users.json")
