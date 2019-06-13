# Install virtualenv for python3
# virtualenv -p python3 venv

# Import all required libraries
import csv
import statistics
import pandas as pd
import numpy as np

import datetime

# Simulate data reading
df = pd.read_excel('/Users/stephenarjanto/Desktop/cloud/trial4.xlsx', sheet_name='Sheet1')
df.columns = ['Value']

# Obtain zero input average values and noise standard deviation
zero_avg = np.mean(df.iloc[0:49,0])
noise = statistics.stdev(df.iloc[0:49,0])

# Determine signal cutoff & remove unneeded data points
threshold_noise = 4*noise
threshold_signal = zero_avg - threshold_noise
clean_df = df[df['Value']<threshold_signal] - zero_avg

# Obtain signal index
index_list = clean_df.index.values

# Calculate the difference between values in the index list 
dif_index = [index_list[i+1] - index_list[i] for i in range(len(index_list)-1)]

# Threshold index (minimum "jump" required)
threshold_index = 50

# Find the index where the index list "jump" and separate data
separation_index = next(x for x, val in enumerate(dif_index) if val > threshold_index)
inhalation = clean_df.iloc[0:separation_index+1,:]
exhalation = clean_df.iloc[separation_index+1:-1,:]
# print('separation_index = ' , separation_index)

# Remove built-in index
new_inhalation = inhalation.values[:,0]
new_exhalation = exhalation.values[:,0]

# Interpolate between inhalation data points
x_inhale = np.linspace(1,len(new_inhalation),len(new_inhalation))
evaluation_points = np.linspace(0,len(new_inhalation),25)
final_inhale = np.interp(evaluation_points,x_inhale,new_inhalation)

# Interpolate between exhalation data points
x_exhale = np.linspace(1,len(new_exhalation),len(new_exhalation))
exhale_evaluation_points = np.linspace(0,len(new_exhalation),25)
final_exhale = np.interp(exhale_evaluation_points,x_exhale,new_exhalation)

# Get current date time
instance_time = datetime.datetime.now()
# print(instance_time)