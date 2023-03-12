import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from cycler import cycler
mpl.rcParams['font.family'] = 'DFKai-SB'
mpl.rcParams["axes.prop_cycle"] = cycler(markersize=["8","8","8"],marker=["o","D","*"])
str1 = r"..\person\出生人數.xlsx"
df = pd.read_excel(str1,header=[2])
df = df.drop(df.head(11).index)
df = df.drop(df.tail(5).index)
str1 = r"..\person\死亡人數.xlsx"
df1 = pd.read_excel(str1,header=[2])
df1 = df1.drop(df1.head(11).index)
df1 = df1.drop(df1.tail(5).index)
fig,pt = plt.subplots(1,figsize=(12,8),constrained_layout=False)
fig.set_facecolor("#FFDDAA")
fig.suptitle("歷年出生死亡人口走勢圖",fontsize=36,color="#0000AA")
pt.step(df["年份"],df["出生人數(人)"],label="出生人數",color="#DB7093")
plt.plot(df["年份"],df["出生人數(人)"],'o--', color='grey',alpha=0.3)
pt.step(df1["年份"],df1["死亡人數"],label="死亡人數",color="#808000")
plt.plot(df1["年份"],df1["死亡人數"],'o--', color='grey',alpha=0.3)
pt.set_xlabel("年份",labelpad=-12,x=1.01,fontsize=22,color='#550088')
pt.set_ylabel("人數",labelpad=-16,y=1,fontsize=22,rotation=360,color='#550088')
pt.legend(loc="upper right",fontsize=7,prop={"size":15})
plt.subplots_adjust(hspace=0.2)
plt.show()