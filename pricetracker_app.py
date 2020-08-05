#################################################################### All LIBRARY IMPORTED ############################################################
import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from threading import *

# Initialize Window

root = Tk()
root.title("Price Alert")
root.geometry("600x600")

HEADER = {
    "User-Agent": "xyz"
}
################################################################ FLIPKART #############################################################################


def flipkart_detail(URL):
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'html.parser')
    # common for both (name and price)
    frame_1 = soup.find('div', class_='_1HmYoV hCUpcT')
    frame_2 = frame_1.find('div', class_='_1HmYoV _35HD7C col-8-12')
    frame_3 = frame_2.find('div', class_='bhgxx2 col-12-12')
    frame_4 = frame_3.find('h1', class_='_9E25nV')
    frame_5 = frame_4.find('span', class_='_35KyD6')
    # flipkart product name
    flipkart_product_name = frame_5.text
    frame_6 = frame_3.find('div', class_='_1uv9Cb')
    # flipkart product price
    flipkart_product_price = frame_6.find(
        'div', class_='_1vC4OE _3qQ9m1').text
    return flipkart_product_name, flipkart_product_price

################################################################ AMAZON #############################################################################


def amazon_detail(URL):
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'html.parser')
    # common for both (name and price)
    frame_1_common = soup.find('div', id='centerCol')
    # amazon product price
    frame_3_price = frame_1_common.find('div', id='unifiedPrice_feature_div')
    frame_4_price = frame_3_price.find('div', id='price')
    frame_5_price = frame_4_price.find('table', class_='a-lineitem')
    try:
        frame_6_price = frame_5_price.find('tr', id='priceblock_saleprice_row')
        frame_7_price = frame_6_price.find('td', class_='a-span12')
        frame_8_price = frame_7_price.find('span', id='priceblock_saleprice')
    except:
        pass
    try:
        frame_6_price = frame_5_price.find('tr', id='priceblock_ourprice_row')
        frame_7_price = frame_6_price.find('td', class_='a-span12')
        frame_8_price = frame_7_price.find('span', id='priceblock_ourprice')
    except:
        pass
    amazon_product_price = frame_8_price.text.strip()

    # amazon product name
    frame_2_title = frame_1_common.find('div', id='title_feature_div')
    frame_3_title = frame_2_title .find('div', id='titleSection')
    frame_4_title = frame_3_title .find(
        'h1', class_='a-size-large a-spacing-none')
    frame_5_title = frame_4_title .find('span', id='productTitle')
    amazon_product_name = frame_5_title.text.strip()

    return amazon_product_price, amazon_product_name

################################################################ EBAY P #############################################################################


def Ebay_p_detail(URL):
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'lxml')

    # common for both (name and price)
    main_content = soup.find('div', id='mainContent')
    frame_1_common = main_content.find(
        'div', class_='product-buy-container product-buy-container-new-ui')

    # ebay p product name
    frame_2_name = frame_1_common.find('div', class_='product')
    frame_3_name = frame_2_name.find(
        'div', class_='product-card-wrapper clearfix')
    frame_4_name = frame_3_name.find(
        'div', class_='product-info no-product-picture')
    ebay_p_product_name = frame_4_name.h1.text.strip()

    # ebay p product price
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

################################################################ EBAY ITM #############################################################################


def Ebay_itm_detail(URL):
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'lxml')

    # common for both (name and price)
    main_content = soup.find('div', id='CenterPanelInternal')
    frame_1_common = main_content.find('div', id='LeftSummaryPanel')

    # ebay itm product price
    frame_2_price = frame_1_common.find('div', id='mainContent')
    frame_3_price = frame_2_price.find(
        'div', class_='c-std vi-ds3cont-box-marpad')
    frame_4_price = frame_3_price.find(
        'div', class_='actPanel vi-noborder')
    frame_5_price = frame_4_price.find(
        'div', class_='u-flL w29 vi-price')
    ebay_itm_product_price = frame_5_price.span.text

    # ebay itm product name
    frame_2_name = frame_1_common.find('div', class_='vi-swc-lsp')
    frame_3_name = frame_2_name.find('span', id='vi-lkhdr-itmTitl')
    ebay_itm_product_name = frame_3_name.text

    return ebay_itm_product_name, ebay_itm_product_price


############################################# MERGING BOTH P AND ITM EBAY FUCNTION ####################################################################

def ebay_finder(URL):
    ebay_len = len('https://www.ebay.com/')
    find_ebay = URL[ebay_len:]
    product_find = URL[ebay_len:].split('/')

    # EBAY FOR P PRODUCT

    if product_find[0] == 'p':
        ebay_p_product_price, ebay_p_product_title = Ebay_p_detail(URL)
        return ebay_p_product_price, ebay_p_product_title

    # ebay for itm product

    if product_find[0] == 'itm':
        ebay_itm_product_price, ebay_itm_product_title = Ebay_itm_detail(URL)
        return ebay_itm_product_price, ebay_itm_product_title

