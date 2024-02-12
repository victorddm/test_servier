import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph_dict):
    """
    Visualizes the graph of connections between drugs, source types, and journals

    Params:
        graph_dict: Dictionary representing the graph of connections between drugs, source types, and journals.
    """
    G = nx.DiGraph()

    edge_labels = {}  # Dictionary to hold edge labels (e.g., dates)

    # Add nodes and edges to the graph, including edge attributes for dates
    for node_key, node_info in graph_dict.items():
        G.add_node(node_key)


        # Handle 'connects_to' relationships for drugs and source types
        if "connects_to" in node_info:
            for connected_node in node_info["connects_to"]:
                G.add_edge(node_key, connected_node)

        # Handle 'cited_by' relationships for journals to drugs
        if "cited_by" in node_info:
            for citing_drug in node_info["cited_by"]:
                G.add_edge(node_key, citing_drug)

        # Handle mentions within drugs pointing to journals with dates
        if "mentions" in node_info:
            for mention in node_info["mentions"]:
                journal_node_key = "Journal: " + mention['journal']
                # Ensure the journal node exists
                if journal_node_key not in G:
                    G.add_node(journal_node_key)
                # Add edge from source type or drug to journal with date
                G.add_edge(node_key, journal_node_key, date=mention['date'])
                edge_labels[(node_key, journal_node_key)] = mention['date']

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
