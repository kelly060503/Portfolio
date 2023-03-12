import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
mpl.rcParams['font.family'] = 'DFKai-SB'
str1 = r"..\person\死亡人數-各縣市2.xlsx"
df = pd.read_excel(str1,header=[2])
df = df.drop(df.tail(5).index)
fig,pt = plt.subplots(1,figsize=(12,10),constrained_layout=True)
fig.set_facecolor("#FFDDAA")
fig.suptitle("2022年死亡人口統計",fontsize=32,color="#0000AA")
area = df["地區"].iloc[0:22]
y111 = df["111年"].iloc[0:22]
cmap1 = mpl.cm.twilight([ (1-0)/len(area) * i for i in range(len(area))])
pt.pie(y111,labels=area,autopct="%1.1f%%",labeldistance=1.02,
       colors=cmap1,counterclock=True,
       explode=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.3],
       textprops=dict(weight="bold",size=10,color="k"),radius=1,
       wedgeprops=dict(edgecolor="w",width=1,linewidth=1.5),
       pctdistance=0.7,startangle=170)
pt.legend(bbox_to_anchor=(1.2, 0.5,0.1,0.5),fontsize=6,prop={"size":12})
plt.show()
