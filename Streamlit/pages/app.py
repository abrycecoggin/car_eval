import re
from time import sleep
import pandas as pd
import numpy as np
import streamlit as st
from streamlit.components.v1 import html
import warnings
import os
import data_setup
from data_setup import integer_mapping, integer_training_setup, oneHotEncoder_setup

def run():
    st.set_page_config(
        page_title="Car Eval Classification",
        layout="wide"
    )
    warnings.simplefilter(action='ignore', category=FutureWarning)
    # Function To Load Our Dataset
    @st.cache_data
    def load_model(model_path):
        return pd.read_pickle(model_path)

    model = pd.read_pickle(r"C:\Users\bryce\OneDrive\Desktop\Projects\car_eval\DT_ROS_Model.pkl")

    header = st.container(border=True)
    content = st.container(border=True)
    st.write("")

    with header:
# Define the CSS styles for the h1 text
        css = """
        h1 {
            color: white;
            background-image: linear-gradient(to right, #ef233c 0%, #9a031e 100%);
            padding: 10px; /* Add padding for better visibility */
            border-radius: 5px; /* Optional: Add border-radius for rounded corners */
            text-align: center;
            border: 5px solid white; /* Add white border */
        }

        .st-emotion-cache-rg896d {
            width: 1754px;
            position: relative;
            justify-items: center;
            text-align: center;
        }
        """
        # Apply the custom CSS styles and display the h1 text
        # Apply the custom CSS styles
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
        # Display the title using Markdown with custom CSS
        st.markdown("<h1 class='center'>Car Eval Classification</h1>", unsafe_allow_html=True)
        #st.markdown("Drug Classification💉🩸")
        st.write("")
        st.write("")
        st.write("")

    with content:
        colu0,col1, col2 = st.columns([1,5,1])
        with col1:
            st.markdown('<div class="center">', unsafe_allow_html=True)
            with st.form("Predict"):
                c1, c2 = st.columns(2)
                with c1:
                    buying = st.selectbox('Buying', options=["VHIGH", 'HIGH', 'MED', 'LOW'], index=0)

                    doors = st.selectbox('Doors', options=["2", '3', '4', '5 or More'], index=0)

                    lug_boot = st.selectbox('Lug Boot', options=['SMALL', 'MED', 'BIG'], index=0)

                with c2:
                    maint = st.selectbox("Maintenance", options=["VHIGH", 'HIGH', 'MED', 'LOW'], index=0)

                    persons = st.selectbox('Persons', options=["2", '3', '4', '5 or MORE'], index=0)

                    safety = st.selectbox('Safety', options=['LOW', 'MED', 'HIGH'], index=0)
                    
                
                predict_button = st.form_submit_button("Predict")

    if predict_button:

        data = {
            'buying': [buying],
            'maint':[maint],
            'doors':[doors],
            'persons':[persons],
            'lug_boot':[lug_boot],
            'safety':[safety]
        }

        df = pd.DataFrame(data)

        df_IM = integer_mapping(df)


        subheader = '<spin style="color:white;font-size:30px; padding: 10px; text-align: center; display: flex; align-items: center; justify-content: center; font-weight: bold;">Input DataFrame:</spin>'
        st.markdown(subheader, unsafe_allow_html=True)

        styler = df_IM.style.background_gradient(cmap='RdYlGn')

        # Customize the styler's CSS properties
        styler = styler.set_properties(**{
            'font-size': '16px',
            'color': 'white',
            'border': '2px solid white',
            'background-image': 'linear-gradient(to right, #ef233c 0%, #9a031e 100%);',
            'display': 'flex;',
            'align-items': 'center;',
            'justify-content': 'center;'
        })

        # Display the styled DataFrame
        st.write(styler)

        prediction = model.predict(df_IM)


        st.write("")
        st.write("")

        markdown_text = '<spin style="color:lightgray;background:#575860;font-size:30px;border: 2px solid lightgray; padding: 10px; align-items: center; justify-content: center; margin: 0 auto;">Predicted Class:</spin>'
        # Display Markdown text
        st.markdown(markdown_text, unsafe_allow_html=True)

        def generate_gradient_css():
            css = """
            <style>
            .gradient-container {
                background: linear-gradient(to right, #ef233c 0%, #9a031e 100%);
                padding: 20px;
                border-radius: 20px ;
                color: white;
                font-size: 30px;
                font-weight: bold;
                text-align: center;
                border-color: white;
            }
            </style>
            """
            return css
        st.markdown(generate_gradient_css(), unsafe_allow_html=True)
        st.markdown(f'<div class="gradient-container">{prediction[0].upper()}</div>', unsafe_allow_html=True)
        st.header("")

run()