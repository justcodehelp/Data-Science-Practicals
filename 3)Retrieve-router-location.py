import sys
import os
import pandas as pd
InputFileNmae='IP_DATA_CORE.csv'
Base='C:/VKHCG'
sFileName=Base+'/01-Vermeulen/00-RawData/'+InputFileName
print('Loading:',SfileName)
IP_DATA_ALL=pd.read_csv(sFileNmae,header=0,low_memory=False,usecols=['Country',Place Name',Latitude','Longitude'],encoding="latin-1")
IP_DATA_ALL.rename(columns={Place Name':'Place_Name'},inplace=True)
sFileDir=Base+'01-Vermeulen/01-Retrieve/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir):
ROUTERLOC=IP_DATA_ALL.drop_duplicates(subset=None,keep='first',inplace=False)
print('Rows:',ROUTERLOC.shape[0])
print('Columns:',ROUTERLOC.shape[1])
sFileName2=sFileDir+'/'+OutputFileName
ROUTERLOC.to_csv(sFileName2,index=False,encoding="latin-1")
print('###Done!!!########################################')
