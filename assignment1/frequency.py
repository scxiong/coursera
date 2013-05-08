import sys
import json

def term_frequency(words_list):
    d = {}
    count = len(words_list)
    for x in words_list:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    for x in d.keys():
        d[x] = d[x]/float(count)
    return d

def main():
    tweet_file = open(sys.argv[1])
    words_list = [] 
    
    for line in tweet_file:
        t = json.loads(line)
        if t.get('text'):# and t.get('lang') and t['lang'] == 'en':
            words_list += t['text'].split()
    freq = term_frequency(words_list)

    for key in freq.keys():
    	print key, freq[key]

if __name__ == '__main__':
    main()
