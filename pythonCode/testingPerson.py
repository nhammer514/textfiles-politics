import spacy
from collections import Counter
import re as regex
import os
from saxonche import PySaxonProcessor


#### Loads all of the necessary variables and functions.
# nlp = spacy.cli.download("en_core_web_lg")
nlp = spacy.load("en_core_web_lg")
#########################################################################################
# ebb: After reading the NLP output, we know spaCy is making some mistakes.
# So, here let's try adding an EntityRuler to customize spaCy's classification. We need
# to configure this BEFORE we send the tokens off to nlp() for processing.
##########################################################################################
# Create the EntityRuler and set it so the ner comes after, so OUR rules take precedence
# Sources:
#   W. J. B. Mattingly: https://ner.pythonhumanities.com/02_01_spaCy_Entity_Ruler.html
#   spaCy documentation on NER Entity Ruler: https://spacy.io/usage/rule-based-matching#entityruler
config = {"spans_key": None, "annotate_ents": True, "overwrite": True, "validate": True}
ruler = nlp.add_pipe("span_ruler", before="ner",  config=config)
# 2023-04-07: ebb: NOTE: before="ner" setting seems to allow the spaCy NER rules to prevail over these patterns where
# there is a conflict.
# after="ner" means that the spaCy NER is TOTALLY OVERWRITTEN and invalidated by our patterns.

# Notes: Mattingly has this: ruler = nlp.add_pipe("entity_ruler", after="ner", config={"validate": True})
# But this only works when spaCy doesn't recognize a word / phrase as a named entity of any kind.
# If it recognizes a named entity but tags it wrong, we correct it with the span_ruler, not the entity_ruler
patterns = [
    {"label": "NULL", "pattern": [{"TEXT": {"REGEX": "^-\w+?"}}]},
    {"label": "NULL", "pattern": [{"TEXT": {"REGEX": "^.$"}}]},
    {"label": "NULL", "pattern": [{"TEXT": {"REGEX": "^\w\w$"}}]},
    {"label": "NULL", "pattern": [{"TEXT": {"REGEX": "^[a-z]+\s+[a-z]+$"}}]},
    {"label": "NULL", "pattern": [{"TEXT": {"REGEX": "^.*?__{2,}.*?$"}}]},
    {"label": "NORP", "pattern": [{"TEXT": {"REGEX": "CHRISTIAN(ITY|DOM)"}}]},
    {"label": "NORP", "pattern": [{"TEXT": {"REGEX": "CHRISTIAN\s+NETWORK"}}]},
    # ebb: Don't match on any single characters!
    {"label": "NULL", "pattern": [{"TEXT": {"REGEX": "[A-Z]{2,}[A-Z][a-z]+"}}]},
    {"label": "NULL", "pattern": [{"TEXT": {"REGEX": "[a-z]{2,}[A-Z][a-z]+"}}]},
    {"label": "NULL", "pattern": [{"TEXT": {"REGEX": "^.*?[a-z][A-Z].*?$"}}]},
    # ebb: Above line attempts to stop matching things like Oak IslandThe Method
    {"label": "NULL", "pattern": [{"TEXT" : {"REGEX": "^[Mm\-]+$"}}]},
    # SOCIALISMBY RICHARD
    # ebb: Above line attempts to stop matching things Mmm-mm or mm , etc.
    {"label": "GPE", "pattern": [{"TEXT": {"REGEX": "Babylon(ia)?"}}]},
    {"label": "NORP", "pattern": [{"TEXT": {"REGEX": "Christiani\s*ty"}}]},
    {"label": "NULL", "pattern": "Christiani"},
    {"label": "NULL", "pattern": "Rea"},
    {"label": "NULL", "pattern": "di"},
    {"label": "DRV", "pattern": "Poltergeists"},
    {"label": "NULL", "pattern": "the user"},
    {"label": "NULL", "pattern": "Advanced"},
    {"label": "NULL", "pattern": "Greets"},
    {"label": "MISC", "pattern": "Plank's constant"},
    {"label": "NORP", "pattern": "Americans"},
    {"label": "GPE", "pattern": "Pennsylvania"},
    {"label": "NULL", "pattern": "ORG"},
    {"label": "PERSON", "pattern": [{"TEXT": {"REGEX": "(Ludwig [Vv]an )?Beethoven"}}]},
    {"label": "ORG", "pattern": "Falangist"},
    {"label": "ORG", "pattern": "Centre of Eternity"},
    {"label": "MISC", "pattern": "Behavior Scan"},
    {"label": "ORG", "pattern": "NOAA"},
    {"label": "ORG", "pattern": "Eurocheque"},
    {"label": "ORG", "pattern": "NASA"},
    {"label": "ORG", "pattern": [{"TEXT": {"REGEX": "(Bush|Reagan|Kennedy|Nixon|Ford|Carter|Eisenhower)\s+Administration"}}]},
    {"label": "NORP", "pattern": "Dropa"},
    {"label": "GPE", "pattern": "Nazareth"},
    {"label": "GPE", "pattern": "Kingdom of God"},
    {"label": "GPE", "pattern": "Washington D.C."},
    {"label": "PERSON", "pattern": "Locust"},
    {"label": "PERSON", "pattern": "Nostradameus"},
    {"label": "PERSON", "pattern": "John Zajac"},
    {"label": "PERSON", "pattern": "Charles McKee"},
    {"label": "NULL", "pattern": "Bab"},
    {"label": "NULL", "pattern": "the "},
    {"label": "NULL", "pattern": "The "},
    {"label": "NULL", "pattern": "Next"},
    {"label": "NULL", "pattern": "econonic aid"},
    {"label": "NULL", "pattern": "megabank"},
    {"label": "GPE", "pattern": "Utah, USA"},
    {"label": "GPE", "pattern": "Brussels, Belgium"},
    {"label": "GPE", "pattern": "Waldport, Oregon"},
    {"label": "GPE", "pattern": "Ludlow, Colorado"},
    {"label": "GPE", "pattern": "Moscow, Russia"},
    {"label": "GPE", "pattern": "Langley, Virginia"},
    {"label": "GPE", "pattern": "Harlingen, Texas"},
    {"label": "GPE", "pattern": "Oakdale, California"},
    {"label": "GPE", "pattern": "Vendenberg AFB, California"},
    {"label": "GPE", "pattern": "Huachuca, Arizona"},
]
ruler.add_patterns(patterns)

