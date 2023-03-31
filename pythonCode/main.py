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
    # creates a new file that includes all of the found entities.
    with open('output.txt', 'w') as f:
        entities = {}
        # goes through each entity in the token list.
        for ent in sorted(tokens.ents):
            entityInfo = [ent.text, ent.label_, spacy.explain(ent.label_)]
            stringify = str(entityInfo)
            f.write(stringify)
            f.write('\n')
            entities[ent.text] = ent.label_
        # return all entities with its label and text.
        return entities

# Function runs regex through given file.
def regexFile(file):
    fileDir = os.path.join(outputPath, file)
    with PySaxonProcessor(license=False) as proc:
        # grabs the original xml file and stores it in a variable for later. this some xquery bs
        xml = open(fileDir, encoding='utf-8').read()
        xp = proc.new_xpath_processor()
        node = proc.parse_xml(xml_text=xml)
        xp.set_context(xdm_item=node)

        # xquery goes through original text, and stores it all in a single string.
        xpath = xp.evaluate('//p ! normalize-space() => string-join()')
        string = xpath.__str__()

        # regex goes through the text and deletes anything that is not a letter or space.
        cleanedText = regex.sub('[^A-z]+', ' ', string)

        # gets the tokens of the clean text.
        tokens = nlp(cleanedText)

        wrappedText = xml
        # grabs all the entities in file and stores it in a list/array.
        listEntities = entitycollector(tokens)
        # if anything exists in the list, the following code will run.
        if listEntities:
            # it will check through each entity in the list and see its entity type. it is looking for "PERSON" tokens
            # in this instance, which includes of nouns and names.
            for entity in listEntities.keys():
                if listEntities[entity] == "PERSON":
                    # key_template variable is the elements we wrap around found instances.
                    key_template = "<ent type = 'person'>" + entity + "</ent>"
                    # loops through wrappedText until all entities are wrapped.
                    wrappedText = wrappedText.replace(entity, key_template)
                    # Saves newly wrapped elements and then writes it into new file.
                    with open(fileDir, 'w', encoding='utf8') as f:
                        f.write(wrappedText)
                        print("WRAPPING " + entity)

# This part of the code does not run. It is a WIP.
## It tries to find weird or invalid elements/tags and fix them.
def checkTags(file):
    content = []
    fileDir = os.path.join(outputPath, file)

    with open(fileDir, 'r', encoding='utf8') as inFile:
        for line in inFile:
            content.append(line)
    # With the contents copied, a loop will go through the array and write it all in a new file in output folder.
    with open(fileDir, 'w', encoding='utf8') as f:
        for line in content:
            match1 = regex.search("(<ent type = 'person'>){2,}(.+?)</ent>", line)
            if match:
                print("broken line found, fixing...")
                newLine = regex.sub("(<ent type = 'person'>){2,}(.+?)</ent>",r"\1 \2",line)
                print(line + "\n INTO.")
                print(newLine)


for file in insideDir:
    copyTextFiles(file)
    regexFile(file)
    #checkTags(file)
    print("File checking finished.")