# Plans
## data types and and data objects vizualization

Data types/object visualization suppose to be build on top of graph DB backends. Both RDF/SPARQL and Neo4j/cypher should be supported.
Data types are to be described in the way compatible with SHACL to facilitate available SHACL verification tools use.
Also programming lang bindings should be defined to allow direct manipulation of database from certain host language system.

## logic rules vizualization

Logic rules defined using OWL and/or Prolog should be possible to visualize along with relevant data types/objects and reasoning pathes.

# Details

Main goal is to build tool for graph database users keeping in mind neuro-symbolic tasks. Such tasks require handling of 
both data types/objects, logic rules defined using that data types, reasoning/interpretation details.

To define data types in graph database we are to use SHACL-based approach. To continue with logic rules we may need to adapt OWL 
and possibly Prolog. Neuro-symbolic users would require additional features to visualize particular methodology parameters. 
E.g soft probabilistic logic would have certain probabilties/ranges associated with logic rules.

See this video for some additional details: https://www.youtube.com/watch?v=q3s72VhaQR0 - 'Neuro-Symbolic AI with AllegroGraph'

