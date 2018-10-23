import urllib2
import json


def temp_city(city):
    

    try:
                data = urllib2.urlopen('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22'+city+'%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')
                weather = json.loads(data.read(10000))
                temp = weather['query']['results']['channel']['item']['condition']['temp']
                town = weather['query']['results']['channel']['location']['city']
                print 'Temp in fahrenheit at %s is %s'%(town,temp)
    except:
                print " Try Again"
                        
    




city = raw_input('Give city: ')
temp_city(city)
