import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('best_model.pkl', 'rb'))

st.title("Movie Revenue Predictor")

# Inputs
budget = st.number_input("Budget")
popularity = st.number_input("Popularity")
runtime = st.number_input("Runtime")
vote_average = st.number_input("Vote Average")
vote_count = st.number_input("Vote Count")
genre_count = st.number_input("Genre Count")
cast_count = st.number_input("Cast Count")
crew_count = st.number_input("Crew Count")

if st.button("Predict Revenue"):
    features = np.array([[budget, popularity, runtime, vote_average, vote_count, genre_count, cast_count, crew_count]])
    prediction = model.predict(features)
    st.success(f"Predicted Revenue: ${prediction[0]:,.2f}")