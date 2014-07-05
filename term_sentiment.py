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
    notsenti={}
    for ln in outputfile:
        ans=0
        senti=json.loads(ln)
        if "text" in ln:
            twitter=senti.get("text").encode('utf-8')
            words=twitter.split( )
            for word in words:
                if word in scores.keys():
                    ans=ans+scores.get(word)
            for word in words:
                if word not in scores.keys():
                    if word not in notsenti.keys():
                        notsenti[word]=ans
                    else:
                        notsenti[word]=notsenti[word]+ans
    for x in notsenti:
        print x,' ',notsenti[x]

if __name__ == '__main__':
    main()
