
import urllib2
import json


def hawaii_vs_maldives():

	#hawaii

	data = urllib2.urlopen('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22honolulu%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys') 

	hawaii = json.loads(data.read(10000))

	#male

	data = urllib2.urlopen('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22male%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')

	
	male = json.loads(data.read(10000))

	temp1 = hawaii['query']['results']['channel']['item']['condition']['temp']
	temp2 = male['query']['results']['channel']['item']['condition']['temp']

	if temp1 > temp2:
		print 'Go Honolulu!!!'
	else:
		print 'Male!!!!!! <3 <3 <3'


hawaii_vs_maldives()
