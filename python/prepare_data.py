import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load raw data
df = pd.read_csv('data/cleaned_spotify_merged.csv')

#show the first few rows of the DataFrame
print(df.head())
print(df.columns)

#Features we want to use for prediction
feature_cols = [
    'danceability', 'energy', 'valence', 'tempo', 'duration_sec',
    'explicit', 'acousticness', 'instrumentalness', 'speechiness'
]

#Convert 'explicit' from boolean to integer 
df['explicit'] = df['explicit'].astype(int)

#Define input features x and target variable y
X = df[feature_cols]
y = df['is_viral'].astype(int)  # Ensure target is 0 or 1

#Quick check shapes and data types
print(X.shape, y.shape)
print(X.dtypes)
print(y.unique())

X = X.fillna(X.mean())  # Fill NaN values with column means

# Split the data into 80% training and 20% testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Scale the features using StandardScaler to have mean=0 and std=1 for better model performance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#Quick check shapes after scaling
print('Train set:', X_train_scaled.shape, y_train.shape)
print('Test set:', X_test_scaled.shape, y_test.shape)

#Initialize Random Forest model 
rf_model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)

#Train the model on the training data
rf_model.fit(X_train_scaled, y_train)

#Test data predictions
y_pred = rf_model.predict(X_test_scaled)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

