#Author: Nurendra Choudhary.
#Algorithm Reference: http://en.wikipedia.org/wiki/Lesk_algorithm

from nltk.corpus import wordnet 
from nltk.tokenize import WordPunctTokenizer
import sys
import wikipedia
import tkinter as tk

window = tk.Tk()
window.title("Task 2 - Wikipedia disambiguation")
window.geometry("950x350")
word = ""
sentence = ""

lable1 = tk.Label(text = "Enter Sentence: ")
guisentence = tk.Entry()
lable1.grid(column = 0, row = 0)
guisentence.grid(column = 1, row = 0)
lable2 = tk.Label(text = "Target word: ")
guiword = tk.Entry()
lable2.grid(column = 0, row = 1)
guiword.grid(column = 1, row = 1)
button = tk.Button(text="Disabbiguate", command=lambda:on_confirm())
button.grid(column = 1, row = 2)
textBox1 = tk.Text(window, height=15, width=100)
textBox1.grid(column = 1, row = 3)

def on_confirm():
    sentence = guisentence.get()
    word = guiword.get()
    a = lesk(word,sentence)
    textBox1.insert(tk.END, "\nSynset: ")
    textBox1.insert(tk.END, wikipedia.summary(a,2))



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
    textBox1.insert(tk.END, synset + "\n")
    summ = wikipedia.page(synset).content
    gloss = set(WordPunctTokenizer().tokenize(summ))
    #for i in synset.examples():
     #    gloss.union(i)
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
    #word=wordnet.morphy(word) if wordnet.morphy(word) is not None else word
    for sense in searchresults:
        if(sense != 'Bar (disambiguation)'):
            overlap = overlapcontext(sense,sentence)
            #for h in sense.hyponyms():
            #    overlap += overlapcontext( h, sentence )
            if overlap > maxoverlap:
                    maxoverlap = overlap
                    bestsense = sense
    return bestsense



window.mainloop()

