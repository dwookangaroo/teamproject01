import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import platform
from matplotlib import font_manager, rc # Runtime Configuration
path = "c:/Windows/Fonts/malgun.ttf"
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic', size=20)
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name, size=20)
else:
    print('Unknown system... sorry~~~~')

# 파일가져오기
# criminal_percent = pd.read_csv('../csv/criminal_percent.csv', encoding='cp949')
# criminal_percent1 =pd.read_csv('../csv/criminal_percent1.csv', encoding='utf-8')
a_crime_heinous1_sub = pd.read_csv('../csv/a_crime_heinous1_sub.csv', encoding='utf-8')
a_crime_heinous2_sub = pd.read_csv('../csv/a_crime_heinous2_sub.csv', encoding='utf-8')
a_crime_heinous3_sub = pd.read_csv('../csv/a_crime_heinous3_sub.csv', encoding='utf-8')
c_crime_heinous1_sub = pd.read_csv('../csv/c_crime_heinous1_sub.csv', encoding='utf-8')
c_crime_heinous2_sub = pd.read_csv('../csv/c_crime_heinous2_sub.csv', encoding='utf-8')
c_crime_heinous3_sub = pd.read_csv('../csv/c_crime_heinous3_sub.csv', encoding='utf-8')

ratio1 = a_crime_heinous1_sub['2019'][7:]
ratio2 = c_crime_heinous1_sub['2019'][7:]
ratio3 = a_crime_heinous2_sub['2019'][5:]
ratio4 = c_crime_heinous2_sub['2019'][5:]
ratio5 = a_crime_heinous3_sub['2019'][6:]
ratio6 = c_crime_heinous3_sub['2019'][6:]


