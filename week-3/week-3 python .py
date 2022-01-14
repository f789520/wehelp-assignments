import urllib.request as request
import json
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json" 
with request.urlopen(src) as response:
  data = json.load(response)
rawdata = data["result"]["results"] 
with open("week3-data.csv", "w", encoding="utf_8_sig") as file:
  
  for view,address,long,lat,pic in zip(rawdata,rawdata,rawdata,rawdata,rawdata): 
    a=pic["file"]
    b="jpg"
    file.write(view["stitle"]+","+address["address"][5:8]+","+long["longitude"]+","+lat["latitude"]+","+a[:a.casefold().index(b)]+"jpg"+"\n") #寫入的時候正确的应该用’+'连接，不然會報錯 TextIOWrapper.write() takes exactly one argument
