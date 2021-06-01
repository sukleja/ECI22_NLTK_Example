import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')

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
