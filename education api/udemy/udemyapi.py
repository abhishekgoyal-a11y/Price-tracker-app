from bs4 import BeautifulSoup
import requests
URL = "https://www.udemy.com/course/datastructurescncpp/"
HEADER = {
    "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:51.0) Gecko/20100101 Firefox/51.0"
}


def Udemy_course(URL):
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'html.parser')
    main_content = soup.find('div', class_='main-content')
    frame_1_common = main_content.find(
        'div', class_='full-width full-width--streamer streamer--complete')
    frame_2_common = frame_1_common.find('div', class_='container')
    frame_3_price = frame_2_common.find(
        'div', class_='js-right-col__content right-col__content')
    frame_4_price = frame_3_price.find(
        'div', class_='right-col__module')
    frame_5_price = frame_4_price.find(
        'div', class_='right-col__inner')
    frame_6_price = frame_5_price.find(
        'div', 'ud-component--clp--price-text')
    frame_7_price = frame_6_price.find(
        'div', 'price-text')
    frame_8_price = frame_7_price.find(
        'span', 'price-text__current')
    udemy_course_price = frame_8_price.text.strip()
    frame_3_title = frame_2_common.find('div', class_='clp-lead')
    frame_4_title = frame_3_title.find('div', class_='clp-component-render')
    frame_5_title = frame_4_title.find('h1')
    udemy_course_name = frame_5_title.text.strip()
    return udemy_course_name, udemy_course_price


udemy_course_name, udemy_course_price = Udemy_course(URL)
print(udemy_course_name, udemy_course_price)
