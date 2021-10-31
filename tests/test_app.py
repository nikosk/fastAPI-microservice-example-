from fastapi.testclient import TestClient

from app.dbapi import delete_user, create_user
from app.main import app

client = TestClient(app)


def test_create_user():
    email = "email@example.com"
    password = "aPassword"
    response = client.post(
        "/api/user/",
        json={"email": email, "password": password, "passwordConfirm": password}
    )
    assert response.status_code == 200
    json = response.json()
    assert json["id"] is not None
    assert json["email"] == email
    assert json["password"] == password
    delete_user(json["id"])


def test_create_user_duplicate_email():
    email = "email+1@example.com"
    password = "aPassword"
    user, error = create_user(email, password)
    response = client.post(
        "/api/user/",
        json={"email": email, "password": password, "passwordConfirm": password}
    )
    assert response.status_code == 422
    json = response.json()
    assert json["message"] == "Email already exists"
    delete_user(user.id)
