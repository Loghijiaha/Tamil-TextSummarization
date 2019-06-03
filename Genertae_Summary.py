import pickle

import para_reader
import rbm
import os
import numpy as np
from sentencePosition import senPos
from sentenceNumerals import numericToken
from stop_word_filter import remove_stop_words
from pos_tami import pos_tag
from tFiDF import tFiDF
from text_segmentation import split_into_sentences
from numberOfNamedEntities import namedEntityRecog
from ParagraphPosition import paraPos


def executeForAFile(filename, cwd):
    os.chdir(cwd + "/data")
    file = open(filename, 'r')
    text = file.read()
    paragraphs = para_reader.show_paragraphs(filename)
    os.chdir(cwd )
    sentences = split_into_sentences(text)
    tokenized_sentences = remove_stop_words(sentences)
    # print(tokenized_sentences)
    # # tagged = pos_tag(remove_stop_words(sentences))
    # print("LENNNNN : ")
    # print(len(senPos(paragraphs)))
    # term frequency score
    tfIdfScore = tFiDF(tokenized_sentences)
    # print('Term frequency')
    # print(tfIdfScore)

    # Number of numerals
    numericTokenScore = numericToken(tokenized_sentences)
    # print('numeric token score')
    # print(numericTokenScore)
    # Number of Named entity
    namedEntityRecogScore = namedEntityRecog(sentences, cwd)
    print('named Entity score')
    print(namedEntityRecogScore)
    #
    # # Sentence position score
    sentencePosScore = senPos(sentences)
    # print('Sentence score')
    # print(sentencePosScore)
    #
    # Sentence Position score
    sentenceParaScore = paraPos(paragraphs)
    # print('Sentence Para score')
    # print(sentenceParaScore)
    featureMatrix = []
    featureMatrix.append(sentencePosScore)
    featureMatrix.append(sentenceParaScore)
    featureMatrix.append(numericTokenScore)
    featureMatrix.append(namedEntityRecogScore)
    featureMatrix.append(tfIdfScore)

    # prepare feature matrix for training
    featureMat = np.zeros((len(sentences), 5))
    for i in range(5):
        for j in range(len(sentences)):
            featureMat[j][i] = featureMatrix[i][j]

    # print("\n\n\nPrinting Feature Matrix : ")
    # print(featureMat)

    # feature sum generation
    # feature_sum = []
    #
    # for i in range(len(np.sum(featureMat, axis=1)))
    #     feature_sum.append(np.sum(featureMat, axis=1)[i])
    # print(feature_sum)

    #training using rbm
    temp =rbm.test_rbm(featureMat,learning_rate=0.1,training_epochs=10,batch_size=5,n_chains=5,n_hidden=5)

    #get enhancedfeature
    enhancedFeatureSum=[]
    for i in range(len(sentences)):
        enhancedFeatureSum.append([np.sum(temp,axis=1)[i],i])

    # print('\n Enhanced Feature Sum')
    # print(enhancedFeatureSum)

    #selecting the max enhanced sum index
    index_sentence=sorted(enhancedFeatureSum,key=lambda x: x[0],reverse=True)[0][1]
    # print("\n\nExtracted Sentence As Summary\n\n\n")
    output=sentences[index_sentence]
    return output
def executeForAFile_input(filename, cwd):
    os.chdir(cwd + "/Input_file")

    file = open(filename, 'r')
    text = file.read()
    file.close()
    # os.chdir(cwd)
    paragraphs = para_reader.show_paragraphs(filename)
    sentences = split_into_sentences(text)
    text_len = len(sentences)

    tokenized_sentences = remove_stop_words(sentences)
    # print(tokenized_sentences)
    # # tagged = pos_tag(remove_stop_words(sentences))
    # print("LENNNNN : ")
    # print(len(senPos(paragraphs)))
    # term frequency score
    tfIdfScore = tFiDF(tokenized_sentences)
    # print('Term frequency')
    # print(tfIdfScore)

    # Number of numerals
    numericTokenScore = numericToken(tokenized_sentences)
    # print('numeric token score')
    # print(numericTokenScore)
    # Number of Named entity
    namedEntityRecogScore = namedEntityRecog(sentences, cwd)
    print('named Entity score')
    print(namedEntityRecogScore)
    #
    # # Sentence position score
    sentencePosScore = senPos(sentences)
    # print('Sentence score')
    # print(sentencePosScore)
    #
    # Sentence Position score
    sentenceParaScore = paraPos(paragraphs)
    # print('Sentence Para score')
    # print(sentenceParaScore)
    featureMatrix = []
    featureMatrix.append(sentencePosScore)
    featureMatrix.append(sentenceParaScore)
    featureMatrix.append(numericTokenScore)
    featureMatrix.append(namedEntityRecogScore)
    featureMatrix.append(tfIdfScore)

    # prepare feature matrix for training
    featureMat = np.zeros((len(sentences), 5))
    for i in range(5):
        for j in range(len(sentences)):
            featureMat[j][i] = featureMatrix[i][j]

    print("\n\n\nPrinting Feature Matrix : ")
    print(featureMat)

    # feature sum generation
    feature_sum = []

    for i in range(len(np.sum(featureMat, axis=1))):
        feature_sum.append(np.sum(featureMat, axis=1)[i])
    print(feature_sum)

    #training using rbm
    temp =rbm.test_rbm(featureMat,learning_rate=0.1,training_epochs=10,batch_size=5,n_chains=5,n_hidden=5)
    enhancedFeatureSum = []
    for i in range(len(sentences)):
        enhancedFeatureSum.append([np.sum(temp, axis=1)[i], i])
    index_sentence = sorted(enhancedFeatureSum, key=lambda x: x[0], reverse=True)[0][1]
    output = sentences[index_sentence]
    #get enhancedfeature
    return output
def train(inputfile):
    cwd = os.getcwd()
    out= "article-1"
    filenames = []
    output_file_list = []

    for file in os.listdir(cwd + "/data"):
        filenames.append(file)
        output_file_list.append(file)
    for i in range(len(filenames) - 2):
        print("Training......." + filenames[i])
        executeForAFile(filenames[i], cwd)
    return executeForAFile_input(inputfile, cwd)
