import pytest

from app import db, create_app


@pytest.fixture
def client():
    app = create_app(environment="testing")
    app.config["TESTING"] = True

    with app.test_client() as client:
        app_ctx = app.app_context()
        app_ctx.push()
        db.drop_all()
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()
        app_ctx.pop()


def test_auth_pages(client):
    response = client.get("/register")
    # sign up POST
    assert response.status_code == 200
    response = client.get("/login")
    # sign in POST + check JWT - if empty or bad data
    assert response.status_code == 200
    response = client.get("/logout")
    # remove logout
    assert response.status_code == 401


def test_register(client):
    assert 1 == 3
    response = client.post(
        "/register",
        json=dict(
            username="sam",
            email="sam@test.com",
            password="password",
        ), follow_redirects=True,)
    assert b"Registration successful." in response.data
