from datetime import datetime
from unidecode import unidecode
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


def normalize_date(date_str):
    '''
    This function takes a date string and returns a normalized
    date string in the format YYYY-MM-DD.
    '''
    for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d %B %Y"):
        try:
            return datetime.strptime(date_str, fmt).date().isoformat()
        except ValueError:
            continue
    raise ValueError(f"Date {date_str} is not in a recognized format.")


def concat_json_csv(donnees_json, donnees_df):
    # Convertir JSON et CSV en DataFrames pandas
    df_json = pd.DataFrame(donnees_json)
    df_final = pd.concat([df_json, donnees_df], axis=0, ignore_index=True)
    return df_final


def generate_new_id_with_prefix(existing_ids):
    """
    Generates a new ID with the prefix 'NEWID' and a sequence of characters,
    ensuring the total length matches the length of the longest existing ID.
    """
    max_id_length = max(len(id) for id in existing_ids)
    prefix = 'NEWID'
    numeric_part_length = max_id_length - len(prefix)
    new_id_sequence = 1
    while True:
        new_id = f"{prefix}{str(new_id_sequence).zfill(numeric_part_length)}"
        if new_id not in existing_ids:
            break
        new_id_sequence += 1

    return new_id


def clean_string(sentence):
    """
    This function takes a string and returns a cleaned version of it.
    """
    return unidecode(sentence.strip().lower())

# TODO change name
def convert_result_to_dict(result_dict):
    """
    Converts the result dictionary to the desired output format.

    Params:
        result_dict: The dictionary with drug mentions dataframes.
    Returns:
        A dictionary suitable for JSON serialization.
    """
    output_dict = {}

    for drug, mentions_df in result_dict.items():
        # replace the title by the scientific one for the trials
        if 'scientific_title' in mentions_df.columns:
            mentions_df['title'] = mentions_df['title'].fillna(
                mentions_df['scientific_title'])
        output_dict[drug] = list(
            map(tuple, mentions_df[
                ['title', 'source', 'date', 'source', 'journal']].values))
    return output_dict
