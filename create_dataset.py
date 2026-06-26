#This file is just to create a dataset file

import pandas as pd 
import random 
import os

#using seed to get same random number everytime dataset is created - SAME DATASET
random.seed(42)

#create data folder
os.makedirs('data', exist_ok=True)
