import csv
from cycler import cycler
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
mpl.rcParams['font.family'] = 'DFKai-SB'
mpl.rcParams["axes.prop_cycle"] = cycler(marker=["*"],markersize="9")
with open(r'..\tour\表2-2-歷年中華民國國民出國目的地人次統計.csv',encoding="utf-8") as csvfile:
    data = csv.reader(csvfile)
    list1 = list(data)
list1_data = list(zip(*list1[:]))
years = list1_data[0][1:]    #每年資料
area_list = list1[1:]  #地區
area_list = list(zip(*area_list[:]))
香港 = [int("".join(list(item.split(",")))) for item in area_list[1]]
澳門 = [int("".join(list(item.split(",")))) for item in area_list[2]]
大陸 = [int("".join(list(item.split(",")))) for item in area_list[3]]
日本 = [int("".join(list(item.split(",")))) for item in area_list[4]]
韓國 = [int("".join(list(item.split(",")))) for item in area_list[5]]
新加坡 = [int("".join(list(item.split(",")))) for item in area_list[6]]
馬來西亞 = [int("".join(list(item.split(",")))) for item in area_list[7]]
泰國 = [int("".join(list(item.split(",")))) for item in area_list[8]]
菲律賓 = [int("".join(list(item.split(",")))) for item in area_list[9]]
印尼 = [int("".join(list(item.split(",")))) for item in area_list[10]]
汶萊 = [int("".join(list(item.split(",")))) for item in area_list[11]]
越南 = [int("".join(list(item.split(",")))) for item in area_list[12]]
緬甸 = [int("".join(list(item.split(",")))) for item in area_list[13]]
柬埔寨 = [int("".join(list(item.split(",")))) for item in area_list[14]]
阿拉伯 = [int("".join(list(item.split(",")))) for item in area_list[15]]
土耳其 = [int("".join(list(item.split(",")))) for item in area_list[16]]
其他地區 = [int("".join(list(item.split(",")))) for item in area_list[17]]
fig,(ax,pt) = plt.subplots(2,1,figsize=(10,8),constrained_layout=False)
fig.set_facecolor("#CCEEFF")
fig.suptitle("國民旅遊亞洲地區人次統計",fontsize=30,color="#CC0000")
str1 = r'..\tour\表2-2-歷年中華民國國民出國目的地人次統計.xlsx'
df = pd.read_excel(str1)
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
df['日期'] = df['日期'].apply(lambda x: x.split("年"))
df['日期'] = df['日期'].apply(lambda x: x[1])
x = df['日期']
y = df.iloc[:,1:]
width = 0.7
ax.bar(x, y['香港'],width,label='香港',color="purple")
ax.bar(x, y['澳門'],width,bottom=y['香港'],label='澳門',color="salmon")
ax.bar(x, y['大陸'],width,bottom=y['香港']+y['澳門'],label='大陸',color="orange")
ax.bar(x, y['日本'],width,bottom=y['香港']+y['澳門']+y['大陸'],label='日本',color="cornflowerblue")
ax.bar(x, y['韓國'],width,bottom=y['香港']+y['澳門']+y['大陸']+y['日本'],label='韓國',color="tan")
ax.bar(x, y['新加坡'],width,bottom=y['香港']+y['澳門']+y['大陸']+y['日本']+y['韓國'],label='新加坡',color="violet")
ax.bar(x, y['馬來西亞'],width,bottom=y['香港']+y['澳門']+y['大陸']+y['日本']+y['韓國']+y['新加坡'],label='馬來西亞',color="turquoise")
ax.bar(x, y['泰國'],width,bottom=y['香港']+y['澳門']+y['大陸']+y['日本']+y['韓國']+y['新加坡']+y['馬來西亞'],label='泰國',color="slategray")
ax.bar(x, y['菲律賓'],width,bottom=y['香港']+y['澳門']+y['大陸']+y['日本']+y['韓國']+y['新加坡']+y['馬來西亞']+y['泰國'],label='菲律賓',color="yellow")
ax.bar(x, y['印尼'],width,bottom=y['香港']+y['澳門']+y['大陸']+y['日本']+y['韓國']+y['新加坡']+y['馬來西亞']+y['泰國']+y['菲律賓'],label='印尼',color="indianred")
ax.bar(x, y['汶萊'],width,bottom=y['香港']+y['澳門']+y['大陸']+y['日本']+y['韓國']+y['新加坡']+y['馬來西亞']+y['泰國']+y['菲律賓']+y['印尼'],label='汶萊',color="khaki")
ax.bar(x, y['越南'],width,bottom=y['香港']+y['澳門']+y['大陸']+y['日本']+y['韓國']+y['新加坡']+y['馬來西亞']+y['泰國']+y['菲律賓']+y['印尼']+y['汶萊'],label='越南',color="olivedrab")
ax.bar(x, y['緬甸'],width,bottom=y['香港']+y['澳門']+y['大陸']+y['日本']+y['韓國']+y['新加坡']+y['馬來西亞']+y['泰國']+y['菲律賓']+y['印尼']+y['汶萊']+y['越南'],label='緬甸',color="navy")
ax.bar(x, y['柬埔寨'],width,bottom=y['香港']+y['澳門']+y['大陸']+y['日本']+y['韓國']+y['新加坡']+y['馬來西亞']+y['泰國']+y['菲律賓']+y['印尼']+y['汶萊']+y['越南']+y['緬甸'],label='柬埔寨',color="peru")
ax.bar(x, y['阿拉伯聯合大公國'],width,bottom=y['香港']+y['澳門']+y['大陸']+y['日本']+y['韓國']+y['新加坡']+y['馬來西亞']+y['泰國']+y['菲律賓']+y['印尼']+y['汶萊']+y['越南']+y['緬甸']+y['柬埔寨'],label='阿拉伯聯合大公國',color="plum")
ax.bar(x, y['土耳其'],width,bottom=y['香港']+y['澳門']+y['大陸']+y['日本']+y['韓國']+y['新加坡']+y['馬來西亞']+y['泰國']+y['菲律賓']+y['印尼']+y['汶萊']+y['越南']+y['緬甸']+y['柬埔寨']+y['阿拉伯聯合大公國'],label='土耳其',color="seagreen")
ax.bar(x, y['其他地區'],width,bottom=y['香港']+y['澳門']+y['大陸']+y['日本']+y['韓國']+y['新加坡']+y['馬來西亞']+y['泰國']+y['菲律賓']+y['印尼']+y['汶萊']+y['越南']+y['緬甸']+y['柬埔寨']+y['阿拉伯聯合大公國']+y['土耳其'],label='其他地區',color="cyan")
ax.legend(labelcolor='k',facecolor='w',fontsize=6.8)
ax.set_xlabel("月份",labelpad=-12,x=1,fontsize=16,color='#0000AA')
ax.set_ylabel("人數(千萬)",labelpad=5,y=1.05,fontsize=16,rotation=360,color='#0000AA')

