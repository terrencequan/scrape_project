from urllib.request import urlopen

url  = "https://s.taobao.com/search?q=Iphone&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=&ie=utf8&initiative_id=tbindexz_20170306&style=list"

response = urlopen(url)
data = response.read()
text = data.decode("utf-8")
print(text)
