import pandas as pd
import csv
import json
import regex as re


def load_csv_data(filepath: str) -> pd.DataFrame:
    """ Load and return a dataframe from a CSV file."""
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        return pd.DataFrame(reader)


def load_json_data(file_path: str) -> dict:
    """ Load and return a JSON object from a JSON file."""
    with open(file_path, 'r') as file:
        json_text = file.read()
    json_text = re.sub(r',(?=\s*])', '', json_text)
    json_data = json.loads(json_text)

    return json_data