import spacy
from collections import Counter
import re as regex
import os
from saxonche import PySaxonProcessor


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
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~ copying " + file + " ~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        inFile.close()
    # With the contents copied, a loop will go through the array and write it all in a new file in output folder.
    with open(outputPath + "/" + file, 'w', encoding='utf8') as f:
        for line in content:
            f.write(str(line))

# Function runs through the tokens of given file. Entities are stored in array, then returned. Called by regexFile().
def entitycollector(tokens):
    with open('output.txt', 'w') as f:
        entities = {}
        for ent in sorted(tokens.ents):
        # if entity.label_ == "NORP" or entity.label_ == "LOC" or entity.label_=="GPE":
        # ebb: The line helps experiment with different spaCy named entity classifiers, in combination if you like:
        # When using it, remember to indent the next lines for the for loop.
            # print(entity.text, entity.label_, spacy.explain(entity.label_))
            entityInfo = [ent.text, ent.label_, spacy.explain(ent.label_)]
            stringify = str(entityInfo)
            f.write(stringify)
            f.write('\n')
        # PRINT TO FILE
            # entities.append(entity.text)
            entities[ent.text] = ent.label_
        return entities

# Function runs regex through given file.
def regexFile(file):
    fileDir = os.path.join(outputPath, file)
    with PySaxonProcessor(license=False) as proc:
        # grabs the original xml file and stores it in a variable for later.
        xml = open(fileDir, encoding='utf-8').read()
        xp = proc.new_xpath_processor()
        node = proc.parse_xml(xml_text=xml)
        xp.set_context(xdm_item=node)
        xpath = xp.evaluate('//p ! normalize-space() => string-join()')
        string = xpath.__str__()
        cleanedText = regex.sub('[^A-z]+', ' ', string)
        tokens = nlp(cleanedText)
        wrappedText = xml
        listEntities = entitycollector(tokens)
        #print(listEntities)
        if listEntities:
            for entity in listEntities.keys():
                #print(entity, listEntities[entity])
                if listEntities[entity] == "PERSON":
                    key_template = "<ent type = 'person'>" + entity + "</ent>"
                    wrappedText = wrappedText.replace(entity, key_template)
                    # Saves newly wrapped elements and then writes it into the copied file.
                    with open(fileDir, 'w', encoding='utf8') as f:
                        f.write(wrappedText)
                        print("WRAPPING " + entity)

for file in insideDir:
    copyTextFiles(file)
    regexFile(file)
    print("File checking finished.")