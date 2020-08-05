from bs4 import BeautifulSoup
import requests
URL = 'https://www.coursera.org/professional-certificates/ibm-data-science'
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}

page = requests.get(URL, headers=HEADER)
soup = BeautifulSoup(page.content, 'html.parser')
frame_1_common = soup.find('div', id='rendered-content')
frame_2_common = frame_1_common.find('div', class_='rc-MetatagsWrapper')
frame_3_common = frame_2_common.find('div', class_='XdpApp')
frame_4_common = frame_3_common.find('div', class_='_1jug6qr SDPPage')
frame_5_price = frame_4_common.find('div', class_='rc-XdpSection')
frame_6_price = frame_5_price.find('div', class_='_1d3lkver p-b-2')
frame_7_price = frame_6_price.find('div', class_='AboutS12n')
frame_8_price = frame_7_price.find('div', class_='_jyhj5r text-xs-left')
frame_9_price = frame_8_price.find('div', class_='_1b7vhsnq m-t-2')
frame_10_price = frame_9_price.find('div', class_='_9cam1z')
frame_11_price = frame_10_price.find(
    'div', class_='LearnerOutcomes__container m-b-2 m-t-3')
print(frame_10_price.prettify())

# frame_5_title = frame_4_common.find('div', class_='BannerS12n')
# frame_6_title = frame_5_title.find(
#     'div', class_='_1kaejd6 Banner text-primary-dark text-xs-left color-white pos-relative')
# frame_7_title = frame_6_title.find(
#     'div', class_='_1d3lkver h-100 p-y-3 p-x-2')
# frame_8_title = frame_7_title.find(
#     'div', class_='_jyhj5r')
# frame_9_title = frame_8_title.find(
#     'div', class_='_1yawxg07')
# frame_10_title = frame_9_title.find(
#     'div', class_='_1bjlpa11 BannerTitle text-xs-left')
# course_title = frame_10_title.h1.text.strip()
# print(course_title)


# deiffrent  links
"https://www.coursera.org/professional-certificates/ibm-data-science"
"https://www.coursera.org/learn/covid-19-contact-tracing?edocomorp=covid-19-contact-tracing"
"https://www.coursera.org/degrees/bachelor-of-science-computer-science-london"
"https://www.coursera.org/specializations/deep-learning"
"https://www.coursera.org/projects/build-portfolio-website-html-css?edocomorp=freegpmay2020"
