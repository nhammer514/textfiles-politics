import spacy
from collections import Counter
import os
# Uncomment this line if you need the language model.
# If you already have it, comment it ou.
# Let's try the different spaCy language models for this. We can compare _lg with _md or _sm
workingDir = os.getcwd()
CollPath = os.path.join(workingDir, '../regexConsp')
insideDir = os.listdir(CollPath)
print(insideDir)

nlp = spacy.load("en_core_web_lg")
def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        readFile = f.read()
        # print(readFile)
        stringFile = str(readFile)
        # lengthFile = len(readFile)
        # print(lengthFile)
        tokens = nlp(stringFile)
        # print(tokens)
        listEntities = entitycollector(tokens)
        print(listEntities)
        # cardinal_freq = Counter(listCardinals)
        # topTen = cardinal_freq.most_common(10)
        # print(topTen)



def entitycollector(tokens):
    entities = []
    for entity in tokens.ents:
        # if entity.label_ == "CARDINAL":
        print(entity.text, entity.label_, spacy.explain(entity.label_))
        entities.append(entity.text)
    return entities


for file in os.listdir(CollPath):
    if file.endswith(".xml"):
        filepath = f"{CollPath}/{file}"
        print(filepath)
        readTextFiles(filepath)





# print(listCardinals)
# cardinal_freq = Counter(listCardinals)
# topTen = cardinal_freq.most_common(10)
# print(topTen)

# grimm = open('grimm.txt', 'r', encoding='utf8')
# grimmDoc = grimm.read()
# grimmNLP = nlp(grimmDoc)
# grimmmSentences = grimmNLP.sents

# def sentenceLengths(sentences):
#     lengths = []
#     for s in sentences:
#         length = len(s.text)
#         lengths.append(length)
#     return sorted(lengths)


# grimmLengths = sentenceLengths(grimmmSentences)
# # print(grimmLengths)
# maxVal = max(grimmLengths)
# minVal = min(grimmLengths)
# print('The shortest sentence is ' + str(minVal) + ' characters long.')
# print('The longest sentence is ' + str(maxVal) + ' characters long.')

# for sentence in grimmNLP.sents:
# #    print(sentence.text)
#     length = len(sentence.text)
#     if length == minVal:
#         print("The shortest sentence is: " + sentence.text)
#     if len(sentence.text) == maxVal:
#         print('The longest sentence is: ' + sentence.text + ' :' + str(maxVal) + 'characters')
