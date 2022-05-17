'''Some examples how to use NLTK with the Wordnet synsets
NLTK homepage: https://www.nltk.org/'''
import nltk
from nltk.corpus import wordnet
from nltk.corpus import names

'''Downloading either with interactive downloader or directly by stating the module,
has to be only done once and can be commented out after the download'''
# nltk.download() #using the interactive downloader
# nltk.download('wordnet') #downloading the specific package without interactive downloader
# nltk.download('names')

'''preparing variables'''
synonyms = []
antonyms = []
examples = []
tag = ''
word = "love"

'''loads the cognitive synonyms for the word from the lexical database wordnet (called synsets in Wordnet)
more information about the database: https://wordnet.princeton.edu/'''
syns = wordnet.synsets(word)

'''appending synonyms and antonyms to list
lemmas are Wordnets canonical forms of words and represent the different synonyms and antonyms in this case'''
for syn in syns:
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

'''handling empty lists and loading example uses of the word'''
if len(antonyms) == 0:
    antonyms.append("No antonyms found")
if len(synonyms) == 0:
    synonyms.append("No synonyms found")

if not syns[0].examples():
    examples.append("No example uses found")
else:
    for ex in syns[0].examples():
        examples.append(ex)

'''Checking part of speach'''
if syns[0].pos() == 'n':
    tag = 'noun'
elif syns[0].pos() == 'a':
    tag = 'adjective'
elif syns[0].pos() == 'v':
    tag = 'verb'
elif syns[0].pos() == 'r':
    tag = 'adverb'

'''Printing out our information'''
print("The definition of: {} ({}) is: {}".format(word, tag, syns[0].definition()))
print("Examples of usage in an sentence: ", examples)
print("Synonyms of {} : {}".format(word, set(synonyms)))
print("Antonyms of {} : {}".format(word, set(antonyms)))
print('')

'''Example for using the names corpus'''
female_names = names.words('female.txt')
male_names = names.words('male.txt')
print("The first six female and male names in the names corpus:")
print(female_names[0:6])
print(male_names[0:6])
