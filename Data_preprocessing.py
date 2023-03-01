# Import libraries
import json
import pandas as pd
import numpy as np

#Import Warnings
import warnings
warnings.filterwarnings("ignore")

# Suppress warnings
np.warnings.filterwarnings('ignore')

# Load games data
with open('Data/gamesdata.json', 'r') as f:
    games_data = json.load(f)

# Create a dataframe from games data
df = pd.DataFrame(games_data)

# Save dataframe as a csv file
df.to_csv('gamesdata.csv', index=False)

# Extract the number of games for each user
num_games = df.groupby('user_id')['items'].count().reset_index()
num_games.columns = ['user_id', 'items_count']

# Save the number of games dataframe as a csv file
num_games.to_csv('numgames.csv', index=False)

# Preview items column values for the first user
print(df.loc[df['user_id'] == 0, 'items'].values[0][:2])

# Get all item_ids for the first user
game_ids = [item['item_id'] for item in df.loc[df['user_id'] == 0, 'items'].values[0]]

# Show first 10 item ids
print(game_ids[:10])

# Create a new dataframe with item_ids and corresponding user_ids
item_ids = df['items'].explode().reset_index()
item_ids = item_ids.rename(columns={'index': 'uid', 'items': 'id'})
item_ids['id'] = item_ids['id']['item_id']
item_ids = item_ids[['uid', 'id']]

# Add a column with binary owned value
item_ids['owned'] = 1

# Convert item_id to integer type
item_ids['id'] = item_ids['id'].astype(int)

# Merge item_ids and games data dataframes
merged_data = pd.merge(item_ids, df, on='id')

# Drop entries with no title
merged_data = merged_data.dropna(subset=['title'])

# Get relevant columns for recommendation engine
rec_data = merged_data[['uid', 'id', 'owned']]

# Save the merged and recommendation dataframes to csv files
merged_data.to_csv('mergeddata.csv', index=False)
rec_data.to_csv('recdata.csv', index=False)
