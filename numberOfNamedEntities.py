import ner_tamil
def namedEntityRecog(sentences) :
    counts = []
    for sentence in sentences :
        count = len(ner_tamil.ner(sentence))
        counts.append(count)
    return counts