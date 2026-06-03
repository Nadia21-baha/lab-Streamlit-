import streamlit as st
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="Visualisations", page_icon="📈", layout="wide")

st.title("📈 Analyses Graphiques & Business Insights")

# 1. Vérification de la présence des données
if "search_results" not in st.session_state or st.session_state["search_results"] is None:
    st.warning("⚠️ Aucune donnée disponible. Veuillez effectuer une recherche sur la page 1_Results_Table.")
else:
    df = st.session_state["search_results"]
    
    # Sécurité : Si le dataframe est vide
    if df.empty:
        st.error("Le tableau de données est vide. Relancez une extraction valide.")
    else:
        # 2. Barre latérale de filtrage
        st.sidebar.header("🎯 Filtres globaux")
        if "current_query" in st.session_state:
            st.sidebar.write(f"Requête active : {st.session_state['current_query']}")
        
        # Récupération de la colonne ID de manière flexible
        id_col = "App ID" if "App ID" in df.columns else df.columns[0]
        title_col = "Title" if "Title" in df.columns else df.columns[1]
        
        all_app_ids = df[id_col].unique().tolist()
        selected_apps = st.sidebar.multiselect(
            "Filtrer par ID d'application :",
            options=all_app_ids,
            default=all_app_ids
        )
        
        # Application du filtre
        df_filtered = df[df[id_col].isin(selected_apps)]
        
        if df_filtered.empty:
            st.error("Veuillez sélectionner au moins une application dans la barre latérale.")
        else:
            # 3. Affichage des graphiques en colonnes
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("⭐ Distribution des Notes (Ratings)")
                score_col = "Score" if "Score" in df_filtered.columns else None
                if score_col:
                    fig_bar = px.bar(
                        df_filtered.sort_values(by=score_col, ascending=False),
                        x=title_col, y=score_col, color=score_col,
                        labels={title_col: "Nom de l'App", score_col: "Note moyenne"},
                        color_continuous_scale="Cividis"
                    )
                    st.plotly_chart(fig_bar, use_container_width=True)
                else:
                    st.info("Données de notes indisponibles.")
                
            with col2:
                st.subheader("💰 Répartition des Modèles (Free vs Paid)")
                type_col = "Type" if "Type" in df_filtered.columns else None
                if type_col and type_col in df_filtered.columns:
                    df_counts = df_filtered[type_col].value_counts().reset_index()
                    df_counts.columns = [type_col, "count"]
                    fig_pie = px.pie(
                        df_counts, names=type_col, values="count",
                        color=type_col, color_discrete_map={"Free": "#2ecc71", "Paid": "#e74c3c"}
                    )
                    st.plotly_chart(fig_pie, use_container_width=True)
                else:
                    st.info("Données de prix indisponibles.")
                
            st.markdown("---")
            
            col3, col4 = st.columns([3, 2])
            
            with col3:
                st.subheader("📥 Volume de Téléchargements par Application")
                installs_col = "Installs" if "Installs" in df_filtered.columns else None
                if installs_col and score_col:
                    fig_scatter = px.scatter(
                        df_filtered, x=title_col, y=installs_col,
                        size=installs_col, color=score_col, hover_name=title_col,
                        labels={installs_col: "Nombre d'installations"},
                        size_max=35
                    )
                    st.plotly_chart(fig_scatter, use_container_width=True)
                else:
                    st.info("Données d'installations indisponibles.")
                
            with col4:
                st.subheader("☁️ Nuage de Mots des Descriptions")
                desc_col = "Description" if "Description" in df_filtered.columns else None
                if desc_col:
                    text = " ".join(desc for desc in df_filtered[desc_col].dropna().astype(str))
                    
                    if text.strip() != "":
                        wordcloud = WordCloud(
                            background_color="white", 
                            width=500, 
                            height=350, 
                            max_words=100
                        ).generate(text)
                        
                        fig_wc, ax = plt.subplots(figsize=(6, 4))
                        ax.imshow(wordcloud, interpolation="bilinear")
                        ax.axis("off")
                        st.pyplot(fig_wc)
                        plt.close(fig_wc)
                    else:
                        st.text("Données textuelles insuffisantes.")
                else:
                    st.text("Colonne Description absente.")