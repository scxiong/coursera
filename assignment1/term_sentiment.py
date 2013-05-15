import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary

    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    terms = {}
    for line in tweet_file:
        t = json.loads(line)
        if t.get('text'):# and t.get('lang') and t['lang'] == 'en':
            sentiment = 0.0
            words = t['text'].split()
            nr_words = len(words)
            for word in words:
            	if scores.has_key(word):
            		sentiment += scores.get(word, 0)
            		nr_words -= 1
            if not(nr_words == 0):
                tentative = sentiment/nr_words

                for word in words:
                	if not(scores.has_key(word)):
                		if terms.has_key(word):
                			value = terms[word][0]
                			count = terms[word][1]
                			terms[word] = [(value * count + tentative) / (count + 1), (count + 1)]
                		else:
                			terms[word] = [tentative, 1]   

    for term in terms.keys():
    	print term.encode('utf-8'), terms[term][0]

if __name__ == '__main__':
    main()
