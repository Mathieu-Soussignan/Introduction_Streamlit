# Introduction à Streamlit : Visualisation et Analyse de Données

Cette application Streamlit est un projet pédagogique visant à explorer les fonctionnalités de base de Streamlit à travers deux modules principaux : la visualisation interactive d'une fonction affine et l'analyse de données à partir de fichiers CSV. Elle inclut des fonctionnalités d'affichage, de visualisation, de filtrage de données, et d'interactions utilisateur.

## Fonctionnalités

### Page 0 : Visualisation interactive d'une fonction affine

- **Visualisation dynamique de la fonction affine `y = ax + b`** :
  - Les utilisateurs peuvent ajuster les paramètres `a` (pente) et `b` (ordonnée à l'origine) à l'aide de sliders interactifs.
  - Le graphique de la fonction est mis à jour en temps réel en fonction des valeurs choisies.
- **Affichage de l'équation de la droite** :
  - L'équation de la fonction est affichée dynamiquement pour refléter les modifications des paramètres.

### Page 1 : Outil d'analyse de données interactif

- **Chargement de données** :
  - Les utilisateurs peuvent charger un fichier CSV via un widget `st.file_uploader`.
  - Les premières lignes du fichier sont affichées pour un aperçu rapide.
- **Exploration des données** :
  - Affichage des statistiques descriptives pour mieux comprendre les données.
  - Sélection des colonnes à afficher avec `st.multiselect` pour filtrer les données visibles.
- **Visualisation de données** :
  - Création d'un nuage de points interactif pour visualiser les relations entre deux colonnes sélectionnées par l'utilisateur.
  - Utilisation de Seaborn et Matplotlib pour générer les graphiques.

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

   Le fichier `requirements.txt` doit inclure les bibliothèques suivantes :
   ```text
   streamlit
   pandas
   numpy
   seaborn
   matplotlib
   ```

## Utilisation

Pour lancer l'application, exécutez la commande suivante :
   ```bash
   streamlit run hello.py
   ```
Cela ouvrira l'application dans votre navigateur par défaut, où vous pourrez naviguer entre les pages et interagir avec les modules.

## Structure du Code

- **pages/0_fonction_affine.py** : Module pour la visualisation interactive d'une fonction affine.
- **pages/1_data_analyst.py** : Module pour l'analyse interactive de données à partir d'un fichier CSV.
- **hello.py** : Fichier principal pour configurer l'application Streamlit.
- **hello.log** : Fichier de journalisation généré pour suivre les événements et interactions utilisateur.

## Fonctionnement de l'Application

### Visualisation interactive d'une fonction affine (Page 0)

L'application permet aux utilisateurs d'explorer les variations d'une fonction affine en modifiant les valeurs de `a` et `b` à l'aide de sliders, avec un affichage en temps réel du graphique et de l'équation.

### Outil d'analyse de données (Page 1)

L'application permet de :
- Charger un fichier CSV et d'explorer les données.
- Afficher les statistiques descriptives.
- Visualiser les relations entre les variables grâce à un nuage de points interactif.

## Tests

Des tests unitaires peuvent être créés pour vérifier les principales fonctions de l'application. Par exemple :
- Tests pour le chargement de données et le traitement des fichiers CSV.
- Tests pour la visualisation de la fonction affine.

Pour exécuter les tests unitaires, utilisez la commande suivante :

```bash
pytest test/
```

## Journalisation

L'application utilise le module `logging` pour enregistrer les événements importants, tels que les interactions utilisateur et le chargement des données, dans le fichier `hello.log` afin de faciliter le suivi des actions et le débogage.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez améliorer l'application, n'hésitez pas à faire une **pull request** ou à ouvrir une **issue**.

## Auteur

- Mathieu Soussignan.