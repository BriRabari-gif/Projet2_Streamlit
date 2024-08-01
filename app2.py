import pandas as pd
import streamlit as st
from fuzzywuzzy import process

# Chargement du DataFrame
df = pd.read_csv('df_streamlit.xls')

# Création de la liste de films
list_movies = list(df["primaryTitle"])

# Fonction pour trouver le meilleur match de film
def trouver_titre_film(entree_utilisateur, liste_film):
    meilleur_match = process.extractOne(entree_utilisateur, liste_film)
    return meilleur_match[0]

# Fonction de recommandation
def recommander_films(titre_film):
    # Trouver l'index du film correspondant
    index_film = df[df['primaryTitle'] == titre_film].index[0]
    # Récupérer les films recommandés et leurs affiches
    films_recommandes = df.iloc[index_film][['film1', 'film2', 'film3', 'film4', 'film5']]
    posters_recommandes = df.iloc[index_film][['path1', 'path2', 'path3', 'path4', 'path5']]
    # Ajouter la base URL aux chemins des posters
    base_url = "https://image.tmdb.org/t/p/w500/"
    posters_recommandes = [base_url + poster for poster in posters_recommandes]
    return films_recommandes.tolist(), posters_recommandes

# Interface utilisateur Streamlit
st.title("Recommandation de Films")

# Saisie de l'utilisateur
entree_utilisateur = st.text_input("Entrez le titre d'un film:")
if entree_utilisateur:
    # Trouver le titre du film le plus proche
    titre_corrige = trouver_titre_film(entree_utilisateur, list_movies)

    # Afficher le titre corrigé
    st.write(f"Titre corrigé: {titre_corrige}")

    # Obtenir des recommandations
    recommandations, posters = recommander_films(titre_corrige)

    # Afficher les recommandations
    st.write(f"Films recommandés pour '{titre_corrige}':")

    # Afficher les films recommandés et leurs affiches en colonne
    cols = st.columns(len(recommandations))
    for i, col in enumerate(cols):
        with col:
            st.image(posters[i], caption=recommandations[i], use_column_width=True)




