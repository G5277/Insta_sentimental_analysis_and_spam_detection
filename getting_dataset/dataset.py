import os
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

dataset_url = 'bwandowando/3-million-instagram-google-store-reviews'
download_path = './dataset'  # Local folder to store the dataset

# Create the folder if it doesn't exist
os.makedirs(download_path, exist_ok=True)

# Download the dataset
api.dataset_download_files(dataset_url, path=download_path, unzip=True)

print(f"Dataset downloaded and unzipped at: {os.path.abspath(download_path)}")
