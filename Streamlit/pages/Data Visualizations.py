import re
from time import sleep
import pandas as pd
import numpy as np
import streamlit as st
from streamlit.components.v1 import html
import warnings
import os
import plotly.express as px
import data_setup
from data_setup import integer_mapping, integer_training_setup, oneHotEncoder_setup

st.set_page_config(
    page_title="Data Viz",
    layout="wide"
)


def pie_chart(variable):
    #  count = data['class']
    #  fig = px.pie(count, values=count.value_counts().values, names=count.value_counts().index, color_discrete_sequence=px.colors.sequential.RdBu)
    #  return fig
    fig = px.pie(variable, values=variable.value_counts().values, names=variable.value_counts().index, color_discrete_sequence=px.colors.sequential.RdBu)
    return fig

def box_plot(var):
    df = pd.read_csv(r'C:\Users\bryce\OneDrive\Desktop\Projects\car_eval\car.csv')
    df = integer_mapping(df)
    fig = px.box(df, x='class', y=str(var), color="class", color_discrete_sequence=px.colors.sequential.RdBu)
    fig.update_layout(xaxis={'categoryorder': 'array', 'categoryarray': ["unacc", "acc", "good","vgood"]})
    return fig

def run():
    data = pd.read_csv(r'C:\Users\bryce\OneDrive\Desktop\Projects\car_eval\car.csv')

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
        st.markdown("<h1 class='center'>Car Eval Data Visualizations</h1>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")

    with content:

        col = st.columns((1, 1), gap='small')
        
        with col[0]:
            st.markdown('##### Boxplot')
            selected_category = st.selectbox('Select Category', data.columns[:-1])
            st.markdown(f'##### {str(selected_category).capitalize()} by Class')
            st.plotly_chart(box_plot(str(selected_category)), use_container_width=True)
            # st.plotly_chart(box_plot(), use_container_width=True)

        with col[1]:
            st.markdown('##### Count by Class')
            st.plotly_chart(pie_chart(data['class']), use_container_width=True,key="class")

        df = pd.read_csv(r'C:\Users\bryce\OneDrive\Desktop\Projects\car_eval\car.csv')
        df = pd.DataFrame(df)
        subheader = '<spin style="color:white;font-size:30px; padding: 10px; text-align: center; display: flex; align-items: center; justify-content: center; font-weight: bold;">DataFrame:</spin>'
        st.markdown(subheader, unsafe_allow_html=True)
        # styler = df.style.background_gradient(cmap='RdYlGn')
        # styler = styler.set_properties(**{
        #     'font-size': '16px',
        #     'color': 'white',
        #     'border': '2px solid white',
        #     'background-image': 'linear-gradient(to right, #ef233c 0%, #9a031e 100%);',
        #     'display': 'flex;',
        #     'align-items': 'center;',
        #     'justify-content': 'center;',
        #     'justify-items': 'center;',
        #     'width': '1754px;',
        #     'position': 'relative;'
        # })
        # st.write(styler)
        # styled_dataframe = st.dataframe(df.style.apply(lambda x: "font-size: 50pt"))
        # styled_dataframe = df.style.set_properties(**{'font-size': '50pt', 'font-family': 'Calibri'})
        st.dataframe(df.style.set_properties(**{'font-size': '50pt', 'font-family': 'Calibri'}),width=1800,height=600)
     
run()