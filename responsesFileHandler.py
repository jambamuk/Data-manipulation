#Import Libararies
import os, glob

#Declare Variables
COLLECTION_RESPONSES_DIRECTORY = './COLLECTIONS_FNB_RESPONSES/'
RESPONSE_FOOTER_LENGTH = 15
BILLINGMETHOD = 25
PRODUCT = 1
VERSION = 1
DATE = 20210824

os.chdir(COLLECTION_RESPONSES_DIRECTORY)

def getFinancialValue(file):
    footer =  file[-RESPONSE_FOOTER_LENGTH:]
    financialValueInRands = int(footer[1:].lstrip('0'))/100
    return financialValueInRands


for file in glob.glob(f'*{BILLINGMETHOD}_{PRODUCT}_{VERSION}_{DATE}*response'):
    openedFile = open(file, 'r')
    fileData = openedFile.read()
    openedFile.close()

    print(getFinancialValue(fileData))