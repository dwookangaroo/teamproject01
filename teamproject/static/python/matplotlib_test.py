import numpy as np
from pandas.io.parsers import read_csv
import matplotlib.pyplot as plt
from matplotlib import font_manager


df = read_csv('../csv/성인재범률.csv', encoding='CP949')
df2 = read_csv('../csv/소년범죄자 재범률.csv', encoding='CP949')
plt.rc('font', family='Malgun Gothic', size=7)
label = df['시점']

x = np.arange(len(label))

plt.bar(x, df['합계'], width=0.2, color='#4E5F76', label='성인')
plt.bar(x+0.2, df2['합계'], width=0.2, color='#353336',label='소년')

for i, v in enumerate(x):
    plt.text(v,df['합계'][i],str(df['합계'][i]),
             fontsize=8,
             color='red',
             horizontalalignment='center',
             verticalalignment='bottom')

for i, v in enumerate(x+0.2):
    plt.text(v,df2['합계'][i],str(df2['합계'][i]),
             fontsize=8,
             color='blue',
             horizontalalignment='center',
             verticalalignment='bottom')


plt.xticks(x, label)
plt.legend()
plt.title("범죄 재범률", fontsize=25)
plt.xlabel("연도")
plt.ylabel("재범률 (단위:%)", labelpad=20)
plt.ylim([40, 48])
# plt.savefig('graph.png')
plt.show()



# df = read_csv('성인재범.csv', encoding='CP949')
# df2 = read_csv('소년범죄 재범.csv', encoding='CP949')
# plt.rc('font', family='Malgun Gothic', size=7)
# label = df['시점']
#
# x = np.arange(len(label))
#
# plt.bar(x, df['소계'], width=0.2, color='black', label='성인')
# plt.bar(x+0.2, df2['소계'], width=0.2, color='blue',label='소년')
# plt.xticks(x, label)
# plt.legend()
# plt.title("범죄수", fontsize=25)
# plt.xlabel("연도")
# plt.ylabel("범죄수", rotation=0, labelpad=10)
# plt.ylim([0,500000])
# plt.show()





