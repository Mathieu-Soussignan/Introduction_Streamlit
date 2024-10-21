# Introduction à Streamlit et Analyse des données Iris

Cette application Streamlit est un exemple d'introduction aux fonctionnalités de base de Streamlit, ainsi qu'une analyse des données du jeu de données *Iris*. Elle inclut des fonctionnalités d'affichage, de filtrage de données, de gestion des interactions utilisateur, de visualisation de graphiques, et de téléchargement de fichiers.

## Fonctionnalités

- **Affichage de texte** : Utilisation de `st.title`, `st.header`, `st.subheader`, et `st.write` pour afficher différents niveaux de texte.
- **Affichage de données** : Affichage de DataFrames et de tableaux à l'aide de `st.dataframe` et `st.table`.
- **Interactions utilisateur** : 
  - Bouton (`st.button`)
  - Case à cocher (`st.checkbox`)
  - Champ de saisie de texte (`st.text_input`)
  - Sélecteur déroulant (`st.selectbox`)
  - Curseur (`st.slider`)
- **Visualisation de données** :
  - Affichage du jeu de données *Iris* avec filtrage des colonnes.
  - Visualisation de graphiques avec Seaborn (`sns.pairplot`) et Matplotlib (`st.pyplot`).
- **Gestion des fichiers** :
  - Téléchargement d'un fichier CSV à l'aide de `st.file_uploader`.
  - Téléchargement d'un fichier généré par l'application à l'aide de `st.download_button`.
- **Journalisation des événements** : Utilisation de la bibliothèque `logging` pour suivre les actions de l'utilisateur.

## Installation

Pour exécuter cette application, assurez-vous d'avoir Python installé. Ensuite, suivez les étapes ci-dessous :

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/ton-utilisateur/ton-repo.git

   ```

2. Accédez au répertoire du projet :
   ```bash
   cd ton-repo

   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt

   ```

    Assurez-vous que le fichier requirements.txt contient les bibliothèques nécessaires, par exemple :
    ```bash
    streamlit
    pandas
    seaborn
    matplotlib

    ```

## Utilisation

Pour lancer l'application, exécutez la commande suivante :
   ```bash
   streamlit run app.py

   ```
Cela ouvrira l'application dans votre navigateur par défaut. Vous pourrez alors interagir avec l'interface Streamlit.

## Structure du Code

- app.py : Fichier principal contenant le code de l'application Streamlit.
- app.log : Fichier de journalisation généré par l'application pour suivre les événements.

## Fonctionnement de l'Application

### Affichage de texte et de données

L'application affiche différents niveaux de texte pour montrer les capacités de mise en forme de Streamlit, ainsi qu'un exemple de DataFrame pour illustrer les fonctionnalités d'affichage de données.

## Visualisation des données Iris

L'application charge le jeu de données Iris, permet de filtrer les colonnes et d'afficher des graphiques de paires pour visualiser les relations entre les variables.

## Gestion des fichiers

Les utilisateurs peuvent télécharger un fichier CSV, voir son contenu dans l'application, et télécharger un fichier généré par l'application.

## Tests

Des tests unitaires peuvent être écrits pour les fonctions principales. Par exemple, les tests unitaires pour vérifier le chargement des données, le filtrage des colonnes et la récupération des détails d'une espèce.

Pour exécuter les tests unitaires, utilisez la commande suivante :

```bash
pytest test_hello.py

```
## Journalisation

L'application utilise le module logging pour enregistrer les événements importants dans un fichier app.log. Les événements tels que les interactions utilisateur, le chargement des données, et les erreurs éventuelles sont journalisés pour faciliter le débogage.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez améliorer l'application, n'hésitez pas à faire une (pull request) ou à ouvrir une request.

## Auteur

- Mathieu Soussignan.




