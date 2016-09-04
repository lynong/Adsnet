import requests , json #Es necesario instalar el modulo request si aun no lo tienes
#Se ingresa la api key obtenida en https://adsnet.info
Api_key = "ApiKey"
base = "https://adsnet.info/api/?api="
Base1 = "&url="
#Se pide que ingrese la url a acortar
link = input('ingresa link a acortar : ')
#Se construye la url final con las bases y l Api Key
url_final= base + Api_key + Base1 + link
"""Se envia una peticion a la url final a cambio se obtiene un documento JSON y en este caso especificamos que queremos
el valor shortenedUrl que es la url ya finalmente acortada"""
r = requests.get(url_final).json()['shortenedUrl']
#Finalmente se imprime en pantalla la url ya acortada
print (r)
