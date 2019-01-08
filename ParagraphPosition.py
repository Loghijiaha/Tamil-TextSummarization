import text_segmentation as tSeg
def paraPos(paragraphs):
    scores = []
    for para in paragraphs:
        sentences = tSeg.split_into_sentences(para)
        print(len(sentences))
        if len(sentences) == 1 :
            scores.append(1.0)
        elif len(sentences) == 2 :
            scores.append(1.0)
            scores.append(1.0)
        else :
            scores.append(1.0)
            for x in range(len(sentences)-2) :
                scores.append(0.0)
            scores.append(1.0)
    return scores