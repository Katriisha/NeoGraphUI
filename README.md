# NeoGraphUI


## Mac install
```
brew install neo4j # cypher-shell is installed
brew services start neo4j # local server start
brew services stop neo4j # local server stop
```
password reset for developers to neo4jneo4j:
```
brew services neo4j stop
/opt/homebrew/opt/neo4j/bin/neo4j-admin dbms set-initial-password neo4jneo4j
brew services neo4j start
```
connect via cypher shell:
```
$ cypher-shell -u neo4j -p neo4jneo4j
Connected to Neo4j using Bolt protocol version 5.8 at neo4j://localhost:7687 as user neo4j.
Type :help for a list of available commands or :exit to exit the shell.
Note that Cypher queries must end with a semicolon.
neo4j@neo4j>
```
ALSO IT IS POSSIBLE TO USE BROWSER: goto http://localhost:7474

## Populate test data

```
$ python test-rdflib-neo4j.py
Uniqueness constraint on :Resource(uri) found.

The store is now: Open
The store is now: Closed
IMPORTED 11018 TRIPLES
$ cypher-shell -u neo4j -p neo4jneo4j
Connected to Neo4j using Bolt protocol version 5.8 at neo4j://localhost:7687 as user neo4j.
Type :help for a list of available commands or :exit to exit the shell.
Note that Cypher queries must end with a semicolon.
neo4j@neo4j> match (n) return count(n);
+----------+
| count(n) |
+----------+
| 2570     |
+----------+

1 row
ready to start consuming query after 25 ms, results consumed after another 0 ms
neo4j@neo4j>
```

To reset database use shell command:
```
$ echo 'match (n) detach delete n; ' | cypher-shell -u neo4j -p neo4jneo4j
```
NOTE THAT constraints are not removed this way. To remove constains use SHOW CONSTRAINS/DROP CONSTRAIN db commands.
