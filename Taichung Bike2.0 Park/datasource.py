import requests
town_names = {"西屯區",
              "北屯區",
              "沙鹿區",
              "清水區",
              "太平區",
              "南區",
              "西區",
              "霧峰區",
              "神岡區",
              "東勢區",
              "豐原區",
              "北區",
              "烏日區",
              "梧棲區",
              "大甲區",
              "大里區",
              "東區",
              "南屯區",
              "大安區",
              "大肚區",
              "大安區",
              "后里區",
              "石岡區",
              "大雅區",
              "龍井區",
              "潭子區",
              "新社區",
              "中區",
              "外埔區",
              "和平區",
              "士林區",
              }


def get_forcase_data(town):
    url = f"https://datacenter.taichung.gov.tw/swagger/OpenData/9af00e84-473a-4f3d-99be-b875d8e86256"
    response = requests.get(url=url)
    response.encoding = "utf-8"
    print(response)

    if response.ok:
        town_forcase = []
        print(f"{town}下載成功")
        source_data = response.json()["retVal"]
        for item in source_data:
            if item["sarea"] == town:
                town_forcase.append(
                    [item["sarea"], item["sna"], item["ar"], item["tot"]])

        if len(town_forcase) == 0:
           raise Exception(f"{town}下載失敗")
           
        return town_forcase
    else:
        raise Exception(f"{town}下載失敗")




