# This module contains functions for creating a graph of connections between drugs, source types (articles or trials),

def create_graph_dict(drug_mentions_dict: dict) -> dict:
    """
    Creates a dictionary representing the graph of connections between drugs, source types (articles or trials),
    and journals, including details for each link.

    Params:
        drug_mentions_dict: Dictionary with drug names as keys and lists of mentions as values.
    Returns:
        A dictionary formatted for graph construction, including details for each drug-journal link and the intermediate source type.
    """
    graph_dict = {}

    for drug, mentions in drug_mentions_dict.items():
        drug_node_key = f"Drug: {drug}"

        # Ensure the drug node is initialized
        if drug_node_key not in graph_dict:
            graph_dict[drug_node_key] = {"mentions": [], "connects_to": []}

        for mention in mentions:
            title, source_type, date, _, journal = mention  # Unpack the mention details

            # Define node keys
            source_type_node_key = f"Source Type: {source_type}"
            journal_node_key = f"Journal: {journal}"

            # Append mention details to the drug node
            mention_detail = {
                "title": title,
                "date": date,
                "journal": journal,
                "source_type": source_type
            }
            graph_dict[drug_node_key]["mentions"].append(mention_detail)

            # If the source type node doesn't exist, initialize it
            if source_type_node_key not in graph_dict:
                graph_dict[source_type_node_key] = {"connects_to": []}

            # If the journal node doesn't exist, initialize it
            if journal_node_key not in graph_dict:
                graph_dict[journal_node_key] = {"cited_by": []}

            # Establish connections: Drug -> Source Type -> Journal
            if source_type_node_key not in graph_dict[drug_node_key][
                "connects_to"]:
                graph_dict[drug_node_key]["connects_to"].append(
                    source_type_node_key)

            if journal_node_key not in graph_dict[source_type_node_key][
                "connects_to"]:
                graph_dict[source_type_node_key]["connects_to"].append(
                    journal_node_key)

            # And finally, establish the connection back from Journal -> Drug
            if drug_node_key not in graph_dict[journal_node_key]["cited_by"]:
                graph_dict[journal_node_key]["cited_by"].append(drug_node_key)

    return graph_dict



