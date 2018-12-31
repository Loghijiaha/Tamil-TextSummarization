# coding: utf-8

import nltk
from nltk.tag.stanford import StanfordNERTagger

# Optional
import os
java_path = "/usr/lib/jvm/java-8-oracle"
os.environ['JAVA_HOME'] = java_path

sentence = u"En 2017, une intelligence artificielle est en mesure de développer par elle-même Super Mario Bros. " \
    "Sans avoir eu accès au code du jeu, elle a récrée ce hit des consoles Nintendo. Des chercheurs de l'Institut " \
    "de Technologie de Géorgie, aux Etats-Unis, viennent de la mettre à l'épreuve."

jar = 'stanford-ner.jar'
model = 'ner-model-french.ser.gz'

ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')

words = nltk.word_tokenize(sentence)
print(ner_tagger.tag(words))