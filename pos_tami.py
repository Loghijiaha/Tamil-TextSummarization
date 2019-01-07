from nltk import *

import os
java_path = "/usr/lib/jvm/java-8-oracle"
os.environ['JAVA_HOME'] = java_path

jar = "stanford-pos-tagger/stanford-postagger-3.9.2.jar"
model="stanford-pos-tagger/tamil-pos-tagger-model"

myTagger = StanfordPOSTagger(model,jar)
sentence=u"கோயம்புத்தூர் மாவட்டமும் இம்மாவட்டத்தின் எல்லைகளாக அமைந்துள்ளன"

print(myTagger.tag(sentence.split()))