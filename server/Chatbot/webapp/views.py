from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.http import HttpResponse
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.corpus import stopwords

import re
import pandas as pd
import numpy as np


def process_word(description):
    #divide the description into tokens
    tokens = word_tokenize(description)

    #remove the punctuations
    punctuation = re.compile(r'[-,!:;._?|0-9]')

    fdist = FreqDist()

    pst = PorterStemmer()
    word_lem = WordNetLemmatizer()

    #process the words by words
    for word in tokens:

        #remove the punctuations.
        word = punctuation.sub("", word)

        # change the word to correct word
        word = word_lem.lemmatize(word)
        # use the stemmer to change give,  giving = give
        word = pst.stem(word)

        # remove the stopwords in the english
        if word in stopwords.words('english'):
            pass
        else:
            fdist[word.lower()] += 1

    return dict(fdist)


class recommend(APIView):
    def post(self, request):
        # nltk.download('wordnet')
        # nltk.download('stopwords')

        # get the description from the request
        description = request.data['description']
        print("The Description provide by the user : " + description)

        des_token = process_word(description);
        # print(des_token)

        # process with file
        data = pd.read_csv('DataSet.csv')
        print("data shape ", data.shape, type(data))
        # print(data.to_string())
        Description_data = data["Description"].tolist()
        Product_data = data["Product"].tolist()

        # store marks to the matching words
        marks = 0
        # to store the index of the element
        index = -1

        for i in range(len(Description_data)):
            #process the csv descriptions and convert that into dictionary
            data_token = process_word(Description_data[i])
            # print(data_token.keys())

            #find the common elements
            common_elements = np.intersect1d(list(data_token.keys()), list(des_token.keys()))

            #check if the marks is low change the index and marks
            if marks < len(common_elements):
                marks = len(common_elements)
                index = i

        #return the product
        return HttpResponse(Product_data[index])




