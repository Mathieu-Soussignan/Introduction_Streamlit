import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Titre de l'application
st.title("Outil d'analyse de données interactif")

# Chargement des données
st.header("Chargement des données")
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type=["csv"])

if uploaded_file is not None:
    # Lecture du fichier CSV
    data = pd.read_csv(uploaded_file)

    # Afficher les premières lignes du DataFrame
    st.subheader("Aperçu des données")
    st.write(data.head())

    # Afficher les statistiques descriptives
    st.subheader("Statistiques descriptives")
    st.write(data.describe())

    # Exploration des données
    st.header("Exploration des données")

    # Sélection des colonnes à afficher
    all_columns = data.columns.tolist()
    selected_columns = st.multiselect("Sélectionnez les colonnes à afficher", all_columns, default=all_columns)
    st.write(data[selected_columns])

    # Visualisation simple
    st.header("Visualisation")
    st.subheader("Nuage de points")
    col_x = st.selectbox("Choisissez la colonne pour l'axe des X", all_columns)
    col_y = st.selectbox("Choisissez la colonne pour l'axe des Y", all_columns)

    # Création du nuage de points
    if col_x and col_y:
        fig, ax = plt.subplots()
        sns.scatterplot(data=data, x=col_x, y=col_y, ax=ax)
        plt.title(f"Nuage de points : {col_x} vs {col_y}")
        st.pyplot(fig)