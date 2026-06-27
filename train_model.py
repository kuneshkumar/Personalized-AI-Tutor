import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import joblib
import os
import json

#CREATE MODEL FOLDER to save trained model file
os.makedirs('models', exist_ok=True)

# LOAD DATA (CSV File)
df = pd.read_csv('data/student_data.csv')

print("\nColumns in dataset:")
print(df.columns.tolist())
print("\nFirst three rows:")
print(df.head(3))


#CONVER TEXT INTO NUMBERS (ML model understand numbers)
#Using LableEncoder to do this conversion automatically

#columns in text
text_columns =['skill_level', 'interest', 'time_available', 'goal']

#dictionary to store encoders
encoders = {}

#convert each text column to numbers
for col in text_columns:
    encoder = LabelEncoder()
    df[col + '_encoded'] = encoder.fit_transform(df[col])
    encoders[col] = encoder 
    print(f"{col} -> Numbers (0 to {len(encoder.classes_)-1})")
    

#SEPERATE INPUTS AND OUTPUTS
#input features:
x= df[[
    'skill_level_encoded',
    'interest_encoded',
    'time_available_encoded',
    'past_performance',
    'goal_encoded'    
]]

#OUTPUTS
#training seperate models for each output (multi-output classification)
y_topic = df['recommended_topic']
y_difficulty = df['difficulty_level']
y_resource = df['resource_type']

print(f"\nInput features: {x.shape[1]}")
print(f"Output 1: recommended_topic ({y_topic.nunique()} unique values)")
print(f"Output 2: difficulty_level ({y_difficulty.nunique()} unique values)")
print(f"Output 3: resource_type ({y_resource.nunique()} unique values)")


#SPLITING DATA FOR TRAINING AND TESTING
#80% for training, 20% for testing
print("\nSplitting data into train (80%) and test (20%)...")

x_train, x_test, y_topic_train, y_topic_test = train_test_split(
    x, y_topic, test_size=0.2, random_state=42
)
# Using SAME split for all outputs
# using y_topic_train/Test as the reference, but training separate models
y_difficulty_train = df.loc[y_topic_train.index, 'difficulty_level']
y_difficulty_test = df.loc[y_topic_test.index, 'difficulty_level']
y_resource_train = df.loc[y_topic_train.index, 'resource_type']
y_resource_test = df.loc[y_topic_test.index, 'resource_type']

print(f"    Training: {len(x_train)} records")
print(f"    Testing: {len(x_test)} records")


#TRAIN THE MODEL
print("\nTraining Random Forest models...")

# Model 1: Predict recommended_topic
print("\n   Training Topic Model...")
model_topic = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model_topic.fit(x_train, y_topic_train)

# Model 2: Predict difficulty_level
print("    Training Difficulty Model...")
model_difficulty = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model_difficulty.fit(x_train, y_difficulty_train)

# Model 3: Predict resource_type
print("    Training Resource Model...")
model_resource = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model_resource.fit(x_train, y_resource_train)

print("All models trained successfully!")


#EVALUATE PERFORMANCE
print("Evaluating Model performance")
# Make predictions on test data
topic_pred = model_topic.predict(x_test)
difficulty_pred = model_difficulty.predict(x_test)
resource_pred = model_resource.predict(x_test)

# Calculate accuracy for each output
topic_accuracy = accuracy_score(y_topic_test, topic_pred)
difficulty_accuracy = accuracy_score(y_difficulty_test, difficulty_pred)
resource_accuracy = accuracy_score(y_resource_test, resource_pred)

print(f"\nACCURACY RESULTS:")
print(f"Topic Prediction Accuracy: {topic_accuracy:.1%}")
print(f"Difficulty Prediction Accuracy: {difficulty_accuracy:.1%}")
print(f"Resource Prediction Accuracy: {resource_accuracy:.1%}")
print(f"Overall Average Accuracy: {(topic_accuracy + difficulty_accuracy + resource_accuracy) / 3:.1%}")

# FEATURE IMPORTANCE - Which inputs are most important for predictions
print("\nFeature Importance (what influences recommendations most):")
feature_names = ['skill_level', 'interest', 'time_available', 'past_performance', 'goal']

#Get Importance from topic_model
importance = model_topic.feature_importances_
importance_df = pd.DataFrame({
    'Features': feature_names,
    'Importance': importance
}).sort_values('Importance', ascending=False)

print(importance_df.to_string(index=False))


## ---SAVE MODELS AND ENCODERS
print("Saving models...")

#Save 3 models
joblib.dump(model_topic,'models/model_topic.pkl')
joblib.dump(model_difficulty,'models/model_difficulty.pkl')
joblib.dump(model_resource,'models/model_resource.pkl')

#save thr encoders
joblib.dump(encoders,'models/encoders.pkl')

print("\nModels and Encoders are saved in 'models' folder")


#SAMPLE PREDICTION FOR TESTING
print("\nTesting with a sample student...")

# Create a sample student (Beginner, Python, 2-4 hours, score 65, Hobby)
sample_input = pd.DataFrame([[
    0,  # Beginner (encoded)
    0,  # Python (encoded)
    1,  # 2-4 hours (encoded)
    65, # Past performance
    3   # Hobby (encoded)
]], columns=x.columns)

# Make predictions
topic_pred = model_topic.predict(sample_input)[0]
difficulty_pred = model_difficulty.predict(sample_input)[0]
resource_pred = model_resource.predict(sample_input)[0]

print(f"\nSample Student:")
print(f"Skill Level: Beginner")
print(f"Interest: Python")
print(f"Time Available: 2-4 hours")
print(f"Past Performance: 65")
print(f"Goal: Hobby")
print(f"\nPredictions:")
print(f"Recommended Topic: {topic_pred}")
print(f"Difficulty Level: {difficulty_pred}")
print(f"Resource Type: {resource_pred}")

#DONE
print("TRAINING COMPLETE.")