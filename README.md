# Test Servier


## Table of Contents
I. [DAG Visualization](#I.-DAG-Visualization)

   a. [Installation](#Installation)
   
   b. [To go further](#To-go-further)
   
   c. [Practical Steps for Implementation](#Practical-Steps-for-Implementation)
   
   d. [Company revenue by day](#Company-revenue-by-day)
   
   e. [Sales by customer and product type](#Sales-by-customer-and-product-type)

II. [SQL](#II.-SQL)
    
   a. [Company revenue by day](#Company-revenue-by-day)
   
   b. [Sales by customer and product type](#Sales-by-customer-and-product-type)

## I. DAG Visualization
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

## To go further

To scale our code to handle large volumes of data, such as files spanning multiple terabytes or millions of files, several critical considerations and potential modifications come into play:

### a. Considerations for Scaling

- Processing Time: Currently running on a standard machine configuration, our code isn't equipped to handle files of several terabytes or process millions of files efficiently due to limited RAM, CPU, and GPU capabilities. Loading such large files into Python's memory on a conventional machine is impractical, and processing times would become prohibitively long.

- Storage: Our current setup involves storing data in text files (CSV and JSON), both before and after processing. While text files are human-readable, their ability to handle large data volumes is limited, potentially making storage and data exchange more expensive and less efficient.

- Data Ingestion: The method of data ingestion, whether streaming (real-time) or batch processing, needs to be considered for handling large data volumes effectively.

### b. Required Modifications

- Enhanced Computational Capacity: Upgrading our hardware infrastructure, either through vertical scaling (adding more RAM, upgrading the CPU) or horizontal scaling (adding more machines to form a cluster), is necessary. Horizontal scaling, in particular, allows for distributing storage and computations across multiple machines using dedicated frameworks.

- Distributed Computing Framework: Implementing a distributed computing framework like Apache Spark, which can process large volumes of data by distributing computations across a cluster, is essential. Spark's ability to handle varied data types, including streaming data, unstructured data, and SQL queries, makes it an ideal tool for adapting to increased data volume and variety.

- Efficient Storage Solution: Moving away from flat files to a column-oriented data storage format can significantly improve query performance and compression. Apache Parquet, for example, is a columnar storage file format that offers substantial benefits over traditional text files, especially when used with distributed computing frameworks like Spark.

- Distributed Database: Considering a distributed database for data storage could enhance scalability and performance. Distributed databases are scalable and can distribute queries across servers, potentially placing data closer to frequent users to minimize access times.

### c. Practical Steps for Implementation

- Scaling Infrastructure: We might start by deploying our code on cloud servers or clusters to leverage scalable resources. This could involve using cloud services like GCP, AWS, or Azure to access scalable computing and storage solutions.

- Adopting Spark or Flink: Replacing pandas with Spark or Flink for data processing tasks would allow us to handle larger datasets more efficiently. Spark, in particular, offers APIs for multiple languages, including Python (PySpark), facilitating the migration from pandas.

- Optimizing Data Storage: For input data, utilizing a data lake on a server could be a simple yet effective solution. However, for output data, leveraging a NoSQL database like MongoDB might be more appropriate to accommodate the JSON format of our output data efficiently.


In summary, to accommodate large volumes of data, we need to consider upgrading our computational resources, utilizing distributed computing frameworks for efficient data processing, and adopting scalable and efficient storage solutions. These steps would ensure our project can handle significantly larger datasets while maintaining or even improving performance.


## II. SQL

## Company revenue by day

For calculating daily revenue for the period from January 1, 2019, to December 31, 2019, you can use the following SQL query. This query aggregates sales by day, calculating the total sales amount by multiplying the unit price by the quantity sold for each transaction within the specified period:

```sql
SELECT 
  T.date AS "Sale Date",
  SUM(T.prod_price * T.prod_qty) AS "Total Revenue"
FROM 
  TRANSACTIONS T
WHERE 
  T.date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY 
  T.date
ORDER BY 
  T.date;

```

In this query:

"Sale Date" is the alias for the transaction date.
"Total Revenue" is the calculated total sales revenue for each day.

## Sales by customer and product type:

For determining sales by customer and product type:
```sql
SELECT 
  T.client_id AS "Customer ID",
  SUM(CASE WHEN PN.product_type = 'MEUBLE' THEN T.prod_price * T.prod_qty ELSE 0 END) AS "Total Furniture Sales",
  SUM(CASE WHEN PN.product_type = 'DECO' THEN T.prod_price * T.prod_qty ELSE 0 END) AS "Total Decor Sales"
FROM 
  TRANSACTIONS T
JOIN 
  PRODUCT_NOMENCLATURE PN ON T.prod_id = PN.product_id
WHERE 
  T.date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY 
  T.client_id
ORDER BY 
  T.client_id;

```

In this query:

"Customer ID" is the alias for the customer's unique identifier.
"Product Type" specifies whether the product is furniture or decor.
"Total Sales" is the total sales amount for each combination of customer and product type.