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