pt.plot(years,香港,label="香港",color="purple")
pt.plot(years,澳門,label="澳門",color="salmon")
pt.plot(years,大陸,label="大陸",color="orange")
pt.plot(years,日本,label="日本",color="cornflowerblue")
pt.plot(years,韓國,label="韓國",color="tan")
pt.plot(years,新加坡,label="新加坡",color="violet")
pt.plot(years,馬來西亞,label="馬來西亞",color="turquoise")
pt.plot(years,泰國,label="泰國",color="slategray")
pt.plot(years,菲律賓,label="菲律賓",color="yellow")
pt.plot(years,印尼,label="印尼",color="indianred")
pt.plot(years,汶萊,label="汶萊",color="khaki")
pt.plot(years,越南,label="越南",color="olivedrab")
pt.plot(years,緬甸,label="緬甸",color="navy")
pt.plot(years,柬埔寨,label="柬埔寨",color="peru")
pt.plot(years,阿拉伯,label="阿拉伯聯合大公國",color="plum")
pt.plot(years,土耳其,label="土耳其",color="seagreen")
pt.plot(years,其他地區,label="其他地區",color="cyan")
pt.legend(loc="upper right",fontsize=6.8)  #圖例位置
pt.set_xlabel("月份",labelpad=-12,x=1.02,fontsize=16,color='#0000AA')
pt.set_ylabel("人數(百萬)",labelpad=8,y=1.05,fontsize=16,rotation=360,color='#0000AA')
pt.set_facecolor("white")
plt.subplots_adjust(hspace=0.2)
plt.show()

