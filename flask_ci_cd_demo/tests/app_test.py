"""
    Verify that the Flask app returns 'DevOps CI/CD demo' when visiting the root.
"""

import pytest
from flask_ci_cd_demo.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    
    # Use context manager to ensure resources are cleaned up after the test
    with app.test_client() as client:
        yield client    # similar to 'return client', but allows executing additional code after the test
        # Optional teardown code can be placed here
        # Currently no teardown is needed since the app is simple

def test_home(client):

    # Simulate a GET request
    resp = client.get("/")

    # Check that the HTTP status code is 200 (success)
    assert resp.status_code == 200

    # Verify that the response contains the expected content
    assert b"DevOps CI/CD demo" in resp.data