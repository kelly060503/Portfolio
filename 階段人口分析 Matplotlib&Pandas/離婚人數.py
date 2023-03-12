import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from cycler import cycler
mpl.rcParams['font.family'] = 'DFKai-SB'
mpl.rcParams["axes.prop_cycle"] = cycler(markersize=["8","8","8"],marker=["o","D","*"])
str1 = r"..\person\離婚人數.xlsx"
df = pd.read_excel(str1,header=[3])
df = df.drop(df.tail(5).index)
df = df.rename(columns={"區域別總計":"區域總計"})
fig,pt = plt.subplots(1,figsize=(12,8),constrained_layout=False)
fig.set_facecolor("#FFDDAA")
fig.suptitle("歷年離婚人口統計",fontsize=36,color="#0000AA")
cmap1 = mpl.cm.summer([ (1-0)/len(df["區域總計"]) * i for i in range(len(df["區域總計"]))])
pt.bar(df["年份"],df["區域總計"],label="總人數",color=cmap1)
pt.set_xlabel("年份",labelpad=-12,x=1.01,fontsize=22,color='#550088')
pt.set_ylabel("人數",labelpad=-16,y=1,fontsize=22,rotation=360,color='#550088')
plt.subplots_adjust(hspace=0.2)
plt.show()