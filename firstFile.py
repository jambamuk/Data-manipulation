from datetime import datetime
import os

COLLECTION_DIRECTORY = './COLLECTIONS_FNB/'

HEADER_LENGTH = 22
FOOTER_LENGTH = 15
ENTRY_LENGTH = 263

#Declare Arrays
fileNames = []
fileData = []
footers = []

fileNames = os.listdir(COLLECTION_DIRECTORY)
for i in range(len(fileNames)):
    file = open(COLLECTION_DIRECTORY + fileNames[i], 'r')
    fileData.append(file.read())
    file.close()

#entries = fileData[0][HEADER_LENGTH:-FOOTER_LENGTH]
#print(entries)

for i in fileData:
    footer = fileData[i]
footer = fileData[0]