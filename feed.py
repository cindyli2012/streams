from datetime import datetime

from elasticsearch import Elasticsearch
import json
import urllib2
es = Elasticsearch()

#es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})

#es.get(index="my-index", doc_type="test-type", id=42)['_source']

url="http://api.ean.com/expe/deals/flights.json?apiKey=yc7cx556qdt9m3yw73ebdksk"

data=json.load(urllib2.urlopen(url))

print data[0][u'tripFrom']
for i in range(len(data)):
	res = es.index(index="streams", doc_type="flights", id=i, body=data[i])

#print(res['ok'])
res = es.get(index="streams", doc_type="flights", id=41)
print(res['_source'])
es.delete(index="streams", doc_type="flights", id=41)


url="http://api.wunderground.com/api/3c3fe3397f363646/conditions/q/NY/New_York.json"
data=json.load(urllib2.urlopen(url))


res = es.index(index="streams", doc_type="weather", id=41, body=data[u'current_observation'])
res = es.get(index="streams", doc_type="weather", id=41)
print(res['_source'])

#es.delete(index="streams", doc_type="weather", id=41)
#data=json.load(urllib2.urlopen("url"))

#url="localhost:9200"

#request = urllib2.Request(url, data)

#response = urllib2.urlopen(request)
 
#html = response.read()


