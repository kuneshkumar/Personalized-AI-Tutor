import streamlit as st
import pandas as pd
import joblib
import json


#Page configuration
st.set_page_config(
    page_title="Personalized AI Tutor",
    page_icon="🎓",
    layout="wide"
)

#CSS File---
st.html("style/style.css")

#Load Models and Data---
@st.cache_resource
def load_models():
    model_topic = joblib.load('models/model_topic.pkl')
    model_difficulty = joblib.load('models/model_difficulty.pkl')
    model_resource = joblib.load('models/model_resource.pkl')
    encoders = joblib.load('models/encoders.pkl')
    
    with open('data/mapping.json', 'r') as f:
        mapping = json.load(f)
    
    return model_topic, model_difficulty, model_resource, encoders, mapping

model_topic, model_difficulty, model_resource, encoders, mapping = load_models()

#Sidebar---
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 10px 0 20px 0;">
        <div style="font-size: 64px;">🎓</div>
        <h2 style="margin: 5px 0; color: #2d3748;">AI Tutor</h2>
        <p style="color: #718096; font-size: 14px;">Personalized Learning Assistant</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 📊 Model Performance")
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric("📚 Topic", "88.3%", delta="Good")
    with c2:
        st.metric("📊 Difficulty", "93.3%", delta="Excellent")
    
    c3, c4 = st.columns(2)
    with c3:
        st.metric("📖 Resource", "100%", delta="Perfect")
    with c4:
        st.metric("🎯 Overall", "93.9%", delta="Excellent")
    
    st.markdown("---")
    st.caption("🤖 Random Forest Classifier • 2000 samples")

#HEADER---
st.markdown("""
<div style="text-align: center; padding: 10px 0 0 0;">
    <h1 style="font-size: 38px; margin: 0;">🎓 Personalized AI Tutor</h1>
    <p style="color: #718096; font-size: 16px;">
        learning recommendations model
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
