import requests , json
#Se ingresa la api key obtenida en https://adsnet.info
Api_key = "ApiKey"
base = "https://adsnet.info/api/?api="
Base1 = "&url="
link = input('ingresa link a acortar : ')
url_final= base + Api_key + Base1 + link
r = requests.get(url_final).json()['shortenedUrl']

print (r)
