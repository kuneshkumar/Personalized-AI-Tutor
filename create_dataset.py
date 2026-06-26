#This file is just to create a dataset file

import pandas as pd 
import random 
import os

#using seed to get same random number everytime dataset is created - SAME DATASET
random.seed(42)

#create data folder
os.makedirs('data', exist_ok=True)

#---ALL POSSIBLE VALUES---

#Skill levels of students
skill_levels = [
    'Beginner',
    'Intermediate',
    'Advanced'
]

#Subjects, students want to learn
interests = [
    'Python',
    'Web Development',
    'Data Science',
    'Machine Learning',
    'Mobile Development'
]

#Time, students can give to study
time_options = [
    '1-2 hours',
    '2-4 hours',
    '4-6 hours',
    '6+ hours'    
]

#why student wants to learn that
goals = [
    'Career',
    'Hobby',
    'Academic',
    'Certifications'
]


#---TOPICS FOR EACH INTEREST AND LEVEL---

topics_by_interest={
    'Python': {
        'Beginner': ['Python Basic', 'Control Flow', 'Functions and Modules'],
        'Intermediate': ['Data Structures', 'Libraries (Pandas/NumPy)', 'Web Scraping'],
        'Advanced': ['Decorators & Generators', 'System Design', 'Optimization']
    },
    'Web Development': {
        'Beginner': ['HTML/CSS Basics', 'JavaScript Basics', 'Responsive Design'],
        'Intermediate': ['React.js', 'Node.js', 'APIs & Backend'],
        'Advanced': ['Full Stack Architecture', 'Microservices', 'Performance Optimization']
    },
    'Data Science': {
        'Beginner': ['Statistics Basics', 'Python for Data', 'Data Visualization'],
        'Intermediate': ['Pandas & Data Cleaning', 'ML Basics', 'SQL for Data'],
        'Advanced': ['Deep Learning', 'Big Data Tools', 'Advanced Visualization']
    },
    'Machine Learning': {
        'Beginner': ['Python for ML', 'Math for ML', 'ML Fundamentals'],
        'Intermediate': ['Scikit-learn', 'Feature Engineering', 'Model Evaluation'],
        'Advanced': ['Neural Networks', 'Reinforcement Learning', 'Model Deployment']
    },
    'Mobile Development': {
        'Beginner': ['App Design Basics', 'Programming Fundamentals', 'UI/UX'],
        'Intermediate': ['React Native', 'Flutter/Dart', 'App State Management'],
        'Advanced': ['Cross-platform Architecture', 'Performance Optimization', 'Native Modules']
    }
}

#Other Possible Outputs
difficulty_levels = ['Easy','Medium', 'Hard']
resource_types = ['Video', 'Article', 'Interactive', 'Book']