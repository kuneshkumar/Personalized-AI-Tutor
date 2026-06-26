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



#---DEFINING RULES - Brain of data---

#Rule 1 - which topic to recommend
def get_topic(interest, skill_level, performance):
  
    #list of topics for interest and level
    level_topics = topics_by_interest.get(interest,{}).get(skill_level,['Basics'])
    
    #if no topics found, return a fallback
    if not level_topics:
        return 'Basics'
    
    #pick topic based on performance
    if performance >= 85:
        return level_topics[2] if len(level_topics) > 2 else level_topics[-1]
    elif performance >= 70:
        return level_topics[1] if len(level_topics) > 1 else level_topics[0]
    else:
        return level_topics[0]
    

#Rule 2 - What Difficulty Level?
def get_difficulty(skill_level, goal, performance):
    #Career Goal + High Performance = Hard
    if goal == 'Career' and performance >= 80:
        return "Hard"
    #Academic/Certification + good performance = Medium
    elif goal in ['Academic', 'Certfications'] and performance >= 70:
        return "Medium"
    #Hobby or Low Performance = Easy
    elif goal == 'Hobby' or performance < 70:
        return "Easy"
    
    #Default: Follow Skill Level
    else:
        if skill_level == 'Advanced':
            return "Hard"
        elif skill_level == 'Intermediate':
            return "Medium"
        else:
            return "Easy"


#Rule 3 - What Resource Type
def get_resource_type(time_available):
    if time_available == '6+ hours':
        return "Book"
    elif time_available == '4-6 hours':
        return "Interactive"
    elif time_available == '2-4 hours':
        return "Video"
    else: #1-2 hours
        return "Article"
    
    
# --- GENERATE STUDENT RECORDS ---
#creating 2000 student records 
#Each record has: 5 Input features, 3 Output features

print("Generating students dataset...")

#Empty list to store all rows
data = []

#loop for 2000 students (student_id 1-2000)
for student_id in range(1,2001):
    #INPUTS - randomly assigns values
    skill_level = random.choice(skill_levels)
    interest = random.choice(interests)
    time_available = random.choice(time_options)
    past_performance = random.randint(50,100)
    goal = random.choice(goals)
    
    #OUTPUTS - Calculate based on the rules above
    recommended_topic = get_topic(interest, skill_level, past_performance) 
    difficulty = get_difficulty(skill_level, goal, past_performance)
    resource = get_resource_type(time_available)
    
    #add this student's complete record to data list
    data.append([
        student_id,
        skill_level,
        interest,
        time_available,
        past_performance,
        goal,
        recommended_topic,
        difficulty,
        resource
    ])   
    
#--- CONVERTING DATA INTO DATAFRAME----
#Define column names
columns = [
    'student_id',
    'skill_level',         
    'interest',            
    'time_available',      
    'past_performance',    
    'goal',                
    'recommended_topic',   
    'difficulty_level',    
    'resource_type' 
]    

#Create Dataframe
df = pd.DataFrame(data,columns=columns)

#save to CSV file
df.to_csv('data/student_data.csv', index=False)

#SUMMARY STATISTICS
print("\nDataset created successfully.")
print(f"Total Records: {len(df)}")

print("\nInput features (5):")
print("   1. skill_level")
print("   2. interest")
print("   3. time_available")
print("   4. past_performance")
print("   5. goal")

print("\nOutputs (3):")
print("   1. recommended_topic")
print("   2. difficulty_level")
print("   3. resource_type")

print("\nDistribution of each feature:")

print("\n1. Skill Level:")
print(df['skill_level'].value_counts())

print("\n2. Interest:")
print(df['interest'].value_counts())

print("\n3. Time Available:")
print(df['time_available'].value_counts())

print("\n4. Goal:")
print(df['goal'].value_counts())

print("\n5. Difficulty Level:")
print(df['difficulty_level'].value_counts())

print("\n6. Resource Type:")
print(df['resource_type'].value_counts())

print("\n First 5 rows (preview):")
print(df.head())

print("\nFile saved to: data/student_data.csv")
