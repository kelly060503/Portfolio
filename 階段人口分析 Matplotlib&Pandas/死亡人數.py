import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from cycler import cycler
mpl.rcParams['font.family'] = 'DFKai-SB'
mpl.rcParams["axes.prop_cycle"] = cycler(markersize=["8"])
str1 = r"..\person\死亡人數.xlsx"
df = pd.read_excel(str1,header=[2])
df = df.drop(df.head(1).index)
df = df.drop(df.tail(5).index)
fig,pt = plt.subplots(1,figsize=(12,8),constrained_layout=False)
fig.set_facecolor("#FFDDAA")
fig.suptitle("歷年死亡人口統計",fontsize=36,color="#0000AA")
pt.plot(df["年份"],df["死亡人數"],'o--',label="總人數",color="#5599FF")
pt.plot(df["年份"],df["男"],'X--',label="男生",color="#227700")
pt.plot(df["年份"],df["女"],'p--',label="女生",color="#C10066")
pt.set_xlabel("年份",labelpad=-12,x=1.01,fontsize=22,color='#550088')
pt.set_ylabel("人數",labelpad=-16,y=1,fontsize=22,rotation=360,color='#550088')
pt.legend(loc="upper left",fontsize=7,prop={"size":15})
plt.subplots_adjust(hspace=0.2)
plt.show()