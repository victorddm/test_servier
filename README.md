# Test Servier

## DAG Visualization
This project aims to analyze and visualize the relationships between drugs and the scientific journals that mention them. Utilizing data extracted from articles and clinical trials, the project constructs a Directed Acyclic Graph (DAG) to illustrate how various drugs are mentioned across different journals. The goal is to provide insights into the frequency and nature of drug mentions, thereby facilitating a better understanding of trends in medical research.

# Installation
To run this project locally, follow these steps:

Clone the project repository

`git clone https://github.com/victorddm/test_servier.git`

Install the required dependencies:

`pip install -r requirements.txt`

Run the main script:
`python src/run.py`

if the script is not working because the python path is not well defined, you can run the following command:
`export PYTHONPATH="${PYTHONPATH}:/path/to/your/project"`

You can find the json file describing the graph in the `output/describe_graph.json` folder.

Moreover, after executing the main script, the project will display a graphical visualization of the relationships between drugs and journals. Explore the graph to uncover trends and insights about drug mentions.

# Traitement ad-hoc


## SQL

Declare any dependencies in `requirements.txt` for `pip` installation.

To install them, run:
