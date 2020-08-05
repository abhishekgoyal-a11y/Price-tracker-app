from bs4 import BeautifulSoup
import requests
URL = '''https://www.snapdeal.com/product/janashree-fashion-red-lycra-saree/627960792119#bcrumbSearch:fashion'''
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}


def snapdeal_detail(URL):
    snapdeal_product_type = {
        "fashion": ['pdp-fash-topcenter-inner layout', 'fashionPriceTile row', 'col-xs-18'],
        "electronics": ['pdp-elec-topcenter-inner layout', 'elecPriceTile buyNowBlock row', 'col-xs-22'],

    }
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'html.parser')
    main_content = soup.find('section', id='overviewBlk')
    frame_1_common = main_content.find(
        'div', class_='product-detail clearfix col-xs-24 reset-padding favDp')
    frame_2_common = frame_1_common.find(
        'div', class_='col-xs-14 right-card-zoom reset-padding')
    frame_3_common = frame_2_common.find(
        'div', class_='pdp-comp comp-product-description clearfix')
    for i in snapdeal_product_type:
        try:
            frame_4_common = frame_3_common.find(
                'div', class_=snapdeal_product_type[i][0])  # pdp-elec-topcenter-inner layout # pdp-fash-topcenter-inner layout
            frame_5_price = frame_4_common.find(
                'div', class_='container-fluid reset-padding')
            frame_6_price = frame_5_price.find(
                'div', class_=snapdeal_product_type[i][1])  # elecPriceTile buyNowBlock row # fashionPriceTile row
            frame_7_price = frame_6_price.find(
                'div', class_='row reset-margin')
            frame_8_price = frame_7_price.find(
                'div', class_='col-xs-14 reset-padding padL8')
            frame_9_price = frame_8_price.find(
                'div', class_='disp-table')
            frame_10_price = frame_9_price.find(
                'div', class_='pdp-e-i-PAY-r disp-table-cell lfloat')
            snapdeal_product_price = frame_10_price.span.text.strip()
            frame_5_name = frame_4_common.find(
                'div', class_='row')
            frame_6_name = frame_5_name.find(
                'div', class_=snapdeal_product_type[i][2])  # col-xs-22  # col-xs-18
            snapdeal_product_name = frame_6_name.h1.text.strip()
            return snapdeal_product_name, snapdeal_product_price
        except:
            pass


snapdeal_product_name, snapdeal_product_price = snapdeal_detail(URL)