# def criminal_rate():
#     fig1, ax1 = plt.subplots(figsize=(50, 35))
#     ax2 = ax1.twinx()
#     x1 = np.arange(2013, 2020)
#     y1 = np.arange(0, 2200000, 200000)
#
#     ax1.set_xticks(x1)
#     ax1.set_xticklabels(['2013', '2014', '2015', '2016', '2017', '2018', '2019'], fontsize=40)
#     ax1.set_yticks(y1)
#     ax1.set_yticklabels(['0', '20만명', '40만명', '60만명', '80만명', '100만명', '120만명', '140만명', '160만명', '180만명', '200만명'],
#                         fontsize=40)
#
#     ax1.bar(x1 - 0.15, criminal_percent1['총범죄자'], width=0.15, color='#C0C0C0', label='총범죄자')
#     ax1.bar(x1 + 0.00, criminal_percent1['성인범'], width=0.15, color='#ADD8E6', label='성인범')
#     ax1.bar(x1 + 0.15, criminal_percent1['소년범'], width=0.15, color='#8FBC8F', label='소년범')
#
#     ax1.set_title("연도별 성인범|소년범 구성", fontsize=61, fontweight='bold', pad=50)
#     ax1.set_xlabel('[년도]', fontsize=40)
#     ax1.set_ylabel('[범죄자수]', fontsize=40)
#     ax1.legend(ncol=3, loc='upper left', fontsize='30')
#
#     y2 = np.arange(0, 110, 10)
#     ax2.set_yticks(y2)
#     ax2.set_yticklabels(['0', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'], fontsize=40)
#
#     ax2.plot(x1, criminal_percent1['성인범비율'], color='#4682B4', marker='o', markersize=15, linewidth=5,
#                      label='성인범비율')
#     ax2.plot(x1, criminal_percent1['소년범비율'], color='#2E8B57', marker='o', markersize=15, linewidth=5,
#                      label='소년범비율')
#
#     ax2.set_ylabel('[범죄자비율]', fontsize=40)
#     ax2.legend(ncol=2, loc='upper right', fontsize='30')
#
#     for i, j in zip(x1, criminal_percent1['성인범비율']):
#         if j == criminal_percent1['성인범비율'].max():
#             plt.text(i, j - 1, j, va='top', ha='center', fontsize='40', color='red', fontweight='bold')
#         elif j == criminal_percent1['성인범비율'].min():
#             plt.text(i, j - 1, j, va='top', ha='center', fontsize='40', color='blue', fontweight='bold')
#         else:
#             plt.text(i, j - 1, j, va='top', ha='center', fontsize='40')
#     for i, j in zip(x1, criminal_percent1['소년범비율']):
#         if j == criminal_percent1['소년범비율'].max():
#             plt.text(i, j + 1, j, va='bottom', ha='center', fontsize='40', color='red', fontweight='bold')
#         elif j == criminal_percent1['소년범비율'].min():
#             plt.text(i, j + 1, j, va='bottom', ha='center', fontsize='40', color='blue', fontweight='bold')
#         else:
#             plt.text(i, j + 1, j, va='bottom', ha='center', fontsize='40')
#     plt.savefig('../img/Criminal_Rate.png')
#     # plt.show()
#     return fig1
#
#
# def criminal_to_crime():
#     # 성인범죄자 중 형법범죄 발생 비율
#     import matplotlib.ticker as ticker
#
#     fig2, ax3 = plt.subplots(ncols=2, figsize=(40, 20))
#     x1 = np.arange(2013, 2020)
#     mean_sales1 = int(np.mean(criminal_percent1['성인범죄비율']))
#     mean_sales2 = int(np.mean(criminal_percent1['소년범죄비율']))
#
#     ax3[0].set_xticks(x1)
#     ax3[0].set_xticklabels(['2013', '2014', '2015', '2016', '2017', '2018', '2019'], fontsize=30)
#     ax3[0].set_ylim([0, 100])
#     ax3[0].yaxis.set_major_locator(ticker.MultipleLocator(10))
#     ax3[0].plot(x1, criminal_percent1['성인범죄비율'], color='#4682B4', marker='o', markersize=17, linewidth=6, label='성인범죄비율')
#     ax3[0].set_title("성인범죄자 대비 범죄건수 비율", fontsize=55, fontweight='bold', pad=50)
#     ax3[0].set_xlabel('[년도]', fontsize=30)
#     ax3[0].set_ylabel('[범죄발생비율]', fontsize=30)
#     ax3[0].axhline(mean_sales1, label='평균', linewidth=4, color='#CD5C5C', alpha=0.5)
#     ax3[0].grid(alpha=0.5, axis='y')
#     for i, j in zip(x1, criminal_percent1['성인범죄비율']):
#         if j == criminal_percent1['성인범죄비율'].max():
#             ax3[0].text(i, j + 3, j, va='top', ha='center', fontsize='30', color='red', fontweight='bold')
#         elif j == criminal_percent1['성인범죄비율'].min():
#             ax3[0].text(i, j - 1, j, va='top', ha='left', fontsize='30', color='blue', fontweight='bold')
#         else:
#             ax3[0].text(i - 0.1, j + 1, j, va='bottom', ha='left', fontsize='30')
#     ax3[0].legend()
#     # plt.tight_layout()
#     ax3[1].set_xticks(x1)
#     ax3[1].set_xticklabels(['2013', '2014', '2015', '2016', '2017', '2018', '2019'], fontsize=30)
#     ax3[1].set_ylim([10, 110])
#     ax3[1].yaxis.set_major_locator(ticker.MultipleLocator(10))
#     ax3[1].plot(x1, criminal_percent1['소년범죄비율'], color='#2E8B57', marker='o', markersize=17, linewidth=6, label='소년범죄비율')
#     ax3[1].set_title("소년범죄자 대비 범죄건수 비율",  fontsize=55, fontweight='bold', pad=50)
#     ax3[1].set_xlabel('[년도]', fontsize=30)
#     ax3[1].set_ylabel('[범죄발생비율]', fontsize=30)
#     ax3[1].axhline(mean_sales2, label='평균', linewidth=4, color='#CD5C5C', alpha=0.5)
#     ax3[1].grid(alpha=0.5, axis='y')
#     ax3[1].legend()
#     for i, j in zip(x1, criminal_percent1['소년범죄비율']):
#         if j == criminal_percent1['소년범죄비율'].max():
#             ax3[1].text(i, j + 1, j, va='bottom', ha='center', fontsize='30', color='red', fontweight='bold')
#         elif j == criminal_percent1['소년범죄비율'].min():
#             ax3[1].text(i, j + 1, j, va='bottom', ha='center', fontsize='30', color='blue', fontweight='bold')
#         else:
#             ax3[1].text(i, j - 1, j, va='top', ha='center', fontsize='30')
#
#     plt.savefig('../img/Criminal_To_Crime.png')
#     # plt.show()
#     return fig2
#
#
# def specific_crime():
#     # 형법범죄 중 재산, 흉악, 폭력범죄 발생 비율
#     # 형법범죄 중 재산, 흉악, 폭력범죄 발생 비율
#     fig3, ax4 = plt.subplots(figsize=(35, 25))
#     x1 = np.arange(2013, 2020)
#     y4 = np.arange(0, 110, 10)
#     ax4.set_ylim([2012, 2020])
#     # ax4.set_yticklabels(['2012', '2013','2014','2015','2016','2017','2018','2019','2020'],fontsize=30)
#     ax4.barh(x1 + 0.2, criminal_percent['성인재산범죄비율'], label='성인재산범죄비율', color='#4169E1', height=0.4)
#     ax4.barh(x1 + 0.2, criminal_percent['성인흉악범죄비율'], left=criminal_percent['성인재산범죄비율'], label='성인흉악범죄비율',
#              color='#6495ED', height=0.4)
#     ax4.barh(x1 + 0.2, criminal_percent['성인폭력범죄비율'], left=criminal_percent['성인재산범죄비율'] + criminal_percent['성인흉악범죄비율'],
#              label='성인폭력범죄비율', color='#87CEFA', height=0.4)
#     ax4.barh(x1 + 0.2, criminal_percent['성인기타범죄율'],
#              left=criminal_percent['성인재산범죄비율'] + criminal_percent['성인흉악범죄비율'] + criminal_percent['성인폭력범죄비율'],
#              label='성인기타범죄비율', color='#add8e6', height=0.4)
#     ax4.set_xticks(y4)
#     ax4.set_xticklabels(['0', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'], fontsize=30)
#     ax4.set_title("연도별 성인 및 소년 특정범죄비율 비교", fontsize=35, fontweight='bold')
#     ax4.set_xlabel('[특정범죄비율]', fontsize=30)
#     ax4.set_ylabel('[년도]', fontsize=30)
#     ax4.grid(alpha=0.5)
#     ax4.legend(ncol=3, loc='upper left', fontsize='20')
#
#     ax5 = ax4.twiny()
#     ax5.barh(x1 - 0.2, criminal_percent['소년재산범죄비율'], label='소년재산범죄비율', color='#2E8B57', height=0.4)
#     ax5.barh(x1 - 0.2, criminal_percent['소년흉악범죄비율'], left=criminal_percent['소년재산범죄비율'], label='소년흉악범죄비율',
#              color='#3CB371', height=0.4)
#     ax5.barh(x1 - 0.2, criminal_percent['소년폭력범죄비율'], left=criminal_percent['소년재산범죄비율'] + criminal_percent['소년흉악범죄비율'],
#              label='소년폭력범죄비율', color='#8FBC8F', height=0.4)
#     ax5.barh(x1 - 0.2, criminal_percent['소년기타범죄율'],
#              left=criminal_percent['소년재산범죄비율'] + criminal_percent['소년흉악범죄비율'] + criminal_percent['소년폭력범죄비율'],
#              label='소년기타범죄비율', color='#66cdaa', height=0.4)
#     ax5.axes.xaxis.set_visible(False)
#     ax5.legend(ncol=3, loc='upper right', fontsize='20')
#     # plt.savefig('data/graph.png')
#
#     for i, j in enumerate(np.arange(2012, 2019)):
#         str_val1 = criminal_percent['성인재산범죄비율'][i]
#         str_val2 = criminal_percent['성인흉악범죄비율'][i]
#         str_val3 = criminal_percent['성인폭력범죄비율'][i]
#         str_val4 = criminal_percent['성인기타범죄율'][i]
#
#         if str_val1 == criminal_percent['성인재산범죄비율'].max():
#             plt.text(str_val1 / 2, j + 1.1, str_val1, fontsize='28', color='red', fontweight='bold')
#         elif str_val1 == criminal_percent['성인재산범죄비율'].min():
#             plt.text(str_val1 / 2, j + 1.1, str_val1, fontsize='28', color='yellow', fontweight='bold')
#         else:
#             plt.text(str_val1 / 2, j + 1.1, str_val1, fontsize='28')
#
#         if str_val2 == criminal_percent['성인흉악범죄비율'].max():
#             plt.text(str_val1 + str_val2 / 2, j + 1.1, str_val2, fontsize='28', color='red', fontweight='bold')
#         elif str_val2 == criminal_percent['성인흉악범죄비율'].min():
#             plt.text(str_val1 + str_val2 / 2, j + 1.1, str_val2, fontsize='28', color='yellow', fontweight='bold')
#         else:
#             plt.text(str_val1 + str_val2 / 2, j + 1.1, str_val2, fontsize='28')
#
#         if str_val3 == criminal_percent['성인폭력범죄비율'].max():
#             plt.text(str_val1 + str_val2 + str_val3 / 2, j + 1.1, str_val3, fontsize='28', color='red',
#                      fontweight='bold')
#         elif str_val3 == criminal_percent['성인폭력범죄비율'].min():
#             plt.text(str_val1 + str_val2 + str_val3 / 2, j + 1.1, str_val3, fontsize='28', color='yellow',
#                      fontweight='bold')
#         else:
#             plt.text(str_val1 + str_val2 + str_val3 / 2, j + 1.1, str_val3, fontsize='28')
#
#         plt.text(str_val1 + str_val2 + str_val3 + str_val4 / 2, j + 1.1, str_val4, fontsize='28')
#
#     for i, j in enumerate(np.arange(2012, 2019)):
#         str_val1 = criminal_percent['소년재산범죄비율'][i]
#         str_val2 = criminal_percent['소년흉악범죄비율'][i]
#         str_val3 = criminal_percent['소년폭력범죄비율'][i]
#         str_val4 = criminal_percent['소년기타범죄율'][i]
#
#         if str_val1 == criminal_percent['소년재산범죄비율'].max():
#             plt.text(str_val1 / 2, j + 0.75, str_val1, fontsize='28', color='red', fontweight='bold')
#         elif str_val1 == criminal_percent['소년재산범죄비율'].min():
#             plt.text(str_val1 / 2, j + 0.75, str_val1, fontsize='28', color='yellow', fontweight='bold')
#         else:
#             plt.text(str_val1 / 2, j + 0.75, str_val1, fontsize='28')
#
#         if str_val2 == criminal_percent['소년흉악범죄비율'].max():
#             plt.text(str_val1 + str_val2 / 2, j + 0.75, str_val2, fontsize='28', color='red', fontweight='bold')
#         elif str_val2 == criminal_percent['소년흉악범죄비율'].min():
#             plt.text(str_val1 + str_val2 / 2, j + 0.75, str_val2, fontsize='28', color='yellow', fontweight='bold')
#         else:
#             plt.text(str_val1 + str_val2 / 2, j + 0.75, str_val2, fontsize='28')
#
#         if str_val3 == criminal_percent['소년폭력범죄비율'].max():
#             plt.text(str_val1 + str_val2 + str_val3 / 2, j + 0.75, str_val3, fontsize='28', color='red',
#                      fontweight='bold')
#         elif str_val3 == criminal_percent['소년폭력범죄비율'].min():
#             plt.text(str_val1 + str_val2 + str_val3 / 2, j + +0.75, str_val3, fontsize='28', color='yellow',
#                      fontweight='bold')
#         else:
#             plt.text(str_val1 + str_val2 + str_val3 / 2, j + 0.75, str_val3, fontsize='28')
#
#         plt.text(str_val1 + str_val2 + str_val3 + str_val4 / 2, j + 0.75, str_val4, fontsize='28')
#
#         plt.savefig('../img/specific_prime.png')
#
#     # plt.show()
#     return fig3
#
#
# def criminal_to_crime1():
#     plt.figure()
#     plt.figure(figsize=(20, 10))
#     x1 = np.arange(2013, 2020)
#     mean_sales1 = int(np.mean(criminal_percent1['성인범죄비율']))
#     mean_sales2 = int(np.mean(criminal_percent1['소년범죄비율']))
#     plt.plot(x1, criminal_percent1['성인범죄비율'], color='#4682B4', marker='o', markersize=17, linewidth=6, label='성인범죄비율')
#     plt.plot(x1, criminal_percent1['소년범죄비율'], color='#2E8B57', marker='o', markersize=17, linewidth=6, label='소년범죄비율')
#     plt.axhline(mean_sales1, label='평균', linewidth=4, color='#4169E1', alpha=0.5)
#     plt.axhline(mean_sales2, label='평균', linewidth=4, color='#8FBC8F', alpha=0.5)
#     plt.xlabel('년도', labelpad=20)
#     plt.ylabel('범죄건수비율', labelpad=20)
#     plt.title("범죄자 대비 범죄건수 비율", fontsize=25, fontweight='bold', pad=20)
#     # plt.legend(ncol=3)
#     # CD5C5C 4169E1
#     for i, j in zip(x1, criminal_percent1['성인범죄비율']):
#         if j == criminal_percent1['성인범죄비율'].max():
#             plt.text(i, j + 1, j, va='bottom', ha='center', fontsize='20', color='red', fontweight='bold')
#         elif j == criminal_percent1['성인범죄비율'].min():
#             plt.text(i - 0.1, j + 1, j, va='bottom', ha='left', fontsize='20', color='blue', fontweight='bold')
#         else:
#             plt.text(i - 0.1, j + 1, j, va='bottom', ha='left', fontsize='20')
#
#     for i, j in zip(x1, criminal_percent1['소년범죄비율']):
#         if j == criminal_percent1['소년범죄비율'].max():
#             plt.text(i + 0.05, j - 0.5, j, va='bottom', ha='left', fontsize='20', color='red', fontweight='bold')
#         elif j == criminal_percent1['소년범죄비율'].min():
#             plt.text(i, j + 1, j, va='bottom', ha='center', fontsize='20', color='blue', fontweight='bold')
#         else:
#             plt.text(i, j - 2, j, va='top', ha='center', fontsize='20')
#
#     plt.savefig('../img/criminal_to_crime1.png')
#     # plt.show()
#
#
# def a_criminal_to_crime():
#     plt.figure()
#     plt.figure(figsize=(20, 10))
#     x1 = np.arange(2013, 2020)
#     mean_sales1 = int(np.mean(criminal_percent1['성인범죄비율']))
#     plt.ylim(30, 100)
#     # mean_sales2 = int(np.mean(criminal_percent['소년범죄비율']))
#     plt.plot(x1, criminal_percent1['성인범죄비율'], color='#4682B4', marker='o', markersize=17, linewidth=6, label='성인범죄비율')
#     # plt.plot(x1, criminal_percent['소년범죄비율'], color='#2E8B57',marker='o', markersize=17,linewidth=6,label='소년범죄비율')
#     plt.axhline(mean_sales1, label='평균', linewidth=4, color='#4169E1', alpha=0.5)
#     # plt.axhline(mean_sales2,label='평균',linewidth=4, color='#8FBC8F',alpha=0.5)
#     plt.xlabel('년도', labelpad=20)
#     plt.ylabel('범죄건수비율', labelpad=20)
#     plt.title("성인범 대비 범죄건수 비율", fontsize=25, fontweight='bold', pad=20)
#     # plt.legend(ncol=3)
#     # CD5C5C 4169E1
#     for i, j in zip(x1, criminal_percent1['성인범죄비율']):
#         if j == criminal_percent1['성인범죄비율'].max():
#             plt.text(i, j + 1, j, va='bottom', ha='center', fontsize='20', color='red', fontweight='bold')
#         elif j == criminal_percent1['성인범죄비율'].min():
#             plt.text(i - 0.1, j + 1, j, va='bottom', ha='left', fontsize='20', color='blue', fontweight='bold')
#         else:
#             plt.text(i - 0.1, j + 1, j, va='bottom', ha='left', fontsize='20')
#     plt.savefig('../img/a_criminal_to_crime.png')
#
#
# def c_criminal_to_crime():
#     plt.figure()
#     plt.figure(figsize=(20, 10))
#     x1 = np.arange(2013, 2020)
#     # mean_sales1 = int(np.mean(criminal_percent['성인범죄비율']))
#     plt.ylim(50, 110)
#     mean_sales2 = int(np.mean(criminal_percent1['소년범죄비율']))
#     # plt.plot(x1, criminal_percent['성인범죄비율'], color='#4682B4',marker='o', markersize=17,linewidth=6,label='성인범죄비율')
#     plt.plot(x1, criminal_percent1['소년범죄비율'], color='#2E8B57', marker='o', markersize=17, linewidth=6, label='소년범죄비율')
#     # plt.axhline(mean_sales1,label='평균',linewidth=4, color='#4169E1',alpha=0.5)
#     plt.axhline(mean_sales2, label='평균', linewidth=4, color='#8FBC8F', alpha=0.5)
#     plt.xlabel('년도', labelpad=20)
#     plt.ylabel('범죄건수비율', labelpad=20)
#     plt.title("소년범 대비 범죄건수 비율", fontsize=25, fontweight='bold', pad=20)
#     # plt.legend(ncol=3)
#     # CD5C5C 4169E1
#     for i, j in zip(x1, criminal_percent1['소년범죄비율']):
#         if j == criminal_percent1['소년범죄비율'].max():
#             plt.text(i + 0.05, j - 0.5, j, va='bottom', ha='left', fontsize='20', color='red', fontweight='bold')
#         elif j == criminal_percent1['소년범죄비율'].min():
#             plt.text(i, j + 1, j, va='bottom', ha='center', fontsize='20', color='blue', fontweight='bold')
#         else:
#             plt.text(i, j - 2, j, va='top', ha='center', fontsize='20')
#     plt.savefig('../img/c_criminal_to_crime.png')


