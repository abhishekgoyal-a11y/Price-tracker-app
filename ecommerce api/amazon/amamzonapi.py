from bs4 import BeautifulSoup
import requests
URL = '''https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B084456GH4/ref=sr_1_1_sspa?dchild=1&keywords=mobile&qid=1591700507&sr=8-1-spons&psc=1&sp
La=ZW5jcnlwdGVkUXVhbGlmaWVyPUExRVFURDJWVENUUEVGJmVuY3J5cHRlZElkPUEwNTQxMDQxMUVZVFZXVVVCVTM1NiZlbmNyeXB0ZWRBZElkPUEwOTc2MDE1MTNCN0FKUDE5VkwwNSZ3aWRnZXROYW1lPXNwX2F0Zi
ZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='''
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}

page = requests.get(URL, headers=HEADER)
soup = BeautifulSoup(page.content, 'html.parser')
frame_1_common = soup.find('div',id='centerCol')

# product price
frame_2_price = frame_1_common.find('div',id='desktop_unifiedPrice')
frame_3_price = frame_2_price.find('div',id='unifiedPrice_feature_div')
frame_4_price = frame_3_price.find('div',id='price')
frame_5_price = frame_4_price.find('table',class_='a-lineitem')
frame_6_price = frame_5_price.find('tr',id='priceblock_ourprice_row')
frame_7_price = frame_6_price.find('td',class_='a-span12')
frame_8_price = frame_7_price.find('span',id='priceblock_ourprice')
product_price =frame_8_price.text.strip()

# product name
frame_2_title = frame_1_common.find('div',id='title_feature_div')
frame_3_title  = frame_2_title .find('div',id='titleSection')
frame_4_title  = frame_3_title .find('h1',class_='a-size-large a-spacing-none')
frame_5_title  = frame_4_title .find('span',id='productTitle')
product_name=frame_5_title.text.strip()

print(product_price,product_name)


# not working links
##'https://www.amazon.in/Worlds-Greatest-Personal-Growth-Wealth/dp/9389432014/ref=sr_1_1_sspa?dchild=1&keywords=books&qid=1591801996&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE1Tzg3MklPTFRNOSZlbmNyeXB0ZWRJZD1BMDY1OTA2NDFOUVhQTlpEUlEzWUQmZW5jcnlwdGVkQWRJZD1BMDI1OTk4NTJLUE83SDA4VklaNU0md2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
