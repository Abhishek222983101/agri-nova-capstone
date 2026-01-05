import pytest
from src.predict import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_rice(client):
    """Test if the model correctly predicts Rice for high rainfall"""
    farmer_data = {
        "N": 90, "P": 42, "K": 43,
        "temperature": 20.8, "humidity": 82.0, 
        "ph": 6.5, "rainfall": 202.9
    }
    
    response = client.post('/predict', json=farmer_data)
    assert response.status_code == 200
    assert response.json['recommended_crop'] == 'rice'
    assert response.json['status'] == 'success'

def test_validation_error(client):
    """Test if the API blocks invalid data"""
    bad_data = {
        "N": -50, "P": 42, "K": 43,
        "temperature": 20.8, "humidity": 82.0, 
        "ph": 6.5, "rainfall": 202.9
    }
    
    response = client.post('/predict', json=bad_data)
    assert response.status_code == 400
    assert 'error' in response.json
