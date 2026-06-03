import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Layouts & Containers", layout="wide")

st.title("🏗️ Organisation de l'Espace : Layouts & Containers")
st.markdown("---")

# ==========================================
# 1. UTILISATION DES COLONNES (st.columns)
# ==========================================
st.header("1. Les Colonnes (`st.columns`)")
st.caption("Permet de placer des éléments côte à côte horizontalement.")

# Création de 3 colonnes de tailles égales
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📊 Métrique A")
    st.metric(label="Téléchargements totaux", value="120 K", delta="+12%")

with col2:
    st.subheader("⭐ Métrique B")
    st.metric(label="Note Moyenne", value="4.6 / 5", delta="-0.2")

with col3:
    st.subheader("💰 Métrique C")
    st.metric(label="Revenus", value="1,500 $", delta="+24%")

st.markdown("---")

# ==========================================
# 2. UTILISATION DES CONTENEURS (st.container)
# ==========================================
st.header("2. Les Conteneurs (`st.container`)")
st.caption("Idéal pour grouper des éléments ensemble, par exemple un formulaire ou un bloc de résultats.")

# Un conteneur avec une bordure visuelle pour bien voir la délimitation
with st.container(border=True):
    st.subheader("📦 Bloc d'Analyse Concurrentielle")
    st.text("Tous les éléments dans ce carré sont groupés à l'intérieur d'un seul conteneur.")
    
    # Simulation de données internes au conteneur
    df_concurrents = pd.DataFrame({
        "App": ["App 1", "App 2", "App 3"],
        "Part de Marché": ["45%", "35%", "20%"]
    })
    df_concurrents

st.markdown("---")

# ==========================================
# 3. COMBINAISON AVANCÉE : ASYMÉTRIE & SIDEBAR
# ==========================================
st.header("3. Structure Asymétrique & Barre Latérale")

# Ajout d'un élément dans la barre latérale (Sidebar)
st.sidebar.header("⚙️ Paramètres Généraux")
st.sidebar.selectbox("Sélectionner la région cible :", ["Global", "Maroc", "Europe"])

# Colonnes de largeurs différentes (Ratio 2 pour la gauche, 1 pour la droite)
col_gauche, col_droite = st.columns([2, 1])

with col_gauche:
    st.subheader("📝 Zone Principale (Large)")
    st.info("Cette colonne prend 2/3 de la largeur de l'écran. Parfait pour afficher de grands graphiques ou des tableaux complexes.")

with col_droite:
    st.subheader("🔍 Filtres (Étroit)")
    st.warning("Cette colonne prend 1/3 de la largeur. Parfait pour des options secondaires.")
    st.checkbox("Masquer les versions bêta")
    st.checkbox("Afficher uniquement les apps gratuites")