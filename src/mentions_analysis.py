import pandas as pd


def analyze_drug_mentions(articles_df: pd.DataFrame,
                          trials_df: pd.DataFrame,
                          drugs_df: pd.DataFrame) -> dict:
    """
    Analyzes drug mentions across articles and trials DataFrames for each drug.

    Params:
        articles_df: DataFrame containing articles data.
        trials_df: DataFrame containing trials data.
        drugs_df: DataFrame containing drugs data.
    Returns:
        all_mentions : A dictionary with drug mentions dataframes.
    """
    all_mentions = {}
    for drug_name in drugs_df['drug']:
        drug_mention = get_mentions_from_drug(articles_df, trials_df, drug_name)
        if drug_mention:
            all_mentions[drug_name] = drug_mention

    # Concatenate all mentions dataframes for each drug into a single dataframe
    for drug, mentions_list in all_mentions.items():
        all_mentions[drug] = pd.concat(mentions_list, ignore_index=True)

    return all_mentions


def get_mentions_from_drug(articles_df: pd.DataFrame, trials_df: pd.DataFrame, drug_name: str) -> list:
    """
    Searches for mentions of a drug within articles and trials DataFrames.

    Params:
        articles_df: DataFrame containing articles data.
        trials_df: DataFrame containing trials data.
        drug_name: The drug name to search for.
    Returns:
        drug_mentions : A DataFrame with mentions of the drug.
    """
    drug_mentions = []
    drug_mentions_articles = find_mentions(articles_df,
                                           'articles',
                                           drug_name)
    drug_mentions_trials = find_mentions(trials_df, 'trials',
                                         drug_name, "scientific_title")

    if not drug_mentions_articles.empty:
        drug_mentions.append(drug_mentions_articles)
    if not drug_mentions_trials.empty:
        drug_mentions.append(drug_mentions_trials)

    return drug_mentions


def find_mentions(data, source_name: str, drug_name,
                  title_column="title") -> pd.DataFrame:
    """
    Searches for mentions of a drug within a DataFrame and annotates them with the source.

    Params:
        data: DataFrame to search within.
        df_source: String indicating the source of the DataFrame ('articles' or 'trials').
        drug_name: The drug name to search for.
        title_column: The name of the column containing publication titles.
    Returns:
        drug_mentions : A DataFrame with mentions of the drug.
    """
    columns_to_select = [title_column, 'date', 'journal']
    drug_mentions = \
        data[data[title_column].str.contains(drug_name, case=False, na=False)][columns_to_select]
    drug_mentions["source"] = source_name
    drug_mentions["drug"] = drug_name

    return drug_mentions

