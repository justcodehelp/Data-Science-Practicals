import string
import datetime as dt
print('#1 Removing leading or lagging spaces from data entry');
baddata="Data science with too many spaces is bad!!!"
print('>',baddata,'<')
cleandata=baddata.strip()
print('>'cleandata,'<')



import string
import datetime as dt
print('#2 Removing nonprintable characters from a data entry')
baddata="Data\x00Science with\x02 funny characters is \x10bad!!!"
cleandata=''.join(filter(lambda x:x in string.printable,baddata))
print('Bad Data:',baddata);
print('Clean Data:',cleandata)



import string
import datetime as dt
Convert YYYY/MM/DD to DD Month YYYY
print('# 3 Reformatting data entry to match specific formatting criteria.')
baddata=dt.data(2019,10,31)
baddata=format(baddata,'%Y-%m-%d')
baddata=dt.datetime.strptime(baddata,'%Y-%m-%d')
baddata=format(gooddata,'%Y-%m-%d')
baddata=format(gooddata,'%d%B%Y')
print('Bad Data:',baddata)
print('Good Data:',gooddata)
