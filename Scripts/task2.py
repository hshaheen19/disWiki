#Author: Nurendra Choudhary.
#Algorithm Reference: http://en.wikipedia.org/wiki/Lesk_algorithm

from nltk.corpus import wordnet 
from nltk.tokenize import WordPunctTokenizer
import sys
import wikipedia


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


sentence = input("Enter the Sentence (or) Context :")
word = input("Enter the word :")

a = lesk(word,sentence)
print ("\n\nSynset:",wikipedia.summary(a,2))
