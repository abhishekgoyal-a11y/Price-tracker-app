from bs4 import BeautifulSoup
import requests
HEADER = {
    "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:51.0) Gecko/20100101 Firefox/51.0"
}


def Ebay_p_detail(URL):
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'lxml')
    main_content = soup.find('div', id='mainContent')
    frame_1_common = main_content.find(
        'div', class_='product-buy-container product-buy-container-new-ui')
    frame_2_name = frame_1_common.find('div', class_='product')
    frame_3_name = frame_2_name.find(
        'div', class_='product-card-wrapper clearfix')
    frame_4_name = frame_3_name.find(
        'div', class_='product-info no-product-picture')
    ebay_p_product_name = frame_4_name.h1.text.strip()
    for count in range(2, 4):
        try:
            frame_2_price = frame_1_common.find('div', id='center-panel')
            frame_3_price = frame_2_price.find('div', id='hero-item')
            frame_4_price = frame_3_price.find(
                'div', class_='app-theme-item-wrapper shown')
            frame_5_price = frame_4_price.find('div', class_='item-desc')
            frame_6_price = frame_5_price.find(
                'div', class_='item-content-wrapper')
            try:
                frame_7_price = frame_6_price.find('div', class_='item-offer')
            except:
                pass
            try:
                frame_8_price = frame_6_price.find(
                    'div', id=f'tab-panel-0-w{count}')  # tab-panel-0-w2
            except:
                pass
            try:
                frame_8_price = frame_7_price.find(
                    'div', id=f'tab-panel-0-w{count}')  # tab-panel-0-w2
            except:
                pass
            frame_9_price = frame_8_price.find(
                'div', class_='item-price-logistics-wrapper')
            ebay_p_product_price = frame_9_price.h2.text.strip()
        except:
            pass
    return ebay_p_product_name, ebay_p_product_price


def Ebay_itm_detail(URL):
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'lxml')
    main_content = soup.find('div', id='CenterPanelInternal')
    frame_1_common = main_content.find('div', id='LeftSummaryPanel')
    frame_2_price = frame_1_common.find('div', id='mainContent')
    frame_3_price = frame_2_price.find(
        'div', class_='c-std vi-ds3cont-box-marpad')
    frame_4_price = frame_3_price.find(
        'div', class_='actPanel vi-noborder')
    frame_5_price = frame_4_price.find(
        'div', class_='u-flL w29 vi-price')
    ebay_itm_product_price = frame_5_price.span.text
    frame_2_name = frame_1_common.find('div', class_='vi-swc-lsp')
    frame_3_name = frame_2_name.find('span', id='vi-lkhdr-itmTitl')
    ebay_itm_product_name = frame_3_name.text
    return ebay_itm_product_name, ebay_itm_product_price


def ebay_finder(URL):
    ebay_len = len('https://www.ebay.com/')
    find_ebay = URL[ebay_len:]
    product_find = URL[ebay_len:].split('/')
    if product_find[0] == 'p':
        ebay_p_product_price, ebay_p_product_title = Ebay_p_detail(URL)
        return ebay_p_product_price, ebay_p_product_title
    if product_find[0] == 'itm':
        ebay_itm_product_price, ebay_itm_product_title = Ebay_itm_detail(URL)
        return ebay_itm_product_price, ebay_itm_product_title


eday_product_name, ebay_product_price = ebay_finder(URL)
print(eday_product_name, ebay_product_price)
