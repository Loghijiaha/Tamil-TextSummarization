import ner_tamil,os
def namedEntityRecog(sentences,cwd) :
    counts = []
    for sentence in sentences :
        words=[]
        for nameEntity in ner_tamil.ner(sentence,cwd):
            if nameEntity[1] != 'O':
                words.append(nameEntity)
        count = len(words)
        counts.append(count)
    return counts

