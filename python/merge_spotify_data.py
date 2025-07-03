import pandas as pd
import ast

#Load raw data 
tracks = pd.read_csv(r'C:\Users\jacse\OneDrive\Documents\hit-predictor-case-study\data\tracks.csv')
artists = pd.read_csv(r'C:\Users\jacse\OneDrive\Documents\hit-predictor-case-study\data\artists.csv')

artists = artists.rename(columns={'id': 'artist_id', 'name': 'artist_name'})

#Some tracks have multiple artists, so we need to merge the artists data into the tracks data

def get_first_artist_id(x):
    try:
        artist_list = ast.literal_eval(x)
        if isinstance(artist_list, list) and len(artist_list) > 0:
            return artist_list[0]
        else:
            return None
    except:
        return None
    
tracks['artist_id'] = tracks['id_artists'].apply(get_first_artist_id)
# Merge tracks with artists
merged = pd.merge(tracks, artists, on='artist_id', how='left')

#Add is_viral column (popularity >= 75)
merged['is_viral'] = merged['popularity_x'].apply(lambda x: True if x >= 75 else False)

#Convert duration into seconds
merged['duration_sec'] = merged['duration_ms'] / 1000

#Select and rename columns you want to keep
clean_df = merged[[
    'id', 'name', 'artist_name', 'release_date', 'duration_sec', 'explicit',
    'popularity_x', 'is_viral', 'danceability', 'energy', 'loudness', 'speechiness',
    'acousticness', 'instrumentalness', 'valence', 'tempo', 'genres'
]].rename(columns={
    'id': 'song_id',
    'name': 'track_name',
    'popularity_x': 'song_popularity'
})

# Save the cleaned data to a new CSV file
clean_df.to_csv(r'C:\Users\jacse\OneDrive\Documents\hit-predictor-case-study\data\cleaned_spotify_merged.csv', index=False)
print("Data cleaning complete. Cleaned data saved to 'cleaned_spotify_merged.csv'.")