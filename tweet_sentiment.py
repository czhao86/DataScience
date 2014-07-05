import sys
import json

def main():
    afinnfile=open(sys.argv[1])
    scores={}
    for line in afinnfile:
        term,score=line.split("\t")
        scores[term]=int(score)

    outputfile=open(sys.argv[2])
    senti={}
    for ln in outputfile:
        ans=0
        senti=json.loads(ln)
        if "text" in ln:
            twitter=senti.get("text").encode('utf-8')
            words=twitter.split( )
            #print words
            for word in words:
                if word in scores.keys():
                    ans=ans+scores.get(word)
        print ans

if __name__ == '__main__':
    main()
