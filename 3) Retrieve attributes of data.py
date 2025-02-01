import sys
import os
import pandas as pd
if sys.platform=='linux':
    Base=os.path.expanduser('~')+'/VKHCG'
else:
    Base:'C:/VKHCG'
sFileName=Base+'/01-Vermeulen/00-RawData/IP_DATA_ALL.csv'
print(Loading:'sFileNmae)
IP_DATA_ALL=pd.read_csv(sFileName,header=0,low_memory=False,encoding="latin-1")
sFileDir=Base+'/01-Vermeulen/01-Retrieve/01-EDS/02-Pythonif not
      os.path.exists(sFileDir):
      os.makedirs(sFileDir)
print('Rows:',IP_DATA_ALL.shape[0])
print('Columns:',IP_DATA_ALL.shape[1])
print('### Raw Data Set ######################################')
for i in range(0,len(IP_DATA_ALL.columns)):
      print(IP_DATA_ALL.columns[i],type(IP_DATA_ALL.columns[i]))
print('### Fixed Data Set ####################################')
for i in range(0,len(IP_DATA_ALL.columns)):
      c.NameOld=IP_DATA_ALL_FIX.columns[i]+' '
      cNameNew=cNameOld.strip().replace("",".")
      IP_DATA_ALL_FIX.columns.values[i]=cNameNew

print(IP_DATA_ALL.columns[i],type(IP_DATA_ALL.columns[i]))
print('Fixed Data Set with ID')
      IP_DATA_ALL_with_ID=IP_DATA_ALL_FIX
      IP_DATA_ALL_with_ID.index.names=['RowID']
      #print(IP_DATA_ALL_with_ID.head())

sFileName2=sFileDir+/'Retrieve_IP_DATA.csv'
IP_DATA_ALL_with_ID.to_csv(sFileName2,index=True,encoding="latin-1")
print('###Done!!!!############################################')
