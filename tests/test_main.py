from main import webserver
import flask
import pytest
 
@pytest.fixture
def client():
    app = webserver()
    return app.test_client()    

#==================INDEX ROUTE TESTS=====================# 
def test_if_index_route_works (client):
    response = client.get('/')
    assert response.status_code==200

def test_if_index_has_its_key_button (client):
    response = client.get('/')
    assert b'<a href="#about" class="get-started-btn scrollto">Get Started</a>' in response.data

def test_if_index_has_emailto_link (client):
    response = client.get('/')
    assert b'<a href="mailto:contact@neveralone.com">contact@neveralone.com</a>' in response.data

def test_if_index_has_callto_link (client):
    response = client.get('/')
    assert b'<a href="tel:+34640518009">+34 640 51 80 09</a>' in response.data
