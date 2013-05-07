import urllib
import json
import sys

def print_tweets(keyword, nr_pages):
	for i in range(1, nr_pages + 1):
		response = urllib.urlopen("http://search.twitter.com/search.json?q=" + keyword + "&page=" + str(nr_pages) )
		# print json.load(response)['text']
		results = json.load(response)['results']
		for x in results:
			print x['text']
			print ''
		# print json.dumps(json.load(response), sort_keys=True, indent=4, separators=(',', ': '))

print_tweets(sys.argv[1], 1)