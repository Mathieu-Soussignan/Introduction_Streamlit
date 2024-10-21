import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import logging

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)

# Fonctions utilitaires
@st.cache
def load_data():
    """Charge le jeu de données Iris."""
    logging.info("Chargement des données Iris.")
    return sns.load_dataset('iris')

def filter_data(df, selected_columns):
    """Filtre le DataFrame en fonction des colonnes sélectionnées."""
    return df[selected_columns]

def get_species_details(df, species):
    """Retourne les détails d'une espèce donnée dans le DataFrame."""
    return df[df['species'] == species]

def log_and_display_data(df):
    """Affiche les données dans Streamlit et les journalise."""
    st.dataframe(df)
    st.table(df)
    logging.info("Affichage du DataFrame et du tableau terminé.")

def log_user_interaction():
    """Gère et journalise les interactions de l'utilisateur avec les widgets."""
    if st.button("Clique-moi 😃"):
        st.write("Bouton cliqué ! 🎉")
        logging.info("Bouton 'Clique-moi' a été cliqué.")

    checkbox_value = st.checkbox("Cochez-moi ✅")
    if checkbox_value:
        st.write("Case cochée ! ✔️")
        logging.info("Case 'Cochez-moi' cochée.")

    user_input = st.text_input("Saisissez quelque chose 📝")
    st.write(f"Vous avez saisi : {user_input}")
    logging.info(f"Texte saisi par l'utilisateur : {user_input}")

    choix = st.selectbox("Choisissez une option", ["Option 1 🚀", "Option 2 🌟", "Option 3 🔥"])
    st.write(f"Vous avez choisi : {choix}")
    logging.info(f"Option sélectionnée : {choix}")

    slider_value = st.slider("Choisissez un nombre 🔢", 0, 100)
    st.write(f"Valeur du curseur : {slider_value}")
    logging.info(f"Valeur du curseur sélectionnée : {slider_value}")

def display_pairplot(df, hue_column):
    """Crée et affiche un graphique de paires Seaborn."""
    sns.pairplot(df, hue=hue_column)
    st.pyplot(plt.gcf())
    logging.info("Graphique de paires affiché.")

def handle_file_upload():
    """Gère le téléchargement de fichiers CSV et permet le téléchargement après traitement."""
    st.header("Télécharger un fichier CSV 📂")
    uploaded_file = st.file_uploader("Choisissez un fichier CSV", type=["csv"])

    if uploaded_file is not None:
        uploaded_data = pd.read_csv(uploaded_file)
        st.write("Contenu du fichier téléchargé :")
        st.dataframe(uploaded_data)
        logging.info("Fichier CSV téléchargé et affiché.")

        # Générer un fichier CSV filtré et permettre le téléchargement
        csv_data = uploaded_data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Télécharger le fichier en CSV 📥",
            data=csv_data,
            file_name='fichier_telecharge.csv',
            mime='text/csv'
        )
        logging.info("Bouton de téléchargement du fichier CSV affiché.")

# Personnalisation de l'interface
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f8ff;
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image('https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2JhaGxjZjRxZjE2Mml1Y242MjhzNnBtMDBtYTBqMndmZDl4am9jMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zXmbOaTpbY6mA/giphy.gif', caption="GIF animé", use_column_width=True)

# Affichage de texte
st.title("Introduction à Streamlit! 🚀")
st.header("Voici un en-tête 🎈")
st.subheader("Et un sous-en-tête 🌈")
st.write("Streamlit est génial pour créer des applications web rapidement ! 🎉")
st.markdown("**Ceci est du Markdown !**")
logging.info("Affichage de texte initial terminé.")

# Afficher un logo en haut de l'application
st.image("img/logo.jpg", use_column_width=True)

# Affichage des données initiales
df_initial = pd.DataFrame({
    'Colonne 1': [1, 2, 3, 4],
    'Colonne 2': [10, 20, 30, 40]
})
log_and_display_data(df_initial)

# Interactions utilisateur
log_user_interaction()

# Charger les données Iris et les manipuler
df = load_data()
st.title("Analyse des données Iris avec Streamlit 📊")
st.header("Filtrage et interactions 🔍")

# Widgets interactifs pour filtrer les colonnes à afficher
colonnes_disponibles = list(df.columns)
colonnes_selectionnees = st.multiselect("Sélectionnez les colonnes à afficher", colonnes_disponibles, default=colonnes_disponibles)
df_filtre = filter_data(df, colonnes_selectionnees)
st.dataframe(df_filtre)
logging.info("DataFrame filtré affiché.")

# Sélection d'une espèce pour afficher plus d'informations
especes = df['species'].unique()
espece_selectionnee = st.selectbox("Sélectionnez une espèce pour plus de détails", especes)
details = get_species_details(df, espece_selectionnee)
st.write(f"Détails sur l'espèce {espece_selectionnee}")
st.dataframe(details)
logging.info(f"Détails sur l'espèce {espece_selectionnee} affichés.")

# Affichage du graphique de paires filtré
display_pairplot(df, 'species')

# États de session pour stocker la sélection de l'utilisateur
if 'nombre_filtrage' not in st.session_state:
    st.session_state.nombre_filtrage = 0
st.session_state.nombre_filtrage += 1
st.write(f"Vous avez filtré les données {st.session_state.nombre_filtrage} fois. 🎊")
logging.info(f"Nombre de filtrages : {st.session_state.nombre_filtrage}")

# Gestion des fichiers
handle_file_upload()