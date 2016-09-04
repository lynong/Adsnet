import requests , json
 
Api_key = "be8ff7aaa4bbfd509e341209646e390bf846e8ef"
base = "https://adsnet.info/api/?api="
Base1 = "&url="
link = input('ingresa link a acortar : ')
url_final= base + Api_key + Base1 + link
r = requests.get(url_final).json()['shortenedUrl']

print (r)