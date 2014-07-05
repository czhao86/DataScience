from __future__ import division

import sys
import json


def main():

    outputfile=open(sys.argv[1])
    senti={}
    notsenti={}
    total=0
    for ln in outputfile:
        senti=json.loads(ln)
        if "text" in ln:
            twitter=senti.get("text").encode('utf-8')
            words=twitter.split( )
            for word in words:
                if word not in notsenti.keys():
                    notsenti[word]=1
                else:
                    notsenti[word]=notsenti[word]+1
                total=total+1
    for x in notsenti:
        print x,' ',notsenti[x]/total

if __name__ == '__main__':
    main()
