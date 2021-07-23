import numpy as np
from pandas.io.parsers import read_csv
import matplotlib.pyplot as plt
from matplotlib import font_manager


df2 = read_csv('../../static/csv/소년범행동기.csv', encoding='utf8')
plt.rc('font', family='Malgun Gothic', size=7)
label = df2['범행동기별']
frequency = df2['합계']

plt.pie(frequency,
             startangle=90,
             counterclock=False,
             autopct=lambda p: '{:.2f}%'.format(p),
             wedgeprops=dict(width=0.5),
             colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple', 'gold', 'silver','goldenrod','lightcoral']
             )
plt.title("소년범 범행동기", fontsize=25)
plt.legend(df2['범행동기별'])
plt.savefig('motive2.png')
plt.show()

