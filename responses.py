from datetime import datetime
import os

COLLECTION_RESPONSES_DIRECTORY = './COLLECTIONS_FNB_RESPONSES/'

REQUEST_FOOTER_LENGTH = 15
RESPONSE_FOOTER_LENGTH = 15

# Declare Arrays
responseFileNames = []
responseFileData = []
responseFinancialValues = []


responseFileNames = os.listdir(COLLECTION_RESPONSES_DIRECTORY)
for i in range(len(responseFileNames)):
    file = open(COLLECTION_RESPONSES_DIRECTORY + responseFileNames[i], 'r')
    responseFileData.append(file.read())
    file.close()


for i in range(len(responseFileData)):
    footer = responseFileData[i][-RESPONSE_FOOTER_LENGTH:]
    financialValueInRands = int(footer[1:].lstrip('0'))/100
    responseFinancialValues.append(financialValueInRands)
    print(f'Financial Value: R{financialValueInRands}')
