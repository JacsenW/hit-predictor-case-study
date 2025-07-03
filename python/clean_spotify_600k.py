import pandas as pd

# Load CSVs
import pandas as pd

# Use raw strings or double backslashes in Windows paths
tracks = pd.read_csv(r'C:\Users\jacse\OneDrive\Documents\hit-predictor-case-study\data\tracks.csv')
artists = pd.read_csv(r'C:\Users\jacse\OneDrive\Documents\hit-predictor-case-study\data\artists.csv')


# Preview the data
print("Tracks:")
print(tracks.head())
print("\nArtists:")
print(artists.head())