workingDir = os.getcwd()
CollPath = os.path.join(workingDir, '../regexConsp')
outputPath = os.path.join(workingDir, 'personTestingOutput/')
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
    with open('conspPERSONentityCollector.txt', 'w') as f:
        entities = {}
        # goes through each entity in the token list.
        for ent in sorted(tokens.ents):
            entityInfo = [ent.text, ent.label_]
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
        string = str(xpath)

        # regex goes through the text and deletes anything that is not a letter or space.
        cleanedText = regex.sub(r'\s{2,}', ' ', string)
        cleanedText = regex.sub(r'[^A-z ]+', ' ', cleanedText)
        cleanedText = regex.sub(r'National\s+Oceanic\s+and\s+Atmospheric\s+Administration', 'NOAA', cleanedText)
        cleanedText = regex.sub(r'National\s+Aeronautics\s+and\s+Space\s+Administration', 'NASA', cleanedText)
        cleanedText = regex.sub(r'Food\s+and\s+Drug\s+Administration', 'FDA', cleanedText)


        # gets the tokens of the clean text.
        tokens = nlp(cleanedText)

        wrappedText = xml
        # grabs all the entities in file and stores it in a list/array.
        dictEntities = entitycollector(tokens)
        # if anything exists in the list, the following code will run.
        if dictEntities:
            # it will check through each entity in the list and see its entity type. it is looking for "PERSON" tokens
            # in this instance, which includes of nouns and names.
            for entity in dictEntities.keys():
                if dictEntities[entity] == "PERSON":
                    # key_template variable is the elements we wrap around found instances.
                    key_template = "<ent type='person'>" + entity + "</ent>"
                    # loops through wrappedText until all entities are wrapped.
                    wrappedText = wrappedText.replace(entity, key_template)
                    # Saves newly wrapped elements and then writes it into new file.
                    with open(fileDir, 'w', encoding='utf8') as f:
                        f.write(wrappedText)
                        print("WRAPPING " + entity)
                    checkTags(file)
                    # ebb: Added above line to send the tagged file to the checkTags() function for cleaning.

# This part of the code is a WIP.
# ebb: I just activated it, and it works! (Nice job.) I altered it just a bit. May need more regexes to match.
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
            # match = regex.search(r"(<ent type='.+?'>[^<>]*?)<ent[^>]+?>([^<>]+?)</ent>([^<>]*?</ent>)", line)
            # if match:
            # print("broken line found, fixing...")
            # ebb: NOTE: IF this function only processes a line when there's a regex match, we'd have a serious problem:
            # we'd not output the rest of the file--only the cleaned matches. So the output files would be mostly empty!
            # Better to just string-clean every line using regex.sub(). Where there's no regex match, no substitution will happen.
            origLine = line
            # newLine = regex.sub(r"(<ent type='.+?'>[^<>]*?)<ent[^>]+?>([^<>]+?)</ent>([^<>]*?</ent>)", r"\1\2\3",line)
            # <spe<ent type='ORG'>cia</ent>l>
            newLine = regex.sub(r"(</?spe)<ent type='ORG'>(cia)</ent>(l>)", r"\1\2\3", origLine)
            # newLine = regex.sub(r"(<)<ent type='ORG'>(di)</ent>(v>)", r"\1\2\3", newLine)
            newLine = regex.sub(r"(<ent type='[A-z]+?'>[^<]*?)<ent type='[A-z]+?'>([^<]+?)</ent>([^<]*?</ent>)", r"\1\2\3", newLine)
            newLine = regex.sub(r"(<ent type='[A-z]+?'>[^<]*?)<ent type='[A-z]+?'>([^<]+?)</ent>([^<]*?</ent>)", r"\1\2\3", newLine)
            newLine = regex.sub(r"(<ent type='[A-z]+?'>[^<]*?)<ent type='[A-z]+?'>([^<]+?)</ent>([^<]*?</ent>)", r"\1\2\3", newLine)
            # ebb: I'm repeating the above just in case of the weird event of triple or quadruple nested <ent> tags in <ent> tags.
            # We saw it happen on the LOTR project and running it through multiple passes of the above line ultimately got rid of them all
            # preserving only the outermost tags.
            newLine = regex.sub(r"(<ent type=')<ent type='ORG'>(ORG)</ent>('>)", r"\1\2\3", newLine)
#
# <spe<ent type='ORG'>cia</ent>l>
# <<ent type='ORG'>di</ent>v>
            if origLine != newLine:
                print("broken line found, fixing...")
                print(origLine + "\n INTO.")
                print(newLine)
            f.write(str(newLine))
    print("File checking finished.")

for file in insideDir:
    copyTextFiles(file)
    regexFile(file)
    #checkTags(file)
    # ebb: You don't really want to activate checkTags here,
    # because it would run over the untagged input files.
