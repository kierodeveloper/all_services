# Import Elasticsearch package
import sys
#reload(sys)

#sys.setdefaultencoding("utf8") 
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
 "doc":{
   "Titulo": "Control de Xbox One, edición especial de medianoche obliga al mando inalámbrico."
 }
}

#doc.encode("utf8")

res = _es.update(index='publies_products_v2', body=doc, id='964893')
print(res)

