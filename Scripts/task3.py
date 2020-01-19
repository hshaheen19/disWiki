import wikipedia
import re 
import codecs
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog
from nltk.tokenize import WordPunctTokenizer
import sys

window = tk.Tk()
window.title("Wikipedia Disambiguation")
window.geometry("600x450")

summarylist = []
newSummary = []
content = ""
searchresults = ""
tokenizedSentence = []

title = tk.Label(text = "Select word for Disambiguation: ")
title.grid(column=0, row=0)
entry_field1 = tk.Entry()
entry_field1.grid(column=1, row=0)
textBox = tk.Text(window , height=30, width=100)
textBox.grid(column = 0, row = 3)

def open_file():
    file = filedialog.askopenfile(mode = 'r', title="Select a file", filetypes=[("html files", "*.htm")])
    content = file.read()
    textBox.insert(tk.END, content)


title = tk.Label(text = "Select file for Disambiguation: ")
title.grid(column=0, row=1)
button2 = tk.Button(text="Select File", command=lambda:open_file())
button2.grid(column = 1, row=1)


button1 = tk.Button(text="Disambiguate", command=lambda:on_confirm())
button1.grid(column=1, row=5)
def on_confirm():
    #window.destroy()
    word = entry_field1.get()
    sentence = textBox.get("1.0", 'end-1c')
    a = lesk(word,sentence)
    print ("\n\nSynset:",wikipedia.summary(a,2))

    #searchresults = wikipedia.search()
    # tokenizedSentence = re.sub("[^\w]", " ", textBox.get("1.0", 'end-1c')).split() 
    # for results in searchresults:
    #     try:
    #         summarylist.append(wikipedia.page(results).content)
    #     except wikipedia.exceptions.DisambiguationError as e:
    #         print(e.options)
    # for item in summarylist:
    #     newSummary.append(item.replace("plant",""))

    # tokenList = []
    # for item in newSummary:
    #     tokenList.append(re.sub("[^\w]", " ", item).split())
    # print_js(tokenList, tokenizedSentence)
    window.destroy()




functionwords = ['about', 'across', 'against', 'along', 'around', 'at',
                 'behind', 'beside', 'besides', 'by', 'despite', 'down',
                 'during', 'for', 'from', 'in', 'inside', 'into', 'near', 'of',
                 'off', 'on', 'onto', 'over', 'through', 'to', 'toward',
                 'with', 'within', 'without', 'anything', 'everything',
                 'anyone', 'everyone', 'ones', 'such', 'it', 'itself',
                 'something', 'nothing', 'someone', 'the', 'some', 'this',
                 'that', 'every', 'all', 'both', 'one', 'first', 'other',
                 'next', 'many', 'much', 'more', 'most', 'several', 'no', 'a',
                 'an', 'any', 'each', 'no', 'half', 'twice', 'two', 'second',
                 'another', 'last', 'few', 'little', 'less', 'least', 'own',
                 'and', 'but', 'after', 'when', 'as', 'because', 'if', 'what',
                 'where', 'which', 'how', 'than', 'or', 'so', 'before', 'since',
                 'while', 'although', 'though', 'who', 'whose', 'can', 'may',
                 'will', 'shall', 'could', 'be', 'do', 'have', 'might', 'would',
                 'should', 'must', 'here', 'there', 'now', 'then', 'always',
                 'never', 'sometimes', 'usually', 'often', 'therefore',
                 'however', 'besides', 'moreover', 'though', 'otherwise',
                 'else', 'instead', 'anyway', 'incidentally', 'meanwhile']

def overlapcontext( synset, sentence ):
    print(synset)
    summ = wikipedia.page(synset).content
    gloss = set(WordPunctTokenizer().tokenize(summ))
    gloss = gloss.difference( functionwords )
    if isinstance(sentence, str):
        sentence = set(sentence.split(" "))
    elif isinstance(sentence, list):
        sentence = set(sentence)
    elif isinstance(sentence, set):
        pass
    else:
        return
    sentence = sentence.difference( functionwords )
    return len( gloss.intersection(sentence) )

def lesk( word, sentence ):
    searchresults = wikipedia.search(word)
    bestsense = None
    maxoverlap = 0
    for sense in searchresults:
        overlap = overlapcontext(sense,sentence)
        if overlap > maxoverlap:
                maxoverlap = overlap
                bestsense = sense
    return bestsense


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

window.mainloop()
        