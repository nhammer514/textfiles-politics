import spacy
from collections import Counter
import re as regex
import os
from saxonche import PySaxonProcessor

nlp = spacy.load("en_core_web_lg")

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

