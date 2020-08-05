import requests
from bs4 import BeautifulSoup
HEADER = {
    "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:51.0) Gecko/20100101 Firefox/51.0"
}


def Edx_Course(URL):
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'html.parser')
    main_content = soup.find('main', id='main-content')
    frame_1_common = main_content.find('div', class_='course-info-content')
    frame_2_price = frame_1_common.find(
        'div', class_='row no-gutters main-content')
    frame_3_price = frame_2_price.find(
        'div', class_='col-lg-4 order-lg-2 offset-lg-1')
    frame_4_price = frame_3_price.find(
        'div', class_='container course-side-area')
    frame_5_price = frame_4_price.find(
        'ul', class_='list-group list-group-flush w-100')
    frames_6_price = frame_5_price.find('p', class_='m-0')
    edx_course_price = frames_6_price.text.strip()
    frame_2_title = frame_1_common.find(
        'header', class_='course-header push-away-from-absolute-header mb-4 row')
    frame_3_title = frame_2_title.find('div', id='course-header')
    frame_4_title = frame_3_title.find('div', class_='row no-gutters w-100')
    frame_5_title = frame_4_title.find(
        'h1', class_='course-intro-heading mb-2')
    edx_course_title = frame_5_title.text.strip()
    return edx_course_price, edx_course_title


def Edx_other_type_course(URL):
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'html.parser')
    main_content = soup.find('main', id='main-content')
    frame_1_price = main_content.find(
        'div', class_='gradient-wrapper program-body')
    frame_2_price = frame_1_price.find(
        'div', class_='container')
    frame_3_price = frame_2_price.find(
        'div', class_='container-fluid program-section')
    frame_4_price = frame_3_price.find('div', class_='row')
    frame_5_price = frame_4_price.find('div', class_='flex-column')
    frame_6_price = frame_5_price.find('div', class_='main d-flex flex-wrap')
    edx_other_type_course_price = frame_6_price.text.strip()
    frame_1_title = main_content.find('div', class_='data-bar shadow')
    for count in range(1, 3):
        try:
            frame_2_title = frame_1_title.find(
                'div', class_=f'data-bar-content partner-count-{count}')  # data-bar-content partner-count-2
            frame_3_title = frame_2_title.find(
                'div', class_='container-fluid')
            frame_4_title = frame_3_title.find(
                'div', class_='row')
            frame_5_title = frame_4_title.find(
                'div', class_='program')
            frame_6_title = frame_5_title.find(
                'div', class_='type')
            frame_7_title = frame_6_title.find(
                'div', class_='title')
            edx_other_type_course_title = frame_7_title.text.strip()
        except:
            pass
    # the course title is in french language , convert into english
    return edx_other_type_course_price, edx_other_type_course_title


def edx_finder(URL):
    edx_len = len('https://www.edx.org/')
    find_edx = URL[edx_len:]
    course_find = URL[edx_len:].split('/')
    if course_find[0] == 'course':
        edx_course_price, edx_course_title = Edx_Course(URL)
        return edx_course_price, edx_course_title
    if course_find[0] != 'course':
        edx_other_type_course_price, edx_other_type_course_title = Edx_other_type_course(
            URL)
        return edx_other_type_course_price, edx_other_type_course_title


edx_title, edx_price = edx_finder(
    'https://www.edx.org/course/cs50s-mobile-app-development-with-react-native')

print(edx_title, edx_price)
# print(edx_finder('https://www.edx.org/course/como-aprender-online'))
# print(edx_finder('https://www.edx.org/xseries/uamx-griego-clasico'))
# print(edx_finder('https://www.edx.org/professional-certificate/usmx-product-management'))
