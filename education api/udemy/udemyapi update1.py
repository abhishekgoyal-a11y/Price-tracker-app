from bs4 import BeautifulSoup
import requests
URL = [
    "https://www.udemy.com/course/aws-certified-solutions-architect-associate/"

]


HEADER = {
    "User-Agent": "Mxyz"
}


def Udemy_course(URL):
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'html.parser')
    main_content = soup.find('div', class_='main-content')
    frame_1_common = main_content.find(
        'div', class_='top-container dark-background')
    frame_2_common = frame_1_common.find(
        'div', class_='dark-background-inner-position-container')
    frame_3_price = frame_2_common.find(
        'div', class_='course-landing-page__main-content course-landing-page__purchase-section__main')
    frame_4_price = frame_3_price.find(
        'div', class_='buy-box-main')
    frame_5_price = frame_4_price.find(
        'div', class_='price-text--container--Ws-fP udlite-clp-price-text')
    frame_6_price = frame_5_price.find(
        'div', class_='price-text--price-part--Tu6MH udlite-clp-discount-price udlite-heading-xl')
    udemy_course_price = frame_6_price.text.strip()
    frame_3_title = frame_2_common.find(
        'h1', class_='clp-lead__title clp-lead__title--small')
    udemy_course_name = frame_3_title.text.strip()
    return udemy_course_name, udemy_course_price


for i in range(len(URL)):
    udemy_course_name, udemy_course_price = Udemy_course(URL[i])
    print(udemy_course_name, udemy_course_price)
