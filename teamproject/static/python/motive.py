import numpy as np
from pandas.io.parsers import read_csv
import matplotlib.pyplot as plt
from matplotlib import font_manager

df = read_csv('../../static/csv/성인범행동기.csv', encoding='cp949')
df2 = read_csv('../../static/csv/소년범행동기.csv', encoding='cp949')
plt.rc('font', family='Malgun Gothic', size=7)
label = df['시점']
frequency = df['합계']

plt.pie(frequency,
             startangle=90,
             counterclock=False,
             autopct=lambda p: '{:.2f}%'.format(p),
             wedgeprops=dict(width=0.5)
             )
plt.title("소년범 범행동기", fontsize=25)
plt.legend()
plt.show()