################################################################ SNAPDEAL #############################################################################


def snapdeal_detail(URL):
    snapdeal_product_type = {
        "fashion": ['pdp-fash-topcenter-inner layout', 'fashionPriceTile row', 'col-xs-18'],
        "electronics": ['pdp-elec-topcenter-inner layout', 'elecPriceTile buyNowBlock row', 'col-xs-22'],

    }
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'html.parser')

    # common for both (name and price)

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

            # snapdeal product price

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

            # snapdeal product name

            frame_5_name = frame_4_common.find(
                'div', class_='row')
            frame_6_name = frame_5_name.find(
                'div', class_=snapdeal_product_type[i][2])  # col-xs-22  # col-xs-18
            snapdeal_product_name = frame_6_name.h1.text.strip()

            return snapdeal_product_name, snapdeal_product_price
        except:
            pass

################################################################ SHOPCLUES #############################################################################


def shopclues_products(URL):
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'html.parser')

    # common for both (name and price)

    main_content = soup.find('div', class_='container')
    frame_1_common = main_content.find('div', class_='wrapper maxStWrap')
    frame_2_common = frame_1_common.find('div', id='main_data')
    frame_3_common = frame_2_common.find('div', class_='shd_box')
    frame_4_common = frame_3_common.find('div', class_='prd_mid_info')

    # shopclues product price

    frame_5_price = frame_4_common.find('div', class_='price')
    frame_6_price = frame_5_price.find('span', class_='f_price')
    shopclues_product_price = frame_6_price.text.strip()

    # shopclues product name
    shopclues_product_name = frame_4_common.h1.text.strip()
    return shopclues_product_name, shopclues_product_price


################################################################ EDX #############################################################################

def Edx_Course(URL):
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'html.parser')

    # common for both (name and price)

    main_content = soup.find('main', id='main-content')
    frame_1_common = main_content.find('div', class_='course-info-content')

    # edx course price

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

    # edx course title

    frame_2_title = frame_1_common.find(
        'header', class_='course-header push-away-from-absolute-header mb-4 row')
    frame_3_title = frame_2_title.find('div', id='course-header')
    frame_4_title = frame_3_title.find('div', class_='row no-gutters w-100')
    frame_5_title = frame_4_title.find(
        'h1', class_='course-intro-heading mb-2')
    edx_course_title = frame_5_title.text.strip()

    return edx_course_price, edx_course_title

################################################################ EDX COURSE OTHER TYPE ###############################################################


def Edx_other_type_course(URL):
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'html.parser')

    # common for both (name and price)

    main_content = soup.find('main', id='main-content')

    # edx other course type price

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

    # edx other course type title

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


######################################################## MERGING BOTH EDX FUCNTION ###################################################################

def edx_finder(URL):
    edx_len = len('https://www.edx.org/')
    find_edx = URL[edx_len:]
    course_find = URL[edx_len:].split('/')

    if course_find[0] == 'course':
        edx_course_price, edx_course_title = Edx_Course(URL)
        return edx_course_price, edx_course_title

    # edx for same other type

    if course_find[0] != 'course':
        edx_other_type_course_price, edx_other_type_course_title = Edx_other_type_course(
            URL)
        return edx_other_type_course_price, edx_other_type_course_title

################################################################ UDEMY ################################################################################


def Udemy_course(URL):
    page = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(page.content, 'html.parser')

    # common for both (name and price)

    main_content = soup.find('div', class_='main-content')
    frame_1_common = main_content.find(
        'div', class_='full-width full-width--streamer streamer--complete')
    frame_2_common = frame_1_common.find('div', class_='container')

    # udemy course price

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

    # udemy course title

    frame_3_title = frame_2_common.find('div', class_='clp-lead')
    frame_4_title = frame_3_title.find('div', class_='clp-component-render')
    frame_5_title = frame_4_title.find('h1')
    udemy_course_name = frame_5_title.text.strip()

    return udemy_course_name, udemy_course_price

# Threading


def product_detail_threading():
    print("start")
    t1 = Thread(target=product_detail)
    t1.start()
    print("done")

########################################################## COMBINING ALL FUNCTION #################################################################


