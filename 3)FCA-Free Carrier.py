import os
import sys
import pandas as pd
##########################################
Inco Term='FCA'
InputFileName='Incoterm_2010.csv'
OutputFileName='Retrieve_Incoterm_'+Inco Term+'_RuleSet.csv'
Company='03-Hillman'
##########################################
Base='C:/VKHCG'
print('####################################')
print('Working Base:',Base,'using',sys.platform)
print('####################################')
##########################################
sFileDir=Base+'/'+Company+'01-Retrieve/01-EDS/02-Python'
if not os,path.exists(sFileDir):
    os.makedirs(sFileDir)
##########################################
sFileName=Base+'/'+Company+'/00-RawData/'+InputFileName
print('#########')
print('Loading:',sFileName)
IncotermGrid=pd.read_csv(sFileName,header=0,low_memory=False)
IncotermRule=IncotermGrid[IcotermGrid.Shipping_Term==IncoTerm]
print('Rows:',IncotermRule.shape[0])
print('Columns:',IncotermRule.shape[1])
print('#########')
print(IncotermRule)
###########################################
sFileName=sFileDir+'/'+OutputFileName
IncotermRule.to_csv(sFileName,index=False)
###########################################
print('###Done!!#############################')
