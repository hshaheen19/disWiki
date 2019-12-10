import wikipedia

searchresults = wikipedia.search("plant")
summarylist = []

for results in searchresults:
    summarylist.append(wikipedia.summary(results))
print(re)