def product_detail():
    url = enter_url.get("1.0", "end").strip()

    # Amazon

    if radiobutton_variable.get() == "1":
        try:
            status_variable.set("Fetching Details....")
            status_label.update()
            amazon_product_price, amazon_product_name = amazon_detail(url)
            product_name_label.update()
            product_name_variable.set(amazon_product_name)
            current_price_label.update()
            current_price_variable.set(amazon_product_price)
            status_variable.set("Ready")
            status_label.update()
        except Exception as e:
            print(e)
            status_variable.set("Try Again....")

    # Flipkart

    if radiobutton_variable.get() == "2":
        try:
            status_variable.set("Fetching Details....")
            status_label.update()
            flipkart_product_name, flipkart_product_price = flipkart_detail(
                url)
            product_name_label.update()
            product_name_variable.set(flipkart_product_name)
            current_price_label.update()
            current_price_variable.set(flipkart_product_price)
            status_variable.set("Ready")
            status_label.update()
        except Exception as e:
            print(e)
            status_variable.set("Try Again....")

    # Edx

    if radiobutton_variable.get() == "3":
        try:
            status_variable.set("Fetching Details....")
            status_label.update()
            edx_price, edx_title = edx_finder(url)
            product_name_label.update()
            product_name_variable.set(edx_title)
            current_price_label.update()
            current_price_variable.set(edx_price)
            status_variable.set("Ready")
            status_label.update()
        except Exception as e:
            print(e)
            status_variable.set("Try Again....")

    # Udemy

    if radiobutton_variable.get() == "4":
        try:
            status_variable.set("Fetching Details....")
            status_label.update()
            udemy_course_name, udemy_course_price = Udemy_course(url)
            product_name_label.update()
            product_name_variable.set(udemy_course_name)
            current_price_label.update()
            current_price_variable.set(udemy_course_price)
            status_variable.set("Ready")
            status_label.update()
        except Exception as e:
            print(e)
            status_variable.set("Try Again....")
            status_variable.set("Try Again....")

    # Ebay

    if radiobutton_variable.get() == "5":
        try:
            status_variable.set("Fetching Details....")
            status_label.update()
            eday_product_name, ebay_product_price = ebay_finder(url)
            product_name_label.update()
            product_name_variable.set(eday_product_name)
            current_price_label.update()
            current_price_variable.set(ebay_product_price)
            status_variable.set("Ready")
            status_label.update()
        except Exception as e:
            print(e)
            status_variable.set("Try Again....")

    # Snapdeal

    if radiobutton_variable.get() == "6":
        try:
            status_variable.set("Fetching Details....")
            status_label.update()
            snapdeal_product_name, snapdeal_product_price = snapdeal_detail(
                url)
            product_name_label.update()
            product_name_variable.set(snapdeal_product_name)
            current_price_label.update()
            current_price_variable.set(snapdeal_product_price)
            status_variable.set("Ready")
            status_label.update()
        except Exception as e:
            print(e)
            status_variable.set("Try Again....")

    # Shopclues

    if radiobutton_variable.get() == "7":
        try:
            status_variable.set("Fetching Details....")
            status_label.update()
            shopclues_product_name, shopclues_product_price = shopclues_products(
                url)
            product_name_label.update()
            product_name_variable.set(shopclues_product_name)
            current_price_label.update()
            current_price_variable.set(shopclues_product_price)
            status_variable.set("Ready")
            status_label.update()
        except Exception as e:
            print(e)
            status_variable.set("Try Again....")


def all_details():
    if radiobutton_variable.get() == "1":
        company_name = "Amazon"
    if radiobutton_variable.get() == "2":
        company_name = "Flipkart"
    if radiobutton_variable.get() == "3":
        company_name = "Edx"
    if radiobutton_variable.get() == "4":
        company_name = "Udemy"
    if radiobutton_variable.get() == "5":
        company_name = "Ebay"
    if radiobutton_variable.get() == "6":
        company_name = "Snapdeal"
    if radiobutton_variable.get() == "6":
        company_name = "Shopclues"
    print(company_name)
    print(product_name_label.cget("text"))
    print(current_price_label.cget("text"))
    print(set_price.get())
    print(set_time.get())
    print(initial_time_type_variable.get())

# increment time


def increment_value():
    if int(set_time.get()) < 0:
        initial_time.set(int(0))
        set_time.update()
    else:
        initial_time.set(int(set_time.get())+1)
        set_time.update()

# decrement time


def decrement_value():
    if int(set_time.get()) < 0:
        initial_time.set(int(0))
        set_time.update()
    if int(set_time.get()) > 0:
        initial_time.set(int(set_time.get())-1)
        set_time.update()

# Main program starts


