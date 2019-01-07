import stemmer
def remove_stop_words(sentences):
    tokenized_sentences = []
    for sentence in sentences:
        tokens = []
        split = sentence.lower().split()
        for word in split:
            if word not in stop:
                try:
                    tokens.append(stemmer.stemWord(word))
                except:
                    tokens.append(word)

        tokenized_sentences.append(tokens)
    return tokenized_sentences