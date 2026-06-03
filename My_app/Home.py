import streamlit as st

st.set_page_config(
    page_title="Competitor Analysis Hub",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Application d'Analyse Concurrentielle")

st.markdown("### Bienvenue sur votre plateforme de veille concurrentielle")
st.markdown("Cette application multi-pages extrait et analyse de manière dynamique les données réelles du Google Play Store.")

st.markdown("#### Fonctionnalités principales :")
st.markdown("* **Accueil :** Présentation de la structure.")
st.markdown("* **Table des Résultats :** Saisie du mot-clé et scraping en temps réel.")
st.markdown("* **Visualisations :** Graphiques interactifs (notes, installations, nuage de mots).")

st.markdown("#### Lancement local :")
st.code("streamlit run Home.py")

if "search_results" not in st.session_state:
    st.session_state["search_results"] = None
if "current_query" not in st.session_state:
    st.session_state["current_query"] = ""