import spacy
from collections import Counter
import re as regex
import os
# Uncomment this line if you need the language model.
# If you already have it, comment it ou.
# Let's try the different spaCy language models for this. We can compare _lg with _md or _sm
workingDir = os.getcwd()
CollPath = os.path.join(workingDir, '../regexConsp')
insideDir = os.listdir(CollPath)
print(insideDir)

if os.path.isfile("outputNames.txt"):
    open("outputNames.txt", 'w').close();

nlp = spacy.load("en_core_web_lg")
def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        readFile = f.read()
        stringFile = str(readFile)
        # Using REGEX to delete all element tags.
        elementsRemoved = regex.sub('<.+?>', '', stringFile)
        # Using REGEX to delete all \n.
        cleanedFile = regex.sub('\n', ' ', elementsRemoved)
        tokens = nlp(cleanedFile)

        listEntities = entitycollector(tokens)
        print(listEntities)

def entitycollector(tokens):
    entities = []
    for entity in tokens.ents:
        if entity.label_ == "PERSON":
            with open("outputNames.txt", 'a') as f:
                f.write("\n" + entity.text)
                print("Writing in outputNames.txt: " + entity.text)
            # print(entity.text, entity.label_, spacy.explain(entity.label_))
            entities.append(entity.text)
        return entities

for file in os.listdir(CollPath):
    if file.endswith(".xml"):
        filepath = f"{CollPath}/{file}"
        print(filepath)
        readTextFiles(filepath)