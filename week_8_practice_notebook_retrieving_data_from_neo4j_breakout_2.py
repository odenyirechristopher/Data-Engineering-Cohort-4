# -*- coding: utf-8 -*-
"""Week 8 Practice Notebook: Retrieving Data from Neo4j - Breakout 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W2fkLdaw5Gh8_M6nSWjBycUIeHGyf_BF

# Practice Notebook: Retrieving Data from Neo4j

## Pre-requisites
"""

# importing neo4j drive
!pip install neo4j

"""### Populate data for Examples"""

# Populate the database with some data
from neo4j import GraphDatabase

# Set the connection details:
bolt_url = "neo4j+s://3dafe14c.databases.neo4j.io"
user = "neo4j"
password = "KTLtlHilZVS6XQZ_-dXk7INW8Dj9zDfdTV9SleRkz0o"

# Connect to the database:
driver = GraphDatabase.driver(bolt_url, auth=(user, password))

# Populate the database with some data
with driver.session() as session:
    session.run("CREATE (p:Person {name: 'Alice', age: 30})")
    session.run("CREATE (p:Person {name: 'Bob', age: 35})")
    session.run("CREATE (p:Person {name: 'Charlie', age: 40})")
    session.run("CREATE (p:Person {name: 'Dave', age: 45})")
    session.run("MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'}) CREATE (a)-[:FRIEND]->(b)")
    session.run("MATCH (a:Person {name: 'Bob'}), (b:Person {name: 'Charlie'}) CREATE (a)-[:FRIEND]->(b)")
    session.run("MATCH (a:Person {name: 'Charlie'}), (b:Person {name: 'Dave'}) CREATE (a)-[:FRIEND]->(b)")

"""### Populate data for Challenges"""

# Define a Cypher query to create sample data
cypher_query = """
CREATE (m1:Movie {title: 'The Matrix', released: 1999, duration: 136, rating: 8.7})
CREATE (m2:Movie {title: 'Inception', released: 2010, duration: 148, rating: 8.8})
CREATE (m3:Movie {title: 'The Dark Knight', released: 2008, duration: 152, rating: 9.0})
CREATE (p1:Person {name: 'Christopher Nolan'})
CREATE (p2:Person {name: 'Keanu Reeves'})
CREATE (p3:Person {name: 'Lana Wachowski'})
CREATE (p4:Person {name: 'Lilly Wachowski'})
CREATE (p1)-[:DIRECTED]->(m2)
CREATE (p1)-[:DIRECTED]->(m3)
CREATE (p2)-[:ACTED_IN]->(m1)
CREATE (p2)-[:ACTED_IN]->(m2)
CREATE (p3)-[:DIRECTED]->(m1)
CREATE (p4)-[:DIRECTED]->(m1)
CREATE (p1)-[:FRIEND]->(p2)
CREATE (p2)-[:FRIEND]->(p3)
CREATE (p3)-[:FRIEND]->(p4)
"""

# Execute the query to create sample data
with driver.session() as session:
    session.run(cypher_query)

"""## Examples and Challenges

### 1. Filtering data with Cypher queries

This code defines a Cypher query that filters the data to only include Person nodes with an age greater than 35. The query returns the name and age of these nodes. The query is executed using the session.run() method, and the results are printed to the console using a for loop.

You can modify the Cypher query to filter the data in different ways, depending on your needs. For example, you could filter the data to only include nodes with a specific name, or to only include nodes that are connected to other nodes in a certain way.
"""

# Define Cypher query to filter data
cypher_query = "MATCH (p:Person) WHERE p.age > 35 RETURN p.name, p.age"

# Execute the query and print the results
with driver.session() as session:
    result = session.run(cypher_query)
    for record in result:
        print(f"{record['p.name']} is {record['p.age']} years old.")

"""### 2. Limiting and skipping results with the LIMIT

This following code snippet executes a Cypher query using the session.run() method. The query selects all nodes with the Person label, returns their name and age properties, orders the results by age, and limits the results to the first 2 records. The results are then printed to the console using a for loop.
"""

with driver.session() as session:
  result = session.run("MATCH (p:Person) RETURN p.name, p.age ORDER BY p.age LIMIT 2")
  for record in result:
    print(record)

"""Write a program that connects to a Neo4j database and executes a Cypher query to retrieve the names of all Movie nodes that have a released property value greater than or equal to 2000 and are tagged with the genre Action. The program should print each movie name to the console.

#### Challenge

Write a program that connects to a Neo4j database, and executes a Cypher query to retrieve the names of all Movie nodes that have a released property value greater than or equal to 2000. The program should print each movie name to the console.
"""

