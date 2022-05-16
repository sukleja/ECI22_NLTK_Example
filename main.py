import nltk
import example
from nltk.corpus import wordnet
from nltk.corpus import names

'''Downloading either with interactive downloader or directly by stating the module'''
#nltk.download()
#nltk.download('wordnet')
#nltk.download('names')

synonyms = []
antonyms = []
examples = []
word = "love"

# loads the cognitive synonyms for the word from wordnet
syns = wordnet.synsets(word)

#appending synonyms and antonyms to list
for syn in syns:
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

#handling empty lists and loading example uses of the word
if len(antonyms) == 0:
    antonyms.append("No antonyms found")

if not syns[0].examples():
    examples.append("No example uses found")
else:
    for ex in syns[0].examples():
        examples.append(ex)
#####################

print("The definition of: ", word, " is: ", syns[0].definition())
print("Example of usage in an sentence: ", examples)
print("Synonyms of:", word, ": ", set(synonyms))
print("Antonyms of:", word, ": ", set(antonyms))
print('')

#loading name files and printing out the first 6 entries of the lists
female_names = names.words('female.txt')
male_names = names.words('male.txt')
print(female_names[0:6])
print(male_names[0:6])
#example.print_out()
