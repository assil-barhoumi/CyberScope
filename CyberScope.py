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
