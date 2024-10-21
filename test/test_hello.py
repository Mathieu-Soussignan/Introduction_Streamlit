import pytest
import pandas as pd
from hello import load_data, filter_data, get_species_details

@pytest.fixture
def sample_data():
    """Fixture pour les données de test."""
    return load_data()

def test_load_data(sample_data):
    """Teste si les données sont correctement chargées."""
    assert isinstance(sample_data, pd.DataFrame), "Les données doivent être un DataFrame"
    assert not sample_data.empty, "Le DataFrame ne doit pas être vide"
    assert 'species' in sample_data.columns, "Le DataFrame doit contenir la colonne 'species'"

def test_filter_data(sample_data):
    """Teste si le filtrage des colonnes fonctionne correctement."""
    selected_columns = ['sepal_length', 'sepal_width']
    filtered_df = filter_data(sample_data, selected_columns)
    assert list(filtered_df.columns) == selected_columns, "Les colonnes filtrées ne correspondent pas aux colonnes sélectionnées"
    assert len(filtered_df) == len(sample_data), "Le nombre de lignes ne doit pas changer lors du filtrage"

def test_get_species_details(sample_data):
    """Teste si les détails d'une espèce sont correctement retournés."""
    species = 'setosa'
    species_details = get_species_details(sample_data, species)
    assert not species_details.empty, "Le DataFrame filtré ne doit pas être vide"
    assert all(species_details['species'] == species), "Toutes les lignes doivent correspondre à l'espèce sélectionnée"