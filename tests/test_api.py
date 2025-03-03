import pytest
import requests
from app import app 


class FakeResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.RequestException("API Error")


def fake_requests_get_success(url):
    fake_data = {
        "tax_brackets": [
            {"min": 0, "max": 50197, "rate": 0.15},
            {"min": 50197, "max": 100392, "rate": 0.205},
            {"min": 100392, "max": 155625, "rate": 0.26},
            {"min": 155625, "max": 221708, "rate": 0.29},
            {"min": 221708, "rate": 0.33}
        ]
    }
    return FakeResponse(fake_data, 200)


def fake_requests_get_failure(url):
    return FakeResponse({}, 500)


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_tax_calculator_success(monkeypatch, client):

    monkeypatch.setattr(requests, "get", fake_requests_get_success)


    response = client.get("/tax_calculator/?salary=60000&tax_year=2021")
    assert response.status_code == 200

    data = response.get_json()

    assert "total_tax" in data
    assert "effective_rate" in data
    assert "tax_breakdown" in data


def test_tax_calculator_api_error(monkeypatch, client):

    monkeypatch.setattr(requests, "get", fake_requests_get_failure)

    response = client.get("/tax_calculator/?salary=60000&tax_year=2021")

    assert response.status_code == 502

    data = response.get_json()
    assert "message" in data
    assert data["message"] == "Error fetching tax brackets. Please try again later."

def test_tax_calculator_zero_salary(monkeypatch, client):
    salary = 0
    def fake_requests_get_should_not_be_called(url):
        pytest.fail(f"requests.get was called, but it shouldn't be for salary={salary}.")

    
    monkeypatch.setattr(requests, "get", fake_requests_get_should_not_be_called)

    response = client.get(f"/tax_calculator/?salary={salary}&tax_year=2021")
    data = response.get_json()

    
    assert response.status_code == 200
    assert data["total_tax"] == 0.0
    assert data["effective_rate"] == 0.0
    assert data["tax_breakdown"] == []