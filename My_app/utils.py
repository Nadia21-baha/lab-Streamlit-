import streamlit as st
import pandas as pd
from google_play_scraper import search, app
import time

@st.cache_data(show_spinner=False)
def get_competitor_data(search_term):
    results = search(
        search_term,
        lang="en",
        country="us",
        n_hits=10
    )
    
    all_apps = []

    for r in results:
        try:
            app_id = r.get("appId")
            if not app_id:
                continue
                
            details = app(
                app_id,
                lang="en",
                country="us"
            )

            app_data = {
                "App ID": str(details.get("appId", "")),
                "Title": str(details.get("title", "")),
                "Description": str(details.get("description", "")),
                "Summary": str(details.get("summary", "")),
                "Score": float(details.get("score", 0.0)),
                "Ratings": int(details.get("ratings", 0)),
                "Installs": int(details.get("realInstalls", 0)),
                "Price": float(details.get("price", 0.0)),
                "Type": "Free" if details.get("free", True) else "Paid",
                "Genre": str(details.get("genre", "Unknown")),
                "Developer": str(details.get("developer", "Unknown"))
            }

            all_apps.append(app_data)
            time.sleep(1)

        except Exception as e:
            continue

    if not all_apps:
        return pd.DataFrame()
        
    return pd.DataFrame(all_apps)