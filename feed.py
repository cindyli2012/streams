from datetime import datetime

from elasticsearch import Elasticsearch
import json
import urllib2
es = Elasticsearch()

#es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})
#es.get(index="my-index", doc_type="test-type", id=42)['_source']
"""
url="http://api.ean.com/expe/deals/flights.json?apiKey=yc7cx556qdt9m3yw73ebdksk"
flights=json.load(urllib2.urlopen(url))


url="http://api.wunderground.com/api/3c3fe3397f363646/conditions/q/CA/San_Francisco.json"
weather=json.load(urllib2.urlopen(url))
"""
skicity={"Denver":"DEN","Reno":"RNO","Portland":"PDX", "Seattle":"SEA","Hartford":"BDL","Minneapolis":"MSP","Bozeman":"BZN","Buffalo":"BUF","Chicago":"ORD"}
surfcity={"Atlantic City":"ACY","Orlando":"MCO","New York":"JFK","Los Angeles":"LAX","Richmond":"RIC","Santa Ana":"SNA","Kahului":"OGG","San Diego":"SAN","Honolulu":"HNL"}
beachcity={"Boston":"BOS","Hilo":"KOA","Orlando":"MCO", "San Diego":"SAN", "Atlantic City":"ACY", "New York":"JFK", "Richmond":"RIC"}
state={"Denver":"CO","Reno":"NV","Portland":"OR", "Seattle":"WA","Atlantic City":"NJ","Orlando":"FL","New York":"NY","Los Angeles":"CA","Richmond":"VA","Santa Ana":"CA","Kahului":"HI","San Diego":"CA","Honolulu":"HI","Boston":"MA","Hilo":"HI","Hartford":"CT","Minneapolis":"MN","Bozeman":"MT","Buffalo":"NY","Chicago":"IL"}

#json.dumps(['ski',])

for city in skicity.keys():
	url="http://api.wunderground.com/api/3c3fe3397f363646/conditions/q/"+str(state[city])+"/"+str(city).replace(" ","_")+".json"
	weather=json.load(urllib2.urlopen(url))
	wea= weather[u'current_observation'][u'weather']
	temp= weather[u'current_observation'][u'temp_f']
	vis=weather[u'current_observation'][u'visibility_mi']
	wind=weather[u'current_observation'][u'wind_mph']
	weaurl= weather[u'current_observation'][u'icon_url']
	url="http://api.ean.com/expe/deals/packages.json?tripFrom=SFO&tripTo="+str(skicity[city])+"&apiKey=wvte3wrgkz7bdudywxknwjyw&userId=launch"
	package=json.load(urllib2.urlopen(url))
	pkg_price=package[0][u'totalPackagePrice']
	pkg_link=package[0][u'packageDeepLink']
	res = es.index(index="streams", doc_type="skiing", id=city, body={"weather":str(wea), "temperature": str(temp), "visibility":str(vis), "wind":str(wind), "weatherurl":str(weaurl), "package_price":str(pkg_price),"package_link":str(pkg_link) })
	print(res)
	print wea 
	print str(wea)



"""
#print data[0][u'tripFrom']
for i in range(len(data)):
	res = es.index(index="streams", doc_type="flights", id=i, body=flights[i])
	es.delete(index="streams", doc_type="flights", id=i)
#print(res['ok'])
#res = es.get(index="streams", doc_type="flights", id=41)
#print(res['_source'])
# es.delete(index="streams", doc_type="flights", id=41)
res = es.index(index="streams", doc_type="weather", id=41, body=data[u'current_observation'])
res = es.get(index="streams", doc_type="weather", id=41)
#print(res['_source'])
es.delete(index="streams", doc_type="weather", id=41)
#data=json.load(urllib2.urlopen("url"))



#url="localhost:9200"

#request = urllib2.Request(url, data)

#response = urllib2.urlopen(request)
 
#html = response.read()

"""
