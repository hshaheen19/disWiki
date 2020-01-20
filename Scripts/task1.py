from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
import tkinter as tk

window = tk.Tk()
window.title("Task 1 - Wordsense")
window.geometry("850x500")
textBox1 = tk.Text(window, height=15, width=100)
textBox1.grid(column = 0, row = 0)
textBox2 = tk.Text(window, height=3, width=100)
textBox2.grid(column = 0, row = 1)
textBox3 = tk.Text(window, height=3, width=100)
textBox3.grid(column = 0, row = 2)
word = "plant"
sentence = 'This plant requires watering every morning'

for ss in wn.synsets(word):
   #print(ss, ss.definition())
   textBox1.insert(tk.END, ss.definition())

tk2 = lesk(sentence,word)
textBox2.insert(tk.END, tk2)

tk3 = lesk(sentence,word,'n')

textBox3.insert(tk.END, tk3)

window.mainloop()