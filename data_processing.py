# Install virtualenv for python3
# virtualenv -p python3 venv

# Import all required libraries
import csv
import statistics
import pandas as pd
import numpy as np

# Simulate data reading
df = pd.read_excel('/Users/stephenarjanto/Desktop/cloud/trial4.xlsx', sheet_name='Sheet1')
df.columns = ['Value']

zero_avg = np.mean(df.iloc[0:49,0])
noise = statistics.stdev(df.iloc[0:49,0])
threshold_noise = 4*noise
# print('noise_stdev = ', noise)
# print('zero_avg = ', zero_avg)

threshold_signal = zero_avg - threshold_noise
# print('threshold_signal = ', threshold_signal)

# Remove all values larger than threshold signal
clean_df = df[df['Value']<threshold_signal] - zero_avg

# print('df', df)
# print('clean_df', clean_df)

# Need to divide the clean_df into two parts (inhale and exhale)
# print(clean_df.index.values)
# first_index = clean_df.index.values[0]
# print('first_index = ', first_index)

# cutoff_index = 0
# for entry in clean_df.index.value:
# 	current_entry = entry

# 	previous_entry = current_entry

index_list = clean_df.index.values
# print(index_list)

# Calculate the difference between values in the index list 
dif_index = [index_list[i+1] - index_list[i] for i in range(len(index_list)-1)]

# Threshold index
threshold_index = 50

# print('dif_index = ', dif_index)

# Find the index where the index list "jump"
separation_index = next(x for x, val in enumerate(dif_index) if val > threshold_index)
# print('separation_index = ' , separation_index)

inhalation = clean_df.iloc[0:separation_index+1,:]
exhalation = clean_df.iloc[separation_index+1:-1,:]

# print('inhalation = ', inhalation)
# print('exhalation = ', exhalation)

# Reset the index
# new_inhalation = inhalation.reset_index(drop=True)
# new_exhalation = exhalation.reset_index(drop=True)
new_inhalation = inhalation.values
new_exhalation = exhalation.values

x_inhale = np.linspace(1,len(new_inhalation),len(new_inhalation))
print('x_inhale = ', x_inhale)
new_inhalation = new_inhalation[:,0]
print('new_inhale = ', new_inhalation)

evaluation_points = np.linspace(0,70,25)
evaluation_points = evaluation_points
final_inhale = np.interp(evaluation_points,x_inhale,new_inhalation)

print('final_inhale = ', final_inhale)
print('final_inhale length =', len(final_inhale))