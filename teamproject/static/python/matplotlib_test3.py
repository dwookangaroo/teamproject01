import numpy as np
from pandas.io.parsers import read_csv
import matplotlib.pyplot as plt
from matplotlib import font_manager

df2 = read_csv('../csv/성인재범기간.csv', encoding='cp949')
plt.rc('font', family='Malgun Gothic', size=7)

label = df2['재범기간']
frequency = df2['합계']

plt.pie(frequency,
             startangle=90,
             counterclock=False,
             autopct=lambda p: '{:.2f}%'.format(p),
             wedgeprops=dict(width=0.5)
             )
plt.title("성인 기간 재범기간", fontsize=25)
plt.legend(df2['재범기간'])
plt.savefig('recidivism.png')
plt.show()