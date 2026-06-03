import streamlit as st
from utils import get_competitor_data

st.set_page_config(page_title="Données Brutes", page_icon="🔍", layout="wide")

st.title("🔍 Extraction & Collecte de Données Réelles")
st.write("Saisissez votre mot-clé cible pour interroger l'API Google Play.")

search_query = st.text_input(
    "Mot-clé de recherche concurrentielle :", 
    value=st.session_state.get("current_query", ""), 
    placeholder="ex: mental health ai, notes, productivity"
)

if st.button("Lancer l'extraction", type="primary"):
    if search_query.strip() != "":
        with st.spinner("Scraping en cours sur Google Play Store... Merci de patienter."):
            df = get_competitor_data(search_query)
            
            if df is not None and not df.empty:
                st.session_state["search_results"] = df
                st.session_state["current_query"] = search_query
            else:
                st.error("Aucune donnée n'a pu être extraite pour ce mot-clé.")
    else:
        st.warning("Veuillez saisir un terme valide avant de lancer l'analyse.")

if st.session_state.get("search_results") is not None:
    df_to_show = st.session_state["search_results"]
    st.success(f"Données chargées avec succès pour : {st.session_state['current_query']}")
    st.dataframe(df_to_show, use_container_width=True)
else:
    st.info("Saisissez un mot-clé ci-dessus et cliquez sur le bouton pour générer le tableau de données.")