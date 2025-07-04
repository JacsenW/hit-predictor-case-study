import pandas as pd
from sqlalchemy import create_engine

# Update this path to your cleaned CSV file location
csv_path = r'C:\Users\jacse\OneDrive\Documents\hit-predictor-case-study\data\cleaned_spotify_merged.csv'

# Load the CSV into a DataFrame
df = pd.read_csv(csv_path)

# PostgreSQL connection info — update password here!
username = 'postgres'
password = '6041'  # <-- Replace this!
host = 'localhost'
port = 5432
database = 'spotify_db'

# Create the SQLAlchemy engine
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

# Write the DataFrame to PostgreSQL table called 'spotify_tracks'
df.to_sql('spotify_tracks', engine, if_exists='replace', index=False)

print("Data loaded successfully!")
