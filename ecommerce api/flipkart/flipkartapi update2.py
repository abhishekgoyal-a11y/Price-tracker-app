from bs4 import BeautifulSoup
import requests


def flipkart_detail(URL):
    HEADER = {
        "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:51.0) Gecko/20100101 Firefox/51.0"
    }

    page = requests.get(URL, headers=HEADER)
    page_encoded=page.content.decode("utf-8","ignore")
    soup = BeautifulSoup(page_encoded, 'html.parser')
    
    frame_2 = soup.find('div', class_='_29OxBi')
    frame_4 = frame_2.find('h1', class_='_9E25nV')
    frame_5 = frame_4.find('span', class_='_35KyD6')
    product_name = frame_5.text
    frame_6 = frame_2.find('div', class_='_1uv9Cb')

    product_price = frame_6.find(
        'div', class_='_1vC4OE _3qQ9m1').text
    return product_name, product_price


URL=["https://www.flipkart.com/redmi-k20-carbon-black-64-gb/p/itmfgfjtkpnd64gb?pid=MOBFG7UYRCCTB7BA&lid=LSTMOBFG7UYRCCTB7BAYTKRNO&marketplace=FLIPKART&srno=b_1_1&otracker=clp_banner_1_10.banner.BANNER_mobiles-big-saving-days-ko7y7ui3-store_FM40BQ4VWVR5&fm=organic&iid=a0255d2e-5671-43a5-a493-1dd34a2db8c4.MOBFG7UYRCCTB7BA.SEARCH&ssid=9nws1979b40000001593152220715",
"https://www.flipkart.com/realme-x2-pro-lunar-white-256-gb/p/itma3203d88190a3?pid=MOBFM2WZ5JEKKM9T&lid=LSTMOBFM2WZ5JEKKM9TIIU9OC&marketplace=FLIPKART&srno=b_1_1&otracker=clp_banner_1_11.bannerX3.BANNER_mobiles-big-saving-days-ko7y7ui3-store_66YSLT539AQA&fm=organic&iid=396938fc-89a6-4f56-8cf7-85a496212f91.MOBFM2WZ5JEKKM9T.SEARCH&ssid=l0a24ba6a80000001593152221681",
"https://www.flipkart.com/realme-6-comet-white-128-gb/p/itm20124d6ca5690?pid=MOBFPCX793UFBX3N&lid=LSTMOBFPCX793UFBX3NBHPRID&marketplace=FLIPKART&srno=b_1_1&otracker=clp_banner_3_11.bannerX3.BANNER_mobiles-big-saving-days-ko7y7ui3-store_9GMM0N8TB5HZ&fm=organic&iid=8588abfc-7531-4b6d-b447-938b3b45c639.MOBFPCX793UFBX3N.SEARCH&ssid=7t71dy32sg0000001593152222791",
"https://www.flipkart.com/iqoo-3-tornado-black-128-gb/p/itm7d075bc17be11?pid=MOBFP4P2CESTHKKR&lid=LSTMOBFP4P2CESTHKKRXDMNL7&marketplace=FLIPKART&srno=b_1_1&otracker=clp_banner_1_12.banner.BANNER_mobiles-big-saving-days-ko7y7ui3-store_1ORFFMPQGESK&fm=organic&iid=89930494-e94e-49c7-b1f6-30323872bddc.MOBFP4P2CESTHKKR.SEARCH&ssid=7rob3q9ms00000001593152224821",
"https://www.flipkart.com/apple-iphone-7-plus-black-32-gb/p/itmen6davhyetcwf?pid=MOBEMK6289R7UFQH&lid=LSTMOBEMK6289R7UFQHEIIGH8&marketplace=FLIPKART&srno=b_1_1&otracker=clp_banner_1_21.bannerX3.BANNER_mobiles-big-saving-days-ko7y7ui3-store_S26IDL27CRUQ&fm=organic&iid=90bd444e-818e-47ac-8c10-cd8b97819500.MOBEMK6289R7UFQH.SEARCH&ssid=9fjaqbeo8w0000001593152227205",
"https://www.flipkart.com/apple-iphone-xs-space-grey-64-gb/p/itmf944ees7rprte?pid=MOBF944E5FTGHNCR&lid=LSTMOBF944E5FTGHNCRAH33S3&otracker=clp_banner_3_21.bannerX3.BANNER_mobiles-big-saving-days-ko7y7ui3-store_OIJHOH2QYMFK&fm=neo%2Fmerchandising&iid=M_93dc95ee-444d-46da-9a80-23ee1588af19_21.OIJHOH2QYMFK&ssid=zjpvplgt7k0000001593152204385",
"https://www.flipkart.com/vivo-nex-black-128-gb/p/itmfb4ctja3mgrcz?pid=MOBFB4CTZYDFUTYH&lid=LSTMOBFB4CTZYDFUTYHBEIJP8&otracker=clp_banner_1_22.banner.BANNER_mobiles-big-saving-days-ko7y7ui3-store_0RDBOGS1X1S0",
"https://www.flipkart.com/apple-iphone-xr-yellow-64-gb/p/itmf9z7z76tayfaq?pid=MOBF9Z7ZUGQ6YDBH&lid=LSTMOBF9Z7ZUGQ6YDBH8DBQTX&marketplace=FLIPKART&srno=b_1_1&otracker=clp_banner_2_23.bannerX3.BANNER_mobiles-big-saving-days-ko7y7ui3-store_SM2M43IA11CX&fm=organic&iid=2d9037fc-27c1-41d7-87d2-cf664ea8b44a.MOBF9Z7ZUGQ6YDBH.SEARCH&ssid=nqcodjhsvk0000001593152230561",
"https://www.flipkart.com/samsung-galaxy-s10-lite-prism-white-128-gb/p/itmb6f6f7cc402e7?pid=MOBFZ8HTSDNVQGPG&lid=LSTMOBFZ8HTSDNVQGPGWWMUEH&marketplace=FLIPKART&srno=b_1_1&otracker=clp_banner_1_24.banner.BANNER_mobiles-big-saving-days-ko7y7ui3-store_S7GH42VX402X&fm=organic&iid=f275f5dc-c6ae-45e5-b874-8135a8109bbb.MOBFZ8HTSDNVQGPG.SEARCH&ssid=foctm27ayo0000001593152231076",
"https://www.flipkart.com/mi-mix-2-black-128-gb/p/itmeyk8z8cwf6faz?pid=MOBEYCHKGHZJMGJZ&lid=LSTMOBEYCHKGHZJMGJZ52RUOA&otracker=clp_banner_1_31.banner.BANNER_mobiles-big-saving-days-ko7y7ui3-store_SXS26OUK18M3",
"https://www.flipkart.com/asus-zenfone-max-pro-m1-grey-64-gb/p/itmf4hg4bhbbng96?pid=MOBF3A8USX5NWRYE&lid=LSTMOBF3A8USX5NWRYE92YR50&marketplace=FLIPKART&srno=b_1_1&otracker=clp_banner_2_32.bannerX3.BANNER_mobiles-big-saving-days-ko7y7ui3-store_DZ1VI6WZGKGK&fm=organic&iid=f8a5cc80-47e5-4176-b247-9bb07edd921e.MOBF3A8USX5NWRYE.SEARCH&ssid=zgim018na80000001593152243692",
"https://www.flipkart.com/oppo-f15-blazing-blue-128-gb/p/itm56d35565691ea?pid=MOBFTYWWZKUAMC24&lid=LSTMOBFTYWWZKUAMC24JB2E4S&marketplace=FLIPKART&srno=b_1_1&otracker=clp_banner_3_32.bannerX3.BANNER_mobiles-big-saving-days-ko7y7ui3-store_13WHHOHBBRGH&fm=organic&iid=aa51914f-c16f-444f-946f-3d80e2a03b53.MOBFTYWWZKUAMC24.SEARCH&ssid=i1y1teak2o0000001593152243743",
"https://www.flipkart.com/acer-aspire-7-core-i5-9th-gen-8-gb-512-gb-ssd-windows-10-home-4-graphics-nvidia-geforce-gtx-1650-a715-75g-50sa-gaming-laptop/p/itmff1cbf710ce62?pid=COMFR6AANWZVZM8Y&lid=LSTCOMFR6AANWZVZM8YICAJ6Z&marketplace=FLIPKART&spotlightTagId=BestsellerId_6bo%2Fb5g&srno=b_1_1&otracker=clp_banner_1_5.bannerX3.BANNER_electronics-big-savings-days-store_6V9SXZN3TA8R&fm=neo%2Fmerchandising&iid=1732074f-a893-4a0e-aa04-fc77061d484e.COMFR6AANWZVZM8Y.SEARCH&ppt=browse&ppn=browse&ssid=vgbc2tm24g0000001593152447869",
"https://www.flipkart.com/miss-chief-boys-solid-cotton-blend-t-shirt/p/itmfbrmefpvrakmn?pid=KTBFBRMEUP7U5NZX&lid=LSTKTBFBRMEUP7U5NZX6VANWA&marketplace=FLIPKART&srno=b_1_1&otracker=clp_omu_Kid%2527s%2BClothing_2_15.dealCard.OMU_Kid%2527s%2BClothing_lifestyle-big-shopping-days-june-20-store_RA4IR9FHYPAA_2&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Kid%2527s%2BClothing_NA_dealCard_cc_2_NA_view-all_2&fm=neo%2Fmerchandising&iid=en_hsYyI7LEwxrBMP1g6XBOFWP6bpKM%2Fva4VpvFR3Its6wMukfOdbMcHz6CCrhsHBiV2YmysZddf7E1p7m4QDoX3g%3D%3D&ppt=browse&ppn=browse&ssid=avnnlv9yyo0000001593152460530",
"https://www.flipkart.com/marq-flipkart-6-kg-self-clean-technology-fully-automatic-front-load-in-built-heater-white/p/itmfhdxuquqngvdh?pid=WMNFHDXUBJFT8WWK&lid=LSTWMNFHDXUBJFT8WWKP3GCTG&marketplace=FLIPKART&srno=b_1_2&otracker=clp_banner_2_37.bannerX3.BANNER_tv-and-appliances-big-saving-days-sale-store_YD0AJKN2WMY9&fm=neo%2Fmerchandising&iid=e75c9569-65fe-4aa7-9555-6eaca7f05e6f.WMNFHDXUBJFT8WWK.SEARCH&ppt=browse&ppn=browse&ssid=f82w14gkow0000001593152474178",
"https://www.flipkart.com/marq-flipkart-6-5-kg-twin-shower-technology-fully-automatic-top-load-grey/p/itmfh8g4eacfjhff?pid=WMNFH8G4QJVS9PZQ&lid=LSTWMNFH8G4QJVS9PZQROM89E&marketplace=FLIPKART&spotlightTagId=TrendingId_j9e%2Fabm%2F8qx&srno=b_1_1&otracker=clp_banner_2_37.bannerX3.BANNER_tv-and-appliances-big-saving-days-sale-store_YD0AJKN2WMY9&fm=neo%2Fmerchandising&iid=e75c9569-65fe-4aa7-9555-6eaca7f05e6f.WMNFH8G4QJVS9PZQ.SEARCH&ppt=browse&ppn=browse&ssid=f82w14gkow0000001593152474178",
"https://www.flipkart.com/roop-mantra-charcoal-facial-kit/p/itmf9c2fe730daf9?pid=FCKFZP6R3QKMETNB&lid=LSTFCKFZP6R3QKMETNB2ENID0&marketplace=FLIPKART&srno=b_1_1&otracker=clp_omu_Beauty%2B%2526%2BGrooming_2_4.dealCard.OMU_Beauty%2B%2526%2BGrooming_bgm-big-savings-days-store_L0OOAYFMYYJ3_1&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Beauty%2B%2526%2BGrooming_NA_dealCard_cc_2_NA_view-all_1&fm=neo%2Fmerchandising&iid=en_59f%2FWmhkLvYsYw2%2BLxp0HL6DiwdWqRTBjrXT7AOkzYR46fA5MJj1Po32VUrNB%2BcjRwFMpa%2F3qnG2juRCCs1buA%3D%3D&ppt=browse&ppn=browse&ssid=ulzvbgiu6o0000001593152497726",
"https://www.flipkart.com/royaloak-tulip-solid-wood-bunk-bed/p/itmecmezha5dmzce?pid=BKLECMEZMNGG7YEG&lid=LSTBKLECMEZMNGG7YEGEN4BQQ&marketplace=FLIPKART&srno=b_1_2&otracker=clp_omu_Kids%2BFurniture_2_12.dealCard.OMU_Kids%2BFurniture_furniture-big-savings-days-store_LXAB0MATFFTN_1&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Kids%2BFurniture_NA_dealCard_cc_2_NA_view-all_1&fm=neo%2Fmerchandising&iid=ed5087c5-9ea0-45a5-84c5-ffe8123b0ccc.BKLECMEZMNGG7YEG.SEARCH&ppt=browse&ppn=browse&ssid=ahy9q3urr40000001593152512908",
"https://www.flipkart.com/renberg-rb-8810-stainless-steel-knife-set/p/itmemfbhhmtahh6c?pid=KHKEMFBHHFJQFKGT&lid=LSTKHKEMFBHHFJQFKGTAYKLTB&marketplace=FLIPKART&spotlightTagId=BestsellerId_upp%2Fnwv%2Fotq&srno=b_1_1&otracker=clp_omu_Household%2BRange_3_5.dealCard.OMU_Household%2BRange_home-big-savings-days-store_3CILKJPAGK40_2&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Household%2BRange_NA_dealCard_cc_3_NA_view-all_2&fm=neo%2Fmerchandising&iid=ca74b543-0f98-4568-82bd-3185786ef59f.KHKEMFBHHFJQFKGT.SEARCH&ppt=browse&ppn=browse&ssid=m1lpyr0a800000001593152533623"]
for i in range(len(URL)):
    product_name, product_price=flipkart_detail(URL[i])
    print(product_name, product_price,i)
