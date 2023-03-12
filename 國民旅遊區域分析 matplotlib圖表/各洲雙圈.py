import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
mpl.rcParams['font.family'] = 'DFKai-SB'
#五大洲
str1 = r'..\tour\歷年中華民國國民出國人次統計1.xlsx'
df = pd.read_excel(str1)
df = df.rename(columns={"亞洲合計 Total":"亞洲",
                  "美洲合計 Total":"美洲",
                  "歐洲合計 Total":"歐洲",
                  "大洋洲合計 Total":"大洋洲",
                  "非洲合計 Total":"非洲",
                  "其他\n Others":"其他",
                  "總計\n Grand Total":"總計"})
df["年份"] = df["年份"].apply(lambda x: x.split("年"))
df["年份"] = df["年份"].apply(lambda x: x[1])
years = df["年份"]
df.index = df["年份"]
df = df.T
data = df["2022"][1:6]
area = df.index[1:6]
fig,(pe1,pe) = plt.subplots(1,2,figsize=(12,8),constrained_layout=True)
fig.set_facecolor("#CCEEFF")
fig.suptitle("2022年國民旅遊地區統計",fontsize=30,color="#CC0000")
cmap1 = mpl.cm.Accent([(1-0)/(len(area)) * i for i in range(len(area)) ])
pe1.pie(data,explode=[0.03,0.03,0.04,0.08,0.35],autopct="%1.1f%%",
        labels=area,colors=cmap1,labeldistance=0.8,
        textprops=dict(weight="bold",size=12,color="k"))
pe1.legend(bbox_to_anchor=(1, 0.7,0.1,0.5))
pe1.set_facecolor("white")

#雙層圈
df = pd.read_excel(str1)
df = df.rename(columns={"亞洲合計 Total":"亞洲"})
df["年份"] = df["年份"].apply(lambda x: x.split("年"))
df["年份"] = df["年份"].apply(lambda x: x[1])
years = df["年份"]
df.index = df["年份"]
df = df.T
data = df["2022"][1:2]
area = df.index[1:2]
spring = cm.get_cmap("Accent",5)
pe.pie(data,labels=area,labeldistance=-0.1,colors=spring(range(5)),radius=1,wedgeprops={'linewidth':2,'edgecolor':'w','width':1})
pe.set_facecolor("white")
#外圓
str2 = r"..\tour\表2-2-歷年中華民國國民出國目的地人次統計.xlsx"
df = pd.read_excel(str2)
df = df.rename(columns={"香港\nHong Kong":"香港",
                         "澳門 Macao":"澳門",
                         "大陸 Mainland China":"大陸",
                         "日本 \nJapan":"日本",
                         "韓國 Korea":"韓國",
                         "新加坡 Singapore":"新加坡",
                         "馬來西亞 Malaysia":"馬來西亞",
                         "泰國 Thailand":"泰國",
                         "菲律賓 Philippines":"菲律賓",
                         "印尼 Indonesia":"印尼",
                         "汶淶 Brunei":"汶萊",
                         "越南 Vietnam":"越南",
                         "緬甸 Myanmar":"緬甸",
                         "柬埔寨 Cambodia":"柬埔寨",
                         "阿拉伯聯合大公國 United Arab Emirates":"阿拉伯聯合大公國",
                         "土耳其 Turkey":"土耳其",
                         "亞洲其他地區 Others":"其他地區"})
df["日期"] = df["日期"].apply(lambda x: x.split("年"))
df["日期"] = df["日期"].apply(lambda x: x[1])
years = df["日期"]
df.index = df["日期"]
df = df.T
area = df.index[1:-1]
data = df["2022"][1:-1]
cmap1 = mpl.cm.twilight_shifted([(1-0)/(len(area)) * i for i in range(len(area)) ])
pe.pie(data,autopct="%1.1f%%",labels=area,labeldistance=0.68,
       colors=cmap1,counterclock=True,
       textprops=dict(weight="bold",size=8,color="r"),radius=1.5,
       wedgeprops={'linewidth':2,'edgecolor':'w','width':1.1},
       pctdistance=0.5,startangle=230)
pe.legend(bbox_to_anchor=(1.4, 0.8,0.1,0.5))
plt.show()
