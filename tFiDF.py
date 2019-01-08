import collections
import math


def tFiDF(tokenized_sentences):
    scores = []
    COUNTS = []
    for sentence in tokenized_sentences:
        counts = collections.Counter(sentence)
        isf = []
        score = 0
        for word in counts.keys():
            count_word = 1
            for sen in tokenized_sentences:
                for w in sen:
                    if word == w:
                        count_word += 1
            score = score + counts[word] * math.log(count_word - 1)
        scores.append(score / len(sentence))
    return scores
