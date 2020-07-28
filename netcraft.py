import requests
import re
import pandas

dominio = input('Domain: ')

sessionobject = requests.Session()
request = sessionobject.get('https://sitereport.netcraft.com/?url=' + dominio, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'})

results = pandas.read_html(request.text)

for table in results:
	table.to_csv('all_results.csv', mode='a+', header=True)

print('¡Datos guardados!')