import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt

# Set page title
st.title("Data Visualization with Streamlit")

# Generate random data
def generate_data(rows=100):
    np.random.seed(42)
    data = {
        'Category': np.random.choice(['A', 'B', 'C', 'D'], size=rows),
        'Value': np.random.randn(rows) * 10 + 50,
        'X': np.random.rand(rows) * 100,
        'Y': np.random.rand(rows) * 100
    }
    return pd.DataFrame(data)

df = generate_data()

# Display dataset
st.subheader("Generated Data")
st.write(df.head())

# Select visualization type
chart_type = st.selectbox("Select chart type", ["Matplotlib", "Plotly", "Altair"])

# Matplotlib Chart
if chart_type == "Matplotlib":
    st.subheader("Matplotlib Bar Chart")
    fig, ax = plt.subplots()
    df.groupby("Category")["Value"].mean().plot(kind="bar", ax=ax, color=['blue', 'green', 'red', 'purple'])
    ax.set_ylabel("Average Value")
    st.pyplot(fig)

# Plotly Chart
elif chart_type == "Plotly":
    st.subheader("Plotly Scatter Plot")
    fig = px.scatter(df, x="X", y="Y", color="Category", size="Value", title="Plotly Scatter Plot")
    st.plotly_chart(fig)

# Altair Chart
elif chart_type == "Altair":
    st.subheader("Altair Line Chart")
    chart = alt.Chart(df).mark_line().encode(
        x="X",
        y="Value",
        color="Category"
    ).properties(title="Altair Line Chart")
    st.altair_chart(chart, use_container_width=True)

# Add an interactive slider for filtering
threshold = st.slider("Filter data above value:", min_value=0, max_value=100, value=50)
filtered_df = df[df["Value"] > threshold]
st.write("Filtered Data:", filtered_df)
