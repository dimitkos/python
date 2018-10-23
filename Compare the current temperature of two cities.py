import urllib2
import json

def temp_city(city):
    

    try:
                data = urllib2.urlopen('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22'+city+'%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')
                weather = json.loads(data.read(10000))
                temp = weather['query']['results']['channel']['item']['condition']['temp']
                town = weather['query']['results']['channel']['location']['city']
                return temp

    except:
                print " Try Again"
                        
    
city1 = raw_input('Give the first city: ')


city2 = raw_input('Give the second city: ')


if (temp_city(city1)>temp_city(city2)):
    print " %s has higher temperature than %s"%(city1,city2)
elif (temp_city(city1)<temp_city(city2)):
    print " %s has higher temperature than %s"%(city2,city1)
else:
    print "These cities has the same Temperature"
    
