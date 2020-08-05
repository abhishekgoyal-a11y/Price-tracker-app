from bs4 import BeautifulSoup
import requests
URL = '''https://www.shopclues.com/g-pet-checkers-jars-plastic-container-brown-cap-set-of-20-1800ml-4-1200ml-4-450ml-4-200ml-4-50ml-4-147015106.html'''
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}


def shopclues_products(URL):
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'html.parser')
    main_content = soup.find('div', class_='container')
    frame_1_common = main_content.find('div', class_='wrapper maxStWrap')
    frame_2_common = frame_1_common.find('div', id='main_data')
    frame_3_common = frame_2_common.find('div', class_='shd_box')
    frame_4_common = frame_3_common.find('div', class_='prd_mid_info')
    frame_5_price = frame_4_common.find('div', class_='price')
    frame_6_price = frame_5_price.find('span', class_='f_price')
    shopclues_product_price = frame_6_price.text.strip()
    shopclues_product_name = frame_4_common.h1.text.strip()
    return shopclues_product_name, shopclues_product_price


shopclues_product_name, shopclues_product_price = shopclues_products(URL)
