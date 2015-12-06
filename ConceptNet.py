#!/usr/bin/env python

#Class to access and work with MIT's ConceptNet web API
#Author: fito_segrera / http://fii.to
#More info about ConceptNet: http://conceptnet5.media.mit.edu/

import json
import urllib2

class conceptNet:

	def __init__(self):
		self.url = "http://conceptnet5.media.mit.edu/data/5.4/"

	def lookup(self, lang, term, verbose):
		url_to_search = self.url + "c/" + lang + "/" + term
		data = urllib2.urlopen(url_to_search)
		json_data = json.load(data)
		if verbose:
			print url_to_search
			for i in json_data["edges"]:
				print "----------------"
				print i["end"]
				print "relation:", i["rel"]
				print i["surfaceEnd"]
				print i["surfaceStart"]
				print "weight:", i["weight"]

	def relation(self, rel, concept, verbose):
		url_to_search = self.url + "search?rel=/r/" + rel +"&end=/c/en/" + concept
		data = urllib2.urlopen(url_to_search)
		json_data = json.load(data)
		if verbose:
			print url_to_search
			for i in json_data["edges"]:
				print "----------------"
				print i["surfaceEnd"]
				print i["surfaceStart"]
				print "weight:", i["weight"]

	def termsAssociation(self, term1, term2, limit, lang, verbose):
		url_to_search = self.url + "assoc/list/en/" + term1 + "," + term2 +"@-1?limit=" + str(limit) + "&filter=/c/" + lang
		data = urllib2.urlopen(url_to_search)
		json_data = json.load(data)
		if verbose:
			print url_to_search
			for i in json_data["similar"]:
				print "----------------"
				for j in i:
					print j