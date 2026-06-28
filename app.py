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


# TWO-COLUMN LAYOUT
col_left, col_right = st.columns([1, 1.2], gap="medium")

# LEFT COLUMN: INPUT FORM
with col_left:
    st.markdown("### 📝 Student Profile")
    
    with st.container():
        # st.markdown('<div class="card">', unsafe_allow_html=True)
        
        # Student Name Input
        student_name = st.text_input(
            "👤 Student Name",
            placeholder="Enter your name",
            value=""
        )
        
        skill_level = st.selectbox(
            "📊 Skill Level",
            options=mapping['skill_levels'],
            help="What is the student's current expertise level?"
        )
        
        interest = st.selectbox(
            "💡 Interest Area",
            options=mapping['interests'],
            help="What subject do you want to learn?"
        )
        
        time_available = st.selectbox(
            "⏰ Time Available (per week)",
            options=mapping['time_options'],
            help="How much time can you commit?"
        )
        
        past_performance = st.slider(
            "📈 Performance Score",
            min_value=50,
            max_value=100,
            value=70,
            step=1,
            help="Previous test/assessment score (50-100)"
        )
        
        goal = st.selectbox(
            "🎯 Learning Goal",
            options=mapping['goals'],
            help="Why are you learning this?"
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
    

    # SNAPSHOT
    
    st.markdown("### 📋 Profile Snapshot")
    
    # Determine performance level
    if past_performance >= 85:
        perf_level = "🌟 Excellent"
    elif past_performance >= 70:
        perf_level = "✅ Good"
    else:
        perf_level = "📈 Needs Improvement"
    
    st.markdown(f"""
    <div class="snapshot">
        <div class="snapshot-item">
            <span class="snapshot-label">👤 Name</span>
            <span class="snapshot-value">{student_name if student_name.strip() else 'Not provided'}</span>
        </div>
        <div class="snapshot-item">
            <span class="snapshot-label">📊 Skill Level</span>
            <span class="snapshot-value">{skill_level}</span>
        </div>
        <div class="snapshot-item">
            <span class="snapshot-label">💡 Interest</span>
            <span class="snapshot-value">{interest}</span>
        </div>
        <div class="snapshot-item">
            <span class="snapshot-label">⏰ Time Available</span>
            <span class="snapshot-value">{time_available}</span>
        </div>
        <div class="snapshot-item">
            <span class="snapshot-label">📈 Performance</span>
            <span class="snapshot-value">{past_performance}/100 {perf_level}</span>
        </div>
        <div class="snapshot-item" style="border-bottom: none;">
            <span class="snapshot-label">🎯 Goal</span>
            <span class="snapshot-value">{goal}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Predict Button
    st.markdown("---")
    predict_clicked = st.button("🎯 Get Recommendation", type="primary")

# RIGHT COLUMN: RESULTS
# ============================================================

with col_right:
    if predict_clicked:
        with st.spinner("🧠 Analyzing student profile..."):
            
            # Encode inputs
            skill_encoded = encoders['skill_level'].transform([skill_level])[0]
            interest_encoded = encoders['interest'].transform([interest])[0]
            time_encoded = encoders['time_available'].transform([time_available])[0]
            goal_encoded = encoders['goal'].transform([goal])[0]
            
            input_data = pd.DataFrame([[
                skill_encoded, interest_encoded, time_encoded,
                past_performance, goal_encoded
            ]], columns=[
                'skill_level_encoded', 'interest_encoded', 
                'time_available_encoded', 'past_performance', 'goal_encoded'
            ])
            
            # Predictions
            topic_pred = model_topic.predict(input_data)[0]
            difficulty_pred = model_difficulty.predict(input_data)[0]
            resource_pred = model_resource.predict(input_data)[0]
            
            topic_proba = model_topic.predict_proba(input_data)[0].max()
            difficulty_proba = model_difficulty.predict_proba(input_data)[0].max()
            resource_proba = model_resource.predict_proba(input_data)[0].max()
        
        
        # RESULTS DISPLAY
        
        
        if student_name.strip():
            st.markdown(f"### 🎯 Your Recommendations, **{student_name}**! 👋")
        else:
            st.markdown("### 🎯 Your Recommendations")
        
        rec_col1, rec_col2, rec_col3 = st.columns(3)
        
        with rec_col1:
            st.markdown(f"""
            <div class="rec-topic">
                <div style="font-size: 13px; opacity: 0.8;">📚 TOPIC</div>
                <div style="font-size: 18px; font-weight: 700; margin: 8px 0;">{topic_pred}</div>
                <div class="conf-bar">
                    <div class="conf-fill" style="width: {topic_proba*100}%;"></div>
                </div>
                <div style="font-size: 12px; opacity: 0.8; margin-top: 5px;">Confidence: {topic_proba:.0%}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with rec_col2:
            st.markdown(f"""
            <div class="rec-difficulty">
                <div style="font-size: 13px; opacity: 0.8;">📊 DIFFICULTY</div>
                <div style="font-size: 18px; font-weight: 700; margin: 8px 0;">{difficulty_pred}</div>
                <div class="conf-bar">
                    <div class="conf-fill" style="width: {difficulty_proba*100}%;"></div>
                </div>
                <div style="font-size: 12px; opacity: 0.8; margin-top: 5px;">Confidence: {difficulty_proba:.0%}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with rec_col3:
            st.markdown(f"""
            <div class="rec-resource">
                <div style="font-size: 13px; opacity: 0.8;">📖 RESOURCE</div>
                <div style="font-size: 18px; font-weight: 700; margin: 8px 0;">{resource_pred}</div>
                <div class="conf-bar">
                    <div class="conf-fill" style="width: {resource_proba*100}%;"></div>
                </div>
                <div style="font-size: 12px; opacity: 0.8; margin-top: 5px;">Confidence: {resource_proba:.0%}</div>
            </div>
            """, unsafe_allow_html=True)
        
        
        # EXPLANATION PANEL
                
        st.markdown("---")
        st.markdown("### 💡 Why This Recommendation?")
        
        greeting = f"Hi {student_name}! 👋" if student_name.strip() else ""
        
        st.markdown(f"""
        <div style="background: white; border-radius: 16px; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
            <p style="font-size: 16px; font-weight: 600;">{greeting}</p>
            <p style="margin: 5px 0;">
                <b>📚 Topic — {topic_pred}</b><br>
                You're a <b>{skill_level}</b> student interested in <b>{interest}</b>. 
                With a performance score of <b>{past_performance}/100</b>, 
                this topic matches your current level and interests.
            </p>
            <p style="margin: 12px 0 5px 0;">
                <b>📊 Difficulty — {difficulty_pred}</b><br>
                Based on your <b>{goal}</b> goal and <b>{past_performance}</b> performance, 
                this difficulty level keeps you challenged without being overwhelming.
            </p>
            <p style="margin: 12px 0 5px 0;">
                <b>📖 Resource — {resource_pred}</b><br>
                With <b>{time_available}</b> available per week, 
                <b>{resource_pred}</b>-based learning is the most effective format for your schedule.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        
        # FEATURE IMPORTANCE CHART
        #write here feature imp chart @kunesh
        
                
    else:
        # PLACEHOLDER
        
        st.markdown("""
        <div class="placeholder">
            <div class="placeholder-icon">🤖</div>
            <h3 style="color: #6c757d;">Ready for Your Input</h3>
            <p style="color: #a0aec0;">
                Enter your name and fill in the student profile on the left<br>
                then click <b>"Get Recommendation"</b>
            </p>
        </div>
        """, unsafe_allow_html=True)


# FOOTER
st.markdown("---")
st.caption("🎓 Personalized AI Tutor | Built with Streamlit, Scikit-learn & Plotly")

#UI Complete