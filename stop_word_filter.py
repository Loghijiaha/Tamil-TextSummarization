import stemmer
from nltk.corpus import stopwords

stop = set(stopwords.words('tamil'))


def remove_stop_words(sentences):
    tokenized_sentences = []
    for sentence in sentences:
        tokens = []
        split = sentence.split()
        for word in split:
            if word not in stop:
                try:
                    tokens.append(stemmer.stemWord(word).strip())
                except:
                    tokens.append(word)

        tokenized_sentences.append(tokens)
    return tokenized_sentences


p = remove_stop_words(['பெங்களூரு என்ற பெயருக்கான முதல்முதல் குறிப்பு ஒன்பதாம்',
                       'நூற்றாண்டு மேற்கு கங்க வம்சத்தின் வீரக் கல் ஒரு மாவீரனின் சிறப்பம்சங்களைப் போற்றும் கல் எழுத்துக்கள் ஒன்றில் செதுக்கப்பட்டுள்ள எழுத்துக்களில் காணத்தக்கதாய் இருக்கிறது'])
print(p)
