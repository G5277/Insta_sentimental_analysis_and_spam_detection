import os
import json

destination_folder = os.path.expanduser('~/.kaggle') 
kaggle_json_path = os.path.join(destination_folder, 'kaggle.json')

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

username = input("Enter your Kaggle username: ")
api_key = input("Enter your Kaggle API key: ")

kaggle_config = {
    "username": username,
    "key": api_key
}

with open(kaggle_json_path, 'w') as f:
    json.dump(kaggle_config, f)

print(f"Successfully created kaggle.json at {kaggle_json_path}")
print("You can now use Kaggle API commands.")
