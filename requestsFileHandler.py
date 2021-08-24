#Import Libararies
import os, glob

#Declare Variables
COLLECTION_REQUESTS_DIRECTORY = './COLLECTIONS_FNB_REQUESTS/'
REQUEST_FOOTER_LENGTH = 24
BILLINGMETHOD = 25
PRODUCT = 1
VERSION = 1
DATE = 20210824

os.chdir(COLLECTION_REQUESTS_DIRECTORY)

def getFinancialValue(file):
    footer =  file[-REQUEST_FOOTER_LENGTH:]
    financialValueInRands = int(footer[7:].lstrip('0'))/100
    return financialValueInRands


for file in glob.glob(f'*{BILLINGMETHOD}_{PRODUCT}_{VERSION}_{DATE}*'):
    openedFile = open(file, 'r')
    fileData = openedFile.read()
    openedFile.close()

    print(getFinancialValue(fileData))