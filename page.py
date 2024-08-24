import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


# Set the title and description of the dashboard
st.set_page_config(page_title="Data Insights Dashboard Of MoonLight-Energy-Solutions ", layout="wide")
st.title("Data Insights Dashboard")
st.write("Explore the data insights using the interactive visualizations below.")

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

dataset_info = {
    "benin": "./src/benin-malanville.csv",
    "sierraleone": "./src/sierraleone-bumbuna.csv",
    "togo": "./src/togo-dapaong_qc.csv"
}

def analyze_dataset(dataset_name, file_path):
    st.subheader(f"{dataset_name}")
    data = pd.read_csv(file_path)
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    # Boxplot for ModA and ModB
    fig = go.Figure()
    fig.add_trace(go.Box(x=data['ModA'], name='ModA'))
    fig.add_trace(go.Box(x=data['ModB'], name='ModB'))
    fig.update_layout(title='Outliers in ModA and ModB')
    st.plotly_chart(fig, use_container_width=True)

    # Line graphs for GHI, DNI, and DHI
    fig = make_subplots(rows=1, cols=1)
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

   
   
    corr_matrix = data[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()

    fig = go.Figure(data=go.Heatmap(
        x=corr_matrix.columns,
        y=corr_matrix.index,
        z=corr_matrix.values,
        colorscale='Plasma',
        zmin=-1, zmax=1
    ))

    fig.update_layout(
        title='Correlation Heatmap',
        xaxis_title='Features',
        yaxis_title='Features',
        width=800,
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write()

# Streamlit app
st.title("Dataset Analysis")

# Create a dropdown to select the dataset
selected_dataset = st.selectbox("Select a dataset", list(dataset_info.keys()))

# Analyze the selected dataset
analyze_dataset(selected_dataset, dataset_info[selected_dataset])