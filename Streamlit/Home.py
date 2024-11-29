import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Home Car Eval",
    page_icon="👋",
)

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
st.markdown("<h1 class='center'>Home Car Eval Web App</h1>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")


st.write("## Hi! Welcome to my Car Eval Web App!👋")

st.markdown(
    """
    This web app was created to perform an analysis on a car evaluation dataset.
    As well as to create a machine learning model to help classify car evals in the future!

    To navigate this web app to view the analysis of the dataset or use the machine learning model,
    please use the navigation bar on the left! Thank you!
"""
)

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
st.dataframe(df,width=1800,height=600)