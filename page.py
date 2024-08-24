import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


# Set the title and description of the dashboard
st.set_page_config(page_title="Data Insights Dashboard Of MoonLight-Energy-Solutions ", layout="wide")
st.title("Data Insights Dashboard")
st.write("Explore the data insights using the interactive visualizations below.")

# Create a sidebar
st.sidebar.title("Filters")

# Load and process the data
dataset_info = [
    ("benin", "./src/benin-malanville.csv"),
    ("sierraleone", "./src/sierraleone-bumbuna.csv"),
    ("togo", "./src/togo-dapaong_qc.csv")
]



def analyze_dataset(dataset_name, file_path):
    st.subheader(f"{dataset_name}")
    data = pd.read_csv(file_path)

    # ModA
    fig = go.Figure()
    fig.add_trace(go.Box(x=data['ModA'], name='ModA'))
    fig.update_layout(title='Outliers in ModA')

    # ModB
    fig2 = go.Figure()
    fig2.add_trace(go.Box(x=data['ModB'], name='ModB'))
    fig2.update_layout(title='Outliers in ModB')

    st.plotly_chart(fig, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)
    st.write()

# Streamlit app
st.title("Dataset Outlier Analysis")



for dataset_name, file_path in dataset_info:
    analyze_dataset(dataset_name, file_path)


import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime

def analyze_dataset(dataset_name, file_path):
    st.subheader(f"{dataset_name}")
    data = pd.read_csv(file_path)
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    fig = make_subplots(rows=1, cols=1, )
    fig.add_trace(go.Scatter(x=data['Timestamp'], y=data['GHI'], mode='lines', name='GHI'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data['Timestamp'], y=data['DNI'], mode='lines', name='DNI'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data['Timestamp'], y=data['DHI'], mode='lines', name='DHI'), row=1, col=1)

    fig.update_layout(
        title='Line Graphs of GHI, DNI, and DHI',
        xaxis_tickformat='%b',
        xaxis_title='Time',
        yaxis_title='Values',
        legend_title_text='Variables'
    )

    st.plotly_chart(fig, use_container_width=True)
    st.write()

# Streamlit app
st.title("Dataset Line Graph Analysis")


for dataset_name, file_path in dataset_info:
    analyze_dataset(dataset_name, file_path)