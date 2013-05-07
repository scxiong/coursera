import json
import sys

afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.

tweet_file = open("output.txt")
for line in tweet_file:
	t = json.loads(line)
	if t.get('text') and t.get('lang') and t['lang'] == 'en':
			sentiment = 0
			for word in t['text'].split():
				sentiment += scores.get(word, 0)
			print t['text']
			print 'sentiment: ', sentiment

# string = "abduction abductions"
# sentiment = 0
# for word in string.split():
# 	sentiment += scores.get(word, 0)
# print string
# print 'sentiment: ', sentiment

# print scores.get("abduction", 0)

