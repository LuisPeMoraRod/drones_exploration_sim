import json


def config_file_data():
    try:
        # Read configuration file and return the data
        with open("./config/config.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading configuration file: {e}")
        return None
