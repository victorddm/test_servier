from src.utils import load_csv_data, load_json_data, convert_result_to_dict
from src.preprocess import preprocess_clinical_trials, preprocess_pubmed_articles, preprocess_drugs
from src.pipeline import analyze_drug_mentions
from src.graph import create_graph_dict, visualize_graph, visualize_graph_unique_journal
import json


def main():
    # Load data
    drugs = load_csv_data('data/drugs.csv')
    pubmed_article = load_csv_data('data/pubmed.csv')
    pubmed_article_extra = load_json_data('data/pubmed.json')
    clinical_trials = load_csv_data('data/clinical_trials.csv')

    # Process the data
    clinical_trials = preprocess_clinical_trials(clinical_trials)
    pubmed_data = preprocess_pubmed_articles(pubmed_article, pubmed_article_extra)
    drugs = preprocess_drugs(drugs)

    # Analyze the data
    drugs_mentions = analyze_drug_mentions(pubmed_data, clinical_trials, drugs)
    drugs_mentions = convert_result_to_dict(drugs_mentions)

    # Create graph
    graph = create_graph_dict(drugs_mentions)
    with open('output/describe_graph.json', 'w') as file:
        graph_file = json.dumps(graph, indent=4)
        file.write(graph_file)
    visualize_graph(graph)
    visualize_graph_unique_journal(graph)



if __name__ == "__main__":
    main()
