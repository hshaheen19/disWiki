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


print(jaccard_similarity(tokenList[0],tokenizedSentence))



