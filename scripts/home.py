import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title and description of the dashboard
st.set_page_config(page_title="Data Insights Dashboard", layout="wide")
st.title("Data Insights Dashboard")
st.write("Explore the data insights using the interactive visualizations below.")

# Create a sidebar
st.sidebar.title("Filters")

# Load and process the data
dataset_info = [
    ("benin", "../src/benin-malanville.csv"),
    ("sierraleone", "../src/sierraleone-bumbuna.csv"),
    ("togo", "../src/togo-dapaong_qc.csv")
]

# Check for outliers in sensor readings (ModA, ModB)

for dataset_name, file_path in dataset_info:
    print(f"{dataset_name}:")
    print()
    data = pd.read_csv(file_path)
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    # ModA
    sns.boxplot(x=data['ModA'], ax=ax[0])
    ax[0].set_title('Outliers in ModA')

    # ModB
    sns.boxplot(x=data['ModB'], ax=ax[1])
    ax[1].set_title('Outliers in ModB')

    plt.show()
    print()
    
# only have upper outlier