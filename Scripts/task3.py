import wikipedia
import re 
import codecs
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog

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
    searchresults = wikipedia.search(entry_field1.get())
    tokenizedSentence = re.sub("[^\w]", " ", textBox.get("1.0", 'end-1c')).split() 
    for results in searchresults:
        try:
            summarylist.append(wikipedia.page(results).content)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
    for item in summarylist:
        newSummary.append(item.replace("plant",""))

    tokenList = []
    for item in newSummary:
        tokenList.append(re.sub("[^\w]", " ", item).split())
    print_js(tokenList, tokenizedSentence)
    window.destroy()



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
        