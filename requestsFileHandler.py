import os

COLLECTION_REQUESTS_DIRECTORY = './COLLECTIONS_FNB_REQUESTS/'

requestFileNames = []
requestFileData = []
requestFinancialValues = []

requestFileNames = os.listdir(COLLECTION_REQUESTS_DIRECTORY)

requestFileNames = []
requestFileData = []
requestFinancialValues = []


for i in range(len(requestFileNames)):
    file = open(COLLECTION_REQUESTS_DIRECTORY + requestFileNames[i], 'r')
    requestFileData.append(file.read())
    file.close()
