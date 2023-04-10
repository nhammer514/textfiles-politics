# My Documentation

Okay, so we are working with this Python script that does natural language processing.

* Python File 1 is the [PersonTagger](personTagger.py)
* Python File 2 is the [CultureTagger](cultureTagger.py)

This is a code block from your project Python that we were just working on:
```py
config = {"spans_key": None, "annotate_ents": True, "overwrite": True, "validate": True}
ruler = nlp.add_pipe("span_ruler", before="ner",  config=config)
# 2023-04-07: ebb: NOTE: before="ner" setting seems to allow the spaCy NER rules to prevail over these patterns where
# there is a conflict.
# after="ner" means that the spaCy ner is TOTALLY OVERWRITTEN and invalidated by our patterns.

# Notes: Mattingly has this: ruler = nlp.add_pipe("entity_ruler", after="ner", config={"validate": True})
# But this only works when spaCy doesn't recognize a word / phrase as a named entity of any kind.
# If it recognizes a named entity but tags it wrong, we correct it with the span_ruler, not the entity_ruler
patterns = [
    {"label": "NULL", "pattern": [{"TEXT" : {"REGEX": "^-\w+?"}}]},
    {"label": "NULL", "pattern": [{"TEXT" : {"REGEX": "^\w$"}}]},
    {"label": "GPE", "pattern": [{"TEXT" : {"REGEX": "Babylon(ia)?"}}]},
    {"label": "NULL", "pattern": "di"},
    {"label": "ORG", "pattern": "Falangist"},
    {"label": "NORP", "pattern": "Dropa"},
    {"label": "GPE", "pattern": "Nazareth"},
    {"label": "NULL", "pattern": "Bab"},
]
ruler.add_patterns(patterns)
```

Now, here is what is happening in this code.






