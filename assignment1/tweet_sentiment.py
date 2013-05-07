import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_file = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary

    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    for line in tweet_file:
        t = json.loads(line)
        if t.get('text'):
                sentiment = 0
                for word in t['text'].split():
                    sentiment += scores.get(word, 0)
                print t['text']
                print sentiment

if __name__ == '__main__':
    main()
