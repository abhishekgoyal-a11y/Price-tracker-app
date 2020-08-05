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
    frame_3 = frame_2.find('div', class_='bhgxx2 col-12-12')
    frame_4 = frame_3.find('h1', class_='_9E25nV')
    frame_5 = frame_4.find('span', class_='_35KyD6')
    product_name = frame_5.text
    frame_6 = frame_3.find('div', class_='_1uv9Cb')

    product_price = frame_6.find(
        'div', class_='_1vC4OE _3qQ9m1').text
    return product_name, product_price


while True:
    try:
        product_name, product_price = flipkart_detail(
            'https://www.flipkart.com/apple-iphone-7-black-32-gb/p/itmen6daftcqwzeg')
        print(product_name, product_price)
    except Exception as e:
        print(e)
