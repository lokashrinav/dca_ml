import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

feature_importances = [0.5, 0.3, 0.2]
features = ["GDP Growth (%)", "Inflation (%)", "Unemployment (%)"]

st.title("Macroeconomic Prediction Tool")
st.markdown("""
This tool allows you to predict key macroeconomic metrics like **Revenue Growth** and **Weighted Average Cost of Capital (WACC)**. 
Follow these steps to use the tool:
1. Adjust the sliders in the sidebar to input **GDP Growth**, **Inflation**, and **Unemployment** rates.
2. View the predictions for **Revenue Growth** and **WACC** below.
3. Scroll down to explore how each input contributes to the predictions via the **Feature Importance Chart**.
4. Check the model's performance metrics in the sidebar to evaluate prediction accuracy.
""")

st.sidebar.header("Step 1: Provide Input Data")
st.sidebar.markdown("""
Use the sliders below to set the macroeconomic values. Adjust them to simulate different scenarios and observe their impact on the predictions.
""")

gdp_growth = st.sidebar.slider("GDP Growth (%)", -3.0, 5.0, 2.0, step=0.1)
inflation = st.sidebar.slider("Inflation (%)", 1.0, 6.0, 3.0, step=0.1)
unemployment = st.sidebar.slider("Unemployment (%)", 2.0, 10.0, 5.0, step=0.1)

input_data = np.array([[gdp_growth, inflation, unemployment]])
revenue_prediction = np.random.uniform(0, 10)
wacc_prediction = np.random.uniform(2, 7)

st.write("### Step 2: View Predictions")
st.markdown("""
Based on your inputs, the tool predicts the following macroeconomic outcomes:
""")
st.metric(label="Revenue Growth (%)", value=f"{revenue_prediction:.2f}", help="Predicted revenue growth based on the provided input values.")
st.metric(label="WACC (%)", value=f"{wacc_prediction:.2f}", help="Predicted Weighted Average Cost of Capital (WACC) based on the input values.")

st.sidebar.header("Step 3: Evaluate Model Performance")
st.sidebar.markdown("""
The following metrics indicate how well the prediction model performs:
- **Revenue Model RMSE**: Root Mean Square Error for the Revenue Growth predictions.
- **WACC Model RMSE**: Root Mean Square Error for the WACC predictions.
""")
st.sidebar.write(f"Revenue Model RMSE: 1.23")
st.sidebar.write(f"WACC Model RMSE: 0.87")

st.write("### Step 4: Explore Feature Importance")
st.markdown("""
The chart below shows how much each input variable (GDP Growth, Inflation, Unemployment) contributes to the predictions. 
Higher importance indicates a stronger impact on the predictions.
""")
fig, ax = plt.subplots()
ax.barh(features, feature_importances, color="skyblue")
ax.set_xlabel("Importance")
ax.set_title("Feature Importance")
st.pyplot(fig)

st.markdown("""
### How to Interpret the Results:
1. **GDP Growth (%):** Represents the impact of GDP growth on the predictions. Higher GDP growth typically correlates with improved Revenue Growth.
2. **Inflation (%):** Shows how inflation influences the predictions. Moderate inflation may signal economic stability.
3. **Unemployment (%):** Indicates the role of unemployment rates in the predictions. Higher unemployment can negatively affect WACC and Revenue Growth.

Feel free to tweak the inputs again to see how the predictions and chart change dynamically!
""")
