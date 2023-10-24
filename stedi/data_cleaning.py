import pandas as pd
import json
import os
import glob

INPUT_PATH = "../../stedihumanbalanceanalyticsdata/"
OUTPUT_PATH = "../../cleaned_data/"

settings = [{'input_path': INPUT_PATH + "customers/*.json",
             'output_path': OUTPUT_PATH + "customers/landing/"},
            {'input_path': INPUT_PATH + "accelerometer/*.json",
             'output_path': OUTPUT_PATH + "accelerometer/landing/"},
            {'input_path': INPUT_PATH + "step_trainer/*.json",
             'output_path': OUTPUT_PATH + "step_trainer/landing/"}]


def read_json_to_df(path):
    # Read the entire file as a single string
    with open(path, 'r') as f:
        data = f.read()

    # Split the string into individual JSON objects, removing leading/trailing whitespace
    data = data.split('}{')
    data[0] = data[0] + '}'
    data[-1] = '{' + data[-1]
    for i in range(1, len(data) - 1):
        data[i] = '{' + data[i] + '}'

    # Convert each string into a Python dict, then convert the entire list into a DataFrame
    df = pd.DataFrame([json.loads(item) for item in data])
    return df


def read_valid_json_to_dict(path):
    # Open the file
    with open(path, 'r') as f:
        data = f.read()

    # Create an empty list to store the valid JSON objects
    json_objects = []

    # Create an empty string to store characters of a single JSON object
    json_str = ''

    # Iterate over each character in the file
    for char in data:
        # Add the character to the current JSON object string
        json_str += char

        # If the character is '}', it indicates the end of a JSON object
        if char == '}':
            # Attempt to parse the JSON string
            try:
                json_obj = json.loads(json_str)
                json_objects.append(json_obj)
            except json.JSONDecodeError:
                print(f"  JSONDecodeError: {e}")
                print (f"  MALFORMED JSON object {json_str}.")
                pass

            # Reset the JSON string to start building the next JSON object
            json_str = ''

    # If the last JSON object is incomplete, print an error
    if json_str.strip() != '':
        print ("  INCOMPLETE JSON file.")

    return json_objects


for setting in settings:
    json_paths = glob.glob(setting['input_path'])
    for json_path in json_paths:
        print("Working on", json_path, "...")
        json_objects = read_valid_json_to_dict(json_path)
        filename = os.path.basename(json_path)

        # Create directories if they don't exist
        os.makedirs(os.path.dirname(setting['output_path']), exist_ok=True)

        with open(os.path.join(setting['output_path'],filename), 'w') as f:
            # Store as a single list of JSON objects.
            # json.dump(json_objects, f)

            # Store as line-by-line JSON objects
            for entry in json_objects:
                json.dump(entry, f)
                f.write('\n')
