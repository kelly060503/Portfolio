import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
mpl.rcParams['font.family'] = 'DFKai-SB'
str1 = r"..\person\出生人數-各縣市2.xlsx"
df = pd.read_excel(str1,header=[2])
df = df.drop(df.tail(5).index)
fig,pt = plt.subplots(1,figsize=(12,10),constrained_layout=True)
fig.set_facecolor("#FFDDAA")
fig.suptitle("2022年出生人口統計",fontsize=32,color="#0000AA")
area = df["地區"].iloc[1:23]
y111 = df["111年"].iloc[1:23]
cmap1 = mpl.cm.twilight([ (1-0)/len(area) * i for i in range(len(area))])
pt.pie(y111,autopct="%1.1f%%",labels=area,labeldistance=1.02,
       colors=cmap1,counterclock=True,
       textprops=dict(weight="bold",size=10,color="k"),radius=1.2,
       pctdistance=0.9,startangle=180)
pt.legend(bbox_to_anchor=(1.2, 0.5,0.1,0.5),fontsize=6,prop={"size":12})
plt.show()