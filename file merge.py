import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Training Data
training_data = pd.read_csv(r'C:\\...\\Training Data.csv')

# Load Data files
data_files = [r'C:\\...\\Data ({i}).csv'.format(i=i) for i in range(1, 15)]
data_list = [pd.read_csv(file) for file in data_files]

# Merge Data files into a single dataframe
data_combined = pd.concat(data_list, ignore_index=True)

# Standardize column names to ensure consistent access
training_data.columns = training_data.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
data_combined.columns = data_combined.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

# Convert columns to lowercase for consistent access
training_data.columns = training_data.columns.str.lower()
data_combined.columns = data_combined.columns.str.lower()

# Function to identify and replace non-numeric values with NaN
def clean_non_numeric(series):
    return pd.to_numeric(series, errors='coerce')

# Apply the function to specific columns
if 'column' in data_combined.columns:
    data_combined['column'] = clean_non_numeric(data_combined['column'])
if 'column' in data_combined.columns:
    data_combined['column'] = clean_non_numeric(data_combined['column'])
if 'column' in training_data.columns:
    training_data['column'] = clean_non_numeric(training_data['column'])
if 'column' in training_data.columns:
    training_data['column'] = clean_non_numeric(training_data['column'])

# Convert numerical columns to numeric, coercing errors to NaN
numerical_columns = ['column', 'column', 'column', 'column']
for column in numerical_columns:
    if column in data_combined.columns:
        data_combined[column] = pd.to_numeric(data_combined[column], errors='coerce')
    if column in training_data.columns:
        training_data[column] = pd.to_numeric(training_data[column], errors='coerce')

# Handling Missing Data in Data Combined
data_combined.fillna({
    'column': data_combined['column'].mean(),
    'column': data_combined['column'].mode()[0],
    # Add more columns as needed
}, inplace=True)

# Handling Missing Data in Training Data
training_data.fillna({
    'column': training_data['column'].mean(),
    'column': training_data['column'].mode()[0],
    # Add more columns as needed
}, inplace=True)

# Ensure "column" remains as integers
training_data['column'] = training_data['column'].astype('Int64')
data_combined['column'] = data_combined['column'].astype('Int64')

# Export to Excel with Two Sheets
with pd.ExcelWriter(r'C:\\...\\Data_merged.xlsx') as writer:
    training_data.to_excel(writer, sheet_name='Training_Data', index=False)
    data_combined.to_excel(writer, sheet_name='Data_Combined', index=False)

# Export combined data to CSV
combined_csv_path = r'C:\\...\\Data_merged.csv'
data_combined.to_csv(combined_csv_path, index=False)

print("Data preprocessing and exporting to Excel and CSV files completed successfully.")