if __name__ == "__main__":

    # price drop heading
    price_drop_alert = Label(root, text="Price Drop Alert",
                             font=("Times", "26", "bold italic"))
    price_drop_alert.place(x=10, y=5)

    # url
    enter_url_label = Label(root, text="Enter URL :",
                            font=("Times", "20"))
    enter_url_label.place(x=60, y=67)
    enter_url = Text(root, width=40, height=3)
    enter_url.place(x=200, y=60)

    # company
    company_label = Label(root, text="Company  :",
                          font=("Times", "20"))
    company_label.place(x=67, y=120)

    # radio buttons
    radiobutton_variable = StringVar()
    radiobutton_variable.set("1")
    Radiobutton1 = Radiobutton(text="Amazon", variable=radiobutton_variable, font=("Times", "10", "bold"),
                               value=1)
    Radiobutton1.place(x=200, y=113)
    Radiobutton2 = Radiobutton(text="Flipkart", variable=radiobutton_variable, font=("Times", "10", "bold"),
                               value=2)
    Radiobutton2.place(x=270, y=113)
    Radiobutton3 = Radiobutton(text="Edx", variable=radiobutton_variable, font=("Times", "10", "bold"),
                               value=3)
    Radiobutton3.place(x=340, y=113)
    Radiobutton4 = Radiobutton(text="Udemy", variable=radiobutton_variable, font=("Times", "10", "bold"),
                               value=4)
    Radiobutton4.place(x=385, y=113)
    Radiobutton5 = Radiobutton(text="Ebay", variable=radiobutton_variable, font=("Times", "10", "bold"),
                               value=5)
    Radiobutton5.place(x=470, y=113)
    Radiobutton6 = Radiobutton(text="Snapdeal", variable=radiobutton_variable, font=("Times", "10", "bold"),
                               value=6)
    Radiobutton6.place(x=280, y=133)
    Radiobutton6 = Radiobutton(text="Shopclues", variable=radiobutton_variable, font=("Times", "10", "bold"),
                               value=7)
    Radiobutton6.place(x=200, y=133)

    # search button
    search = Button(root, text="Search Product",
                    font=("Times", "20", "bold italic"), command=product_detail_threading)
    search.place(x=200, y=160)

    # product name
    product_name = Label(root, text="Product name :", font=("Times", "20"))
    product_name.place(x=60, y=223)

    product_name_variable = StringVar()
    product_name_variable.set("")
    product_name_label = Label(
        root, textvariable=product_name_variable, fg='red',
        width=50, height=3, anchor="nw", wraplength=300)
    product_name_label.place(x=230, y=231)

    # current price
    current_price = Label(root, text="Current price :", font=("Times", "20"))
    current_price.place(x=60, y=275)

    current_price_variable = StringVar()
    current_price_variable.set("")
    current_price_label = Label(
        root, textvariable=current_price_variable, fg='red',
        width=20, anchor="nw", wraplength=300)
    current_price_label.place(x=230, y=285)

    # if above details are not correct
    detial_not_correct_label = Label(
        root, text='''          If Above Details are not correct , 
        Please send the searched link on this email
        "kumar.abhishekgoyal@gmail.com"''',
        font=("Times", "15"), fg='red')
    detial_not_correct_label.place(x=80, y=330)

    # set price
    set_price_label = Label(root, text="Set Price :", font=("Times", "20"))
    set_price_label.place(x=60, y=410)
    set_price = Entry(root, font=("Times", "20"))
    set_price.place(x=180, y=410)

    # set time
    initial_time = IntVar()
    initial_time.set(1)
    set_time_label = Label(root, text="Set Time :", font=("Times", "20"))
    set_time_label.place(x=60, y=460)
    set_time = Entry(root, textvariable=initial_time, font=("Times", "20"),
                     width=3)
    set_time.place(x=180, y=460)

    # increment time
    increment_image = 'images/increment_triangle.jpg'
    increment_image_icon = ImageTk.PhotoImage(Image.open(increment_image))
    increment_button = Button(root, command=increment_value)
    increment_button.place(x=235, y=462)
    increment_button.config(image=increment_image_icon)

    # decrement time
    decrement_image = 'images/decrement_triangle.jpg'
    decrement_image_icon = ImageTk.PhotoImage(Image.open(decrement_image))
    decrement_button = Button(root, command=decrement_value)
    decrement_button.place(x=235, y=478)
    decrement_button.config(image=decrement_image_icon)

    # dropdown time type
    initial_time_type_variable = StringVar()
    initial_time_type_variable.set('Days')
    initial_time_type_values = {'Minutes', 'Hours',
                                'Days', 'Weeks', 'Months', 'Years'}
    initial_time_type_drp = OptionMenu(
        root, initial_time_type_variable, *initial_time_type_values)
    initial_time_type_drp.place(x=260, y=460)

    # # save button
    save_button = Button(root, text="Save",
                         font=("Times", "20", "bold italic"), command=all_details)
    save_button.place(x=300, y=500)

    # status
    status_variable = StringVar()
    status_variable.set("Ready")
    status_label = Label(
        root, textvariable=status_variable, anchor="nw", fg='red', relief=SUNKEN)
    status_label.pack(fill=X, side=BOTTOM)

    root.configure()
    root.mainloop()
