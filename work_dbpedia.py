from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper(endpoint='http://ja.dbpedia.org/sparql', returnFormat='json')
sparql.setQuery("""                                                                                                                                                                      
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    PREFIX owl:  <http://dbpedia.org/ontology/>                                                                                                                           
    PREFIX rs: <http://ja.dbpedia.org/resource/>
    PREFIX prop: <http://ja.dbpedia.org/property/>

    SELECT DISTINCT ?p ?o WHERE {                                                                                                                                                                 
      rs:東京 ?p ?o .
       } LIMIT 100
""")
results = sparql.query().convert()

print('-------------  result of DBpedia')
for i, r in enumerate(results["results"]["bindings"]):
    print(r)
