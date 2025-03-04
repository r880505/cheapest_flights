import json
import os

def read_json(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file = os.path.join(current_dir, filename)
    
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"The JSON file '{json_file}' was not found.")
        return None
    except json.JSONDecodeError:
        print("The JSON file is not valid.")
        return None
    