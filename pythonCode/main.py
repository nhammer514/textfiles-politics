import spacy
from collections import Counter
import re as regex
import os

#### Loads all of the necessary variables and functions.
nlp = spacy.load("en_core_web_lg")
workingDir = os.getcwd()
CollPath = os.path.join(workingDir, '../regexConsp')
outputPath = os.path.join(workingDir, 'output/')
# Everything in original conspiracy directory.
insideDir = os.listdir(CollPath)
print(insideDir)


# Copies files in case they do not exist
def copyTextFiles(file):
    content = []
    # Reads the contents of file, and saves each line of file into the content array.
    with open(CollPath + "/" + file, 'r', encoding='utf8') as inFile:
        for line in inFile:
            content.append(line)
        print("copying " + file)
        inFile.close()
    # With the contents copied, a loop will go through the array and write it all in a new file in output folder.
    with open(outputPath + "/" + file, 'w', encoding='utf8') as f:
        for line in content:
            f.write(str(line))

# Function runs through the tokens of given file. Entities are stored in array, then returned. Called by regexFile().
def entitycollector(tokens):
    entities = []
    for entity in tokens.ents:
        if entity.label_ == "PERSON":
            entities.append(entity.text)
        return entities

# Function runs regex through given file.
def regexFile(file):
    #  First, it reads file given. Supposedly, the newly created file in output folder.
    with open(outputPath + "/" + file, 'r', encoding='utf8') as inFile:
        rawText = str(inFile.read())
        # Regex finds all elements in a file and deletes them. Then Regex finds anything that is not a letter, and
        # deletes. It is stored in a variable that is supposedly clean from anything extra.
        cleanedText = regex.sub('[^A-z]+', ' ', regex.sub('<.+?>', ' ', rawText))
        # token stuff
        tokens = nlp(cleanedText)
        listEntities = entitycollector(tokens)
        # If the listEntity array has content in it, it will go through the list to see if the content is located
        # anywhere in the original, raw text.
        if listEntities:
            for entity in listEntities:
                wrappedText = regex.sub(str(entity), '<person>' + entity + '</person>',rawText)
                # Saves newly wrapped elements and then writes it into the copied file.
                with open(outputPath + "/" + file, 'w', encoding='utf8') as f:
                    f.write(wrappedText)
                    print("WRAPPING " + entity)
                    f.close()
        else:
            print("No names... Probably did not detect any?")

# Goes through all of the original conspiracy texts
for file in insideDir:
    copyTextFiles(file)
    regexFile(file)