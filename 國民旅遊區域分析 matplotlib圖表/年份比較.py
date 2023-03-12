import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
with open(r'..\tour\表2-2-歷年中華民國國民出國目的地人次統計.csv',encoding="utf-8") as csvfile:
    data = csv.reader(csvfile)
    list1 = list(data)
mpl.rcParams['font.family']='DFKai-SB'
mpl.rcParams["axes.prop_cycle"] = cycler(color=["seagreen"])
list1_data = list(zip(*list1[:]))      #分地區
years = list1_data[0][1:]
year = years[:]                        #每年資料
years = years[::-1]                    #年份反向
num_str = ["".join(list(list1[j][-1].split(","))) for j in range(1,len(list1)) ]
num_int = [int(x) for x in num_str ]   #每年數據
num_int1 = num_int[::-1]               #數據反向
cmap1 = mpl.cm.winter([ (1-0)/len(years) * i  for i in range(len(years)) ])
fig,(pt,pt2) = plt.subplots(2,1,figsize=(12,6),constrained_layout=False)
fig.set_facecolor("#CCEEFF")
pt.barh(years,num_int1,color=cmap1)
pt.set_title("歷年國民旅遊亞洲地區人次統計",fontsize=30,color="#CC0000")
pt.set_xlabel('人數\n(千萬)',color='#0000AA',fontsize=16,labelpad=-30,x=1.03)
pt.set_ylabel('年份',color='#0000AA', fontsize=16,labelpad=-10,y=1,rotation=360)
pt.set_facecolor("w")
pt2.set_xlabel("月份",labelpad=-12,x=1,fontsize=16,color='#0000AA')
pt2.set_ylabel("人數",labelpad=0,y=1,fontsize=16,rotation=360,color='#0000AA')
pt2.step(year,num_int,label="歷年人數")
pt2.legend()
plt.subplots_adjust(hspace=0.4)   #調整模塊布局
plt.show()