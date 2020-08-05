from bs4 import BeautifulSoup
import requests
URL =[
    "https://www.amazon.in/Redmi-Note-Arctic-White-Storage/dp/B086982ZKF/ref=sr_1_3?dchild=1&fst=as%3Aoff&qid=1595668673&refinements=p_89%3ARedmi&rnid=3837712031&s=electronics&sr=1-3"
    ]
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}
for i in range(len(URL)):
    page = requests.get(URL[i], headers=HEADER)
    soup = BeautifulSoup(page.content, 'html.parser')
    frame_1_common = soup.find('div',id='centerCol')

    # product price
    frame_3_price = frame_1_common.find('div',id='unifiedPrice_feature_div')
    frame_4_price = frame_3_price.find('div',id='price')
    frame_5_price = frame_4_price.find('table',class_='a-lineitem')
    try:
        frame_6_price = frame_5_price.find('tr',id='priceblock_saleprice_row')
        frame_7_price = frame_6_price.find('td',class_='a-span12')
        frame_8_price = frame_7_price.find('span',id='priceblock_saleprice') 
    except:pass
    try:
        frame_6_price = frame_5_price.find('tr',id='priceblock_ourprice_row')
        frame_7_price = frame_6_price.find('td',class_='a-span12')
        frame_8_price = frame_7_price.find('span',id='priceblock_ourprice') 
    except:pass
    try:
        frame_6_price = frame_5_price.find('tr',id='priceblock_dealprice_row')
        frame_7_price = frame_6_price.find('td',class_='a-span12')
        frame_8_price = frame_7_price.find('span',id='priceblock_dealprice') 
    except:pass
    product_price =frame_8_price.text.strip()

    # product name
    frame_2_title = frame_1_common.find('div',id='title_feature_div')
    frame_3_title  = frame_2_title .find('div',id='titleSection')
    frame_4_title  = frame_3_title .find('h1',class_='a-size-large a-spacing-none')
    frame_5_title  = frame_4_title .find('span',id='productTitle')
    product_name=frame_5_title.text.strip()

    print(product_name,product_price)
    print("comp")