# Your code goes here
with driver.session() as session:
  result = session.run("MATCH (m:Movie) WHERE m.released >= 2000 RETURN m.title ORDER BY m.released")
  for record in result:
    print(record['m.title'])

"""#### Solution"""

# Define Cypher query to filter data
cypher_query = "MATCH (m:Movie) WHERE m.released >= 2000 RETURN m.title"

# Execute the query and print the results
with driver.session() as session:
    result = session.run(cypher_query)
    for record in result:
        print(record['m.title'])

"""### 3. Sorting results with the ORDER BY keyword

The following code executes a Cypher query using the session.run() method. The query selects all nodes with the Person label that are connected to other Person nodes by a FRIEND relationship. The query returns the names of the connected Person nodes and orders the results by the name property of the first node in descending order. The results are then printed to the console using a for loop.
"""

with driver.session() as session:
  result = session.run("MATCH (p:Person)-[:FRIEND]->(q:Person) RETURN p.name, q.name ORDER BY p.name DESC")
  for record in result:
    print(record)

"""#### Challenge

Write a program that connects to a Neo4j database and executes a Cypher query to retrieve the titles of all Movie nodes that are connected to a Person node with a DIRECTED relationship. The program should print each movie title to the console.
"""

# Your code goes here
with driver.session() as session:
  result = session.run("MATCH (p:Person)-[:DIRECTED]->(m:Movie) RETURN m.title")
  for record in result:
    print(record['m.title'])

"""#### Sample solution"""

# Define Cypher query to filter data
cypher_query = "MATCH (p:Person)-[:DIRECTED]->(m:Movie) RETURN m.title"

# Execute the query and print the results
with driver.session() as session:
    result = session.run(cypher_query)
    for record in result:
        print(record['m.title'])

"""### 4. Aggregating data with functions like COUNT(), SUM(), and AVG()

The following code uses the session.run() method to execute a Cypher query that aggregates data about all Person nodes in the graph. The COUNT(), SUM(), and AVG() functions are used to count the number of nodes, calculate the sum of the age property values, and calculate the average of the age property values, respectively. The AS keyword is used to assign aliases to the aggregated values, which can then be accessed using the aliases in the for loop.
"""

with driver.session() as session:
  result = session.run("MATCH (p:Person) RETURN COUNT(p) AS num_people, SUM(p.age) AS total_age, AVG(p.age) AS avg_age")
  for record in result:
    print(record)

"""#### Challenge

Write a program that connects to a Neo4j database, and executes a Cypher query to retrieve the count of all Movie nodes, the sum of their duration properties, and the average of their rating properties. The program should print the results to the console.
"""

# Your code goes here
with driver.session() as session:
  result = session.run("MATCH (m:Movie) RETURN SUM(m.duration) AS total_duration, AVG(m.rating) AS average_rating, COUNT(m) as no_of_movies ")
  for record in result:
    print(record)

"""#### Sample solution"""

# Define Cypher query to aggregate data
cypher_query = "MATCH (m:Movie) RETURN COUNT(m) AS num_movies, SUM(m.duration) AS total_duration, AVG(m.rating) AS avg_rating"

# Execute the query and print the results
with driver.session() as session:
    result = session.run(cypher_query)
    for record in result:
        print(f"Number of movies: {record['num_movies']}")
        print(f"Total duration: {record['total_duration']} minutes")
        print(f"Average rating: {record['avg_rating']:.2f} stars")

"""### 5. Using pattern matching to retrieve specific nodes and relationships

The following selects all nodes with the Person label that are connected by a FRIEND relationship, and filters the results to only include nodes with a name property equal to "Alice". The query returns the name properties of both nodes. The for loop iterates over the result records and prints each record to the console.
"""

with driver.session() as session:
  result = session.run("MATCH (p:Person)-[:FRIEND]->(q:Person) WHERE p.name = 'Alice' RETURN p.name, q.name")
  for record in result:
    print(record)

"""#### Challenge

Write a program that connects to a Neo4j database, and executes a Cypher query to retrieve the names of all Person nodes that are connected to a FRIEND relationship with another Person node, and whose name starts with the letter "B". The program should print each person's name to the console.
"""

# Your code goes here
with driver.session() as session:
  result = session.run("MATCH (p:Person)-[:FRIEND]->(q:Person) WHERE q.name STARTS WITH 'B' RETURN p.name, q.name")
  for record in result:
    print(record)

"""#### Sample Solution"""

# Define Cypher query to filter data
cypher_query = "MATCH (p1:Person)-[:FRIEND]->(p2:Person) WHERE p1.name =~ 'B.*' RETURN p1.name"

# Execute the query and print the results
with driver.session() as session:
    result = session.run(cypher_query)
    for record in result:
        print(record['p1.name'])

"""### 6. Close the database connection

"""

driver.close()