import sys
import json

def term_count(words_list):
    d = {}
    for x in words_list:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    return d

def main():
    tweet_file = open(sys.argv[1])
    words_list = [] 
    
    for line in tweet_file:
        t = json.loads(line)
        if t.get("entities") and t["entities"]["hashtags"] != []:# and t.get('lang') and t['lang'] == 'en':
            for tag in t["entities"]["hashtags"]:
                words_list += [tag['text']]

    hashtags = term_count(words_list)
    
    i = 0
    for hashtag in sorted(hashtags, key = hashtags.get, reverse = True):
        if i < 10:
            print hashtag, + float(hashtags[hashtag])
            i += 1

if __name__ == '__main__':
    main()
