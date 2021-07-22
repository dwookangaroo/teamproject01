import numpy as np
from pandas.io.parsers import read_csv
import pandas as pd
import matplotlib.pyplot as plt

kor = pd.read_csv('../csv/kor_crime.csv', index_col='범죄')

usa = pd.read_csv('../csv/usa_crime.csv', index_col='crime')

plt.rc('font', family='Malgun Gothic', size=7)
columns = ['2013', '2014', '2015', '2016', '2017', '2018', '2019']
n_data = len(columns)
index = np.arange(n_data)
#----------------------------------총범죄수
#plt.bar(index, kor.iloc[0], width=0.2, color = 'skyblue')
#plt.bar(index + 0.2, usa.iloc[0], width=0.2, color = 'orange')
#plt.xticks(index + 0.1, columns)
#plt.title('소년 100,000 당 총 범죄수')
#plt.xlabel('연도')
#plt.ylabel('총건수')
#plt.legend(['KOR', "USA"])
#plt.savefig('korusa.png')
#--------------------------------------재산범죄
#plt.bar(index, kor.iloc[1], width=0.2, color = 'skyblue')
#plt.bar(index + 0.2, usa.iloc[1], width=0.2, color = 'orange')
#plt.xticks(index + 0.1, columns)
#plt.title('100,000 당 재산범죄 건수')
#plt.xlabel('연도')
#plt.ylabel('건수')
#plt.legend(['KOR', "USA"])
#plt.savefig('property.png')

#--------------------------------------폭행
#plt.bar(index, kor.iloc[2], width=0.2, color = 'skyblue')
#plt.bar(index + 0.2, usa.iloc[2], width=0.2, color = 'orange')
#plt.xticks(index + 0.1, columns)
#plt.title('100,000 당 폭행범죄 건수')
#plt.xlabel('연도')
#plt.ylabel('건수')
#plt.legend(['KOR', "USA"])
#plt.savefig('assault.png')
#--------------------------------------강도
#plt.bar(index, kor.iloc[3], width=0.2, color = 'skyblue')
#plt.bar(index + 0.2, usa.iloc[3], width=0.2, color = 'orange')
#plt.xticks(index + 0.1, columns)
#plt.title('100,000 당 강도범죄 건수')
#plt.xlabel('연도')
#plt.ylabel('건수')
#plt.legend(['KOR', "USA"])
#plt.savefig('robbery.png')
#--------------------------------------방화
#plt.bar(index, kor.iloc[4], width=0.2, color = 'skyblue')
#plt.bar(index + 0.2, usa.iloc[4], width=0.2, color = 'orange')
#plt.xticks(index + 0.1, columns)
#plt.title('100,000 당 방화범죄 건수')
#plt.xlabel('연도')
#plt.ylabel('건수')
#plt.legend(['KOR', "USA"])
#plt.savefig('arson.png')
#--------------------------------------살인
#plt.bar(index, kor.iloc[5], width=0.2, color = 'skyblue')
#plt.bar(index + 0.2, usa.iloc[5], width=0.2, color = 'orange')
#plt.xticks(index + 0.1, columns)
#plt.title('100,000 당 살인범죄 건수')
#plt.xlabel('연도')
#plt.ylabel('건수')
#plt.legend(['KOR', "USA"])
#plt.savefig('murder.png')
plt.show()