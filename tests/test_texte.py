import pytest
from app.texte import nettoyer_texte


@pytest.mark.parametrize("entree, attendu", [
    ("  BONJOUR   monde  ", "bonjour monde"),
    (" déjà propre ", "déjà propre"),
    ("", ""),
    ("     ", ""),
    ("PYTHON", "python")
])
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu


def test_nettoyer_texte_entier():
    with pytest.raises(TypeError):
        nettoyer_texte(123)


def test_nettoyer_texte_none():
    with pytest.raises(TypeError):
        nettoyer_texte(None)


def test_nettoyage_idempotent():
    texte = "  BONJOUR   monde  "
    resultat = nettoyer_texte(texte)

    assert nettoyer_texte(resultat) == resultat