import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('D:/csv/ratio.csv',encoding='cp949')
df.drop('범죄별(1)',axis=1,inplace=True)

df.rename(columns={"범죄별(2)":"crime"},inplace=True)
df.drop(0, axis=0, inplace=True)
import platform
from matplotlib import font_manager, rc # Runtime Configuration
path = "c:/Windows/Fonts/malgun.ttf"
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')

df = df.astype({'2019' : 'float'})
df = df.sort_values(by='2019', ascending=False)

matplotlib.rcParams['axes.unicode_minus'] = False
plt.title('2006년 대비 범죄 증감표')
plt.xlabel('범죄명')
plt.ylabel('범죄증감율')
plt.bar(df['crime'], df['2019'], color=['r','g','b'], edgecolor='black')
plt.text('강력범죄(흉악)', -180, '1808건 증가', fontsize=13)
plt.text('강력범죄(폭력)', -180, '518건 증가',fontsize=13)
plt.text('재산범죄', 50, '1697건 감소',fontsize=13)
plt.savefig('indecrease.png', edgecolor='black')
plt.show()