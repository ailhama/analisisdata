# main.py
import streamlit as st
from streamlit_option_menu import option_menu

# Importing the apps
import EDA
import kesimpulan

st.set_page_config(layout='centered', page_icon="📊", page_title="Data Analysis Detik")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Sidebar
        with st.sidebar:
            app = option_menu(
                menu_title='Menu',
                options=['EDA', 'Kesimpulan'],
                icons=['bar-chart', 'info-circle'],
                menu_icon='cast',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        # Menu
        if app == "EDA":
            EDA.app()
        elif app == "Kesimpulan":
            kesimpulan.app()

# Create an instance of the app and run it
app = MultiApp()
app.add_app("EDA", EDA.app)
app.add_app("Kesimpulan", kesimpulan.app)
app.run()
