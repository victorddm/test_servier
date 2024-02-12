import networkx as nx
import matplotlib.pyplot as plt


def visualize_graph(graph_dict):
    """
    Visualizes the graph of connections between drugs, source types, and journals.

    Params:
        graph_dict: Dictionary representing the graph of connections between drugs, source types, and journals.
    """
    G = nx.DiGraph()  # Create a directed graph

    # Add nodes for drugs, source types, and journals
    for node_key, node_info in graph_dict.items():
        G.add_node(node_key)

        # Add edges for 'connects_to' relationships (Drug -> Source Type and Source Type -> Journal)
        if "connects_to" in node_info:
            for target_node in node_info["connects_to"]:
                G.add_edge(node_key,
                           target_node)

        # Add edges for 'cited_by' relationships (Journal -> Drug)
        if "cited_by" in node_info:
            for source_node in node_info["cited_by"]:
                G.add_edge(node_key,
                           source_node)

    # Draw the graph
    plt.figure(figsize=(20, 15))
    pos = nx.spring_layout(G, k=2,
                           iterations=80)  # Adjust layout parameters as needed for better visualization
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue',
            arrows=True, font_size=10, edge_color='gray')
    plt.title("Drug Mentions Graph")
    plt.show()


def visualize_graph_unique_journal(graph_dict):
    """
    Visualizes the graph of connections between drugs, source types, and journals, with unique journal nodes.

    Params:
        graph_dict: Dictionary representing the graph of connections between drugs, source types, and journals.
    """
    G = nx.DiGraph()

    edge_labels = {}  # Dictionary to hold edge labels (e.g., dates)

    # Add nodes and edges to the graph, including edge attributes for dates
    for node_key, node_info in graph_dict.items():
        G.add_node(node_key)

        # 'connects_to' relationships
        for target_node in node_info.get("connects_to", []):
            G.add_edge(node_key, target_node)

        # 'cited_by' relationships with date as edge attribute
        if "cited_by" in node_info:
            for source_node in node_info["cited_by"]:
                # Assume we have a way to determine the date of citation here
                # For demonstration, let's just use a placeholder date "2022-01-01"
                # In practice, you would extract this from your data structure
                date = "2022-01-01"
                G.add_edge(node_key, source_node, date=date)
                # Add the date as an edge label
                edge_labels[(node_key, source_node)] = date

    # Draw the graph
    plt.figure(figsize=(20, 15))
    pos = nx.spring_layout(G, k=2,
                           iterations=80)  # Adjust layout parameters as needed for better visualization
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue',
            arrows=True, font_size=10, edge_color='gray')

    # Draw edge labels (dates)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
                                 font_color='red')

    plt.title("Drug Mentions Graph with Dates on Arrows")
    plt.show()
