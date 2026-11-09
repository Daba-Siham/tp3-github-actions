import pytest
from unittest.mock import Mock
from app.moderation import decider

def test_moderation_spam():
    modele = Mock()
    modele.predict.return_value = "spam"
    resultat = decider(modele, "Offre miracle")
    assert resultat == "bloquer"
    modele.predict.assert_called_once_with("Offre miracle")

def test_moderation_normal():
    modele = Mock()
    modele.predict.return_value = "normal"
    resultat = decider(modele, "Bonjour")
    assert resultat == "autoriser"
    modele.predict.assert_called_once_with("Bonjour")

def test_moderation_modele_indisponible():
    modele = Mock()
    modele.predict.side_effect = RuntimeError("Modele indisponible")
    with pytest.raises(RuntimeError):
        decider(modele, "Message test")