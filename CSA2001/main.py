import pandas as pd

# 1. Load the dataset
df = pd.read_csv('dataset.csv')

# 2. Basic Cleaning (First-year fundamental step!)
# Remove any rows with missing values
df = df.dropna()

# 3. Define "Focus" vs "Distraction" logic
# Focus: High instrumentalness, Low energy, Low speech
focus_criteria = (df['instrumentalness'] > 0.5) & (df['energy'] < 0.4)

# Distraction: High energy OR High speechiness (lyrics/talking)
distraction_criteria = (df['energy'] > 0.8) | (df['speechiness'] > 0.5)

# 4. Create a new column called 'target' (0 for Distraction, 1 for Focus)
df['is_focus'] = 0
df.loc[focus_criteria, 'is_focus'] = 1

# 5. Keep only the songs that fit these two clear categories for training
training_data = df[focus_criteria | distraction_criteria]

print(f"Dataset Loaded! We have {len(training_data)} songs for the AI to learn from.")
print(training_data[['track_name', 'is_focus']].head())