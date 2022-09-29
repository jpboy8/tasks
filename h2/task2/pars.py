import json

from bs4 import BeautifulSoup

import requests


# headers = {
#     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
# }

# url = 'https://nationalbank.kz/ru/exchangerates/ezhednevnye-oficialnye-rynochnye-kursy-valyut'

# req = requests.get(url=url, headers=headers)
# src = req.text

# with open('index.html', 'w') as file:
#     file.write(src)

with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'html.parser')

table = soup.find('table')

trs = table.find_all('tr')

info_dict = []

for i in trs:
    all_tds = i.find_all('td')
    currency = all_tds[2].text
    rate = all_tds[3].text
    info_dict.append({
        "currency": currency[:3],
        "rate": float(rate),
    })

with open('currency.json', 'w') as file:
    json.dump(info_dict, file, indent=4, ensure_ascii=False)
