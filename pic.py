import streamlit as st
import pickle
import numpy as np

# 🎨 Page config
st.set_page_config(
    page_title="🎬 Movie Revenue Predictor",
    page_icon="🎥",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 🌈 Custom CSS Styling
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
    }
    .main {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 🎯 Title
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🎬 Movie Revenue Predictor</h1>", unsafe_allow_html=True)
st.markdown("Use this ML-powered tool to predict box office revenue based on movie attributes. Just enter the values below 👇")

# 🧠 Load model
try:
    with open('best_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("🚫 Model file not found. Please upload 'best_model.pkl'.")
    st.stop()

# 📊 Sidebar Info
st.sidebar.title("📁 About")
st.sidebar.info("""
This app predicts a movie's revenue using a trained ML model based on:
- Budget
- Popularity
- Runtime
- Vote statistics
- Genre and cast/crew info
""")
st.sidebar.success("Made with 💡 by your name")

# 🎛 Inputs
st.markdown("### 🎚 Enter Movie Details")

col1, col2 = st.columns(2)

with col1:
    budget = st.number_input("💸 Budget ($)", value=10000000, step=1000000)
    popularity = st.number_input("🔥 Popularity Score", value=10.0, step=1.0)
    runtime = st.number_input("🎞 Runtime (min)", value=120, step=10)
    vote_average = st.slider("⭐ Vote Average", 0.0, 10.0, 6.5)

with col2:
    vote_count = st.number_input("🗳 Vote Count", value=1000, step=100)
    genre_count = st.number_input("🎭 Genre Count", value=3, step=1)
    cast_count = st.number_input("👤 Cast Members", value=10, step=1)
    crew_count = st.number_input("🎬 Crew Members", value=5, step=1)

# 📈 Prediction
if st.button("🚀 Predict Revenue"):
    features = np.array([[budget, popularity, runtime, vote_average, vote_count,
                          genre_count, cast_count, crew_count]])
    prediction = model.predict(features)[0]
    
    st.markdown(f"""
    <div style='background-color:#e6f7ff;padding:20px;border-radius:10px;'>
        <h2 style='color:#007acc;'>💰 Predicted Revenue: <span style='color:#28a745;'>${prediction:,.2f}</span></h2>
    </div>
    """, unsafe_allow_html=True)

    # 🎉 Add an optional success animation
    st.balloons()
