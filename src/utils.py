from datetime import datetime
from unidecode import unidecode
import pandas as pd


def normalize_date(date_str: str) -> str:
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


def concat_json_csv(data_json: dict, donnees_df: pd.DataFrame) -> pd.DataFrame:
    """ Concatenates a JSON object and a DataFrame."""
    df_json = pd.DataFrame(data_json)
    df_final = pd.concat([df_json, donnees_df], axis=0, ignore_index=True)
    return df_final


def clean_string(sentence: str) -> str:
    """
    This function takes a string and returns a cleaned version of it.
    """
    return unidecode(sentence.strip().lower())


def reformat_dict_serialization(graph_dict):
    """
    Converts the result dictionary to the desired output format.
    """
    serializable_graph_dict = {}

    for drug, mentions_df in graph_dict.items():
        # replace the title by the scientific one for the trials
        if 'scientific_title' in mentions_df.columns:
            mentions_df['title'] = mentions_df['title'].fillna(
                mentions_df['scientific_title'])
        serializable_graph_dict[drug] = list(
            map(tuple, mentions_df[
                ['title', 'source', 'date', 'source', 'journal']].values))
    return serializable_graph_dict
