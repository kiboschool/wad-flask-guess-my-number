import pytest
from app import *

@pytest.fixture()
def client():
    return app.test_client()

def test_index_link(client):
    response = client.get("/")
    assert b"<a" in response.data
    assert b'href="/game"' in response.data or b"href='/game'" in response.data

def test_numbers_appear(client):
    response = client.get("/game")
    assert b"1" in response.data
    assert b"10" in response.data
    assert b"45" in response.data
    assert b"82" in response.data

def test_low(client):
    game = client.get("/game")
    guess = client.get("/guess/1")
    assert b"low" in guess.data or b"Low" in guess.data

def test_high(client):
    game = client.get("/game")
    guess = client.get("/guess/99")
    assert b"high" in guess.data or b"High" in guess.data

if __name__ == "__main__":
    pytest.main()
