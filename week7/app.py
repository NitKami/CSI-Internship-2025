import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load model
model = joblib.load('model.pkl')
iris = load_iris()

st.title("🌼 Iris Flower Predictor")
st.write("Input flower measurements and get the species prediction!")

# Input sliders
sepal_length = st.slider('Sepal Length (cm)', 4.0, 8.0, 5.0)
sepal_width = st.slider('Sepal Width (cm)', 2.0, 4.5, 3.0)
petal_length = st.slider('Petal Length (cm)', 1.0, 7.0, 4.0)
petal_width = st.slider('Petal Width (cm)', 0.1, 2.5, 1.0)

# Prediction
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(input_data)
prediction_proba = model.predict_proba(input_data)

st.subheader("Prediction")
st.write(f"Species: **{iris.target_names[prediction][0]}**")

st.subheader("Prediction Probabilities")
st.write(pd.DataFrame(prediction_proba, columns=iris.target_names))

# Feature importance
st.subheader("Feature Importance")
feat_importances = pd.Series(model.feature_importances_, index=iris.feature_names)
fig, ax = plt.subplots()
feat_importances.plot(kind='barh', ax=ax)
st.pyplot(fig)
