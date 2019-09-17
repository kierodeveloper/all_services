# Import Elasticsearch package 
from elasticsearch import Elasticsearch 
# Connect to the elastic cluster

def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Conectado')
        return(_es)
    else:
        return('Awww it could not connect!')
    return _es

_es = connect_elasticsearch()

doc = {
  "query":{
     "match" : {
        "Producto_Id":"1904268"
     }
  }
}
res = _es.search(index='publies_products_v2', body=doc)
print(res)


