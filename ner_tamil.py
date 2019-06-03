from nltk import word_tokenize
from nltk.tag import StanfordNERTagger
import os


def ner(sentence, cwd):
    jar = cwd + "/stanford-ner-tagger/stanford-ner.jar"
    model = cwd + "/stanford-ner-tagger/ner-model-tamil.ser.gz"
    ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')
    words = word_tokenize(sentence)
    return (ner_tagger.tag(words))

