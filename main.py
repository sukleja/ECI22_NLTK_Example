import nltk
from nltk.corpus import wordnet
from nltk.corpus import names
nltk.download('wordnet')
nltk.download('names')

synonyms = []
antonyms = []
word="love"

syns=wordnet.synsets(word)

for syn in syns:
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print("The definition of: ",word," is: ",syns[0].definition())
print("Example of usage in an sentence: ",syns[0].examples())
print("Synonyms of:", word,": ",set(synonyms))
print("Antonyms of:", word,": ",set(antonyms))

female_names=names.words('female.txt')
male_names=names.words('male.txt')
print(female_names)
print(male_names)