import pandas as pd
import streamlit as st
import plotly.express as px

st.title('New York Uber App')

DATA_URL = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'
DATE_COLUMN = 'Date/Time'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

def filter_map(data, hora):
    filtered_df = data[data[DATE_COLUMN].dt.hour == hora]
    fig = px.scatter_mapbox(filtered_df, lat='Lat', lon='Lon', color='Base', hover_name='Date/Time', color_discrete_sequence=px.colors.qualitative.Dark24_r).update_layout(mapbox={"style": "carto-positron"}, margin={"t":0,"b":0,"l":0,"r":0})
    return fig    

st.header('Mapa')
st.write('Mapa con viajes de Uber en la ciudad de Nueva York filtrado por hora.')

df = load_data(100000)

hora = st.slider('Control Hora del Día', 0, 23)

fig = filter_map(df, hora)

st.write(fig)