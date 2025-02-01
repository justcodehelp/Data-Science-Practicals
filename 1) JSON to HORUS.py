import pandas as pd
sInputFileName='C:/VKHCG/05-DS/9999-Data/Country_Code.json'
InputData=pd.read_json(sInputFileName,orient='index',encoding="latin-1")
print('Input Data Values=====================================')
print(InputData)
print('======================================================')

ProcessData=InputData
ProcessData.drop('ISO-2-CODE',axis=1,inplace=True)
ProcessData.drop('ISO-3-CODE',axis=1,inplace=True)
ProcessData.rename(columns={'Country':'CountryName'},inplace=True)
ProcessData.rename(columns={'ISO-M49':'CountryNumber'),inplace=True)

ProcessData.set_index('CountryNumber',inplace=True)
ProcessData.sort_values('CountryName',axis=0,ascending=False,inplace=True)

print('Process Data Values===================================')
print(ProcessData)
print('======================================================')

OutputData=ProcessData
sOutputFileName='C:/VKHCG/05-DS/9999-Data/HOURS-JSON-Country.csv'
OutputData.to_csv(sOutputFileName,index=False)
print('JSON to HORUS-Done')
