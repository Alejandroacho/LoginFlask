from main import webserver
import pytest
 
@pytest.fixture
def client():
    app = webserver()
    return app.test_client()    
 
def test_index_pages_works(client):
    response = client.get('/')
    assert response.status_code==200

#def test_index_pages_works(client):
#    response = client.get('mailto:contact@neveralone.com')
#    assert response.status_code==200