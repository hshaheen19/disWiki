import wikipedia
import re 
import codecs

searchresults = wikipedia.search("THAILAND ")
summarylist = []
newSummary = []
f = codecs.open("APW19980603_0791.htm", 'r')
mainSentence = f.read()
#mainSentence = mainSentence.replace("plant","")

#replace function doesnt seem to work!

tokenizedSentence = re.sub("[^\w]", " ", mainSentence).split()
print(searchresults, '\n')

for results in searchresults:
    print(wikipedia.summary(results, 2), '\n')
    summarylist.append(wikipedia.page(results).content)

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
        print('Jaccard Similarity of sense', i, '\n', jaccard_similarity(tlist[i], tsentence), '\n')
        i += 1
    print(max(jsresult))
    indextlist = jsresult.index(max(jsresult))
    print(summarylist[indextlist])
        
print_js(tokenList,tokenizedSentence)

