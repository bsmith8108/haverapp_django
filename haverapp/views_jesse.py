from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render

import urllib2
import datetime
from xml.etree import ElementTree

'''
def jesse(request):
	var = "I'm Commander Shepard, and this is my favorite webpage on the internet!"
	return render(request, "cool_test_page.html", {"my_variable":var})
'''
def jesse(request):
	raw_response = urllib2.urlopen("http://www.haverford.edu/goevents/").read()
	xml_response = ElementTree.fromstring(raw_response)
	product = ""
	for i in xml_response:
		product += u"<div>{1}</div> <div>{0}</div> <br>".format(i[0].text, i[1].text)
	return HttpResponse(product)
