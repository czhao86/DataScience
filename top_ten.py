import sys
import json
import operator

def main():

    outputfile=open(sys.argv[1])
    senti={}
    topten={}
    for ln in outputfile:
        ans=0
        senti=json.loads(ln)
        if "text" in ln and senti.get("entities").get("hashtags"):
            hashtag=senti.get("entities").get("hashtags")[0].get("text")
            if hashtag in topten:
                topten[hashtag]+=1
            else:
                topten[hashtag]=1
    sorted_topten=sorted(topten.iteritems(),key=operator.itemgetter(1),reverse=True)
    for i in range(0,10):
        print sorted_topten[i][0],' ',sorted_topten[i][1]

if __name__ == '__main__':
    main()
