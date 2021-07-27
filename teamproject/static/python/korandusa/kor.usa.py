import numpy as np
from pandas.io.parsers import read_csv
import pandas as pd
import matplotlib.pyplot as plt

kor = pd.read_csv('../csv/kor_crime.csv', index_col='범죄')

usa = pd.read_csv('../csv/usa_crime.csv', index_col='crime')

inc_final = pd.read_csv('../csv/inc_final.csv' )

plt.rc('font', family='Malgun Gothic', size=7)
columns = ['2013', '2014', '2015', '2016', '2017', '2018', '2019']
n_data = len(columns)
index = np.arange(n_data)
#----------------------------------총범죄수
# plt.figure(figsize=(8,6))
# plt.bar(index, kor.iloc[0], width=0.2, color = 'skyblue')
# plt.bar(index + 0.2, usa.iloc[0], width=0.2, color = 'orange')
# plt.xticks(index + 0.1, columns)
# plt.title('소년 100,000 당 총 범죄수')
# plt.xlabel('연도')
# plt.ylabel('총건수')
# plt.legend(['KOR', "USA"])
# plt.savefig('korusa.png')
# plt.show()
#--------------------------------------재산범죄
# plt.figure(figsize=(8,6))
# plt.bar(index, kor.iloc[1], width=0.2, color = 'skyblue')
# plt.bar(index + 0.2, usa.iloc[1], width=0.2, color = 'orange')
# plt.xticks(index + 0.1, columns)
# plt.title('100,000 당 재산범죄 건수')
# plt.xlabel('연도')
# plt.ylabel('건수')
# plt.legend(['KOR', "USA"])
# plt.savefig('property.png')

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
#plt.savefig('violent.png')
#plt.show()
#--------------------------------------------------흉악
# plt.figure(figsize=(8,6))
# plt.subplot(221)
#
# plt.bar(index, kor.iloc[4], width=0.2, color = 'skyblue')
# plt.bar(index + 0.2, usa.iloc[4], width=0.2, color = 'orange')
# plt.xticks(index + 0.1, columns)
# plt.title('방화범죄')
#
# plt.ylabel('청소년 100,000명당 건수')
# plt.legend(['KOR', "USA"])
#
#
# plt.subplot(222)
# plt.bar(index, kor.iloc[5], width=0.2, color = 'skyblue')
# plt.bar(index + 0.2, usa.iloc[5], width=0.2, color = 'orange')
# plt.xticks(index + 0.1, columns)
# plt.title('살인범죄')
#
# plt.ylabel('건수')
#
# plt.subplot(223)
# plt.bar(index, kor.iloc[3], width=0.2, color = 'skyblue')
# plt.bar(index + 0.2, usa.iloc[3], width=0.2, color = 'orange')
# plt.xticks(index + 0.1, columns)
# plt.title('강도범죄')
#
# plt.ylabel('건수')
#
#
# plt.subplot(224)
# plt.bar(index, kor.iloc[2], width=0.2, color = 'skyblue')
# plt.bar(index + 0.2, usa.iloc[2], width=0.2, color = 'orange')
# plt.xticks(index + 0.1, columns)
# plt.title('폭행범죄')
#
# plt.ylabel('건수')
# plt.savefig('violent.png')
# plt.show()

#-----------------------------------증감률
import matplotlib
from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
    # 윈도우인 경우
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:
    # Mac 인 경우
    rc('font', family='AppleGothic')

matplotlib.rcParams['axes.unicode_minus'] = False
# 그래프에서 마이너스 기호가 표시되도록 하는 설정입니다.


plt.figure(figsize=(8, 6))
x = np.arange(7)
years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019']
values = inc_final['kor']
values2 = inc_final['usa']

plt.grid()
plt.bar(x - 0.1, values, width=0.2)
plt.bar(x + 0.1, values2, width=0.2)

for i, v in enumerate(x):
    if (values[i] > 0):
        plt.text(v - 0.1, values[i], values[i],
                 fontsize=10,
                 color='black',
                 horizontalalignment='center',
                 verticalalignment='bottom')
    else:
        plt.text(v - 0.1, values[i], values[i],
                 fontsize=10,
                 color='black',
                 horizontalalignment='center',
                 verticalalignment='top')

for i, v in enumerate(x):
    if (values2[i] > 0):
        plt.text(v + 0.1, values2[i], values2[i],
                 fontsize=10,
                 color='black',
                 horizontalalignment='center',
                 verticalalignment='bottom')
    else:
        plt.text(v + 0.1, values2[i], values2[i],
                 fontsize=10,
                 color='black',
                 horizontalalignment='center',
                 verticalalignment='top')
plt.xticks(x, years)
plt.title('전년대비 증감율')
plt.legend(['kor', 'usa'])
plt.savefig('inc_rate.png')
plt.show()





