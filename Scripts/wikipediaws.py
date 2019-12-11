import wikipedia
import re 

searchresults = wikipedia.search("plant")
summarylist = []
newSummary = []

mainSentence = "This plant requires watering every morning Plants"
mainSentence = mainSentence.replace("plant","")

tokenizedSentence = re.sub("[^\w]", " ", mainSentence).split()

for results in searchresults:
    summarylist.append(wikipedia.summary(results))

for item in summarylist:
    newSummary.append(item.replace("plant",""))

tokenList = []
for item in newSummary:
    tokenList.append(re.sub("[^\w]", " ", item).split())

def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union
    
#calculats the sense with the biggest jaccard similarity and prints it
#Needs to be cleand up
def print_js(tlist, tsentence):
    length = len(tlist)
    i = 0
    jsresult = []
    while i < length:
        jsresult.append(jaccard_similarity(tlist[i],tsentence))
        i += 1
    print(max(jsresult))
    indextlist = jsresult.index(max(jsresult))
    print(tlist[indextlist])
        
print_js(tokenList,tokenizedSentence)