def a_crime_heinous1():
    plt.figure()
    plt.figure(figsize=(10, 10))
    labels = ['절도', '장물', '사기', '횡령', '배임', '손괴']
    colors = ['#91d8fa', '#aab9ff', '#82b3ed', '#d2e1ff', '#b4b4ff', '#b4e5ff']
    explode = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
    plt.title("2019년 성인범 재산범죄", fontsize=25, fontweight='bold', pad=20)
    plt.pie(ratio1, labels=labels, autopct='%.2f%%', counterclock=False, explode=explode, colors=colors)
    plt.savefig('../img/a_crime_heinous1.png')


def a_crime_heinous2():
    plt.figure()
    plt.figure(figsize=(10, 10))
    labels = ['살인', '강도', '방화', '성폭력']
    colors = ['#ffd9e4', '#ffb2af', '#ffb4ff', '#e08eb1']
    explode = [0.05, 0.05, 0.05, 0.05]
    plt.title("2019년 성인범 흉악범죄", fontsize=25, fontweight='bold', pad=20)
    plt.pie(ratio3, labels=labels, autopct='%.2f%%', counterclock=False, explode=explode, colors=colors)
    # plt.show()
    plt.savefig('../img/a_crime_heinous2.png')


def a_crime_heinous3():
    plt.figure()
    plt.figure(figsize=(10, 10))
    labels = ['폭행', '상해', '협박', '공갈', '기타폭력']
    colors = ['#ff9696', '#cd7a7a', '#cbacac', '#ff7878', '#ff4646']
    explode = [0.05, 0.05, 0.05, 0.05, 0.05]
    plt.title("2019년 성인범 폭력범죄", fontsize=25, fontweight='bold', pad=20)
    plt.pie(ratio5, labels=labels, autopct='%.2f%%', counterclock=False, explode=explode, colors=colors)
    # plt.show()
    plt.savefig('../img/a_crime_heinous3.png')


