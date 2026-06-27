import pandas as pd
import os

#CREATE MODEL FOLDER to save trained model file
os.makedirs('models', exist_ok=True)

# LOAD DATA (CSV File)
df = pd.read_csv('data/student_data.csv')

print("\nColumns in dataset:")
print(df.columns.tolist())
print("\nFirst three rows:")
print(df.head(3))


