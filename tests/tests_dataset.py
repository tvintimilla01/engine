import pytest
import pandas as pd
from data_preprocessing import process_dataset_1, process_dataset_2

# Replace 'your_data_processing_module' with the name of your actual data processing module

def test_dataset_1():
    # Load Dataset 1 (replace with actual file path)
    dataset_1 = pd.read_csv('path/to/dataset_1.csv')

    # Process Dataset 1
    processed_dataset_1 = process_dataset_1(dataset_1)

    # Check if the processed dataset has the required columns
    expected_columns = [
        'user_id', 'game_id', 'playtime', 'review_sentiment',
        'genre', 'developer', 'publisher'
    ]
    for column in expected_columns:
        assert column in processed_dataset_1.columns

    # Check if the processed dataset has no null values
    assert processed_dataset_1.isnull().sum().sum() == 0

def test_dataset_2():
    # Load Dataset 2 (replace with actual file paths)
    steamspy_data = pd.read_csv('path/to/steamspy_data.csv')
    steam_api_data = pd.read_csv('path/to/steam_api_data.csv')

    # Process Dataset 2
    processed_dataset_2 = process_dataset_2(steamspy_data, steam_api_data)

    # Check if the processed dataset has the required columns
    expected_columns = [
        'game_id', 'owners', 'playtime', 'user_reviews',
        'price', 'release_date', 'genre'
    ]
    for column in expected_columns:
        assert column in processed_dataset_2.columns

    # Check if the processed dataset has no null values
    assert processed_dataset_2.isnull().sum().sum() == 0

if __name__ == "__main__":
    pytest.main([__file__])
