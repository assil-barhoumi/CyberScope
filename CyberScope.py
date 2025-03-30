import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from google.colab import drive
import pandas as pd
import os

drive.mount('/content/drive', force_remount=True)
file_path = "/content/drive/MyDrive/pfa/cyber_data.csv"

if not os.path.exists(file_path):
    print(f"ERROR: The file {file_path} does not exist. Please check your Google Drive!")
else:
    print("File found, loading...")
    df = pd.read_csv(file_path)
    print("Preview of the first rows:")
    print(df.head())

date_pattern = r'^\d{2}/\d{2}/\d{4} 0:00$'

valid_dates_count = df['AttackDate'].str.match(date_pattern).sum()
print(f"Number of rows that match the '%d/%m/%Y 0:00' format: {valid_dates_count}")

df['AttackDate'] = df['AttackDate'].str.replace('0:00', '')

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

columns = ['spam', 'ransomware', 'local_infection', 'exploit', 'malicious_mail', 'network_attack', 'on_demand_scan', 'web_threat']

missing_values = df[columns].isnull().sum() / len(df) * 100
print("Missing Values Before Imputation:")
print(missing_values.round(2), "
")

for col in columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df[col], bins=30, kde=True)
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()

    df[col].fillna(df[col].median(), inplace=True)
    if df[col].skew() > 1:  
        df[f"{col}_log"] = np.log1p(df[col])  # log(1 + x) to avoid log(0)
        print(f"Log transformation applied to {col}")


missing_values_after = df[columns].isnull().sum().sum()
if missing_values_after == 0:
    print("
All missing values have been handled successfully!")
else:
    print(f"
Remaining missing values: {missing_values_after}") 
