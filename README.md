# Personalized-AI-Tutor
An AI Tutor for personalized student learning recommendations. it helps students find the right topics, difficulty levels, and resources based on their profile.

## Team Members
Kunesh Kumar - 2k23/CSE/70

Nazir Ahmed - 2k23/CSE/118

Abdul Samad - 2k23/CSE/12

## Features
- **Student Profile Input** — Name, skill level, interest, time availability, performance score, learning goal
- **ML-Based Recommendations** — Random Forest predicts Topic, Difficulty, and Resource Type
- **Confidence Scores** — Visual bars show prediction confidence
- **Explainability** — Natural language explanation + Feature Importance chart
- **Visual UI** — Clean, modern design with Streamlit and Plotly
- **Profile Snapshot** — Quick view of student profile

## Tech Stack
- **Python** - Programming language
- **Streamlit** - Web UI framework
- **Streamlit** - Web UI framework
- **Scikit-learn** - Machine Learning (Random Forest)
- **Plotly** - Interactive charts
- **Pandas** - Data manipulation
- **Joblib** - Model persistence

## Project Structure
  Personalized-AI-Tutor/
  
    ├── app.py # Main Streamlit application
  
    ├── train_model.py # Model training script
  
    ├── create_dataset.py # Dataset generation script
  
    ├── requirements.txt # Python dependencies
  
    ├── README.md # Project documentation
  
    ├── data/
  
      │ ├── student_data.csv # Dataset (2000 sample records)
  
      │ └── mapping.json # UI dropdown mapping
  
    ├── models/
  
      │ ├── model_topic.pkl # Topic prediction model
  
      │ ├── model_difficulty.pkl # Difficulty prediction model
  
      │ ├── model_resource.pkl # Resource prediction model
  
      │ └── encoders.pkl # Label encoders
  
    └── screenshots/ # UI screenshots

## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/kuneshkumar/Personalized-AI-Tutor.git
cd Personalized-AI-Tutor
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Generate Dataset (Optional — already included)
```bash
python create_dataset.py
```
### 4. Train Models (Optional — already included)
```bash
python train_model.py
```
### 5. Run the Application
```bash
streamlit run app.py
```

## Screenshots
Available in screenshots folder. 

## How it works

### Input
Student fills in their profile:

- **Skill Level:** Beginner / Intermediate / Advanced

- **Interest:** Python, Web Development, Data Science, ML, Mobile Development

- **Time Available:** 1-2 hrs / 2-4 hrs / 4-6 hrs / 6+ hrs

- **Performance Score:** 50-100

- **Learning Goal:** Career / Hobby / Academic / Certification

### Processing
- Inputs are encoded using LabelEncoders

- Three Random Forest models predict:
  - Recommended Topic
  - Difficulty Level (Easy/Medium/Hard)
  - Resource Type (Video/Article/Interactive/Book)

### Output
- Recommendations with confidence bars
- Natural language explanation
- Feature importance chart

## Model Performance
- Topic Prediction:	88.3%
- Difficulty Prediction:	93.3%
- Resource Prediction:	100%
- Overall:	93.9%

## Feature Importance
- Past Performance:	32.2%
- Interest:	30.6%
- Skill Level:	24.3%
- Time Available:	6.9%
- Goal:	6.0%
-- Past Performance and Interest are the strongest factors influencing recommendations.

## Explainability Module
The app provides two types of explanations:

**Natural Language Explanation**

- Shows why the recommendation was made
- Links each output to the student's input

**Feature Importance Chart**
- Shows which factors influenced the decision
- Past Performance and Interest are the strongest factors

## Future Work
- Deploy with real student data
- Add more features(Age, Previous experience)

## Limitations
- Dataset is synthetic (not real student data)
- Limited to 5 interests and 3 skill levels
- Confidence scores depend on dataset diversity

## License
This project is for educational purposes only.

## Acknowledgments
Developed as part of the Artificial Intelligence Lab course.
