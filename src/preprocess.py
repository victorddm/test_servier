import pandas as pd
from src.utils import generate_new_id_with_prefix, concat_json_csv, \
    normalize_date, clean_string


def preprocess_pubmed_articles(article_df: pd.DataFrame,
                               article_json: dict) -> pd.DataFrame:
    """
    Preprocesses the pubmed articles data by replacing empty titles and journals with an empty string
    and generating new IDs for entries with missing or empty IDs.
    """
    all_articles = concat_json_csv(article_json, article_df)
    all_articles['date'] = all_articles['date'].apply(normalize_date)
    all_articles['journal'] = all_articles['journal'].apply(clean_string)
    all_articles['title'] = all_articles['title'].apply(clean_string)

    # generate new IDs for entries with missing or empty IDs
    all_articles['id'] = all_articles['id'].fillna('')
    # make all id as string
    all_articles['id'] = all_articles['id'].astype(str)
    # Then, create a set of existing IDs, excluding those that are empty or contain only whitespace
    existing_ids = set(all_articles[all_articles['id'].str.strip() != '']['id'])

    for index, row in all_articles.iterrows():
        if not row['id'].strip():
            # Generate a new ID and update it in the DataFrame
            new_id = generate_new_id_with_prefix(existing_ids)
            all_articles.at[index, 'id'] = new_id
            # Update the set of existing IDs
            existing_ids.add(new_id)
    return all_articles


def preprocess_clinical_trials(trials_data: pd.DataFrame) -> pd.DataFrame:
    """
    Proccesing the clinical trials data by replacing empty titles and journal with an empty string
    and generating new IDs for entries with missing or empty IDs.
    """
    trials_data['id'] = trials_data['id'].fillna('')
    # Then, create a set of existing IDs, excluding those that are empty or contain only whitespace
    existing_ids = set(trials_data[trials_data['id'].str.strip() != '']['id'])

    trials_data['date'] = trials_data['date'].apply(normalize_date)
    trials_data['journal'] = trials_data['journal'].apply(clean_string)
    trials_data['title'] = trials_data['scientific_title'].apply(clean_string)

    for index, row in trials_data.iterrows():
        if not row['id'].strip():
            # Generate a new ID and update it in the DataFrame
            new_id = generate_new_id_with_prefix(existing_ids)
            trials_data.at[index, 'id'] = new_id
            # Update the set of existing IDs
            existing_ids.add(new_id)

    return trials_data


def preprocess_drugs(drugs: pd.DataFrame) -> pd.DataFrame:
    """Load and format the drugs into a DataFrame."""
    drugs['drug'] = drugs['drug'].apply(clean_string)
    return drugs
