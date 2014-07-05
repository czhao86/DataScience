import sys
import json
import operator

def main():
    states = {
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

    afinnfile=open(sys.argv[1])
    scores={}
    for line in afinnfile:
        term,score=line.split("\t")
        scores[term]=int(score)

    outputfile=open(sys.argv[2])
    senti={}    
    happystate={}
    happystate=states
    for key in happystate:
        happystate[key]=0

    for ln in outputfile:
        ans=0
        senti=json.loads(ln)
        if ("text" in ln) and (senti.get("lang")=="en"):
            www=senti.get("user").get("location").split( )
            for ww in www:
                if ww in states:
                    twitter=senti.get("text").encode('utf-8')
                    words=twitter.split( )
                    #print words
                    for word in words:
                        if word in scores.keys():
                            ans=ans+scores.get(word)
                    happystate[ww]=happystate[ww]+ans
    #print happystate
    print max(happystate.iteritems(),key=operator.itemgetter(1))[0]


if __name__ == '__main__':
    main()
