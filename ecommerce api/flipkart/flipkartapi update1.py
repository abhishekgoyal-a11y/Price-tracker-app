from bs4 import BeautifulSoup
import requests


def flipkart_detail(URL):
    HEADER = {
        "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:51.0) Gecko/20100101 Firefox/51.0"
    }

    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'html.parser')

    frame_1 = soup.find('div', class_='_1HmYoV hCUpcT')
    frame_2 = frame_1.find('div', class_='_1HmYoV _35HD7C col-8-12')
    frame_4 = frame_2.find('h1', class_='_9E25nV')
    frame_5 = frame_4.find('span', class_='_35KyD6')
    product_name = frame_5.text
    frame_6 = frame_2.find('div', class_='_1uv9Cb')

    product_price = frame_6.find(
        'div', class_='_1vC4OE _3qQ9m1').text
    return product_name, product_price


while True:
    try:
        product_name, product_price = flipkart_detail('https://www.flipkart.com/asus-zenfone-max-pro-m1-grey-64-gb/p/itmf4hg4bhbbng96?pid=MOBF3A8USX5NWRYE&lid=LSTMOBF3A8USX5NWRYE92YR50&marketplace=FLIPKART&srno=b_1_1&otracker=clp_banner_2_32.bannerX3.BANNER_mobiles-big-saving-days-ko7y7ui3-store_DZ1VI6WZGKGK&fm=organic&iid=f8a5cc80-47e5-4176-b247-9bb07edd921e.MOBF3A8USX5NWRYE.SEARCH&ssid=zgim018na80000001593152243692')
        print(product_name, product_price)
    except Exception as e:
        print(e)
