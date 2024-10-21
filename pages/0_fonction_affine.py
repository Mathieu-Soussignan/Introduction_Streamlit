import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Visualisation interactive d'une fonction affine")

# Sliders pour les paramètres a et b
a = st.slider("Coefficient directeur (a)", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
b = st.slider("Ordonnée à l'origine (b)", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)

# Génération des valeurs x et calcul des valeurs y
x = np.linspace(-10, 10, 100) 
y = a * x + b

# Création du graphique
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f'y = {a}x + {b}', color='b')
plt.title("Graphique de la fonction affine y = ax + b")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

# Affichage du graphique dans Streamlit
st.pyplot(plt.gcf())

# Affichage de l'équation de la droite
st.write(f"Équation de la droite : y = {a}x + {b}")