def c_crime_heinous1():
    plt.figure()
    plt.figure(figsize=(10, 10))
    labels = ['절도', '장물', '사기', '횡령', '배임', '손괴']
    colors = ['#70d2b4', '#dcffdc', '#78e6e6', '#b4f0b4', '#87c6c8', '#73eaa8']
    explode = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
    plt.title("2019년 소년범 재산범죄", fontsize=25, fontweight='bold', pad=20)
    plt.pie(ratio2, labels=labels, autopct='%.2f%%', counterclock=False, explode=explode, colors=colors)
    # plt.show()
    plt.savefig('../img/c_crime_heinous1.png')


def c_crime_heinous2():
    plt.figure()
    plt.figure(figsize=(10, 10))
    labels = ['살인', '강도', '방화', '성폭력']
    colors = ['#d29953', '#ffc800', '#ffaf00', '#fde6be']
    explode = [0.05, 0.05, 0.05, 0.05]
    plt.title("2019년 소년범 흉악범죄", fontsize=25, fontweight='bold', pad=20)
    plt.pie(ratio4, labels=labels, autopct='%.2f%%', counterclock=False, explode=explode, colors=colors)
    # plt.show()
    plt.savefig('../img/c_crime_heinous2.png')


def c_crime_heinous3():
    plt.figure()
    plt.figure(figsize=(10, 10))
    labels = ['폭행', '상해', '협박', '공갈', '기타폭력']
    colors = ['#ff9dff', '#c964e2', '#bc55ef', '#b246b2', '#a014a0']
    explode = [0.05, 0.05, 0.05, 0.05, 0.05]
    plt.title("2019년 소년범 폭력범죄", fontsize=25, fontweight='bold', pad=20)
    plt.pie(ratio6, labels=labels, autopct='%.2f%%', counterclock=False, explode=explode, colors=colors)
    # plt.show()
    plt.savefig('../img/c_crime_heinous3.png')
# criminal_rate()
# criminal_to_crime()
# specific_crime()
# criminal_to_crime1()
# a_criminal_to_crime()
# c_criminal_to_crime()
a_crime_heinous1()
a_crime_heinous2()
a_crime_heinous3()
c_crime_heinous1()
c_crime_heinous2()
c_crime_heinous3()
