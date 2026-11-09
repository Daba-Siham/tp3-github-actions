import pytest
from app.web import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_message_normal(client):
    reponse = client.post(
        "/moderate",
        json={"message": "bonjour"}
    )

    assert reponse.status_code == 200
    assert reponse.get_json() == {"decision": "autoriser"}


def test_message_spam(client):
    reponse = client.post(
        "/moderate",
        json={"message": "ceci est du SPAM"}
    )

    assert reponse.status_code == 200
    assert reponse.get_json() == {"decision": "bloquer"}


def test_message_absent(client):
    reponse = client.post(
        "/moderate",
        json={}
    )

    assert reponse.status_code == 400
    assert reponse.get_json() == {"error": "Invalid message"}


def test_message_nombre(client):
    reponse = client.post(
        "/moderate",
        json={"message": 42}
    )

    assert reponse.status_code == 400
    assert reponse.get_json() == {"error": "Invalid message"}


def test_message_espaces(client):
    reponse = client.post(
        "/moderate",
        json={"message": "   "}
    )

    assert reponse.status_code == 400
    assert reponse.get_json() == {"error": "Invalid message"}


def test_message_liste(client):
    reponse = client.post(
        "/moderate",
        json=[]
    )

    assert reponse.status_code == 400
    assert reponse.get_json() == {"error": "JSON object required"}