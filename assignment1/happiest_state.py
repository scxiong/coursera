import sys
import json

states_dict = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
inv_states_dict = {v:k for k, v in states_dict.items()}

def main():
    global states_dict, inv_states_dict
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary

    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    states = {}
    for line in tweet_file:
        t = json.loads(line)
        find_state = True
        if t.get('text') and t.get('place') and t['place'].get('country'):
            if t['place']['country'] == "United States" and t['place'].get("full_name"):
                place = t['place']["full_name"]
                area = place.split(',')[-1].strip()
                if area == 'US':
                    area = place.split(',')[-2].strip()
                    # print place + "=>" + area + ", and will be furtuer converted"

                if states_dict.has_key(area):
                    state = area
                elif inv_states_dict.has_key(area):
                    state = inv_states_dict[area]
                    # print place + "=>" + state
                else:
                    find_state = False

                if find_state:
                    sentiment = 0.0
                    for word in t['text'].split():
                        sentiment += scores.get(word, 0)
                    if states.has_key(state):
                        value = states[state][0]
                        count = states[state][1]
                        states[state] = [(value * count + sentiment) / (count + 1), (count + 1)]
                    else:
                        states[state] = [sentiment, 1]
    
    value = -5
    for state in states.keys():
        if states[state][0] > value:
            value = states[state][0]
            happy_state = state

    print happy_state


if __name__ == '__main__':
    main()
