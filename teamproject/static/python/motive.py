import numpy as np
from pandas.io.parsers import read_csv
import matplotlib.pyplot as plt
from matplotlib import font_manager

df = read_csv('../../static/csv/성인범행동기.csv', encoding='utf8')
plt.rc('font', family='Malgun Gothic', size=7)
label = df['범행동기별']
frequency = df['합계']

plt.pie(frequency,
             startangle=90,
             counterclock=False,
             autopct=lambda p: '{:.2f}%'.format(p),
             wedgeprops=dict(width=0.5),
            colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple', 'gold', 'silver','goldenrod','lightcoral']
             )
plt.title("성인범 범행동기", fontsize=25)
plt.legend(df['범행동기별'])
plt.savefig('motive.png')
plt.show()
