#!/usr/bin/env python3

import pickle

exampleObj = {'Python':3,'KDE':5,'Windows':10}

fileObj = open('data.obj', 'wb')
pickle.dump(exampleObj,fileObj)
fileObj.close()

import pickle   

fileObj = open('data.obj', 'rb')
exampleObj = pickle.load(fileObj)
fileObj.close()
print(exampleObj)