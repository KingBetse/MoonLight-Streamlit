# MoonLight Energy Solutions

## Project Overview
This project aims to analyze a dataset containing solar energy-related data, such as Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), Diffuse Horizontal Irradiance (DHI), and module temperatures (TModA and TModB). The goal is to provide insights into the relationships between these variables through statistical analysis and visualization.

## Dataset
The dataset used in this project includes data from three different locations: Benin, Sierra Leone, and Togo. The dataset can be found in the `./src/` directory of the project, with the following file names:
- `benin-malanville.csv`
- `sierraleone-bumbuna.csv`
- `togo-dapaong_qc.csv`

## Streamlit Application
To make the analysis more accessible, a Streamlit application has been developed. This application allows users to select a dataset and view a correlation heatmap that visualizes the relationships between the various features in the data.

### Usage
1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the Streamlit application:
   ```
   streamlit run page.py
   ```
3. The application will open in your default web browser, and you can interact with the interface to explore the dataset.

### Correlation Heatmap
The main feature of the Streamlit application is the correlation heatmap. This visualization provides a clear overview of the relationships between the different variables in the dataset, making it easier to identify patterns and trends.

The heatmap is generated using the Plotly library, which provides a visually appealing and interactive representation of the data. The color scale used in the heatmap ranges from -1 to 1, where blue represents a negative correlation, white represents no correlation, and red represents a positive correlation.

![Correlation Heatmap][]

By providing this interactive visualization, the Streamlit application enables users to quickly and easily interpret the relationships within the dataset, supporting their decision-making process and contributing to the overall understanding of solar energy performance.

## Conclusion
The MoonLight Energy Solutions project demonstrates the power of data analysis and visualization in the context of solar energy research. By leveraging the Streamlit framework and the Plotly library, this project offers an engaging and informative way to explore the dataset, ultimately supporting the development of more efficient and effective solar energy solutions.
