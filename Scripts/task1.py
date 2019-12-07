from nltk.wsd import lesk
from nltk.corpus import wordnet as wn

word = "plant"
sentence = 'This plant requires watering every morning'

for ss in wn.synsets(word):
    print(ss, ss.definition())

print(lesk(sentence,word))
print(lesk(sentence,word,'n'))
