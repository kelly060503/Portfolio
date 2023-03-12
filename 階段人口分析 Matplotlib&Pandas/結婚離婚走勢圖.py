import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from cycler import cycler
mpl.rcParams['font.family'] = 'DFKai-SB'
mpl.rcParams["axes.prop_cycle"] = cycler(markersize=["8","8","8"],marker=["o","D","*"])
str1 = r"..\person\結婚人數.xlsx"
df = pd.read_excel(str1,header=[3])
df = df.drop(df.tail(5).index)
df = df.rename(columns={"區域別總計 / 計":"區域總計"})
str1 = r"..\person\離婚人數.xlsx"
df1 = pd.read_excel(str1,header=[3])
df1 = df1.drop(df1.tail(5).index)
df1 = df1.rename(columns={"區域別總計":"區域總計"})
fig,pt = plt.subplots(1,figsize=(12,8),constrained_layout=False)
fig.set_facecolor("#FFDDAA")
fig.suptitle("歷年結婚離婚人口走勢圖",fontsize=36,color="#0000AA")
pt.stackplot(df["年份"],df["區域總計"],labels="結婚",colors={"#DB7093"})
pt.stackplot(df["年份"],df1["區域總計"],labels="離婚",colors={"#808000"})
pt.set_xlabel("年份",labelpad=-12,x=1.01,fontsize=22,color="#550088")
pt.set_ylabel("人數",labelpad=-16,y=1,fontsize=22,rotation=360,color='#550088')
pt.legend(["結婚人數","離婚人數"],loc="upper right",fontsize=7,prop={"size":15})
plt.subplots_adjust(hspace=0.2)
plt.show()