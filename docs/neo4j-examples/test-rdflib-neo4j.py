# from https://neo4j.com/blog/developer/rdflib-neo4j-rdf-integration-neo4j/

# venv setup
# $ python3 -m venv ~/venv/rdflib-neo4j
# $ source ~/venv/rdflib-neo4j/bin/activate
# $ pip install rdflib-neo4j


from rdflib_neo4j import Neo4jStoreConfig, Neo4jStore, HANDLE_VOCAB_URI_STRATEGY
from rdflib import Graph

auth_data = {'uri': "bolt://localhost", 'database':"neo4j", 'user':"neo4j", 'pwd':"neo4jneo4j"}
config = Neo4jStoreConfig(auth_data=auth_data,
                          #custom_prefixes=prefixes,
                          handle_vocab_uri_strategy=HANDLE_VOCAB_URI_STRATEGY.IGNORE,
                          batching=True)

file_path = 'https://github.com/jbarrasa/gc-2022/raw/main/search/onto/concept-scheme-skos.ttl'

neo4j_aura = Graph(store=Neo4jStore(config=config))

# Calling the parse method will implicitly open the store
neo4j_aura.parse(file_path, format="ttl")

neo4j_aura.close(True)
