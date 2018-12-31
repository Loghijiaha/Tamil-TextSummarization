# coding: utf-8

import nltk
from nltk.tag.stanford import StanfordNERTagger

# Optional
import os
java_path = "/usr/lib/jvm/java-8-oracle"
os.environ['JAVA_HOME'] = java_path

sentence = u"சென்னை நகருக்கு நீண்ட வரலாறு உள்ளது. கி.பி. 1ஆம் நூற்றாண்டு முதல் பல்லவ, சோழ மற்றும் விஜயநகர பேரரசுகளில் சென்னை ஒரு முக்கிய இடமாக விளங்கியதாகக் கருதப்படுகிறது. வெளிநாடுகளிலிருந்து வர்த்தகர்களும் மத போதகர்களும் சென்னைக் கடற்கரை மூலம் வந்துள்ளனர். இந்தப் பகுதி முதலில் சென்னப்பட்டணம் என்ற சிறிய கிராமமாக இருந்தது."

jar = 'stanford-ner.jar'
model = 'ner-model-tamil.ser.gz'

ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')

words = nltk.word_tokenize(sentence)
print (words)
print(ner_tagger.tag(words))