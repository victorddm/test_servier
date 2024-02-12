import pandas as pd
from src.utils import concat_json_csv, normalize_date, clean_string


def preprocess_pubmed_articles(article_df: pd.DataFrame,
                               article_json: dict) -> pd.DataFrame:
    """
    Preprocesses the pubmed articles data by replacing empty titles and journals with an empty string
    """
    all_articles = concat_json_csv(article_json, article_df)
    all_articles['date'] = all_articles['date'].apply(normalize_date)
    all_articles['journal'] = all_articles['journal'].apply(clean_string)
    all_articles['title'] = all_articles['title'].apply(clean_string)

    return all_articles


def preprocess_clinical_trials(trials_data: pd.DataFrame) -> pd.DataFrame:
    """
    Proccesing the clinical trials data by replacing empty titles and journal with an empty string
    """
    trials_data['id'] = trials_data['id'].fillna('')
    trials_data['date'] = trials_data['date'].apply(normalize_date)
    trials_data['journal'] = trials_data['journal'].apply(clean_string)
    trials_data['title'] = trials_data['scientific_title'].apply(clean_string)

    return trials_data


def preprocess_drugs(drugs: pd.DataFrame) -> pd.DataFrame:
    """Load and format the drugs into a DataFrame."""
    drugs['drug'] = drugs['drug'].apply(clean_string)

    return drugs
