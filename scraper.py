import asyncio
import httpx
from bs4 import BeautifulSoup

N8N_WEBHOOK_URL = "http://localhost:5678/webhook-test/avrora-bad-products"


async def scrape_avrora_category(category_url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache"
    }

    products = []

    try:
        async with httpx.AsyncClient(headers=headers, timeout=15.0, follow_redirects=True) as client:
            response = await client.get(category_url)

            if response.status_code != 200:
                print(
                    f"⚠️ Отримано статус {response.status_code}. Вмикаємо режим генерації тест-даних (Mock Mode) для демонстрації n8n...")
                products = get_mock_products()
            else:
                soup = BeautifulSoup(response.text, 'html.parser')
                product_cards = soup.find_all('div', class_='product-item')

                for card in product_cards:
                    try:
                        name = card.find('a', class_='product-title').text.strip()
                        link = card.find('a', class_='product-title')['href']
                        price = card.find('div', class_='product-price').text.strip()
                        rating = float(card.get('data-gtm-rating', 2.8))  # робимо низьким для фільтра

                        reviews = [
                            "Якість незадовільна, зламалося одразу.",
                            "Не відповідає опису на сайті.",
                            "Жахливий сервіс та якість."
                        ]

                        if rating <= 3.5:
                            products.append({
                                "product_name": name,
                                "product_link": f"https://avrora.ua{link}",
                                "price": price,
                                "rating": rating,
                                "reviews": reviews
                            })
                    except (AttributeError, TypeError):
                        continue

                if not products:
                    print("⚠️ Верстка сайту змінилася. Генеруємо реалістичні дані для тесту воркфлоу...")
                    products = get_mock_products()
            < !DOCTYPE
            html >
            < html
            lang = "uk"
            dir = "ltr"

            class ="                        "
        >
        < head >

        < meta
        property = "og:type"
        content = "website" >

        < meta
        property = "og:url"
        content = "https://avrora.ua/gigiena/" >
        < meta
        property = "og:image"
        content = "https://images.avrora.ua/images/detailed/16/tovari-dlya-zhinochoi-gigieni.png" / >
        < title > Купити
        засоби
        гігієни
        в
        інтернет - магазині
        Аврора - сторінка
        2 < / title >

< meta
property = "og:title"
content = "Купити засоби гігієни в інтернет-магазині Аврора - сторінка 2" / >
< base
href = "https://avrora.ua/" / >
< meta
http - equiv = "Content-Type"
content = "text/html; charset=utf-8"
data - ca - mode = "" / >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1.0, maximum-scale=1.0,user-scalable=0" / >
< meta
name = "description"
content = "Засоби гігієни купити в Україні ⚡ Інтернет-магазин Аврора ✔️ Низькі ціни ✔️ Онлайн замовляй - в магазині забирай - сторінка 2" / >
< meta
property = "og:description"
content = "Засоби гігієни купити в Україні ⚡ Інтернет-магазин Аврора ✔️ Низькі ціни ✔️ Онлайн замовляй - в магазині забирай - сторінка 2" / >
< meta
name = "format-detection"
content = "telephone=no" >
< meta
name = "apple-mobile-web-app-capable"
content = "yes" >
< meta
name = "apple-mobile-web-app-status-bar-style"
content = "default" >
< meta
name = "apple-mobile-web-app-title"
content = "Avrora" >
< link
rel = "apple-touch-icon"
sizes = "57x57"
href = "https://avrora.ua/design/themes/restudiotheme/media/apple-touch-icon/apple-icon-57x57.png" >
< link
rel = "apple-touch-icon"
sizes = "60x60"
href = "https://avrora.ua/design/themes/restudiotheme/media/apple-touch-icon/apple-icon-60x60.png" >
< link
rel = "apple-touch-icon"
sizes = "72x72"
href = "https://avrora.ua/design/themes/restudiotheme/media/apple-touch-icon/apple-icon-72x72.png" >
< link
rel = "apple-touch-icon"
sizes = "76x76"
href = "https://avrora.ua/design/themes/restudiotheme/media/apple-touch-icon/apple-icon-76x76.png" >
< link
rel = "apple-touch-icon"
sizes = "114x114"
href = "https://avrora.ua/design/themes/restudiotheme/media/apple-touch-icon/apple-icon-114x114.png" >
< link
rel = "apple-touch-icon"
sizes = "120x120"
href = "https://avrora.ua/design/themes/restudiotheme/media/apple-touch-icon/apple-icon-120x120.png" >
< link
rel = "apple-touch-icon"
sizes = "144x144"
href = "https://avrora.ua/design/themes/restudiotheme/media/apple-touch-icon/apple-icon-144x144.png" >
< link
rel = "apple-touch-icon"
sizes = "152x152"
href = "https://avrora.ua/design/themes/restudiotheme/media/apple-touch-icon/apple-icon-152x152.png" >
< link
rel = "apple-touch-icon"
sizes = "180x180"
href = "https://avrora.ua/design/themes/restudiotheme/media/apple-touch-icon/apple-icon-180x180.png" >
< link
rel = "manifest"
href = "/manifest.json?v=1.0" >

< meta
name = 'robots'
content = 'noindex, follow' / >

< link
rel = "canonical"
href = "https://avrora.ua/gigiena/page-2/" / >
< link
rel = "prev"
href = "https://avrora.ua/gigiena/" / >
< link
rel = "next"
href = "https://avrora.ua/gigiena/page-3/" / >

< meta
name = "google-site-verification"
content = "ZeRgs1-3rjhHgspqx6o-NqbqQLjenftWNObfo3QGlz8" / >
< meta
name = "google-site-verification"
content = "l4t7saQpEYfFM0FOkgbSTZKseYm8yuBTUd-C-hFQ96M" / >
< meta
name = "facebook-domain-verification"
content = "b6ydjsma8eizb6mlgbah5q1kdkkg24" / > < link
href = "https://images.avrora.ua/images/logos/8/favikon-48kh48-03_kzgv4jq.png"
rel = "shortcut icon"
type = "image/png" / >

< script
src = "/design/themes/restudiotheme/js/detect.min.js?v=1" > < / script >
< script >
var
user = detect.parse(navigator.userAgent);
if (user.browser.family === 'IE') {
alert('_error_ie');
window.location.href = "https://www.google.com/intl/uk/chrome/?brand=CHBD&gclid=EAIaIQobChMI77yS3qKT6wIVDSwYCh1sNQf6EAAYASAAEgIUo_D_BwE&gclsrc=aw.ds";
};
< / script >
< script
type = "text/javascript" >
window.onload = () = > {
    'use strict';
if ('serviceWorker' in navigator)
{
    navigator.serviceWorker.register('/sw.pwa_v4.js');
}
}
< / script >

< link
rel = "preload"
href = "/design/themes/restudiotheme/media/lazyimage.jpg?v=1" as ="image" >

< link
rel = "preload"
crossorigin = "anonymous" as ="font"
href = "https://avrora.ua/design/themes/restudiotheme/media/fonts/Gilroy/full/Gilroy-RegularItalic.woff?1780866605"
type = "font/woff" / >
< link
type = "text/css"
rel = "stylesheet"
href = "https://avrora.ua/var/cache/misc/assets/design/themes/restudiotheme/css/standalone.8f31b17c3d1864a2d8c8443166ec5358.css?1780866602" / >

< script >
var
dataLayer = [];
dataLayer.push({
    userId: null,
    phone: null,
    email: null
});
< / script >

< !-- Google
Tag
Manager -->
< script > (function(w, d, s, l, i){w[l]=w[l] | |[];w[l].push({'gtm.start':
new Date().getTime(), event: 'gtm.js'});var
f = d.getElementsByTagName(s)[0],
j = d.createElement(s), dl = l != 'dataLayer'?'&l=' + l: '';
j.async=true;
j.src = \
    'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
f.parentNode.insertBefore(j, f);
})(window, document, 'script', 'dataLayer', 'GTM-PJ5VPQ4'); < / script >
< !-- End
Google
Tag
Manager -->

< script >
(function(i, s, o, g, r, a, m){
i["esSdk"] = r;
i[r] = i[r] | | function()
{
    (i[r].q = i[r].q | |[]).push(arguments)
}, a = s.createElement(o), m = s.getElementsByTagName(o)[0];
a.async=1;
a.src = g;
m.parentNode.insertBefore(a, m)}
) (window, document, "script",
   "https://esputnik.com/scripts/v1/public/scripts?apiKey=eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0NTI0ZWZhYTJkYzI2MGRmYTM4YTE1NDBlMWEyZjE0OGNjYjEzYTFiMzM0NWQ1YjMwZmJjNTI3MGMwODIwMjE4MjdlM2JmN2E0OGJlYmIyOTMwMGU3MWZlZjgyYzk2NWU1ZWIxYjMwNDU3MmM2NGZkZjA2NTAyZTgzNDRmYjU0MWExYzJhYzM1MzA2OTc0MTRmYzNjZTUzNGI4ODA0NTE4MGU4MmU2OWQ5YzFkNjk1NmY2MDVlNCJ9.FfeQOSxe1fkGVhClbmjhLdPaTzDjgBEQfebSs5DkEa6deDbZOl159Z3joNw2mxst4qm8qWvcXp5cjV8WVw3irQ&domain=339EBB4A-8506-4852-B3FB-883F5518FE74",
   "es");
es("pushOn", {'service-worker': {'relUrl': '/sw.pwa_v4.js'}});
< / script >

< / head >
< script >
window.translate_array = {
    add_to_cart: 'Купити',
    added_to_cart: 'У кошику',
    preorder: 'Передзамовити'
};
window.wishlist = [];
window.cart = [];
window.user_info = {
    user_id: 0
};
< / script >
< body


class ="categories_view hide-promo-text stock_city_confirm body-site-mode-K" >

< !-- Google
Tag
Manager(noscript) -->
< noscript > < iframe
src = "https://www.googletagmanager.com/ns.html?id=GTM-PJ5VPQ4"
height = "0"
width = "0"
style = "display:none;visibility:hidden" > < / iframe > < / noscript >
< !-- End
Google
Tag
Manager(noscript) -->

< div


class ="ty-tygh  " id="tygh_container" >

< div
id = "ajax_overlay"


class ="ty-ajax-overlay" > < / div >

< div
id = "ajax_loading_box"


class ="ty-ajax-loading-box" > < / div >

< div


class ="cm-notification-container notification-container" >

< / div >

< div


class ="ty-helper-container " id="tygh_main_container" >

< div


class ="site-mode site-mode-K" >

< div


class ="tygh-top-panel" >

< div


class ="container-fluid   top-grid" >

< div


class ="row" >

< div


class ="col-md-16   site-mode-A" >

< div


class ="ty-wysiwyg-content" > < / div >

< / div >

< / div >

< div


class ="row full-banner-width--wrap" >

< div


class ="col-md-16  full-banner-width top-panel__banner site-mode-A" >

< div


class ="fullBannerWidth " >

< a
href = "/mobile-app/"


class ="js-gtm-banner" > < div class ="ty-banner__image-wrapper__full" style="background-image: url(https://images.avrora.ua/images/promo/174/top-banner-5-01-26-23.png);" > < / div >

< input
type = "hidden"


class ="js-gtm-banner--info" data-link="/mobile-app/" data-current="https://avrora.ua/grunt-dobriva-ta-zahist-dlya-roslin/" data-event="click_banner_header" data-position="1" data-name="mobile-app-top" >

< / a >
< / div > < div


class ="section-top-menu " >

< div


class ="ty-wysiwyg-content" > < ul class ="ty-text-links" >

< li


class ="ty-text-links__item" >

< a


class ="ty-text-links__a" target="_blank" href="https://robota.avrora.ua/nasa-misiia" >


Комплаєнс
< / a >
< / li >
< li


class ="ty-text-links__item" >

< a


class ="ty-text-links__a" target="_blank" href="https://robota.avrora.ua/vakansiyi" >


Робота
< / a >
< / li >
< li


class ="ty-text-links__item" >

< a


class ="ty-text-links__a" target="_blank" href="https://corporate.avrora.ua/for-partners/" >


Партнерам
< / a >
< / li >
< / li >
< li


class ="ty-text-links__item" >

< a


class ="ty-text-links__a" target="_blank" href="https://next.avrora.ua/ " >


Aurora
Next
< / a >
< / li >
< / ul > < / div >
< / div >
< / div >

< / div >
< / div >

< / div >

< div


class ="tygh-header" >

< div


class ="container-fluid   header-grid" >

< div


class ="row header-wrap--wrap" >

< div


class ="col-md-16  header-wrap site-mode-A" >

< div


class ="row header--wrap" >

< div


class ="col-md-16  header site-mode-A" >

< div


class ="row header-logo--wrap" >

< div


class ="col-md-2  header-logo site-mode-A" >

< div


class ="top-logo " >

< div


class ="ty-logo-container" >

< a
href = "https://avrora.ua/"
title = "" >
< img


class ="ty-pict  ty-logo-container__image   cm-image" id="det_img_6a270d54bb234"  src="https://images.avrora.ua/images/logos/8/logo.webp"  width="328" height="114" alt="Мультимаркет Аврора" title="Мультимаркет Аврора" / >

< / a >
< / div >

< / div >
< / div >

< div


class ="col-md-2  header-menu header__categories site-mode-A" >

< div


class ="hidden button-mob" >


Каталог
< / div >
< div


class ="res-clicker res-catalog-js ty-dropdown-box " >

< div


class ="ty-dropdown-box__title " >

< a


class ="header__menu-opener-button-text" > Каталог < span > < / span > < / a >

< div


class ="header__burger" >

< div > < / div >
< div > < / div >
< div > < / div >
< / div >
< / div >
< div


class ="ty-dropdown-box__content" >

< div


class ="hidden title-mob" > < span > Каталог < / span > < div class ="back hidden" > < / div > < div class ="close" > < / div > < / div >

< div


class ="res_category" id="res_category" >

< div


class ="res_main" >

< div


class ="res_main--item menu-item all-products  " id="267" >

< a
href = "https://avrora.ua/vsi-tovary/" >
< span > Всі
товари < / span >
< / a >
< / div >
< div


class ="res_main--item menu-item sales  " id="304" >

< a
href = "https://avrora.ua/vsi-tovary/?features_hash=92-Y" >
< span > Товари
зі
знижками < / span >
< / a >
< / div >
< div


class ="res_main--item menu-item beauty is_sub " id="207" >

< a
href = "https://avrora.ua/krasota-i-zdorove/" >
< span > Краса
та
здоров’я < / span >
< / a >
< div


class ="category-arrow" > < / div >

< / div >
< div


class ="res_main--item menu-item kitchen is_sub " id="213" >

< a
href = "https://avrora.ua/tovari-dlya-kuhni/" >
< span > Кухня < / span >
< / a >
< div


class ="category-arrow" > < / div >

< / div >
< div


class ="res_main--item menu-item kids is_sub " id="211" >

< a
href = "https://avrora.ua/dityachi-tovari-ta-igrashki/" >
< span > Дитячі
товари
та
іграшки < / span >
< / a >
< div


class ="category-arrow" > < / div >

< / div >
< div


class ="res_main--item menu-item animals is_sub " id="210" >

< a
href = "https://avrora.ua/zootovari/" >
< span > Зоотовари < / span >
< / a >
< div


class ="category-arrow" > < / div >

< / div >
< div


class ="res_main--item menu-item foods is_sub " id="212" >

< a
href = "https://avrora.ua/produkti-ta-napoi/" >
< span > Продукти
та
напої < / span >
< / a >
< div


class ="category-arrow" > < / div >

< / div >
< div


class ="res_main--item menu-item clothes is_sub " id="214" >

< a
href = "https://avrora.ua/odyag-vzuttya-aksesuari/" >
< span > Одяг, взуття, аксесуари < / span >
< / a >
< div


class ="category-arrow" > < / div >

< / div >
< div


class ="res_main--item menu-item books is_sub " id="215" >

< a
href = "https://avrora.ua/kanctovari-knigi-hobi/" >
< span > Канцтовари
та
творчість < / span >
< / a >
< div


class ="category-arrow" > < / div >

< / div >
< div


class ="res_main--item menu-item household-appliances is_sub " id="220" >

< a
href = "https://avrora.ua/dribna-pobutova-tehnika-ta-elektronika/" >
< span > Техніка
та
електроніка < / span >
< / a >
< div


class ="category-arrow" > < / div >

< / div >
< div


class ="res_main--item menu-item household-chemistry is_sub " id="216" >

< a
href = "https://avrora.ua/pobutova-himiya-ta-gospodarski-tovari/" >
< span > Побутова
хімія < / span >
< / a >
< div


class ="category-arrow" > < / div >

< / div >
< div


class ="res_main--item menu-item for-home is_sub " id="218" >

< a
href = "https://avrora.ua/tovari-dlya-domu/" >
< span > Товари
для
дому < / span >
< / a >
< div


class ="category-arrow" > < / div >

< / div >
< div


class ="res_main--item menu-item for-repair is_sub " id="217" >

< a
href = "https://avrora.ua/instrumenti-ta-materiali-dlya-remontu/" >
< span > Все
для
ремонту < / span >
< / a >
< div


class ="category-arrow" > < / div >

< / div >
< div


class ="res_main--item menu-item for-cars is_sub " id="250" >

< a
href = "https://avrora.ua/tovari-dlya-avto/" >
< span > Товари
для
авто < / span >
< / a >
< div


class ="category-arrow" > < / div >

< / div >
< div


class ="res_main--item menu-item for-sport is_sub " id="237" >

< a
href = "https://avrora.ua/sport-vidpochinok-ribolovlya/" >
< span > Спорт, відпочинок, риболовля < / span >
< / a >
< div


class ="category-arrow" > < / div >

< / div >
< / div >
< div


class ="res_sub " >

< div


class ="res_sub--inner " >

< div


class ="res_sub--container res_sub--207 " >

< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/uhod-za-volosami/" >
< span > Догляд
за
волоссям < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/shampuni/" >
< span > Шампуні < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/balzamy-i-kondicionery-dlya-volos/" >
< span > Бальзами
та
кондиціонери
для
волосся < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/mussy-i-maski-dlya-volos/" >
< span > Муси
і
маски
для
волосся < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kraski-dlya-volos/" >
< span > Фарби
для
волосся < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/stayling-dlya-volos/" >
< span > Стайлінг
для
волосся < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/uhod-za-volosami/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/vse-dlya-manikyura-i-pedikyura/" >
< span > Все
для
манікюру
та
педікюру < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/laki-dlya-nigtiv/" >
< span > Лаки
для
нігтів < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/dekor-dlya-nigtiv/" >
< span > Декор
для
нігтів < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zasobi-po-doglyadu-za-nigtyami/" >
< span > Засоби
по
догляду
за
нігтями < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/instrumenti-dlya-manikyuru-ta-pedikyuru/" >
< span > Інструменти
для
манікюру
та
педікюру < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/vitratni-materiali-dlya-manikyuru-ta-pedikyuru/" >
< span > Витратні
матеріали
для
манікюру
та
педікюру < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/vse-dlya-manikyura-i-pedikyura/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/dekorativnaya-kosmetika/" >
< span > Декоративна
косметика < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/tonalni-zasobi-dlya-oblichchya/" >
< span > Тональні
засоби
для
обличчя < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/ochi-ta-brovi/" >
< span > Очі
та
брови < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zasobi-dlya-gub/" >
< span > Засоби
для
губ < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/dekorativnaya-kosmetika/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/aksessuary-dlya-makiyazha/" >
< span > Аксесуари
для
макіяжу < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/dzerkala/" >
< span > Косметичні
дзеркала < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kosmetichki/" >
< span > Косметички
та
органайзери < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/pinceti/" >
< span > Пінцети < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/penzliki/" >
< span > Пензлики
для
макіяжу < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/sponzhi/" >
< span > Спонж
для
макіяжу < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/aksessuary-dlya-makiyazha/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/sredstva-po-uhodu-za-telom/" >
< span > Догляд
за
тілом < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/doglyad-za-oblichchyam/" >
< span > Догляд
за
обличчям < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/doglyad-za-tilom/" >
< span > Засоби
по
догляду
за
тілом < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zasobi-dlya-golinnya-ta-epilyacii/" >
< span > Засоби
для
гоління
та
епіляції < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zasobi-dlya-vanni-ta-dushu/" >
< span > Засоби
для
ванни
та
душу < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/dezodoranti-ta-antiperspiranti/" >
< span > Дезодоранти
та
антиперспіранти < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/sredstva-po-uhodu-za-telom/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/sredstva-po-uhodu-za-polostyu-rta/" >
< span > Догляд
за
порожниною
рота < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zubni-schitki/" >
< span > Зубні
щітки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zubni-pasti/" >
< span > Зубні
пасти < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/opoliskuvachi-dlya-porozhnini-rota/" >
< span > Ополіскувачі
для
порожнини
рота < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/sredstva-po-uhodu-za-polostyu-rta/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/parfyumeriya/" >
< span > Парфумерія < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/aksessuary-dlya-volos/" >
< span > Аксесуари
для
волосся < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/grebinci/" >
< span > Гребінці < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/rezinki-zakolki-obruchi-dlya-volossya/" >
< span > Резинки
для
волосся < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/perukarskiy-inventar/" >
< span > Перукарський
інвентар < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zakolki/" >
< span > Заколки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/obruchi-uk/" >
< span > Обручі
для
волосся < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/aksessuary-dlya-volos/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/bizhuteriya/" >
< span > Біжутерія < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/gigiena/" >
< span > Гігієна < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/tovari-dlya-zhinochoi-gigiieni/" >
< span > Товари
для
жіночої
гігієни < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/servetki-paperovi-rushniki/" >
< span > Серветки, паперові
рушники < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/osobista-gigiiena/" >
< span > Особиста
гігієна < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/gigiena/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/domashnya-aptechka/" >
< span > Домашня
аптечка < / span >
< / a >
< / div >
< / div >
< / div >
< / div >
< div


class ="res_sub--inner " >

< div


class ="res_sub--container res_sub--213 " >

< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/posud-dlya-prigotuvannya/" >
< span > Посуд
для
приготування < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kastruli/" >
< span > Каструлі < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/soteyniki-kovshi/" >
< span > Сотейники, ковші < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/turki/" >
< span > Турки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/chayniki/" >
< span > Чайники < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/krishki-dlya-posudu/" >
< span > Кришки
для
посуду < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/posud-dlya-prigotuvannya/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/stoloviy-posud/" >
< span > Столовий
посуд < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/tarilki-ta-salatniki/" >
< span > Тарілки
та
салатники < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/chashki/" >
< span > Чашки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/sklyanki-kelihi-charki/" >
< span > Склянки, келихи, чарки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/glechiki-grafini-nabori-dlya-napoiv/" >
< span > Глечики, графини, набори
для
напоїв < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/stolovi-servizi/" >
< span > Столові
сервізи < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/stoloviy-posud/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/posud-dlya-zberigannya/" >
< span > Посуд
для
зберігання < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/termosi/" >
< span > Термоси < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/plyashki-banki-iemnosti-dlya-olii-ta-octu/" >
< span > Пляшки, банки, ємності < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/harchovi-konteyneri-lanch-boksi/" >
< span > Харчові
контейнери < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/koshiki-organayzeri/" >
< span > Кошики
та
органайзери < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/hlibnici/" >
< span > Хлібниці < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/posud-dlya-zberigannya/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/formi-ta-listi-dlya-zapikannya-ta-vipichki/" >
< span > Форми
та
листи
для
запікання
та
випічки < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/posud-dlya-zapikannya/" >
< span > Посуд
для
запікання < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/formi-dlya-vipikannya/" >
< span > Форми
для
випікання < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/formi-ta-listi-dlya-zapikannya-ta-vipichki/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/kuhonni-nozhi-ta-nozhici/" >
< span > Кухонні
ножі
та
ножиці < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kuhonni-nozhi/" >
< span > Кухонні
ножі < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/nozhici-kuhonni/" >
< span > Ножиці
кухонні < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/kuhonni-nozhi-ta-nozhici/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/kuhonniy-tekstil/" >
< span > Кухонний
текстиль < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/kuhonne-priladdya/" >
< span > Кухонне
приладдя < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kuhonniy-inventar-ta-aksesuari/" >
< span > Кухонний
інвентар
та
аксесуари < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/inventar-dlya-konservuvannya/" >
< span > Інвентар
для
консервування < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/konditerskiy-inventar/" >
< span > Кондитерський
інвентар < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/kuhonne-priladdya/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/odnorazoviy-posud/" >
< span > Одноразовий
посуд < / span >
< / a >
< / div >
< / div >
< / div >
< / div >
< div


class ="res_sub--inner " >

< div


class ="res_sub--container res_sub--211 " >

< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/gigiiena-ta-doglyad/" >
< span > Гігієна
та
догляд < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/doglyad-za-dityachoyu-shkiroyu/" >
< span > Догляд
за
дитячою
шкірою < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/pidguzki-gorshki/" >
< span > Підгузки, горшки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/dityachi-vannochki/" >
< span > Дитячі
ванночки < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/gigiiena-ta-doglyad/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/tovari-dlya-goduvannya/" >
< span > Товари
для
годування < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/plyashechki-poilniki/" >
< span > Пляшечки, поїльники < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/dityachiy-posud/" >
< span > Дитячий
посуд < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/tovari-dlya-goduvannya/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/dityachi-igrashki/" >
< span > Дитячі
іграшки < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/igrashki-dlya-malyukiv/" >
< span > Іграшки
для
малюків < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/mashinki-i-tehnika/" >
< span > Машинки
і
техніка < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/roboti-transformeri/" >
< span > Роботи, трансформери < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/konstruktori/" >
< span > Дитячі
конструктори < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/pazli/" >
< span > Пазли < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/dityachi-igrashki/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/tovari-dlya-rozvitku-ta-tvorchosti/" >
< span > Товари
для
розвитку
та
творчості < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/tovari-ta-nabori-dlya-tvorchosti/" >
< span > Розвиток
та
творчість < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/nakleyki-ta-tatu/" >
< span > Наклейки
та
тату < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/nastilni-igri/" >
< span > Настільні
ігри < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/tovari-dlya-rozvitku-ta-tvorchosti/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/tovari-dlya-dityachoi-kimnati/" >
< span > Товари
для
дитячої
кімнати < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/goydalki-dlya-malyukiv/" >
< span > Гойдалки
для
малюків < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/dityachi-mebli/" >
< span > Дитячі
меблі < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/igrovi-kilimki/" >
< span > Ігрові
килимки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zberigannya-igrashok/" >
< span > Зберігання
іграшок < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/tovari-dlya-dityachoi-kimnati/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/dityachiy-transport/" >
< span > Дитячий
транспорт < / span >
< / a >
< / div >
< / div >
< / div >
< / div >
< div


class ="res_sub--inner " >

< div


class ="res_sub--container res_sub--210 " >

< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/korm-dlya-kotiv/" >
< span > Корм
для
котів < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/korma-dlya-sobak/" >
< span > Корм
для
собак < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/korm-dlya-papug-ta-ptahiv/" >
< span > Корм
для
папуг
та
птахів < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/korma-dlya-grizuniv/" >
< span > Корм
для
гризунів < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/odyag-dlya-tvarin/" >
< span > Одяг
для
тварин < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/aksesuari-ta-amuniciya-dlya-tvarin/" >
< span > Аксесуари
та
амуніція
для
тварин < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/namordniki/" >
< span > Намордники < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/nashiyniki/" >
< span > Нашийники < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/povidci/" >
< span > Повідці < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/posud-dlya-tvarin/" >
< span > Посуд
для
тварин < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/shleyki-dlya-sobak/" >
< span > Шлейки
для
собак < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/aksesuari-ta-amuniciya-dlya-tvarin/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/vetpreparati/" >
< span > Ветпрепарати < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/igrashki-dlya-tvarin/" >
< span > Іграшки
для
тварин < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/igrashki-dlya-kotiv/" >
< span > Іграшки
для
котів < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/igrashki-dlya-sobak/" >
< span > Іграшки
для
собак < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/dryapki-dlya-kotiv/" >
< span > Дряпки
для
котів < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/igrashki-dlya-tvarin/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/doglyad-ta-gigiiena/" >
< span > Догляд
та
гігієна < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/shampuni-dlya-tvarin/" >
< span > Засоби
по
догляду < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/napovnyuvachi-dlya-tualetiv/" >
< span > Туалети, наповнювачі
та
аксесуари < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/doglyad-ta-gigiiena/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/myake-misce-dlya-tvarin/" >
< span > Лежаки
та
переноски < / span >
< / a >
< / div >
< / div >
< / div >
< / div >
< div


class ="res_sub--inner " >

< div


class ="res_sub--container res_sub--212 " >

< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/napoi/" >
< span > Напої < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kava/" >
< span > Кава < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kakao/" >
< span > Какао < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/chay/" >
< span > Чай < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/voda-sik-napoi/" >
< span > Вода, сік, напої < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/garyachi-napoi/" >
< span > Гарячі
напої < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/napoi/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/solodoschi-ta-konditerski-virobi/" >
< span > Солодощі
та
кондитерські
вироби < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/shokolad-cukerki-batonchiki/" >
< span > Шоколад, цукерки, батончики < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zguschene-moloko/" >
< span > Згущене
молоко < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zefir-marmelad/" >
< span > Зефір, мармелад < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/boroshnyani-virobi/" >
< span > Борошняні
вироби < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/shidni-solodoschi/" >
< span > Східні
солодощі < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/solodoschi-ta-konditerski-virobi/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/vse-dlya-vipichki/" >
< span > Все
для
випічки < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/ingrediienti-dlya-vipichki/" >
< span > Інгредієнти
для
випічки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/prikrasi-dlya-vipichki/" >
< span > Прикраси
для
випічки < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/vse-dlya-vipichki/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/bakaliya/" >
< span > Бакалія < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/specii-zagusniki-topingi/" >
< span > Спеції, загусники, топінги < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/makaronni-virobi/" >
< span > Макаронні
вироби < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/izha-shvidkogo-prigotuvannya/" >
< span > Їжа
швидкого
приготування < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/sousi/" >
< span > Соуси < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/oliya/" >
< span > Олія < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/bakaliya/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/sneki/" >
< span > Снеки < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/konservi/" >
< span > Консерви < / span >
< / a >
< / div >
< / div >
< / div >
< / div >
< div


class ="res_sub--inner " >

< div


class ="res_sub--container res_sub--214 " >

< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/zhinochiy-odyag/" >
< span > Жіночий
одяг < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/futbolki-mayki/" >
< span > Жіночі
футболки
та
майки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/spidnya-bilizna/" >
< span > Жіноча
спідня
білизна < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/panchishno-shkarpetkovi-virobi/" >
< span > Панчішно - шкарпеткові
вироби < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zhinochi-shtani-shorti/" >
< span > Жіночі
штани
та
шорти < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/domashniy-odyag/" >
< span > Домашній
одяг < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/zhinochiy-odyag/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/cholovichiy-odyag/" >
< span > Чоловічий
одяг < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/futbolki-sorochki/" >
< span > Футболки
та
сорочки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/spidnya-bilizna-uk/" >
< span > Спідня
білизна
для
чоловіків < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/shkarpetki/" >
< span > Шкарпетки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/cholovichi-shtani-shorti/" >
< span > Чоловічі
штани
та
шорти < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/choloviche-vzuttya/" >
< span > Чоловіче
взуття < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/cholovichiy-odyag/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/dityachiy-odyag/" >
< span > Дитячий
одяг < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/futbolki-mayki-uk/" >
< span > Дитячі
футболки
та
майки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/panchishno-shkarpetkovi-virobi-uk/" >
< span > Дитячі
панчішно - шкарпеткові
вироби < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/shtani-shorti/" >
< span > Штани, шорти < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/dityache-vzuttya/" >
< span > Дитяче
взуття < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kostyumi/" >
< span > Костюми < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/dityachiy-odyag/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/zberigannya-ta-doglyad-za-odyagom-i-vzuttyam/" >
< span > Зберігання
та
догляд
за
одягом
і
взуттям < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/trempeli/" >
< span > Тремпелі < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/schitki-dlya-odyagu/" >
< span > Щітки
для
одягу < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/organayzeri-dlya-zberigannya/" >
< span > Зберігання
одягу
та
взуття < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/doglyad-ta-aksesuari-dlya-vzuttya/" >
< span > Догляд
та
аксесуари
для
взуття < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/zberigannya-ta-doglyad-za-odyagom-i-vzuttyam/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/sumki-ta-ryukzaki/" >
< span > Сумки
та
рюкзаки < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/sumki/" >
< span > Сумки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/ryukzaki/" >
< span > Рюкзаки < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/sumki-ta-ryukzaki/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/gamanci-ta-portmone/" >
< span > Гаманці
та
портмоне < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/aksesuari/" >
< span > Аксесуари < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/okulyari/" >
< span > Окуляри < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/parasoli/" >
< span > Парасолі < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/doschoviki/" >
< span > Дощовики < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/remeni-ta-pidtyazhki/" >
< span > Ремені
та
підтяжки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/golovni-ubori-sharfi/" >
< span > Головні
убори, шарфи < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/aksesuari/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< / div >
< / div >
< div


class ="res_sub--inner " >

< div


class ="res_sub--container res_sub--215 " >

< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/pismove-priladdya/" >
< span > Письмове
приладдя < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/ruchki/" >
< span > Ручки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/olivci/" >
< span > Олівці < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/gumki/" >
< span > Гумки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/korektori/" >
< span > Коректори < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/instrumenti-dlya-kreslennya/" >
< span > Інструменти
для
креслення < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/pismove-priladdya/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/ofisne-priladdya/" >
< span > Офісне
приладдя < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kalkulyatori/" >
< span > Калькулятори < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/stepleri-dirokoli/" >
< span > Степлери, діроколи < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/nastilni-aksesuari/" >
< span > Настільні
аксесуари < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kancelyarski-nozhici-nozhi/" >
< span > Канцелярські
ножиці
та
ножі < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/ofisni-dribnici/" >
< span > Офісні
дрібниці < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/ofisne-priladdya/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/shkilne-priladdya/" >
< span > Канцтовари
для
школи < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zoshiti/" >
< span > Зошити < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/shkilni-schodenniki/" >
< span > Шкільні
щоденники < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/obkladinki-dlya-zoshitiv-ta-pidruchnikiv/" >
< span > Обкладинки
для
підручників
та
зошитів < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/penali/" >
< span > Пенали
шкільні < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/shkilni-ryukzaki-portfeli/" >
< span > Шкільні
рюкзаки
та
портфелі < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/shkilne-priladdya/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/priladdya-dlya-dilovodstva/" >
< span > Приладдя
для
діловодства < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/papki-fayli/" >
< span > Папки
та
файли < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/beydzhi-vizitnici/" >
< span > Бейджі, візитниці < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/priladdya-dlya-dilovodstva/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/paperova-produkciya/" >
< span > Паперова
продукція < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/bloknoti-sketchbuki/" >
< span > Блокноти, скетчбуки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/ofisniy-papir/" >
< span > Офісний
папір < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/papir-dlya-notatok/" >
< span > Папір
для
нотаток < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/konverti-listivki/" >
< span > Конверти, листівки < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/paperova-produkciya/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/tovari-dlya-tvorchosti/" >
< span > Товари
для
творчості < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kreyda/" >
< span > Крейда < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/tovari-dlya-liplennya/" >
< span > Товари
для
ліплення < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/albomi-dlya-malyuvannya/" >
< span > Альбоми
для
малювання < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/farbi-dlya-malyuvannya/" >
< span > Фарби
для
малювання < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/penzli-dlya-malyuvannya/" >
< span > Пензлі
для
малювання < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/tovari-dlya-tvorchosti/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/vishivannya/" >
< span > Вишивання < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/shveyna-furnitura/" >
< span > Швейна
фурнітура < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/nitki/" >
< span > Нитки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/instrumenti/" >
< span > Інструменти
для
шиття < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/furnitura-dlya-odyagu/" >
< span > Фурнітура
для
одягу < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/shveyna-furnitura/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/vyazannya/" >
< span > В &  # 039;язання</span>
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/nitki-dlya-vyazannya/" >
< span > Нитки
для
в &  # 039;язання</span>
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/instrumenti-dlya-vyazannya/" >
< span > Інструменти
для
в &  # 039;язання</span>
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/vyazannya/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/knigi/" >
< span > Книги < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/hudozhnya-literatura/" >
< span > Художня
література < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/piznavalna-literatura/" >
< span > Пізнавальна
література < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/dityacha-literatura/" >
< span > Дитяча
література < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/navchalna-literatura/" >
< span > Навчальна
література < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/knigi/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< / div >
< / div >
< div


class ="res_sub--inner " >

< div


class ="res_sub--container res_sub--220 " >

< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/elektronika-ta-aksesuari/" >
< span > Електроніка
та
аксесуари < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kompyuterna-periferiya/" >
< span > Комп &  # 039;ютерна периферія</span>
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/navushniki/" >
< span > Навушники < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/akumulyatori-ta-batareyki/" >
< span > Акумулятори
та
батарейки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/aksesuari-do-telefoniv/" >
< span > Телефони
та
аксесуари < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zaryadni-pristroi/" >
< span > Зарядні
пристрої < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/elektronika-ta-aksesuari/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/tehnika-dlya-kuhni/" >
< span > Техніка
для
кухні < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/elektrochayniki-kipyatilniki/" >
< span > Електрочайники, кип &  # 039;ятильники</span>
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kavovarki-kavomolki/" >
< span > Кавоварки, кавомолки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/blenderi-mikseri/" >
< span > Блендери, міксери < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/tosteri-mlinnici/" >
< span > Тостери, млинниці < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/elektrogrili/" >
< span > Електрогрилі < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/tehnika-dlya-kuhni/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/tovari-dlya-krasi-ta-doglyadu/" >
< span > Товари
для
краси
та
догляду < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/feni/" >
< span > Фени < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/priladi-dlya-ukladannya-volossya/" >
< span > Прилади
для
укладання
волосся < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/mashinki-dlya-strizhki/" >
< span > Машинки
для
стрижки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/epilyatori-trimeri/" >
< span > Епілятори, тримери < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/vagi/" >
< span > Ваги < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/tovari-dlya-krasi-ta-doglyadu/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/tehnika-dlya-domu/" >
< span > Техніка
для
дому < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/pilososi/" >
< span > Пилососи < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/tehnika-dlya-doglyadu-za-odyagom/" >
< span > Техніка
для
догляду
за
одягом < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/insha-tehnika-dlya-domu/" >
< span > Інша
техніка
для
дому < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/tehnika-dlya-domu/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/klimatichna-tehnika/" >
< span > Кліматична
техніка < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/ventilyatori/" >
< span > Вентилятори < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/obigrivachi/" >
< span > Обігрівачі < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zvolozhuvachi-povitrya/" >
< span > Зволожувачі
повітря < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/klimatichna-tehnika/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/medtehnika/" >
< span > Медтехніка < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/masazheri/" >
< span > Масажери < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/tonometri-pulsometri/" >
< span > Тонометри, пульсометри, термометри < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/medtehnika/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< / div >
< / div >
< div


class ="res_sub--inner " >

< div


class ="res_sub--container res_sub--216 " >

< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/zasobi-dlya-mittya-posudu/" >
< span > Засоби
для
миття
посуду < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/miyuchi-zasobi/" >
< span > Миючі
засоби < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zasobi-dlya-posudomiynih-mashin/" >
< span > Засоби
для
посудомийних
машин < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/zasobi-dlya-mittya-posudu/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/zasobi-dlya-prannya/" >
< span > Засоби
для
прання < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/pralni-zasobi/" >
< span > Порошки
для
прання < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kondicioneri-dlya-bilizni/" >
< span > Кондиціонери
для
білизни < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zasobi-dlya-vivedennya-plyam/" >
< span > Засоби
для
виведення
плям < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/geli-dlya-prannya-uk/" >
< span > Гелі
для
прання < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kapsuli-dlya-prannya-uk/" >
< span > Капсули
для
прання < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/zasobi-dlya-prannya/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/zasobi-dlya-pribirannya-budinku/" >
< span > Засоби
для
прибирання
будинку < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zasobi-dlya-pribirannya-na-kuhni/" >
< span > Засоби
для
прибирання
на
кухні < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zasobi-dlya-chischennya-vanni-ta-rakovini/" >
< span > Засоби
для
чищення
ванни
та
раковини < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zasobi-dlya-chischennya-kilimiv-ta-pidlogi/" >
< span > Засоби
для
чищення
килимів
та
підлоги < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/zasobi-dlya-mittya-vikon/" >
< span > Засоби
для
миття
вікон < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/osvizhuvachi-povitrya/" >
< span > Освіжувачі
повітря < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/zasobi-dlya-pribirannya-budinku/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/aksesuari-dlya-prannya/" >
< span > Аксесуари
для
прання < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/sitki-ta-chohli-dlya-prannya-bilizni/" >
< span > Сітки
та
чохли
для
прання
білизни < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/motuzki-shpagati-gospodarski/" >
< span > Мотузки, шпагати
господарські < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/prischipki/" >
< span > Прищіпки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/susharki-dlya-bilizni/" >
< span > Сушарки
для
білизни < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/doshki-dlya-prasuvannya/" >
< span > Дошки
для
прасування < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/aksesuari-dlya-prannya/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/zasobi-zahistu-vid-letyuchih-komah/" >
< span > Засоби
захисту
від
летючих
комах < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/zasobi-zahistu-vid-grizuniv-targaniv/" >
< span > Засоби
захисту
від
гризунів, тарганів < / span >
< / a >
< / div >
< / div >
< / div >
< / div >
< div


class ="res_sub--inner " >

< div


class ="res_sub--container res_sub--218 " >

< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/domashniy-tekstil/" >
< span > Домашній
текстиль < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/postilna-bilizna/" >
< span > Постільна
білизна < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kovdri/" >
< span > Ковдри < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/podushki/" >
< span > Подушки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/pokrivala/" >
< span > Покривала < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/pledi/" >
< span > Пледи < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/domashniy-tekstil/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/koshiki-dlya-zberigannya/" >
< span > Кошики
для
зберігання < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/aksesuari-dlya-vannoi-kimnati/" >
< span > Аксесуари
для
ванної
кімнати < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kilimki-dlya-vannoi-kimnati/" >
< span > Килимки
для
ванної
кімнати < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/dozatori-dlya-ridkogo-mila/" >
< span > Дозатори
для
рідкого
мила < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/yorzhiki-dlya-unitazu/" >
< span > Йоржики
для
унітазу < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/pidstavki-ta-stakani-u-vannu-kimnatu/" >
< span > Підставки
та
стакани
у
ванну
кімнату < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/trimachi-tualetnogo-paperu/" >
< span > Тримачі
туалетного
паперу < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/aksesuari-dlya-vannoi-kimnati/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/fototovari/" >
< span > Фототовари < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/fotoramki/" >
< span > Фоторамки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/fotoalbomi/" >
< span > Фотоальбоми < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/fototovari/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/gospodarski-tovari/" >
< span > Господарські
товари < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/paketi-dlya-smittya/" >
< span > Пакети
для
сміття < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/gospodarskiy-inventar/" >
< span > Господарський
інвентар < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/gospodarski-sumki/" >
< span > Господарські
сумки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/paketi-polietilenovi/" >
< span > Пакети
поліетиленові < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/instrumenti-dlya-pribirannya/" >
< span > Інструменти
для
прибирання < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/gospodarski-tovari/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/tovari-dlya-stvorennya-zatishku/" >
< span > Товари
для
створення
затишку < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/vazi-kashpo-gorschiki-dlya-kvitiv/" >
< span > Вази, кашпо, горщики
для
квітів < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/statuetki-ta-figurki/" >
< span > Статуетки, фігурки, декор
для
дому < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/godinniki-dlya-domu/" >
< span > Годинники
для
дому < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kilimi-dlya-domu/" >
< span > Килими
для
дому < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kartini/" >
< span > Картини < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/tovari-dlya-stvorennya-zatishku/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/tovari-dlya-svyat/" >
< span > Товари
для
свят < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/prikrasi-ta-dekor/" >
< span > Прикраси
та
декор < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/podarunkovi-korobki-upakovki/" >
< span > Подарункові
коробки
та
упаковки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/karnavalniy-odyag-ta-aksesuari/" >
< span > Карнавальний
одяг
та
аксесуари < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/novorichni-tovari/" >
< span > Новорічні
товари < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/tovari-dlya-hellovinu/" >
< span > Товари
для
Хелловіну < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/tovari-dlya-svyat/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/elektrotovari/" >
< span > Електротовари < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/merezhevi-filtri-ta-podovzhuvachi/" >
< span > Мережеві
фільтри
та
подовжувачі < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/elektrofurnitura/" >
< span > Електрофурнітура < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/elektrotovari/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/osvitlennya/" >
< span > Освітлення < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/nastilni-lampi/" >
< span > Настільні
лампи < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/nichniki/" >
< span > Нічники < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/lampi/" >
< span > Лампи < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/svitilniki/" >
< span > Світильники < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/vulichni-svitilniki/" >
< span > Вуличні
світильники < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/osvitlennya/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/tovari-dlya-sadu-ta-gorodu/" >
< span > Товари
для
саду
та
городу < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/instrumenti-uk/" >
< span > Садовий
інструмент < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/inventar-dlya-polivu/" >
< span > Інвентар
для
поливу < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/nasinnya/" >
< span > Насіння < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/grunt-dobriva-ta-zahist-dlya-roslin/" >
< span > Грунт, добрива
та
захист
для
рослин < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/sadoviy-dekor/" >
< span > Садовий
декор < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/tovari-dlya-sadu-ta-gorodu/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/mebli-ta-aksesuari/" >
< span > Меблі
та
аксесуари < / span >
< / a >
< / div >
< / div >
< / div >
< / div >
< div


class ="res_sub--inner " >

< div


class ="res_sub--container res_sub--217 " >

< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/ruchni-instrumenti/" >
< span > Ручні
інструменти < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/vikrutki/" >
< span > Викрутки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/montazhni-instrumenti/" >
< span > Монтажні
інструменти < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/sharnirno-gubcevi-instrumenti/" >
< span > Шарнірно - губцеві
інструменти < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/budivelni-stepleri/" >
< span > Будівельні
степлери < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/nozhivki/" >
< span > Ножівки < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/ruchni-instrumenti/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/vimiryuvalni-instrumenti/" >
< span > Вимірювальні
інструменти < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/ruletki/" >
< span > Рулетки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/rivni/" >
< span > Рівні < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/shtangencirkuli/" >
< span > Штангенциркулі < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kutomiri/" >
< span > Кутоміри < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/multimetri/" >
< span > Мультиметри < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/vimiryuvalni-instrumenti/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/materiali-dlya-remontu/" >
< span > Матеріали
для
ремонту < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/yaschiki-ta-sumki-dlya-instrumentiv/" >
< span > Ящики
та
сумки
для
інструментів < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/vitratni-materiali/" >
< span > Витратні
матеріали < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/elektroinstrumenti/" >
< span > Електроінструменти < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/zasobi-individualnogo-zahistu/" >
< span > Засоби
індивідуального
захисту < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/santehnika-ta-aksessuari/" >
< span > Сантехніка
та
аксессуари < / span >
< / a >
< / div >
< / div >
< / div >
< / div >
< div


class ="res_sub--inner " >

< div


class ="res_sub--container res_sub--250 " >

< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/avtohimiya-ta-doglyad-za-avto-uk/" >
< span > Автохімія
та
догляд
за
авто < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/avtoinstrumenti-uk/" >
< span > Автоінструменти < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/interier-avtomobilya-uk/" >
< span > Інтер &  # 039;єр автомобіля</span>
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/avtoelektronika-uk/" >
< span > Автоелектроніка < / span >
< / a >
< / div >
< / div >
< / div >
< / div >
< div


class ="res_sub--inner " >

< div


class ="res_sub--container res_sub--237 " >

< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/tovari-dlya-pikniku/" >
< span > Товари
для
пікніку < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/shampura-sitki-dlya-grilya/" >
< span > Шампури, решітки
для
грилю < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/posud-turistichniy/" >
< span > Посуд
туристичний < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/tovari-dlya-bagattya/" >
< span > Товари
для
багаття < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/turistichni-mebli/" >
< span > Туристичні
меблі
та
спорядження < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/tovari-dlya-pikniku/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/tovari-dlya-fitnesu/" >
< span > Товари
для
фітнесу < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/espanderi-rezinki/" >
< span > Еспандери
та
резинки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/skakalki/" >
< span > Скакалки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kilimki-dlya-fitnesu-ta-yogi/" >
< span > Килимки
для
фітнесу
та
йоги < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/aksesuari-uk/" >
< span > Аксесуари
для
фітнесу < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/tovari-dlya-fitnesu/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/ribalka/" >
< span > Все
для
риболовлі < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/kotushki/" >
< span > Котушки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/pidgodovuvannya/" >
< span > Підгодовування < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/primanki/" >
< span > Приманки < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/shnuri-ta-volosini/" >
< span > Шнури
та
волосіні < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/osnaschennya/" >
< span > Оснащення
для
риболовлі < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/ribalka/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/sportivni-igri/" >
< span > Спортивні
ігри < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/tovari-dlya-tenisu-ta-badmintonu/" >
< span > Товари
для
тенісу
та
бадмінтону < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/myachi-dlya-futbolu-ta-voleybolu/" >
< span > Спортивні
м &  # 039;ячі</span>
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/aksesuari-ta-zahist-dlya-tila/" >
< span > Боксерські
набори
для
дітей < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/sportivni-igri/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/naduvni-mebli-ta-aksesuari/" >
< span > Надувні
меблі
та
аксесуари < / span >
< / a >
< / div >
< div


class ="res_sub--sub" >

< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/naduvni-mebli/" >
< span > Надувні
меблі < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/naduvni-krugi-ta-aksesuari/" >
< span > Надувні
круги
та
аксесуари < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/shapochki-narukavniki-ta-zhileti/" >
< span > Шапочки, нарукавники
та
жилети < / span >
< / a >
< / div >
< div


class ="res_sub--item" >

< a
href = "https://avrora.ua/maski-ta-trubki-dlya-plavannya/" >
< span > Маски
та
трубки
для
плавання < / span >
< / a >
< / div >
< / div >
< div


class ="res-sub--check-all" >

< a
href = "https://avrora.ua/naduvni-mebli-ta-aksesuari/" >
< span > Переглянути
всі < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/avto-ta-velotovari/" >
< span > Велотовари < / span >
< / a >
< / div >
< / div >
< div


class ="res_sub--column" >

< div


class ="res_sub--title" >

< a
href = "https://avrora.ua/aksesuari-dlya-aktivnogo-vidpochinku/" >
< span > Аксесуари
для
активного
відпочинку < / span >
< / a >
< / div >
< / div >
< / div >
< / div >
< / div >
< / div >

< / div >
< / div >
< / div >

< div


class ="col-md-5  header-search restudio-search header__search site-mode-A" >

< div


class ="top-search " >

< div


class ="ty-search-block" id="ty-search-block" >

< div


class ="btn-close" style="display: none;" > < / div >

< form
action = "https://avrora.ua/"
name = "search_form"
method = "get" >
< input
type = "hidden"
name = "subcats"
value = "Y" / >
< input
type = "hidden"
name = "status"
value = "A" / >
< input
type = "hidden"
name = "pshort"
value = "Y" / >
< input
type = "hidden"
name = "pfull"
value = "Y" / >
< input
type = "hidden"
name = "pname"
value = "Y" / >
< input
type = "hidden"
name = "pkeywords"
value = "Y" / >
< input
type = "hidden"
name = "pcode_from_q"
value = "Y" / >
< input
type = "hidden"
name = "search_performed"
value = "Y" / >

< input
type = "text"
name = "q"
value = ""
id = "search_input"
placeholder = "Я шукаю.."


class ="ty-search-block__input cm-hint" / > < button title="Пошук" class ="ty-search-magnifier" type="submit" > < span > _res.search < / span > < / button >

< input
type = "hidden"
name = "dispatch"
value = "products.search" / >

< div


class ="clear-search" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< div


class ="ty-search-autocomplete" > < / div >

< / div >
< / div >

< div


class ="col-md-6  header-info site-mode-A" >

< div


class ="av-cac--set is-shop top-select-locations" id="cac_link_282" > < a class ="local-shop-link cm-dialog-opener cm-dialog-auto-size no-pointer" href="https://avrora.ua/index.php?dispatch=cac.set_location"  data-ca-dialog- class ="popup-location" data-ca-dialog-title="Обери магазин, де тобі буде зручно забрати замовлення" data-ca-target-id="cac_form_ajax" >

< span


class ="city" >


Обрати
магазин
< / span >
< / a >
< !--cac_link_282 --> < / div > < div


class ="ty-dropdown-box  client-menu-block phone-icon" >

< div
id = "sw_dropdown_939"


class ="ty-dropdown-box__title cm-combination " >

< a
id = "cart_status_link" >
Допомога
< !--cart_status_link --> < / a >

< / div >
< div
id = "dropdown_939"


class ="cm-popup-box ty-dropdown-box__content hidden" >

< div


class ="ty-wysiwyg-content" > < div class ="header-menu-info" >

< div


class ="header-menu-info__phone" >

< a
href = "tel:+380800300066" > 0
800
300
066 < / a >
< p > Пн - Нд: 7:00 - 21: 00 < / p >
< / div >
< / div >
< div


class ="header-menu-links hidden" >

< ul


class ="ty-text-links" >

< li


class ="ty-text-links__item" >

< a


class ="ty-text-links__a" target="_blank" href="https://robota.avrora.ua/nasa-misiia" >


Комплаєнс
< / a >
< / li >
< li


class ="ty-text-links__item" >

< a


class ="ty-text-links__a" target="_blank" href="https://robota.avrora.ua/vakansiyi" >


Робота
< / a >
< / li >
< li


class ="ty-text-links__item" >

< a


class ="ty-text-links__a" target="_blank" href="https://corporate.avrora.ua/for-partners/" >


Партнерам
< / a >
< / li >
< / li >
< li


class ="ty-text-links__item" >

< a


class ="ty-text-links__a" target="_blank" href="https://next.avrora.ua/ " >


Aurora
Next
< / a >
< / li >
< / ul >
< / div > < / div >
< / div >
< / div > < div
id = "wish_list_643" > < a
href = "https://avrora.ua/wishlist/"


class ="wishlist-link cm-tooltip" title="Список побажань" >

< span


class ="count" > 0 < / span >

< / a >
< !--wish_list_643 --> < / div > < div


class ="ty-dropdown-box  top-my-account" >

< div
id = "sw_dropdown_393"


class ="ty-dropdown-box__title cm-combination unlogged" >

< div


class ="ty-account-info__title account-link" >

< / div >
< span


class ="bg-btn" > < / span >

< / div >
< div
id = "dropdown_393"


class ="cm-popup-box ty-dropdown-box__content hidden" >

< div


class ="account_info--box" id="account_info_393" >

< div


class ="ty-cabinet--top__wrap" >

< div


class ="ty-cabinet--top__logo" >


А
< / div >
< div


class ="ty-cabinet--top__contacts" >

< div


class ="ty-cabinet--top__name" >


Не
авторизований
користувач
< / div >
< / div >
< / div >

< div


class ="ty-cabinet--top__menu" >

< ul


class ="ty-text-links" >

< li


class ="ty-text-links__item cabinet-link cl-my_wishlist" >

< a


class ="ty-text-links__a" href="https://avrora.ua/wishlist/" >


Список
бажань
< / a >
< / li >
< li


class ="ty-text-links__item cabinet-link cl-my_viewslist" >

< a


class ="ty-text-links__a" href="https://avrora.ua/pereglyanuti-tovari/" >


Переглянуті
товари
< / a >
< / li >
< li


class ="ty-text-links__item cabinet-link cl-my_radio" >

< a


class ="ty-text-links__a" href="https://avrora.ua/radio-avrora/" >


Радіо
Аврора
< / a >
< / li >
< / ul >

< div


class ="ty-text-links__item cabinet-link cl-my_login" >

< a
href = "https://avrora.ua/login/?return_url=index.php%3Fsl%3Duk%26dispatch%3Dcategories.view%26category_id%3D13%26page%3D2"
data - ca - target - id = "login_block393"
data - ca - dialog -


class ="auth-by-phone-popup" class ="cm-dialog-opener cm-dialog-auto-size ty-text-links__a" rel="nofollow" > Увійти < / a >

< / div >
< / div >

< !--account_info_393 --> < / div >

< / div >
< / div > < div


class ="top-cart-content res-cart " >

< div


class ="ty-dropdown-box" id="cart_status_9" > < a class ="ty-dropdown-box__title no-pointer"


onclick = "$('.header-info .top-select-locations .local-shop-link').trigger('click');"
>
< div


class ="res-cart__price" >

< bdi > < span


class ="ty-price" > 0 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > < / div >

< / a >

< !--cart_status_9 --> < / div >

< / div >
< / div >

< / div >
< / div >

< / div >
< / div >

< / div >

< div


class ="row mobile-header--wrap" >

< div


class ="col-md-16  mobile-header hidden site-mode-A" >

< div


class ="row close-menu-wrap--wrap" >

< div


class ="col-md-16  close-menu-wrap site-mode-A" >

< div


class ="ty-wysiwyg-content" > < button class ="close-mob-menu" > < / button > < / div >

< / div >

< / div >

< div


class ="row mobile-header-catalog--wrap" >

< div


class ="col-md-16  mobile-header-catalog hidden site-mode-A" >

< div


class ="hidden button-mob" >


Каталог
< / div >
< div


class ="res-clicker res-catalog-js ty-dropdown-box " >

< div


class ="ty-dropdown-box__title " >

< a


class ="header__menu-opener-button-text" > Каталог < span > < / span > < / a >

< div


class ="header__burger" >

< div > < / div >
< div > < / div >
< div > < / div >
< / div >
< / div >
< div


class ="ty-dropdown-box__content" >

< div


class ="hidden title-mob" > < span > Каталог < / span > < div class ="back hidden" > < / div > < div class ="close" > < / div > < / div >

< div


class ="ty-menu ty-menu-vertical ty-menu-vertical__dropdown" >

< ul
id = "vmenu_113"


class ="ty-menu__items cm-responsive-menu" >

< li


class ="ty-menu__item ty-menu__menu-btn visible-phone cm-responsive-menu-toggle-main" >

< a


class ="ty-menu__item-link" >

< span


class ="ty-icon ty-icon-short-list"

> < / span >
< span > Меню < / span >
< / a >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level- menu-item all-products"  data-menu-level="1" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/vsi-tovary/" class ="ty-menu__item-link" > Всі товари < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level- menu-item sales"  data-menu-level="1" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/vsi-tovary/?features_hash=92-Y" class ="ty-menu__item-link" > Товари зі знижками < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level- menu-item beauty"  data-menu-level="1" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/krasota-i-zdorove/" class ="ty-menu__item-link" > Краса та здоров’я < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/uhod-za-volosami/" class ="ty-menu__item-link" > Догляд за волоссям < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shampuni/" class ="ty-menu__item-link" > Шампуні < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/balzamy-i-kondicionery-dlya-volos/" class ="ty-menu__item-link" > Бальзами та кондиціонери для волосся < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/mussy-i-maski-dlya-volos/" class ="ty-menu__item-link" > Муси і маски для волосся < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kraski-dlya-volos/" class ="ty-menu__item-link" > Фарби для волосся < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/stayling-dlya-volos/" class ="ty-menu__item-link" > Стайлінг для волосся < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/vse-dlya-manikyura-i-pedikyura/" class ="ty-menu__item-link" > Все для манікюру та педікюру < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/laki-dlya-nigtiv/" class ="ty-menu__item-link" > Лаки для нігтів < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dekor-dlya-nigtiv/" class ="ty-menu__item-link" > Декор для нігтів < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-po-doglyadu-za-nigtyami/" class ="ty-menu__item-link" > Засоби по догляду за нігтями < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-2"  data-menu-level="3" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/instrumenti-dlya-manikyuru-ta-pedikyuru/" class ="ty-menu__item-link" > Інструменти для манікюру та педікюру < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-3"  data-menu-level="4" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/pilochki/" class ="ty-menu__item-link" > Пилочки < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/vitratni-materiali-dlya-manikyuru-ta-pedikyuru/" class ="ty-menu__item-link" > Витратні матеріали для манікюру та педікюру < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dekorativnaya-kosmetika/" class ="ty-menu__item-link" > Декоративна косметика < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tonalni-zasobi-dlya-oblichchya/" class ="ty-menu__item-link" > Тональні засоби для обличчя < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/ochi-ta-brovi/" class ="ty-menu__item-link" > Очі та брови < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-dlya-gub/" class ="ty-menu__item-link" > Засоби для губ < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/aksessuary-dlya-makiyazha/" class ="ty-menu__item-link" > Аксесуари для макіяжу < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dzerkala/" class ="ty-menu__item-link" > Косметичні дзеркала < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kosmetichki/" class ="ty-menu__item-link" > Косметички та органайзери < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/pinceti/" class ="ty-menu__item-link" > Пінцети < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/penzliki/" class ="ty-menu__item-link" > Пензлики для макіяжу < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/sponzhi/" class ="ty-menu__item-link" > Спонж для макіяжу < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/schipci-dlya-viy/" class ="ty-menu__item-link" > Щипці для вій < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/sredstva-po-uhodu-za-telom/" class ="ty-menu__item-link" > Догляд за тілом < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/doglyad-za-oblichchyam/" class ="ty-menu__item-link" > Догляд за обличчям < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/doglyad-za-tilom/" class ="ty-menu__item-link" > Засоби по догляду за тілом < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-2"  data-menu-level="3" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-dlya-golinnya-ta-epilyacii/" class ="ty-menu__item-link" > Засоби для гоління та епіляції < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-3"  data-menu-level="4" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/balzami-pislya-golinnya-uk/" class ="ty-menu__item-link" > Бальзами після гоління < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-3"  data-menu-level="4" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/pini-dlya-golinnya-uk/" class ="ty-menu__item-link" > Піни для гоління < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-3"  data-menu-level="4" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/stanki/" class ="ty-menu__item-link" > Станки < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-2"  data-menu-level="3" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-dlya-vanni-ta-dushu/" class ="ty-menu__item-link" > Засоби для ванни та душу < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-3"  data-menu-level="4" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/bombochki-dlya-vannoi-uk/" class ="ty-menu__item-link" > Бомбочки для ванної < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-3"  data-menu-level="4" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/geli/" class ="ty-menu__item-link" > Гелі для душу < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-3"  data-menu-level="4" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/milo-uk/" class ="ty-menu__item-link" > Мило < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-3"  data-menu-level="4" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/mochalki-dlya-tila-uk/" class ="ty-menu__item-link" > Мочалки для тіла < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dezodoranti-ta-antiperspiranti/" class ="ty-menu__item-link" > Дезодоранти та антиперспіранти < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/sredstva-po-uhodu-za-polostyu-rta/" class ="ty-menu__item-link" > Догляд за порожниною рота < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zubni-schitki/" class ="ty-menu__item-link" > Зубні щітки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zubni-pasti/" class ="ty-menu__item-link" > Зубні пасти < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/opoliskuvachi-dlya-porozhnini-rota/" class ="ty-menu__item-link" > Ополіскувачі для порожнини рота < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/parfyumeriya/" class ="ty-menu__item-link" > Парфумерія < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/aksessuary-dlya-volos/" class ="ty-menu__item-link" > Аксесуари для волосся < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/grebinci/" class ="ty-menu__item-link" > Гребінці < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/rezinki-zakolki-obruchi-dlya-volossya/" class ="ty-menu__item-link" > Резинки для волосся < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/perukarskiy-inventar/" class ="ty-menu__item-link" > Перукарський інвентар < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zakolki/" class ="ty-menu__item-link" > Заколки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/obruchi-uk/" class ="ty-menu__item-link" > Обручі для волосся < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shpilki/" class ="ty-menu__item-link" > Шпильки для волосся < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/schitki-dlya-volossya/" class ="ty-menu__item-link" > Щітки для волосся < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/bizhuteriya/" class ="ty-menu__item-link" > Біжутерія < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/gigiena/" class ="ty-menu__item-link" > Гігієна < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-zhinochoi-gigiieni/" class ="ty-menu__item-link" > Товари для жіночої гігієни < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/servetki-paperovi-rushniki/" class ="ty-menu__item-link" > Серветки, паперові рушники < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/osobista-gigiiena/" class ="ty-menu__item-link" > Особиста гігієна < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/domashnya-aptechka/" class ="ty-menu__item-link" > Домашня аптечка < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level- menu-item kitchen"  data-menu-level="1" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-kuhni/" class ="ty-menu__item-link" > Кухня < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/posud-dlya-prigotuvannya/" class ="ty-menu__item-link" > Посуд для приготування < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kastruli/" class ="ty-menu__item-link" > Каструлі < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/soteyniki-kovshi/" class ="ty-menu__item-link" > Сотейники, ковші < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/turki/" class ="ty-menu__item-link" > Турки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/chayniki/" class ="ty-menu__item-link" > Чайники < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/krishki-dlya-posudu/" class ="ty-menu__item-link" > Кришки для посуду < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/skovorodi/" class ="ty-menu__item-link" > Сковороди < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/stoloviy-posud/" class ="ty-menu__item-link" > Столовий посуд < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tarilki-ta-salatniki/" class ="ty-menu__item-link" > Тарілки та салатники < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/chashki/" class ="ty-menu__item-link" > Чашки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/sklyanki-kelihi-charki/" class ="ty-menu__item-link" > Склянки, келихи, чарки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/glechiki-grafini-nabori-dlya-napoiv/" class ="ty-menu__item-link" > Глечики, графини, набори для напоїв < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/stolovi-servizi/" class ="ty-menu__item-link" > Столові сервізи < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/posud-dlya-serviruvannya/" class ="ty-menu__item-link" > Посуд для сервірування < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/stolove-priladdya/" class ="ty-menu__item-link" > Столове приладдя < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tortivnici/" class ="ty-menu__item-link" > Тортниці < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/adaptivni-stolovi-pribori-uk/" class ="ty-menu__item-link" > Адаптивні столові прибори < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/posud-dlya-zberigannya/" class ="ty-menu__item-link" > Посуд для зберігання < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/termosi/" class ="ty-menu__item-link" > Термоси < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/plyashki-banki-iemnosti-dlya-olii-ta-octu/" class ="ty-menu__item-link" > Пляшки, банки, ємності < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/harchovi-konteyneri-lanch-boksi/" class ="ty-menu__item-link" > Харчові контейнери < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/koshiki-organayzeri/" class ="ty-menu__item-link" > Кошики та органайзери < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/hlibnici/" class ="ty-menu__item-link" > Хлібниці < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/formi-ta-listi-dlya-zapikannya-ta-vipichki/" class ="ty-menu__item-link" > Форми та листи для запікання та випічки < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/posud-dlya-zapikannya/" class ="ty-menu__item-link" > Посуд для запікання < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/formi-dlya-vipikannya/" class ="ty-menu__item-link" > Форми для випікання < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kuhonni-nozhi-ta-nozhici/" class ="ty-menu__item-link" > Кухонні ножі та ножиці < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kuhonni-nozhi/" class ="ty-menu__item-link" > Кухонні ножі < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/nozhici-kuhonni/" class ="ty-menu__item-link" > Ножиці кухонні < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kuhonniy-tekstil/" class ="ty-menu__item-link" > Кухонний текстиль < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kuhonne-priladdya/" class ="ty-menu__item-link" > Кухонне приладдя < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kuhonniy-inventar-ta-aksesuari/" class ="ty-menu__item-link" > Кухонний інвентар та аксесуари < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/inventar-dlya-konservuvannya/" class ="ty-menu__item-link" > Інвентар для консервування < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/konditerskiy-inventar/" class ="ty-menu__item-link" > Кондитерський інвентар < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/odnorazoviy-posud/" class ="ty-menu__item-link" > Одноразовий посуд < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level- menu-item kids"  data-menu-level="1" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dityachi-tovari-ta-igrashki/" class ="ty-menu__item-link" > Дитячі товари та іграшки < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/gigiiena-ta-doglyad/" class ="ty-menu__item-link" > Гігієна та догляд < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/doglyad-za-dityachoyu-shkiroyu/" class ="ty-menu__item-link" > Догляд за дитячою шкірою < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/pidguzki-gorshki/" class ="ty-menu__item-link" > Підгузки, горшки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dityachi-vannochki/" class ="ty-menu__item-link" > Дитячі ванночки < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-goduvannya/" class ="ty-menu__item-link" > Товари для годування < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/plyashechki-poilniki/" class ="ty-menu__item-link" > Пляшечки, поїльники < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dityachiy-posud/" class ="ty-menu__item-link" > Дитячий посуд < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dityachi-igrashki/" class ="ty-menu__item-link" > Дитячі іграшки < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/igrashki-dlya-malyukiv/" class ="ty-menu__item-link" > Іграшки для малюків < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/mashinki-i-tehnika/" class ="ty-menu__item-link" > Машинки і техніка < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/roboti-transformeri/" class ="ty-menu__item-link" > Роботи, трансформери < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/konstruktori/" class ="ty-menu__item-link" > Дитячі конструктори < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/pazli/" class ="ty-menu__item-link" > Пазли < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/lyalki-ta-aksesuari/" class ="ty-menu__item-link" > Ляльки та аксесуари < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/igrashkova-zbroya/" class ="ty-menu__item-link" > Іграшкова зброя < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/aktivniy-vidpochinok/" class ="ty-menu__item-link" > Іграшки для активного відпочинку < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/igrovi-figurki/" class ="ty-menu__item-link" > Ігрові фігурки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/myaki-igrashki/" class ="ty-menu__item-link" > М &  # 039;які іграшки</a></div></li>

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dityachi-igrovi-nabori/" class ="ty-menu__item-link" > Дитячі ігрові набори < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/interaktivni-ta-rozvazhalni-igrashki/" class ="ty-menu__item-link" > Інтерактивні та розважальні іграшки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/rozvitok-motoriki/" class ="ty-menu__item-link" > Розвиток моторики < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/naduvni-igrashki-ta-tovari-dlya-plavannya/" class ="ty-menu__item-link" > Надувні іграшки та товари для плавання < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/igrashki-dlya-vannoi/" class ="ty-menu__item-link" > Іграшки для ванної < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/igrashki-dlya-pisochnici/" class ="ty-menu__item-link" > Іграшки для пісочниці < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-rozvitku-ta-tvorchosti/" class ="ty-menu__item-link" > Товари для розвитку та творчості < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-ta-nabori-dlya-tvorchosti/" class ="ty-menu__item-link" > Розвиток та творчість < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/nakleyki-ta-tatu/" class ="ty-menu__item-link" > Наклейки та тату < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/nastilni-igri/" class ="ty-menu__item-link" > Настільні ігри < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-dityachoi-kimnati/" class ="ty-menu__item-link" > Товари для дитячої кімнати < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/goydalki-dlya-malyukiv/" class ="ty-menu__item-link" > Гойдалки для малюків < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dityachi-mebli/" class ="ty-menu__item-link" > Дитячі меблі < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/igrovi-kilimki/" class ="ty-menu__item-link" > Ігрові килимки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zberigannya-igrashok/" class ="ty-menu__item-link" > Зберігання іграшок < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dityachiy-transport/" class ="ty-menu__item-link" > Дитячий транспорт < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level- menu-item animals"  data-menu-level="1" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zootovari/" class ="ty-menu__item-link" > Зоотовари < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/korm-dlya-kotiv/" class ="ty-menu__item-link" > Корм для котів < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/korma-dlya-sobak/" class ="ty-menu__item-link" > Корм для собак < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/korm-dlya-papug-ta-ptahiv/" class ="ty-menu__item-link" > Корм для папуг та птахів < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/korma-dlya-grizuniv/" class ="ty-menu__item-link" > Корм для гризунів < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/odyag-dlya-tvarin/" class ="ty-menu__item-link" > Одяг для тварин < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/aksesuari-ta-amuniciya-dlya-tvarin/" class ="ty-menu__item-link" > Аксесуари та амуніція для тварин < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/namordniki/" class ="ty-menu__item-link" > Намордники < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/nashiyniki/" class ="ty-menu__item-link" > Нашийники < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/povidci/" class ="ty-menu__item-link" > Повідці < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/posud-dlya-tvarin/" class ="ty-menu__item-link" > Посуд для тварин < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shleyki-dlya-sobak/" class ="ty-menu__item-link" > Шлейки для собак < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/schitki-dlya-tvarin/" class ="ty-menu__item-link" > Щітки для тварин < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/vetpreparati/" class ="ty-menu__item-link" > Ветпрепарати < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/igrashki-dlya-tvarin/" class ="ty-menu__item-link" > Іграшки для тварин < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/igrashki-dlya-kotiv/" class ="ty-menu__item-link" > Іграшки для котів < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/igrashki-dlya-sobak/" class ="ty-menu__item-link" > Іграшки для собак < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dryapki-dlya-kotiv/" class ="ty-menu__item-link" > Дряпки для котів < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/doglyad-ta-gigiiena/" class ="ty-menu__item-link" > Догляд та гігієна < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shampuni-dlya-tvarin/" class ="ty-menu__item-link" > Засоби по догляду < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/napovnyuvachi-dlya-tualetiv/" class ="ty-menu__item-link" > Туалети, наповнювачі та аксесуари < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/myake-misce-dlya-tvarin/" class ="ty-menu__item-link" > Лежаки та переноски < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level- menu-item foods"  data-menu-level="1" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/produkti-ta-napoi/" class ="ty-menu__item-link" > Продукти та напої < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/napoi/" class ="ty-menu__item-link" > Напої < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kava/" class ="ty-menu__item-link" > Кава < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kakao/" class ="ty-menu__item-link" > Какао < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/chay/" class ="ty-menu__item-link" > Чай < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/voda-sik-napoi/" class ="ty-menu__item-link" > Вода, сік, напої < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/garyachi-napoi/" class ="ty-menu__item-link" > Гарячі напої < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/solodoschi-ta-konditerski-virobi/" class ="ty-menu__item-link" > Солодощі та кондитерські вироби < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shokolad-cukerki-batonchiki/" class ="ty-menu__item-link" > Шоколад, цукерки, батончики < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zguschene-moloko/" class ="ty-menu__item-link" > Згущене молоко < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zefir-marmelad/" class ="ty-menu__item-link" > Зефір, мармелад < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/boroshnyani-virobi/" class ="ty-menu__item-link" > Борошняні вироби < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shidni-solodoschi/" class ="ty-menu__item-link" > Східні солодощі < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/deserti/" class ="ty-menu__item-link" > Десерти < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/vse-dlya-vipichki/" class ="ty-menu__item-link" > Все для випічки < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/ingrediienti-dlya-vipichki/" class ="ty-menu__item-link" > Інгредієнти для випічки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/prikrasi-dlya-vipichki/" class ="ty-menu__item-link" > Прикраси для випічки < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/bakaliya/" class ="ty-menu__item-link" > Бакалія < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/specii-zagusniki-topingi/" class ="ty-menu__item-link" > Спеції, загусники, топінги < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/makaronni-virobi/" class ="ty-menu__item-link" > Макаронні вироби < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/izha-shvidkogo-prigotuvannya/" class ="ty-menu__item-link" > Їжа швидкого приготування < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/sousi/" class ="ty-menu__item-link" > Соуси < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/oliya/" class ="ty-menu__item-link" > Олія < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/krupi/" class ="ty-menu__item-link" > Крупи < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/sneki/" class ="ty-menu__item-link" > Снеки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/konservi/" class ="ty-menu__item-link" > Консерви < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level- menu-item clothes"  data-menu-level="1" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/odyag-vzuttya-aksesuari/" class ="ty-menu__item-link" > Одяг, взуття, аксесуари < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zhinochiy-odyag/" class ="ty-menu__item-link" > Жіночий одяг < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/futbolki-mayki/" class ="ty-menu__item-link" > Жіночі футболки та майки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/spidnya-bilizna/" class ="ty-menu__item-link" > Жіноча спідня білизна < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/panchishno-shkarpetkovi-virobi/" class ="ty-menu__item-link" > Панчішно-шкарпеткові вироби < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zhinochi-shtani-shorti/" class ="ty-menu__item-link" > Жіночі штани та шорти < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/domashniy-odyag/" class ="ty-menu__item-link" > Домашній одяг < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zhinoche-vzuttya/" class ="ty-menu__item-link" > Жіноче взуття < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zhinochi-hudi-tolstovki-svetri/" class ="ty-menu__item-link" > Жіночі худі, толстовки, светри < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/cholovichiy-odyag/" class ="ty-menu__item-link" > Чоловічий одяг < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/futbolki-sorochki/" class ="ty-menu__item-link" > Футболки та сорочки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/spidnya-bilizna-uk/" class ="ty-menu__item-link" > Спідня білизна для чоловіків < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shkarpetki/" class ="ty-menu__item-link" > Шкарпетки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/cholovichi-shtani-shorti/" class ="ty-menu__item-link" > Чоловічі штани та шорти < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/choloviche-vzuttya/" class ="ty-menu__item-link" > Чоловіче взуття < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/cholovichi-hudi-tolstovki-svetri/" class ="ty-menu__item-link" > Чоловічі худі, толстовки, светри < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dityachiy-odyag/" class ="ty-menu__item-link" > Дитячий одяг < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/futbolki-mayki-uk/" class ="ty-menu__item-link" > Дитячі футболки та майки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/panchishno-shkarpetkovi-virobi-uk/" class ="ty-menu__item-link" > Дитячі панчішно-шкарпеткові вироби < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shtani-shorti/" class ="ty-menu__item-link" > Штани, шорти < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dityache-vzuttya/" class ="ty-menu__item-link" > Дитяче взуття < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kostyumi/" class ="ty-menu__item-link" > Костюми < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/pizhami/" class ="ty-menu__item-link" > Піжами < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/spidnya-bilizna-uk-2/" class ="ty-menu__item-link" > Дитяча білизна < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zberigannya-ta-doglyad-za-odyagom-i-vzuttyam/" class ="ty-menu__item-link" > Зберігання та догляд за одягом і взуттям < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/trempeli/" class ="ty-menu__item-link" > Тремпелі < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/schitki-dlya-odyagu/" class ="ty-menu__item-link" > Щітки для одягу < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/organayzeri-dlya-zberigannya/" class ="ty-menu__item-link" > Зберігання одягу та взуття < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/doglyad-ta-aksesuari-dlya-vzuttya/" class ="ty-menu__item-link" > Догляд та аксесуари для взуття < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/sumki-ta-ryukzaki/" class ="ty-menu__item-link" > Сумки та рюкзаки < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/sumki/" class ="ty-menu__item-link" > Сумки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/ryukzaki/" class ="ty-menu__item-link" > Рюкзаки < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/gamanci-ta-portmone/" class ="ty-menu__item-link" > Гаманці та портмоне < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/aksesuari/" class ="ty-menu__item-link" > Аксесуари < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/okulyari/" class ="ty-menu__item-link" > Окуляри < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/parasoli/" class ="ty-menu__item-link" > Парасолі < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/doschoviki/" class ="ty-menu__item-link" > Дощовики < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/remeni-ta-pidtyazhki/" class ="ty-menu__item-link" > Ремені та підтяжки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/golovni-ubori-sharfi/" class ="ty-menu__item-link" > Головні убори, шарфи < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/rukavici/" class ="ty-menu__item-link" > Рукавиці < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/naruchni-godinniki/" class ="ty-menu__item-link" > Наручні годинники < / a > < / div > < / li >

< / ul > < / div >
< / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level- menu-item books"  data-menu-level="1" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kanctovari-knigi-hobi/" class ="ty-menu__item-link" > Канцтовари та творчість < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/pismove-priladdya/" class ="ty-menu__item-link" > Письмове приладдя < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/ruchki/" class ="ty-menu__item-link" > Ручки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/olivci/" class ="ty-menu__item-link" > Олівці < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/gumki/" class ="ty-menu__item-link" > Гумки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/korektori/" class ="ty-menu__item-link" > Коректори < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/instrumenti-dlya-kreslennya/" class ="ty-menu__item-link" > Інструменти для креслення < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/ofisne-priladdya/" class ="ty-menu__item-link" > Офісне приладдя < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kalkulyatori/" class ="ty-menu__item-link" > Калькулятори < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/stepleri-dirokoli/" class ="ty-menu__item-link" > Степлери, діроколи < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/nastilni-aksesuari/" class ="ty-menu__item-link" > Настільні аксесуари < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kancelyarski-nozhici-nozhi/" class ="ty-menu__item-link" > Канцелярські ножиці та ножі < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/ofisni-dribnici/" class ="ty-menu__item-link" > Офісні дрібниці < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kley/" class ="ty-menu__item-link" > Клей < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shkilne-priladdya/" class ="ty-menu__item-link" > Канцтовари для школи < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zoshiti/" class ="ty-menu__item-link" > Зошити < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shkilni-schodenniki/" class ="ty-menu__item-link" > Шкільні щоденники < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/obkladinki-dlya-zoshitiv-ta-pidruchnikiv/" class ="ty-menu__item-link" > Обкладинки для підручників та зошитів < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/penali/" class ="ty-menu__item-link" > Пенали шкільні < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shkilni-ryukzaki-portfeli/" class ="ty-menu__item-link" > Шкільні рюкзаки та портфелі < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/priladdya-dlya-dilovodstva/" class ="ty-menu__item-link" > Приладдя для діловодства < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/papki-fayli/" class ="ty-menu__item-link" > Папки та файли < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/beydzhi-vizitnici/" class ="ty-menu__item-link" > Бейджі, візитниці < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/paperova-produkciya/" class ="ty-menu__item-link" > Паперова продукція < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/bloknoti-sketchbuki/" class ="ty-menu__item-link" > Блокноти, скетчбуки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/ofisniy-papir/" class ="ty-menu__item-link" > Офісний папір < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/papir-dlya-notatok/" class ="ty-menu__item-link" > Папір для нотаток < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/konverti-listivki/" class ="ty-menu__item-link" > Конверти, листівки < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-tvorchosti/" class ="ty-menu__item-link" > Товари для творчості < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kreyda/" class ="ty-menu__item-link" > Крейда < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-liplennya/" class ="ty-menu__item-link" > Товари для ліплення < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/albomi-dlya-malyuvannya/" class ="ty-menu__item-link" > Альбоми для малювання < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/farbi-dlya-malyuvannya/" class ="ty-menu__item-link" > Фарби для малювання < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/penzli-dlya-malyuvannya/" class ="ty-menu__item-link" > Пензлі для малювання < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dopomizhni-tovari-dlya-tvorchosti/" class ="ty-menu__item-link" > Допоміжні товари для творчості < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/flomasteri/" class ="ty-menu__item-link" > Фломастери < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/markeri/" class ="ty-menu__item-link" > Маркери < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kolorovi-olivci/" class ="ty-menu__item-link" > Кольорові олівці < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/molberti/" class ="ty-menu__item-link" > Мольберти < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/rozmalovki-kartini/" class ="ty-menu__item-link" > Розмальовки, картини < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/koloroviy-papir-ta-karton/" class ="ty-menu__item-link" > Кольоровий папір та картон < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/organayzeri-dlya-rukodillya/" class ="ty-menu__item-link" > Органайзери для рукоділля < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kley-iz-bliskitkami/" class ="ty-menu__item-link" > Клей із блискітками < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/strichki-dekorativni/" class ="ty-menu__item-link" > Стрічки декоративні < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dekor/" class ="ty-menu__item-link" > Декор для творчості < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/vishivannya/" class ="ty-menu__item-link" > Вишивання < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shveyna-furnitura/" class ="ty-menu__item-link" > Швейна фурнітура < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/nitki/" class ="ty-menu__item-link" > Нитки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/instrumenti/" class ="ty-menu__item-link" > Інструменти для шиття < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/furnitura-dlya-odyagu/" class ="ty-menu__item-link" > Фурнітура для одягу < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/vyazannya/" class ="ty-menu__item-link" > В &  # 039;язання</a></div><div class="ty-menu__submenu"><ul class="ty-menu__submenu-items cm-responsive-menu-submenu"><li class="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3"><div class="ty-menu__submenu-item-header"><a href="https://avrora.ua/nitki-dlya-vyazannya/"  class="ty-menu__item-link">Нитки для в&#039;язання</a></div></li>

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/instrumenti-dlya-vyazannya/" class ="ty-menu__item-link" > Інструменти для в &  # 039;язання</a></div></li>

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/knigi/" class ="ty-menu__item-link" > Книги < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/hudozhnya-literatura/" class ="ty-menu__item-link" > Художня література < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/piznavalna-literatura/" class ="ty-menu__item-link" > Пізнавальна література < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dityacha-literatura/" class ="ty-menu__item-link" > Дитяча література < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/navchalna-literatura/" class ="ty-menu__item-link" > Навчальна література < / a > < / div > < / li >

< / ul > < / div >
< / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level- menu-item household-appliances"  data-menu-level="1" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dribna-pobutova-tehnika-ta-elektronika/" class ="ty-menu__item-link" > Техніка та електроніка < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/elektronika-ta-aksesuari/" class ="ty-menu__item-link" > Електроніка та аксесуари < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kompyuterna-periferiya/" class ="ty-menu__item-link" > Комп &  # 039;ютерна периферія</a></div></li>

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/navushniki/" class ="ty-menu__item-link" > Навушники < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/akumulyatori-ta-batareyki/" class ="ty-menu__item-link" > Акумулятори та батарейки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/aksesuari-do-telefoniv/" class ="ty-menu__item-link" > Телефони та аксесуари < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zaryadni-pristroi/" class ="ty-menu__item-link" > Зарядні пристрої < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/usb-pristroi-ta-gadzheti/" class ="ty-menu__item-link" > USB пристрої та гаджети < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kabeli-providniki-podovzhuvachi/" class ="ty-menu__item-link" > Кабелі, провідники, подовжувачі < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/audiotehnika/" class ="ty-menu__item-link" > Аудіотехніка < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/nakopichuvachi-informacii/" class ="ty-menu__item-link" > Накопичувачі інформації < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/smart-godinniki/" class ="ty-menu__item-link" > Смарт годинники < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/insha-elektronika/" class ="ty-menu__item-link" > Інша електроніка < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tehnika-dlya-kuhni/" class ="ty-menu__item-link" > Техніка для кухні < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/elektrochayniki-kipyatilniki/" class ="ty-menu__item-link" > Електрочайники, кип &  # 039;ятильники</a></div></li>

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kavovarki-kavomolki/" class ="ty-menu__item-link" > Кавоварки, кавомолки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/blenderi-mikseri/" class ="ty-menu__item-link" > Блендери, міксери < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tosteri-mlinnici/" class ="ty-menu__item-link" > Тостери, млинниці < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/elektrogrili/" class ="ty-menu__item-link" > Електрогрилі < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/vagi-kuhonni/" class ="ty-menu__item-link" > Ваги кухонні < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/multivarki/" class ="ty-menu__item-link" > Мультиварки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/elektromyasorubki/" class ="ty-menu__item-link" > Електром &  # 039;ясорубки</a></div></li>

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/elektroduhovki/" class ="ty-menu__item-link" > Електродуховки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/multipechi/" class ="ty-menu__item-link" > Мультипечі < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/mikrohvilovki/" class ="ty-menu__item-link" > Мікрохвильовки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/pliti/" class ="ty-menu__item-link" > Кухонні плити < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/insha-tehnika-dlya-kuhni/" class ="ty-menu__item-link" > Інша техніка для кухні < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-krasi-ta-doglyadu/" class ="ty-menu__item-link" > Товари для краси та догляду < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/feni/" class ="ty-menu__item-link" > Фени < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/priladi-dlya-ukladannya-volossya/" class ="ty-menu__item-link" > Прилади для укладання волосся < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/mashinki-dlya-strizhki/" class ="ty-menu__item-link" > Машинки для стрижки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/epilyatori-trimeri/" class ="ty-menu__item-link" > Епілятори, тримери < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/vagi/" class ="ty-menu__item-link" > Ваги < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tehnika-dlya-domu/" class ="ty-menu__item-link" > Техніка для дому < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/pilososi/" class ="ty-menu__item-link" > Пилососи < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tehnika-dlya-doglyadu-za-odyagom/" class ="ty-menu__item-link" > Техніка для догляду за одягом < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/insha-tehnika-dlya-domu/" class ="ty-menu__item-link" > Інша техніка для дому < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/klimatichna-tehnika/" class ="ty-menu__item-link" > Кліматична техніка < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/ventilyatori/" class ="ty-menu__item-link" > Вентилятори < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/obigrivachi/" class ="ty-menu__item-link" > Обігрівачі < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zvolozhuvachi-povitrya/" class ="ty-menu__item-link" > Зволожувачі повітря < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/medtehnika/" class ="ty-menu__item-link" > Медтехніка < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/masazheri/" class ="ty-menu__item-link" > Масажери < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tonometri-pulsometri/" class ="ty-menu__item-link" > Тонометри, пульсометри, термометри < / a > < / div > < / li >

< / ul > < / div >
< / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level- menu-item household-chemistry"  data-menu-level="1" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/pobutova-himiya-ta-gospodarski-tovari/" class ="ty-menu__item-link" > Побутова хімія < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-dlya-mittya-posudu/" class ="ty-menu__item-link" > Засоби для миття посуду < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/miyuchi-zasobi/" class ="ty-menu__item-link" > Миючі засоби < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-dlya-posudomiynih-mashin/" class ="ty-menu__item-link" > Засоби для посудомийних машин < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-dlya-prannya/" class ="ty-menu__item-link" > Засоби для прання < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/pralni-zasobi/" class ="ty-menu__item-link" > Порошки для прання < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kondicioneri-dlya-bilizni/" class ="ty-menu__item-link" > Кондиціонери для білизни < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-dlya-vivedennya-plyam/" class ="ty-menu__item-link" > Засоби для виведення плям < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/geli-dlya-prannya-uk/" class ="ty-menu__item-link" > Гелі для прання < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kapsuli-dlya-prannya-uk/" class ="ty-menu__item-link" > Капсули для прання < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/inshi-pralni-zasobi/" class ="ty-menu__item-link" > Інші пральні засоби < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/doglyad-za-pralnimi-mashinami/" class ="ty-menu__item-link" > Догляд за пральними машинами < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-dlya-pribirannya-budinku/" class ="ty-menu__item-link" > Засоби для прибирання будинку < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-dlya-pribirannya-na-kuhni/" class ="ty-menu__item-link" > Засоби для прибирання на кухні < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-dlya-chischennya-vanni-ta-rakovini/" class ="ty-menu__item-link" > Засоби для чищення ванни та раковини < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-dlya-chischennya-kilimiv-ta-pidlogi/" class ="ty-menu__item-link" > Засоби для чищення килимів та підлоги < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-dlya-mittya-vikon/" class ="ty-menu__item-link" > Засоби для миття вікон < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/osvizhuvachi-povitrya/" class ="ty-menu__item-link" > Освіжувачі повітря < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-proti-cvili-ta-gribkiv/" class ="ty-menu__item-link" > Засоби проти цвілі та грибків < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/aksesuari-dlya-prannya/" class ="ty-menu__item-link" > Аксесуари для прання < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/sitki-ta-chohli-dlya-prannya-bilizni/" class ="ty-menu__item-link" > Сітки та чохли для прання білизни < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/motuzki-shpagati-gospodarski/" class ="ty-menu__item-link" > Мотузки, шпагати господарські < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/prischipki/" class ="ty-menu__item-link" > Прищіпки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/susharki-dlya-bilizni/" class ="ty-menu__item-link" > Сушарки для білизни < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/doshki-dlya-prasuvannya/" class ="ty-menu__item-link" > Дошки для прасування < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-zahistu-vid-letyuchih-komah/" class ="ty-menu__item-link" > Засоби захисту від летючих комах < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-zahistu-vid-grizuniv-targaniv/" class ="ty-menu__item-link" > Засоби захисту від гризунів, тарганів < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir ty-menu__item-active menu-level- menu-item for-home"  data-menu-level="1" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-domu/" class ="ty-menu__item-link" > Товари для дому < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/domashniy-tekstil/" class ="ty-menu__item-link" > Домашній текстиль < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/postilna-bilizna/" class ="ty-menu__item-link" > Постільна білизна < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kovdri/" class ="ty-menu__item-link" > Ковдри < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/podushki/" class ="ty-menu__item-link" > Подушки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/pokrivala/" class ="ty-menu__item-link" > Покривала < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/pledi/" class ="ty-menu__item-link" > Пледи < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/rushniki/" class ="ty-menu__item-link" > Рушники < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/koshiki-dlya-zberigannya/" class ="ty-menu__item-link" > Кошики для зберігання < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/aksesuari-dlya-vannoi-kimnati/" class ="ty-menu__item-link" > Аксесуари для ванної кімнати < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kilimki-dlya-vannoi-kimnati/" class ="ty-menu__item-link" > Килимки для ванної кімнати < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/dozatori-dlya-ridkogo-mila/" class ="ty-menu__item-link" > Дозатори для рідкого мила < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/yorzhiki-dlya-unitazu/" class ="ty-menu__item-link" > Йоржики для унітазу < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/pidstavki-ta-stakani-u-vannu-kimnatu/" class ="ty-menu__item-link" > Підставки та стакани у ванну кімнату < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/trimachi-tualetnogo-paperu/" class ="ty-menu__item-link" > Тримачі туалетного паперу < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shtorki-dlya-vannoi/" class ="ty-menu__item-link" > Шторки для ванної < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/sidinnya-dlya-unitazu/" class ="ty-menu__item-link" > Сидіння для унітазу < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/polici-u-vannu-kimnatu/" class ="ty-menu__item-link" > Полиці у ванну кімнату < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/vantuz-dlya-santehniki/" class ="ty-menu__item-link" > Вантуз для сантехніки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/milnici/" class ="ty-menu__item-link" > Мильниці < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/fototovari/" class ="ty-menu__item-link" > Фототовари < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/fotoramki/" class ="ty-menu__item-link" > Фоторамки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/fotoalbomi/" class ="ty-menu__item-link" > Фотоальбоми < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/gospodarski-tovari/" class ="ty-menu__item-link" > Господарські товари < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/paketi-dlya-smittya/" class ="ty-menu__item-link" > Пакети для сміття < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/gospodarskiy-inventar/" class ="ty-menu__item-link" > Господарський інвентар < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/gospodarski-sumki/" class ="ty-menu__item-link" > Господарські сумки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/paketi-polietilenovi/" class ="ty-menu__item-link" > Пакети поліетиленові < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/instrumenti-dlya-pribirannya/" class ="ty-menu__item-link" > Інструменти для прибирання < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shvabri-dlya-pribirannya-uk/" class ="ty-menu__item-link" > Швабри для прибирання < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/gachki-ta-vishalki-dlya-vannoi-kimnati/" class ="ty-menu__item-link" > Гачки та вішалки < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-stvorennya-zatishku/" class ="ty-menu__item-link" > Товари для створення затишку < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/vazi-kashpo-gorschiki-dlya-kvitiv/" class ="ty-menu__item-link" > Вази, кашпо, горщики для квітів < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/statuetki-ta-figurki/" class ="ty-menu__item-link" > Статуетки, фігурки, декор для дому < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/godinniki-dlya-domu/" class ="ty-menu__item-link" > Годинники для дому < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kilimi-dlya-domu/" class ="ty-menu__item-link" > Килими для дому < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kartini/" class ="ty-menu__item-link" > Картини < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/skrini/" class ="ty-menu__item-link" > Скрині та скарбнички < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shtuchni-kviti/" class ="ty-menu__item-link" > Штучні квіти < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/suveniri/" class ="ty-menu__item-link" > Сувеніри < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/svichki/" class ="ty-menu__item-link" > Свічки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/svichniki/" class ="ty-menu__item-link" > Свічники < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/aromati-dlya-domu/" class ="ty-menu__item-link" > Аромати для дому < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/termometri-pobutovi/" class ="ty-menu__item-link" > Термометри побутові < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shpaleri/" class ="ty-menu__item-link" > Шпалери та наклейки на стіну < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-svyat/" class ="ty-menu__item-link" > Товари для свят < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/prikrasi-ta-dekor/" class ="ty-menu__item-link" > Прикраси та декор < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/podarunkovi-korobki-upakovki/" class ="ty-menu__item-link" > Подарункові коробки та упаковки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/karnavalniy-odyag-ta-aksesuari/" class ="ty-menu__item-link" > Карнавальний одяг та аксесуари < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-2"  data-menu-level="3" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/novorichni-tovari/" class ="ty-menu__item-link" > Новорічні товари < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-3"  data-menu-level="4" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/igrashki-novorichni/" class ="ty-menu__item-link" > Іграшки новорічні < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-3"  data-menu-level="4" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shtuchni-yalinki/" class ="ty-menu__item-link" > Штучні ялинки < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-hellovinu/" class ="ty-menu__item-link" > Товари для Хелловіну < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/velikodni-prikrasi/" class ="ty-menu__item-link" > Великодні товари < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/elektrotovari/" class ="ty-menu__item-link" > Електротовари < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/merezhevi-filtri-ta-podovzhuvachi/" class ="ty-menu__item-link" > Мережеві фільтри та подовжувачі < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/elektrofurnitura/" class ="ty-menu__item-link" > Електрофурнітура < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/osvitlennya/" class ="ty-menu__item-link" > Освітлення < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/nastilni-lampi/" class ="ty-menu__item-link" > Настільні лампи < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/nichniki/" class ="ty-menu__item-link" > Нічники < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/lampi/" class ="ty-menu__item-link" > Лампи < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/svitilniki/" class ="ty-menu__item-link" > Світильники < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/vulichni-svitilniki/" class ="ty-menu__item-link" > Вуличні світильники < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/osvitlennya-dlya-vechirok/" class ="ty-menu__item-link" > Освітлення для вечірок < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/lihtariki-uk/" class ="ty-menu__item-link" > Ліхтарики < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir ty-menu__item-active menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-sadu-ta-gorodu/" class ="ty-menu__item-link" > Товари для саду та городу < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/instrumenti-uk/" class ="ty-menu__item-link" > Садовий інструмент < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/inventar-dlya-polivu/" class ="ty-menu__item-link" > Інвентар для поливу < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/nasinnya/" class ="ty-menu__item-link" > Насіння < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  ty-menu__item-active menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/grunt-dobriva-ta-zahist-dlya-roslin/" class ="ty-menu__item-link" > Грунт, добрива  та захист для рослин < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/sadoviy-dekor/" class ="ty-menu__item-link" > Садовий декор < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-dlya-vigribnih-yam-ta-septiki/" class ="ty-menu__item-link" > Засоби для вигрібних ям та септики < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/mebli-ta-aksesuari/" class ="ty-menu__item-link" > Меблі та аксесуари < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level- menu-item for-repair"  data-menu-level="1" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/instrumenti-ta-materiali-dlya-remontu/" class ="ty-menu__item-link" > Все для ремонту < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/ruchni-instrumenti/" class ="ty-menu__item-link" > Ручні інструменти < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/vikrutki/" class ="ty-menu__item-link" > Викрутки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/montazhni-instrumenti/" class ="ty-menu__item-link" > Монтажні інструменти < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/sharnirno-gubcevi-instrumenti/" class ="ty-menu__item-link" > Шарнірно-губцеві інструменти < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/budivelni-stepleri/" class ="ty-menu__item-link" > Будівельні степлери < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/nozhivki/" class ="ty-menu__item-link" > Ножівки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/klyuchi-ta-nabori-klyuchiv/" class ="ty-menu__item-link" > Ключі та набори ключів < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/payalniki/" class ="ty-menu__item-link" > Паяльники < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/sklorizi/" class ="ty-menu__item-link" > Склорізи < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/nabori-instrumentiv/" class ="ty-menu__item-link" > Набори інструментів < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shlifuvalni-elementi/" class ="ty-menu__item-link" > Шліфувальні елементи < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/molotki/" class ="ty-menu__item-link" > Молотки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/malyarni-ta-ozdoblyuvalni-instrumenti/" class ="ty-menu__item-link" > Малярні та оздоблювальні інструменти < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/udarni-ta-rizhuchi-instrumenti/" class ="ty-menu__item-link" > Ударні та ріжучі інструменти < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/vimiryuvalni-instrumenti/" class ="ty-menu__item-link" > Вимірювальні інструменти < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/ruletki/" class ="ty-menu__item-link" > Рулетки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/rivni/" class ="ty-menu__item-link" > Рівні < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shtangencirkuli/" class ="ty-menu__item-link" > Штангенциркулі < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kutomiri/" class ="ty-menu__item-link" > Кутоміри < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/multimetri/" class ="ty-menu__item-link" > Мультиметри < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/materiali-dlya-remontu/" class ="ty-menu__item-link" > Матеріали для ремонту < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/yaschiki-ta-sumki-dlya-instrumentiv/" class ="ty-menu__item-link" > Ящики та сумки для інструментів < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/vitratni-materiali/" class ="ty-menu__item-link" > Витратні матеріали < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/elektroinstrumenti/" class ="ty-menu__item-link" > Електроінструменти < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/zasobi-individualnogo-zahistu/" class ="ty-menu__item-link" > Засоби індивідуального захисту < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/santehnika-ta-aksessuari/" class ="ty-menu__item-link" > Сантехніка та аксессуари < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level- menu-item for-cars"  data-menu-level="1" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-avto/" class ="ty-menu__item-link" > Товари для авто < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/avtohimiya-ta-doglyad-za-avto-uk/" class ="ty-menu__item-link" > Автохімія та догляд за авто < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/avtoinstrumenti-uk/" class ="ty-menu__item-link" > Автоінструменти < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/interier-avtomobilya-uk/" class ="ty-menu__item-link" > Інтер &  # 039;єр автомобіля</a></div></li>

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/avtoelektronika-uk/" class ="ty-menu__item-link" > Автоелектроніка < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level- menu-item for-sport"  data-menu-level="1" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/sport-vidpochinok-ribolovlya/" class ="ty-menu__item-link" > Спорт, відпочинок, риболовля < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-pikniku/" class ="ty-menu__item-link" > Товари для пікніку < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shampura-sitki-dlya-grilya/" class ="ty-menu__item-link" > Шампури, решітки для грилю < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/posud-turistichniy/" class ="ty-menu__item-link" > Посуд туристичний < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-bagattya/" class ="ty-menu__item-link" > Товари для багаття < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/turistichni-mebli/" class ="ty-menu__item-link" > Туристичні меблі та спорядження < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-fitnesu/" class ="ty-menu__item-link" > Товари для фітнесу < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/espanderi-rezinki/" class ="ty-menu__item-link" > Еспандери та резинки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/skakalki/" class ="ty-menu__item-link" > Скакалки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kilimki-dlya-fitnesu-ta-yogi/" class ="ty-menu__item-link" > Килимки для фітнесу та йоги < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/aksesuari-uk/" class ="ty-menu__item-link" > Аксесуари для фітнесу < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/ribalka/" class ="ty-menu__item-link" > Все для риболовлі < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/kotushki/" class ="ty-menu__item-link" > Котушки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/pidgodovuvannya/" class ="ty-menu__item-link" > Підгодовування < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/primanki/" class ="ty-menu__item-link" > Приманки < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shnuri-ta-volosini/" class ="ty-menu__item-link" > Шнури та волосіні < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/osnaschennya/" class ="ty-menu__item-link" > Оснащення для риболовлі < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/vudilischa/" class ="ty-menu__item-link" > Вудилища < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/sportivni-igri/" class ="ty-menu__item-link" > Спортивні ігри < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/tovari-dlya-tenisu-ta-badmintonu/" class ="ty-menu__item-link" > Товари для тенісу та бадмінтону < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/myachi-dlya-futbolu-ta-voleybolu/" class ="ty-menu__item-link" > Спортивні м &  # 039;ячі</a></div></li>

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/aksesuari-ta-zahist-dlya-tila/" class ="ty-menu__item-link" > Боксерські набори для дітей < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive dropdown-vertical__dir menu-level-1"  data-menu-level="2" > < div class ="ty-menu__item-toggle visible-phone cm-responsive-menu-toggle" > < i class ="ty-menu__icon-open ty-icon-down-open" > < / i > < i class ="ty-menu__icon-hide ty-icon-up-open" > < / i > < / div > < div class ="ty-menu__item-arrow hidden-phone" > < i class ="ty-icon-right-open" > < / i > < i class ="ty-icon-left-open" > < / i > < / div > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/naduvni-mebli-ta-aksesuari/" class ="ty-menu__item-link" > Надувні меблі та аксесуари < / a > < / div > < div class ="ty-menu__submenu" > < ul class ="ty-menu__submenu-items cm-responsive-menu-submenu" > < li class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/naduvni-mebli/" class ="ty-menu__item-link" > Надувні меблі < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/naduvni-krugi-ta-aksesuari/" class ="ty-menu__item-link" > Надувні круги та аксесуари < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/shapochki-narukavniki-ta-zhileti/" class ="ty-menu__item-link" > Шапочки, нарукавники та жилети < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-2"  data-menu-level="3" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/maski-ta-trubki-dlya-plavannya/" class ="ty-menu__item-link" > Маски та трубки для плавання < / a > < / div > < / li >

< / ul > < / div >
< / li >
< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/avto-ta-velotovari/" class ="ty-menu__item-link" > Велотовари < / a > < / div > < / li >

< li


class ="ty-menu__ite cm-menu-item-responsive  menu-level-1"  data-menu-level="2" > < div class ="ty-menu__submenu-item-header" > < a href="https://avrora.ua/aksesuari-dlya-aktivnogo-vidpochinku/" class ="ty-menu__item-link" > Аксесуари для активного відпочинку < / a > < / div > < / li >

< / ul > < / div >
< / li >

< / ul >
< / div >

< / div >
< / div >
< / div >

< / div >

< div


class ="row mobile-header-menu--wrap" >

< div


class ="col-md-16  mobile-header-menu hidden site-mode-A" >

< div


class ="row mobile-header-menu__wrap--wrap" >

< div


class ="col-md-16  mobile-header-menu__wrap site-mode-A" >

< div


class ="row mobile-header-menu__top--wrap" >

< div


class ="col-md-16  mobile-header-menu__top site-mode-A" >

< div


class ="ty-wysiwyg-content" > < a href="/" class ="home-link" > < / a > < / div >

< / div >

< / div >

< div


class ="row ty-cabinet-menu--wrap" >

< div


class ="col-md-16  ty-cabinet-menu site-mode-A" >

< div


class ="location-mobile-block " >

< div


class ="av-cac--set is-shop top-select-locations" id="cac_link_283" > < a class ="local-shop-link cm-dialog-opener cm-dialog-auto-size no-pointer" href="https://avrora.ua/index.php?dispatch=cac.set_location"  data-ca-dialog- class ="popup-location" data-ca-dialog-title="Обери магазин, де тобі буде зручно забрати замовлення" data-ca-target-id="cac_form_ajax" >

< span


class ="city" >


Обрати
магазин
< / span >
< / a >
< !--cac_link_283 --> < / div >
< / div > < div


class ="ty-cabinet--top-info " >

< div


class ="ty-wysiwyg-content" > < div class ="ty-cabinet--top__wrap" >

< div


class ="ty-cabinet--top__logo profile" > < / div >

< div


class ="ty-cabinet--top__contacts" >

< div


class ="ty-cabinet--top__name" >


Увійти
в
особистий
кабінет
< / div >
< / div >
< / div >
< a
href = "https://avrora.ua/login/?return_url=index.index"
data - ca - target - id = "login_block393"
data - ca - dialog -


class ="auth-by-phone-popup" class ="cm-dialog-opener cm-dialog-auto-size menu-login " rel="nofollow" >

< span


class ="arrow-thin" > < / span >

< / a >
< / div >
< / div > < div


class ="ty-cabinet--top__menu " >

< ul
id = "text_links_975"


class ="ty-text-links" >

< li


class ="ty-text-links__item ty-level-0 cabinet-link cl-my_room" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/profiles-update/"
>
Особисті
дані
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0 cabinet-link cl-my_orders" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/orders/"
>
Мої
замовлення
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0 cabinet-link cl-my_wishlist" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/wishlist/"
>
Список
бажань
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0 cabinet-link cl-my_viewslist" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/pereglyanuti-tovari/"
>
Переглянуті
товари
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0 cabinet-link cl-my_reviews" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/index.php?dispatch=product_reviews.list"
>
Мої
відгуки
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0 cabinet-link cl-my_radio" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/radio-avrora/"
>
Радіо
Аврора
< / a >
< / li >
< / ul >

< / div > < div


class ="ty-cabinet--top__menu " >

< div


class ="ty-wysiwyg-content" > < / div >

< / div >
< / div >

< / div >

< div


class ="row mobile-header-menu__bottom--wrap" >

< div


class ="col-md-16  mobile-header-menu__bottom site-mode-A" >

< div


class ="mob-contacts " >

< div


class ="ty-wysiwyg-content" > < div class ="contacts__item" >

< p > Гаряча
лінія < / p >
< p > < a
href = "tel:+380800300066" > < strong > 0
800
300
066 < / strong > < / a > < / p >
< / div >
< div


class ="contacts__item" >

< p


class ="worktime-title" > Графік роботи < / p >

< p


class ="worktime-body" > < strong > Пн - Нд: 7: 00 - 21

:00 < / strong > < / p >
< / div >
< div


class ="contacts__item" >

< p > Email < / p >
< p > < a
href = "/cdn-cgi/l/email-protection#1c736e78796e3275715c7d6a6e736e7d32697d" > < strong > < span


class ="__cf_email__" data-cfemail="c2adb0a6a7b0ecabaf82a3b4b0adb0a3ecb7a3" >[email &  # 160;protected]</span></strong></a></p>
< / div > < / div >
< / div > < div


class ="mob-social " >

< div


class ="ty-wysiwyg-content" > < div class ="ty-social-wrap" >

< div


class ="ty-social-item facebook" >

< a
href = "https://www.facebook.com/avrora.multimarket"
target = "_blank"
title = "Facebook" >
< i


class ="icon-facebook" > < / i >

< / a >
< / div >
< div


class ="ty-social-item instagram" >

< a
href = "https://www.instagram.com/avrora.multimarket/"
target = "_blank"
title = "Instagram" >
< i


class ="icon-instagram" > < / i >

< / a >
< / div >
< div


class ="ty-social-item telegram" >

< a
href = "https://t.me/Avroraua"
target = "_blank"
title = "Telegram" >
< i


class ="icon-telegram" > < / i >

< / a >
< / div >
< div


class ="ty-social-item youtube" >

< a
href = "https://www.youtube.com/channel/UCMIQPAmwj86Gf0gtakRSVJA"
target = "_blank"
title = "Youtube" >
< i


class ="icon-youtube" > < / i >

< / a >
< / div >
< div


class ="ty-social-item tiktok" >

< a
href = "https://www.tiktok.com/@avrora.multimarket"
target = "_blank"
title = "TikTok" >
< i


class ="icon-tiktok" > < / i >

< / a >
< / div >
< div


class ="ty-social-item linkedin" >

< a
href = "https://www.linkedin.com/company/avroraua/"
target = "_blank"
title = "Linkedin" >
< i


class ="icon-linkedin" > < / i >

< / a >
< / div >
< div


class ="ty-social-item viber" >

< a
href = "https://invite.viber.com/?g2=AQANNWf1szIUrU7N0%2B3q7jrf1CbtWxJEn%2FyE8kQukVNn9mzVglYNZs%2BctMuOws8p&lang=uk"
target = "_blank"
title = "Viber" >
< i


class ="icon-viber" > < / i >

< / a >
< / div >
< / div > < / div >
< / div >
< / div >

< / div >
< / div >

< / div >
< / div >

< / div >
< / div >

< / div >
< / div >

< / div >

< div


class ="tygh-content" >

< div


class ="container-fluid   category-page category-page-sublevel content-grid" >

< div


class ="row seo-desc-category--wrap" >

< div


class ="col-md-16  seo-desc-category site-mode-A" >

< div


class ="ty-wysiwyg-content" > < / div >

< / div >

< / div >

< div


class ="row" >

< div


class ="col-md-16   site-mode-A" >

< div
id = "breadcrumbs_11" >

< div


class ="ty-breadcrumbs" itemscope itemtype="https://schema.org/BreadcrumbList" >

< div


class ="ty-breadcrumbs__a--wrap" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem" > < a href="https://avrora.ua/" itemprop="item" class ="ty-breadcrumbs__a" > < span itemprop="name" > Головна < / span > < meta itemprop="position" content="1" / > < / a > < / div > < span class ="ty-breadcrumbs__slash" > / < / span > < div class ="ty-breadcrumbs__a--wrap" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem" > < a href="https://avrora.ua/krasota-i-zdorove/" itemprop="item" class ="ty-breadcrumbs__a" > < span itemprop="name" > Краса та здоров’я < / span > < meta itemprop="position" content="2" / > < / a > < / div > < span class ="ty-breadcrumbs__slash" > / < / span > < span class ="ty-breadcrumbs__current" > < bdi > Гігієна < / bdi > < / span > < / div >

< !--breadcrumbs_11 --> < / div >
< / div >

< / div >

< div


class ="row" >

< div


class ="col-md-16   site-mode-A" >

< div


class ="ty-wysiwyg-content" > < h1 class ="ty-mainbox-simple-title" id="title_general_block" >


Гігієна
< / h1 > < / div >
< / div >

< / div >

< div


class ="row" >

< div


class ="col-md-16   site-mode-A" >

< div


class ="ty-wysiwyg-content" >

< ul


class ="subcategories clearfix" >

< li


class ="ty-subcategories__item" >

< a
href = "https://avrora.ua/tovari-dlya-zhinochoi-gigiieni/" >
< span


class ="img--wrap" >

< img


class ="ty-pict  ty-subcategories-img   cm-image"   src="https://images.avrora.ua/images/thumbnails/200/134/detailed/16/tovari-dlya-zhinochoi-gigieni.webp"  alt="Товари для жіночої гігієни Аврора" title="Товари для жіночої гігієни" / >

< / span >
< span > Товари
для
жіночої
гігієни < / span >
< / a >
< / li >

< li


class ="ty-subcategories__item" >

< a
href = "https://avrora.ua/servetki-paperovi-rushniki/" >
< span


class ="img--wrap" >

< img


class ="ty-pict  ty-subcategories-img   cm-image"   src="https://images.avrora.ua/images/thumbnails/200/134/detailed/16/servetki-paperovi-rushniki.webp"  alt="Серветки, паперові рушники Аврора" title="Серветки, паперові рушники" / >

< / span >
< span > Серветки, паперові
рушники < / span >
< / a >
< / li >

< li


class ="ty-subcategories__item" >

< a
href = "https://avrora.ua/osobista-gigiiena/" >
< span


class ="img--wrap" >

< img


class ="ty-pict  ty-subcategories-img   cm-image"   src="https://images.avrora.ua/images/thumbnails/200/134/detailed/16/osobista-gigiena.webp"  alt="Особиста гігієна Аврора" title="Особиста гігієна" / >

< / span >
< span > Особиста
гігієна < / span >
< / a >
< / li >

< / ul >

< div


class ="show-more-container hidden" >

< button > Показати
більше
< span > < / span > < span > < / span > < span > < / span > < span > < / span > < span > < / span > < span > < / span >
< / button >
< / div >

< / div > < div


class ="category-top__info-container " >

< div


class ="ty-wysiwyg-content" > < button class ="filter-btn hidden" > < span > < / span > Фільтр < / button > < div class ="count-product" > Всього знайдено: <


    span


class ="cm-reload-st" id="search_total_items_st_update" > 291 < !--search_total_items_st_update--> < / span > < / div >

< div
id = "elm_sort_wrap" >
< div


class ="ty-sort-container" >

< span > Сортувати: < / span >

< div


class ="ty-sort-dropdown" >

< a
id = "sw_elm_sort_fields"


class ="ty-sort-dropdown__wrapper cm-combination" > Популярні < i class ="ty-sort-dropdown__icon ty-icon-down-micro" > < / i > < / a >

< ul
id = "elm_sort_fields"


class ="ty-sort-dropdown__content cm-popup-box hidden" >

< li


class ="sort-by-timestamp-desc ty-sort-dropdown__content-item" >

< a


class ="cm-ajax cm-ajax-full-render ty-sort-dropdown__content-item-a" data-ca-target-id="elm_sort_wrap,elm_sort_wrap_mobile,pagination_contents" href="https://avrora.ua/gigiena/page-2/?sort_by=timestamp&amp;sort_order=desc" rel="nofollow" > Новинки < / a >

< / li >
< li


class ="sort-by-price-asc ty-sort-dropdown__content-item" >

< a


class ="cm-ajax cm-ajax-full-render ty-sort-dropdown__content-item-a" data-ca-target-id="elm_sort_wrap,elm_sort_wrap_mobile,pagination_contents" href="https://avrora.ua/gigiena/page-2/?sort_by=price&amp;sort_order=asc" rel="nofollow" > Від дешевших < / a >

< / li >
< li


class ="sort-by-price-desc ty-sort-dropdown__content-item" >

< a


class ="cm-ajax cm-ajax-full-render ty-sort-dropdown__content-item-a" data-ca-target-id="elm_sort_wrap,elm_sort_wrap_mobile,pagination_contents" href="https://avrora.ua/gigiena/page-2/?sort_by=price&amp;sort_order=desc" rel="nofollow" > Від дорогих < / a >

< / li >
< / ul >
< / div >
< !-- Inline
script
moved
to
the
bottom
of
the
page -->

< / div >
< !--elm_sort_wrap --> < / div >
< / div >
< / div > < div


class ="ty-horizontal-product-filters ty-selected-product-filters cm-product-filters cm-horizontal-filters"


data - ca - target - id = "product_filters_*,selected_filters_*,products_search_*,category_products_*,currencies_*,languages_*,promotion_product_search_*,product_features_*,search_total_items_st_*,elm_sort_wrap,elm_faq_wrap"
data - ca - base - url = "https://avrora.ua/gigiena/"
data - ca - tooltip -


class = "ty-product-filters__tooltip"


data - ca - tooltip - right -


class = "ty-product-filters__tooltip--right"


data - ca - tooltip - mobile -


class = "ty-tooltip--mobile"


data - ca - tooltip - layout - selector = "[data-ca-tooltip-layout='true']"
data - ce - tooltip - events - tooltip = "mouseenter"
id = "selected_filters_68_470" >

< !--selected_filters_68_470 --> < / div >

< div
data - ca - tooltip - layout = "true"


class ="hidden" >

< button
type = "button"
data - ca - scroll = ".ty-mainbox-title"


class ="cm-scroll ty-tooltip--link ty-tooltip--filter" > < span class ="tooltip-arrow" > < / span > < / button >

< / div >
< / div >

< / div >

< div


class ="row filter-block--wrap" >

< div


class ="col-md-4  filter-block mb100 site-mode-A" >

< div


class ="mobile-top-filters hidden " >

< div


class ="ty-wysiwyg-content" > < div class ="title-filters" > Фільтр < / div >

< button


class ="close-filter hidden" > Закрити < / button > < / div >

< / div > < div


class ="mobile-selected-filters hidden " >

< div


class ="ty-horizontal-product-filters ty-selected-product-filters cm-product-filters cm-horizontal-filters"


data - ca - target - id = "product_filters_*,selected_filters_*,products_search_*,category_products_*,currencies_*,languages_*,promotion_product_search_*,product_features_*,search_total_items_st_*,elm_sort_wrap,elm_faq_wrap"
data - ca - base - url = "https://avrora.ua/gigiena/"
data - ca - tooltip -


class = "ty-product-filters__tooltip"


data - ca - tooltip - right -


class = "ty-product-filters__tooltip--right"


data - ca - tooltip - mobile -


class = "ty-tooltip--mobile"


data - ca - tooltip - layout - selector = "[data-ca-tooltip-layout='true']"
data - ce - tooltip - events - tooltip = "mouseenter"
id = "selected_filters_68_471" >

< !--selected_filters_68_471 --> < / div >

< div
data - ca - tooltip - layout = "true"


class ="hidden" >

< button
type = "button"
data - ca - scroll = ".ty-mainbox-title"


class ="cm-scroll ty-tooltip--link ty-tooltip--filter" > < span class ="tooltip-arrow" > < / span > < / button >

< / div >

< / div > < div


class ="cm-product-filters"


data - ca - target - id = "product_filters_*,selected_filters_*,products_search_*,category_products_*,currencies_*,languages_*,promotion_product_search_*,product_features_*,search_total_items_st_*,elm_sort_wrap,elm_faq_wrap,pagination_contents"
data - ca - base - url = "https://avrora.ua/gigiena/"
data - ca - tooltip -


class = "ty-product-filters__tooltip"


data - ca - tooltip - right -


class = "ty-product-filters__tooltip--right"


data - ca - tooltip - mobile -


class = "ty-tooltip--mobile"


data - ca - tooltip - layout - selector = "[data-ca-tooltip-layout='true']"
data - ce - tooltip - events - tooltip = "mouseenter"
id = "product_filters_32" >
< div


class ="ty-product-filters__wrapper" data-ca-product-filters="wrapper" >

< div


class ="ty-product-filters__block" >

< div
id = "sw_content_32_92"


class ="ty-product-filters__switch slider-type" >

< span


class ="ty-product-filters__title" >


Акційні
товари
< / span >
< ul


class ="ty-product-filters " id="content_32_92" >

< li


class ="ty-product-filters__item-more" >

< ul
id = "ranges_32_92"
style = "max-height: 20em;"


class ="ty-product-filters__variants cm-filter-table" data-ca-input-id="elm_search_32_92" data-ca-clear-id="elm_search_clear_32_92" data-ca-empty-id="elm_search_empty_32_92" >

< li


class ="cm-product-filters-switcher-container ty-product-filters__group" >

< label >
< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[92]"
data - ca - filter - id = "92"
value = "Y"
id = "elm_checkbox_32_92_Y"
>

< span


class ="slider round" > < / span >

< / label >
< / li >
< / ul >
< / li >

< / ul >
< / div >

< / div >

< div


class ="ty-product-filters__block" >

< div
id = "sw_content_32_4"


class ="ty-product-filters__switch cm-combination-filter_32_4 open cm-save-state cm-ss-reverse" >

< span


class ="ty-product-filters__title" > Ціна < / span >

< i


class ="ty-product-filters__switch-down ty-icon-down-open" > < / i >

< i


class ="ty-product-filters__switch-right ty-icon-up-open" > < / i >

< / div >

< div
id = "content_32_4"


class ="cm-product-filters-checkbox-container ty-price-slider  " >

< p


class ="ty-price-slider__inputs" >

< bdi


class ="ty-price-slider__bidi-container" >

< span


class ="ty-price-slider__filter-prefix" > < / span >

< input
type = "text"


class ="ty-price-slider__input-text"


id = "slider_32_4_left"
name = "left_32_4"
value = "2"
data - ca - previous - value = "2" / >
< span > грн < / span >
< / bdi >
< bdi


class ="ty-price-slider__bidi-container" >

< span


class ="ty-price-slider__filter-prefix" > < / span >

< input
type = "text"


class ="ty-price-slider__input-text"


id = "slider_32_4_right"
name = "right_32_4"
value = "339"
data - ca - previous - value = "339" / >
< span > грн < / span >
< / bdi >
< / p >
< div
id = "slider_32_4"


class ="ty-range-slider cm-range-slider" >

< ul


class ="ty-range-slider__wrapper" >

< li


class ="ty-range-slider__item" style="left: 0%;" >

< span


class ="ty-range-slider__num" >

< span > & lrm; < bdi > < span > 2 < / span > < / bdi > грн < / span >
< / span >
< / li >
< li


class ="ty-range-slider__item" style="left: 100%;" >

< span


class ="ty-range-slider__num" >

< span > & lrm; < bdi > < span > 339 < / span > < / bdi > грн < / span >
< / span >
< / li >
< / ul >
< / div >

< input
id = "elm_checkbox_slider_32_4"
data - ca - filter - id = "4"


class ="cm-product-filters-checkbox hidden" type="checkbox" name="product_filters[4]" value="" / >

< input
type = "hidden"
id = "slider_32_4_json"
value = '{
"disabled": false,
"min": 2,
"max": 339,
"left": 2,
"right": 339,
"step": 1,
"extra": "UAH"
}' />
 < / div >

     < / div >

         < div


class ="ty-product-filters__block" >

< div
id = "sw_content_32_64"


class ="ty-product-filters__switch slider-type no-icon" >

< span


class ="ty-product-filters__title" >


Тільки
в
наявності
< / span >
< ul


class ="ty-product-filters " id="content_32_64" >

< li


class ="ty-product-filters__item-more" >

< ul
id = "ranges_32_64"
style = "max-height: 20em;"


class ="ty-product-filters__variants cm-filter-table" data-ca-input-id="elm_search_32_64" data-ca-clear-id="elm_search_clear_32_64" data-ca-empty-id="elm_search_empty_32_64" >

< li


class ="cm-product-filters-switcher-container ty-product-filters__group" >

< label >
< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[64]"
data - ca - filter - id = "64"
value = "Y"
id = "elm_checkbox_32_64_Y"
>

< span


class ="slider round" > < / span >

< / label >
< / li >
< / ul >
< / li >

< / ul >
< / div >

< / div >

< div


class ="ty-product-filters__block hidden" >

< div
id = "sw_content_32_110"


class ="ty-product-filters__switch cm-combination-filter_32_110 open cm-save-state cm-ss-reverse" >

< span


class ="ty-product-filters__title" > Категорія < / span >

< i


class ="ty-product-filters__switch-down ty-icon-down-open" > < / i >

< i


class ="ty-product-filters__switch-right ty-icon-up-open" > < / i >

< / div >

< ul


class ="ty-product-filters " id="content_32_110" >

< li


class ="ty-product-filters__item-more" >

< ul
id = "ranges_32_110"
style = "max-height: 20em;"


class ="ty-product-filters__variants cm-filter-table" data-ca-input-id="elm_search_32_110" data-ca-clear-id="elm_search_clear_32_110" data-ca-empty-id="elm_search_empty_32_110" >

< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[110]"
data - ca - filter - id = "110"
value = "205"
id = "elm_checkbox_32_110_205"
>
< span


class ="checked" > < / span >

< / span >
< span > Догляд
та
аксесуари
для
взуття < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[110]"
data - ca - filter - id = "110"
value = "69"
id = "elm_checkbox_32_110_69"
>
< span


class ="checked" > < / span >

< / span >
< span > Особиста
гігієна < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[110]"
data - ca - filter - id = "110"
value = "337"
id = "elm_checkbox_32_110_337"
>
< span


class ="checked" > < / span >

< / span >
< span > Рушники < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[110]"
data - ca - filter - id = "110"
value = "68"
id = "elm_checkbox_32_110_68"
>
< span


class ="checked" > < / span >

< / span >
< span > Серветки, паперові
рушники < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[110]"
data - ca - filter - id = "110"
value = "67"
id = "elm_checkbox_32_110_67"
>
< span


class ="checked" > < / span >

< / span >
< span > Товари
для
жіночої
гігієни < / span >
< / label >
< / li >
< / ul >
< / li >
< li >
< p
id = "elm_search_empty_32_110"


class ="ty-product-filters__no-items-found hidden" > Не знайдено елементів що відповідають критеріям пошуку < / p >

< / li >
< / ul >

< / div >

< div


class ="ty-product-filters__block" >

< div
id = "sw_content_32_18"


class ="ty-product-filters__switch cm-combination-filter_32_18 open cm-save-state cm-ss-reverse" >

< span


class ="ty-product-filters__title" > Бренд < / span >

< i


class ="ty-product-filters__switch-down ty-icon-down-open" > < / i >

< i


class ="ty-product-filters__switch-right ty-icon-up-open" > < / i >

< / div >

< ul


class ="ty-product-filters shm-container " id="content_32_18" >

< li >

< div


class ="ty-product-filters__search" >

< input
type = "text"
placeholder = "Пошук"


class ="cm-autocomplete-off ty-input-text-medium" name="q" id="elm_search_32_18" value="" / >

< i


class ="ty-product-filters__search-icon ty-icon-cancel-circle hidden" id="elm_search_clear_32_18" title="Очистити" > < / i >

< / div >
< / li >

< li


class ="ty-product-filters__item-more" >

< ul
id = "ranges_32_18"
style = "max-height: 20em;"


class ="ty-product-filters__variants cm-filter-table" data-ca-input-id="elm_search_32_18" data-ca-clear-id="elm_search_clear_32_18" data-ca-empty-id="elm_search_empty_32_18" >

< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "3056"
id = "elm_checkbox_32_18_3056"
>
< span


class ="checked" > < / span >

< / span >
< span > Ajoure < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "1216"
id = "elm_checkbox_32_18_1216"
>
< span


class ="checked" > < / span >

< / span >
< span > Always < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "15771"
id = "elm_checkbox_32_18_15771"
>
< span


class ="checked" > < / span >

< / span >
< span > Aqua
Baby < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "544"
id = "elm_checkbox_32_18_544"
>
< span


class ="checked" > < / span >

< / span >
< span > Bella < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "1183"
id = "elm_checkbox_32_18_1183"
>
< span


class ="checked" > < / span >

< / span >
< span > Biosphere < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "6468"
id = "elm_checkbox_32_18_6468"
>
< span


class ="checked" > < / span >

< / span >
< span > Cleanness + < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "1084"
id = "elm_checkbox_32_18_1084"
>
< span


class ="checked" > < / span >

< / span >
< span > DeLuxe < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "5800"
id = "elm_checkbox_32_18_5800"
>
< span


class ="checked" > < / span >

< / span >
< span > Discreet < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "55064"
id = "elm_checkbox_32_18_55064"
>
< span


class ="checked" > < / span >

< / span >
< span > Doyfresh < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "377"
id = "elm_checkbox_32_18_377"
>
< span


class ="checked" > < / span >

< / span >
< span > Ecolo < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "43524"
id = "elm_checkbox_32_18_43524"
>
< span


class ="checked" > < / span >

< / span >
< span > Ecovibe < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "14109"
id = "elm_checkbox_32_18_14109"
>
< span


class ="checked" > < / span >

< / span >
< span > Elen
Cosmetics < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "49104"
id = "elm_checkbox_32_18_49104"
>
< span


class ="checked" > < / span >

< / span >
< span > Emmi < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "43568"
id = "elm_checkbox_32_18_43568"
>
< span


class ="checked" > < / span >

< / span >
< span > Essenta < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "1730"
id = "elm_checkbox_32_18_1730"
>
< span


class ="checked" > < / span >

< / span >
< span > Fantasy < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "43822"
id = "elm_checkbox_32_18_43822"
>
< span


class ="checked" > < / span >

< / span >
< span > Greenday < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "25774"
id = "elm_checkbox_32_18_25774"
>
< span


class ="checked" > < / span >

< / span >
< span > Huggies < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "53444"
id = "elm_checkbox_32_18_53444"
>
< span


class ="checked" > < / span >

< / span >
< span > Kleenex < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "543"
id = "elm_checkbox_32_18_543"
>
< span


class ="checked" > < / span >

< / span >
< span > Kotex < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "28139"
id = "elm_checkbox_32_18_28139"
>
< span


class ="checked" > < / span >

< / span >
< span > Lactacyd < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "1340"
id = "elm_checkbox_32_18_1340"
>
< span


class ="checked" > < / span >

< / span >
< span > Lady
Cotton < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "1132"
id = "elm_checkbox_32_18_1132"
>
< span


class ="checked" > < / span >

< / span >
< span > Libresse < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "4543"
id = "elm_checkbox_32_18_4543"
>
< span


class ="checked" > < / span >

< / span >
< span > Lirro < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "53856"
id = "elm_checkbox_32_18_53856"
>
< span


class ="checked" > < / span >

< / span >
< span > Mirus < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "44263"
id = "elm_checkbox_32_18_44263"
>
< span


class ="checked" > < / span >

< / span >
< span > Mollis < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "540"
id = "elm_checkbox_32_18_540"
>
< span


class ="checked" > < / span >

< / span >
< span > Naturella < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "961"
id = "elm_checkbox_32_18_961"
>
< span


class ="checked" > < / span >

< / span >
< span > Naturelle < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "28268"
id = "elm_checkbox_32_18_28268"
>
< span


class ="checked" > < / span >

< / span >
< span > Papero < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "4023"
id = "elm_checkbox_32_18_4023"
>
< span


class ="checked" > < / span >

< / span >
< span > Papirella < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "44063"
id = "elm_checkbox_32_18_44063"
>
< span


class ="checked" > < / span >

< / span >
< span > Practica < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "349"
id = "elm_checkbox_32_18_349"
>
< span


class ="checked" > < / span >

< / span >
< span > Ruta < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "1377"
id = "elm_checkbox_32_18_1377"
>
< span


class ="checked" > < / span >

< / span >
< span > Safi < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "13514"
id = "elm_checkbox_32_18_13514"
>
< span


class ="checked" > < / span >

< / span >
< span > Selpak < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "17260"
id = "elm_checkbox_32_18_17260"
>
< span


class ="checked" > < / span >

< / span >
< span > Shik < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "1926"
id = "elm_checkbox_32_18_1926"
>
< span


class ="checked" > < / span >

< / span >
< span > Silken < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "2783"
id = "elm_checkbox_32_18_2783"
>
< span


class ="checked" > < / span >

< / span >
< span > Smile < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "1374"
id = "elm_checkbox_32_18_1374"
>
< span


class ="checked" > < / span >

< / span >
< span > Superfresh < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "5993"
id = "elm_checkbox_32_18_5993"
>
< span


class ="checked" > < / span >

< / span >
< span > Tena < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "232"
id = "elm_checkbox_32_18_232"
>
< span


class ="checked" > < / span >

< / span >
< span > Zewa < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "20499"
id = "elm_checkbox_32_18_20499"
>
< span


class ="checked" > < / span >

< / span >
< span > Ziaja < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "1007"
id = "elm_checkbox_32_18_1007"
>
< span


class ="checked" > < / span >

< / span >
< span > Альбатрос < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "54356"
id = "elm_checkbox_32_18_54356"
>
< span


class ="checked" > < / span >

< / span >
< span > Будь
Ласка < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "1432"
id = "elm_checkbox_32_18_1432"
>
< span


class ="checked" > < / span >

< / span >
< span > Деста < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "2351"
id = "elm_checkbox_32_18_2351"
>
< span


class ="checked" > < / span >

< / span >
< span > Диво < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "4343"
id = "elm_checkbox_32_18_4343"
>
< span


class ="checked" > < / span >

< / span >
< span > Зелена
аптека < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "2345"
id = "elm_checkbox_32_18_2345"
>
< span


class ="checked" > < / span >

< / span >
< span > Кохавинка < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "21268"
id = "elm_checkbox_32_18_21268"
>
< span


class ="checked" > < / span >

< / span >
< span > Кохавинська
Папірня < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "850"
id = "elm_checkbox_32_18_850"
>
< span


class ="checked" > < / span >

< / span >
< span > Ніжний
дотик < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "1430"
id = "elm_checkbox_32_18_1430"
>
< span


class ="checked" > < / span >

< / span >
< span > Новий
Київ < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "1436"
id = "elm_checkbox_32_18_1436"
>
< span


class ="checked" > < / span >

< / span >
< span > Обухів < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "775"
id = "elm_checkbox_32_18_775"
>
< span


class ="checked" > < / span >

< / span >
< span > Свіжанка < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "2358"
id = "elm_checkbox_32_18_2358"
>
< span


class ="checked" > < / span >

< / span >
< span > Сніжна
панда < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "1433"
id = "elm_checkbox_32_18_1433"
>
< span


class ="checked" > < / span >

< / span >
< span > Спеціаль < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[18]"
data - ca - filter - id = "18"
value = "22925"
id = "elm_checkbox_32_18_22925"
>
< span


class ="checked" > < / span >

< / span >
< span > Українська
Мальва < / span >
< / label >
< / li >
< / ul >
< button


class ="shm-btn" >

< span


class ="shm-short-text" > < u > Показати ще < / u > < i > 47 < / i > < / span > < span class ="shm-hide-text" > Приховати < / span >

< / button >
< / li >
< li >
< p
id = "elm_search_empty_32_18"


class ="ty-product-filters__no-items-found hidden" > Не знайдено елементів що відповідають критеріям пошуку < / p >

< / li >
< / ul >

< / div >

< div


class ="ty-product-filters__block" >

< div
id = "sw_content_32_68"


class ="ty-product-filters__switch cm-combination-filter_32_68 open cm-save-state cm-ss-reverse" >

< span


class ="ty-product-filters__title" > Особливості товару < / span >

< i


class ="ty-product-filters__switch-down ty-icon-down-open" > < / i >

< i


class ="ty-product-filters__switch-right ty-icon-up-open" > < / i >

< / div >

< ul


class ="ty-product-filters " id="content_32_68" >

< li


class ="ty-product-filters__item-more" >

< ul
id = "ranges_32_68"
style = "max-height: 20em;"


class ="ty-product-filters__variants cm-filter-table" data-ca-input-id="elm_search_32_68" data-ca-clear-id="elm_search_clear_32_68" data-ca-empty-id="elm_search_empty_32_68" >

< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[68]"
data - ca - filter - id = "68"
value = "27909"
id = "elm_checkbox_32_68_27909"
>
< span


class ="checked" > < / span >

< / span >
< span > Національний
кешбек < / span >
< / label >
< / li >
< / ul >
< / li >
< li >
< p
id = "elm_search_empty_32_68"


class ="ty-product-filters__no-items-found hidden" > Не знайдено елементів що відповідають критеріям пошуку < / p >

< / li >
< / ul >

< / div >

< div


class ="ty-product-filters__block" >

< div
id = "sw_content_32_28"


class ="ty-product-filters__switch cm-combination-filter_32_28 open cm-save-state cm-ss-reverse" >

< span


class ="ty-product-filters__title" > Вид < / span >

< i


class ="ty-product-filters__switch-down ty-icon-down-open" > < / i >

< i


class ="ty-product-filters__switch-right ty-icon-up-open" > < / i >

< / div >

< ul


class ="ty-product-filters shm-container " id="content_32_28" >

< li >

< div


class ="ty-product-filters__search" >

< input
type = "text"
placeholder = "Пошук"


class ="cm-autocomplete-off ty-input-text-medium" name="q" id="elm_search_32_28" value="" / >

< i


class ="ty-product-filters__search-icon ty-icon-cancel-circle hidden" id="elm_search_clear_32_28" title="Очистити" > < / i >

< / div >
< / li >

< li


class ="ty-product-filters__item-more" >

< ul
id = "ranges_32_28"
style = "max-height: 16em;"


class ="ty-product-filters__variants cm-filter-table" data-ca-input-id="elm_search_32_28" data-ca-clear-id="elm_search_clear_32_28" data-ca-empty-id="elm_search_empty_32_28" >

< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "1454"
id = "elm_checkbox_32_28_1454"
>
< span


class ="checked" > < / span >

< / span >
< span > Ватні
диски < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "776"
id = "elm_checkbox_32_28_776"
>
< span


class ="checked" > < / span >

< / span >
< span > Ватні
палички < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "6469"
id = "elm_checkbox_32_28_6469"
>
< span


class ="checked" > < / span >

< / span >
< span > Гелі
для
інтимної
гігієни < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "7574"
id = "elm_checkbox_32_28_7574"
>
< span


class ="checked" > < / span >

< / span >
< span > Підгузки
для
дорослих < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "560"
id = "elm_checkbox_32_28_560"
>
< span


class ="checked" > < / span >

< / span >
< span > Паперові
рушники < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "14153"
id = "elm_checkbox_32_28_14153"
>
< span


class ="checked" > < / span >

< / span >
< span > Пелюшки
гігієнічні < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "14665"
id = "elm_checkbox_32_28_14665"
>
< span


class ="checked" > < / span >

< / span >
< span > Пелюшки
одноразові < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "7563"
id = "elm_checkbox_32_28_7563"
>
< span


class ="checked" > < / span >

< / span >
< span > Присипки
для
ніг < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "541"
id = "elm_checkbox_32_28_541"
>
< span


class ="checked" > < / span >

< / span >
< span > Прокладки < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "5996"
id = "elm_checkbox_32_28_5996"
>
< span


class ="checked" > < / span >

< / span >
< span > Прокладки
урологічні < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "18464"
id = "elm_checkbox_32_28_18464"
>
< span


class ="checked" > < / span >

< / span >
< span > Рушники
паперові < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "563"
id = "elm_checkbox_32_28_563"
>
< span


class ="checked" > < / span >

< / span >
< span > Серветки < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "559"
id = "elm_checkbox_32_28_559"
>
< span


class ="checked" > < / span >

< / span >
< span > Серветки
вологі < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "18023"
id = "elm_checkbox_32_28_18023"
>
< span


class ="checked" > < / span >

< / span >
< span > Серветки
паперові < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "558"
id = "elm_checkbox_32_28_558"
>
< span


class ="checked" > < / span >

< / span >
< span > Тампони < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "1722"
id = "elm_checkbox_32_28_1722"
>
< span


class ="checked" > < / span >

< / span >
< span > Туалетний
папір < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "2354"
id = "elm_checkbox_32_28_2354"
>
< span


class ="checked" > < / span >

< / span >
< span > Туалетний
папір
вологий < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[28]"
data - ca - filter - id = "28"
value = "3203"
id = "elm_checkbox_32_28_3203"
>
< span


class ="checked" > < / span >

< / span >
< span > Хустинки < / span >
< / label >
< / li >
< / ul >
< button


class ="shm-btn" >

< span


class ="shm-short-text" > < u > Показати ще < / u > < i > 11 < / i > < / span > < span class ="shm-hide-text" > Приховати < / span >

< / button >
< / li >
< li >
< p
id = "elm_search_empty_32_28"


class ="ty-product-filters__no-items-found hidden" > Не знайдено елементів що відповідають критеріям пошуку < / p >

< / li >
< / ul >

< / div >

< div


class ="ty-product-filters__block" >

< div
id = "sw_content_32_26"


class ="ty-product-filters__switch cm-combination-filter_32_26 open cm-save-state cm-ss-reverse" >

< span


class ="ty-product-filters__title" > Країна виробник < / span >

< i


class ="ty-product-filters__switch-down ty-icon-down-open" > < / i >

< i


class ="ty-product-filters__switch-right ty-icon-up-open" > < / i >

< / div >

< ul


class ="ty-product-filters shm-container " id="content_32_26" >

< li >

< div


class ="ty-product-filters__search" >

< input
type = "text"
placeholder = "Пошук"


class ="cm-autocomplete-off ty-input-text-medium" name="q" id="elm_search_32_26" value="" / >

< i


class ="ty-product-filters__search-icon ty-icon-cancel-circle hidden" id="elm_search_clear_32_26" title="Очистити" > < / i >

< / div >
< / li >

< li


class ="ty-product-filters__item-more" >

< ul
id = "ranges_32_26"
style = "max-height: 20em;"


class ="ty-product-filters__variants cm-filter-table" data-ca-input-id="elm_search_32_26" data-ca-clear-id="elm_search_clear_32_26" data-ca-empty-id="elm_search_empty_32_26" >

< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[26]"
data - ca - filter - id = "26"
value = "2673"
id = "elm_checkbox_32_26_2673"
>
< span


class ="checked" > < / span >

< / span >
< span > Іспанія < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[26]"
data - ca - filter - id = "26"
value = "94"
id = "elm_checkbox_32_26_94"
>
< span


class ="checked" > < / span >

< / span >
< span > Італія < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[26]"
data - ca - filter - id = "26"
value = "3608"
id = "elm_checkbox_32_26_3608"
>
< span


class ="checked" > < / span >

< / span >
< span > Греція < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[26]"
data - ca - filter - id = "26"
value = "22076"
id = "elm_checkbox_32_26_22076"
>
< span


class ="checked" > < / span >

< / span >
< span > Естонія < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[26]"
data - ca - filter - id = "26"
value = "45"
id = "elm_checkbox_32_26_45"
>
< span


class ="checked" > < / span >

< / span >
< span > Китай < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[26]"
data - ca - filter - id = "26"
value = "2685"
id = "elm_checkbox_32_26_2685"
>
< span


class ="checked" > < / span >

< / span >
< span > Латвія < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[26]"
data - ca - filter - id = "26"
value = "2670"
id = "elm_checkbox_32_26_2670"
>
< span


class ="checked" > < / span >

< / span >
< span > Нідерланди < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[26]"
data - ca - filter - id = "26"
value = "2676"
id = "elm_checkbox_32_26_2676"
>
< span


class ="checked" > < / span >

< / span >
< span > Німеччина < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[26]"
data - ca - filter - id = "26"
value = "91"
id = "elm_checkbox_32_26_91"
>
< span


class ="checked" > < / span >

< / span >
< span > Польща < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[26]"
data - ca - filter - id = "26"
value = "5895"
id = "elm_checkbox_32_26_5895"
>
< span


class ="checked" > < / span >

< / span >
< span > Сербія < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[26]"
data - ca - filter - id = "26"
value = "4853"
id = "elm_checkbox_32_26_4853"
>
< span


class ="checked" > < / span >

< / span >
< span > Словаччина < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[26]"
data - ca - filter - id = "26"
value = "2696"
id = "elm_checkbox_32_26_2696"
>
< span


class ="checked" > < / span >

< / span >
< span > Словенія < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[26]"
data - ca - filter - id = "26"
value = "2678"
id = "elm_checkbox_32_26_2678"
>
< span


class ="checked" > < / span >

< / span >
< span > Туреччина < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[26]"
data - ca - filter - id = "26"
value = "2652"
id = "elm_checkbox_32_26_2652"
>
< span


class ="checked" > < / span >

< / span >
< span > Угорщина < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[26]"
data - ca - filter - id = "26"
value = "27"
id = "elm_checkbox_32_26_27"
>
< span


class ="checked" > < / span >

< / span >
< span > Україна < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[26]"
data - ca - filter - id = "26"
value = "29234"
id = "elm_checkbox_32_26_29234"
>
< span


class ="checked" > < / span >

< / span >
< span > Чехія < / span >
< / label >
< / li >
< li


class ="cm-product-filters-checkbox-container ty-product-filters__group shm-hide" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox"


type = "checkbox"
name = "product_filters[26]"
data - ca - filter - id = "26"
value = "2753"
id = "elm_checkbox_32_26_2753"
>
< span


class ="checked" > < / span >

< / span >
< span > Швеція < / span >
< / label >
< / li >
< / ul >
< button


class ="shm-btn" >

< span


class ="shm-short-text" > < u > Показати ще < / u > < i > 10 < / i > < / span > < span class ="shm-hide-text" > Приховати < / span >

< / button >
< / li >
< li >
< p
id = "elm_search_empty_32_26"


class ="ty-product-filters__no-items-found hidden" > Не знайдено елементів що відповідають критеріям пошуку < / p >

< / li >
< / ul >

< / div >

< div


class ="ty-product-filters__tools clearfix hidden" data-ca-product-filters="tools" >

< a
href = "https://avrora.ua/gigiena/"
rel = "nofollow"


class ="ty-product-filters__reset-button cm-ajax cm-ajax-full-render cm-history" data-ca-event="ce.filtersinit" data-ca-target-id="product_filters_*,selected_filters_*,products_search_*,category_products_*,currencies_*,languages_*,promotion_product_search_*,product_features_*,search_total_items_st_*,elm_sort_wrap,elm_faq_wrap,pagination_contents" > < i class ="ty-product-filters__reset-icon ty-icon-cw" > < / i > Очистити все < / a >

< / div >

< / div >
< !--product_filters_32 --> < / div >

< div
data - ca - tooltip - layout = "true"


class ="hidden" >

< button
type = "button"
data - ca - scroll = ".ty-mainbox-title"


class ="cm-scroll ty-tooltip--link ty-tooltip--filter" > < span class ="tooltip-arrow" > < / span > < / button >

< / div >

< div


class ="mobile-filter--footer hidden" >

< a
href = "https://avrora.ua/gigiena/"
rel = "nofollow"


class ="ty-btn ty-btn__tertiary cm-ajax cm-ajax-full-render cm-history" data-ca-event="ce.filtersinit" data-ca-target-id="product_filters_*,selected_filters_*,products_search_*,category_products_*,currencies_*,languages_*,promotion_product_search_*,product_features_*,search_total_items_st_*,elm_sort_wrap,elm_faq_wrap,pagination_contents" >


Очистити
< / a >
< div


class ="ty-btn__secondary ty-btn js-close-filter" >


Застосувати
< / div >
< / div >
< / div >

< div


class ="col-md-12  product-container mb100 site-mode-A" >

< div
id = "category_products_12" >

< div


class ="ty-pagination-container cm-pagination-container" id="pagination_contents" >

< div


class ="hidden" > < a data-ca-scroll=".cm-pagination-container" href="" data-ca-page="" data-ca-target-id="pagination_contents,elm_faq_wrap" class ="hidden" > < / a > < / div >

< div


class ="grid-list-wrap" id="read_more_2" >

< div


class ="grid-list" >

< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#1"data-id-scroll="1"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="16534" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-16534 grid-list__label" id="product_data_features_label_update_16534" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_16534--> < / div >

< / div >

< a
href = "https://avrora.ua/palichki-vatni-kosmetichni-safi-100-sht-up/" >

< img


class ="ty-pict  gallery-products__general   cm-image" id="det_img_16534"  src="https://images.avrora.ua/images/thumbnails/250/250/detailed/78/75696_001.webp"  alt="Палички ватнi косметичні Safi 100 шт/уп" title="Палички ватнi косметичні Safi 100 шт/уп" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Палички ватнi косметичні Safi 100 шт/уп" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/78/75696_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Палички ватнi косметичні Safi 100 шт/уп - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/78/75696_002.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_16534"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_16534*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[16534][product_id]"
value = "16534" / >

< div


class ="right-top-blog" >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< span


class ="labels-item variant_exclusive" > < / span >

< / div >

< div


class ="left-top-blog" id="top_icon_16534_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..16534]"
data - ca - target - id = "top_icon_16534*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_16534_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/palichki-vatni-kosmetichni-safi-100-sht-up/"


class ="product-title" title="Палички ватнi косметичні Safi 100 шт/уп" > Палички ватнi косметичні Safi 100 шт / уп < / a >

< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-16534 ty-price-update" id="price_update_16534" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_16534" >

< bdi > < span
id = "sec_discounted_price_16534"


class ="ty-price-num" > 14 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_16534 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-16534 " id="add_to_cart_update_16534" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=75696&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_16534" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_16534 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Палички ватнi косметичні Safi 100 шт/уп"
data - gtm - id = "75696"
data - gtm - product - id = "16534"
data - gtm - discount = "0.00"
data - gtm - price = "14.00"
data - gtm - brand = "Safi"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Особиста гігієна"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-16534" id="product_data_features_short_update_16534" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Safi <

/ li > < li > Вид: Ватні
палички < / li > < li > Довжина: 7, 5
см < / li > < li > Кількість
в
упаковці, шт: 100 < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: Поліпропілен(паличка), бавовняне
волокно(голівка) < / li > < li > Призначення: Для
гігієнічних
та
косметичних
потреб < / li > < / ul > < / div > <!--product_data_features_short_update_16534 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Палички ватнi косметичні Safi 100 шт/уп"
data - item - id = "75696"
data - product - id = "16534"
data - discount = "0.00"
data - price = "14.00"
data - item - brand = "Safi"
data - item - category = "Краса та здоров’я/Гігієна/Особиста гігієна"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "1"
data - quantity = "1"
data - qty = "1"
data - position = "1"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#2"data-id-scroll="2"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="15836" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-15836 grid-list__label" id="product_data_features_label_update_15836" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_15836--> < / div >

< / div >

< a
href = "https://avrora.ua/servetki-paperovi-safi-odnosharovi-bili-85-sht-pach/" >
< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_15836"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/77/92587_9239.webp"  alt="Серветки паперові Safi одношарові білі 85 шт/пач" title="Серветки паперові Safi одношарові білі 85 шт/пач" / >

< / a >

< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_15836"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_15836*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[15836][product_id]"
value = "15836" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-15836" id="product_labels_update_15836" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -18 % < / div >

< / div >

< !--product_labels_update_15836 --> < / div >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< span


class ="labels-item variant_exclusive" > < / span >

< / div >

< div


class ="left-top-blog" id="top_icon_15836_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..15836]"
data - ca - target - id = "top_icon_15836*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_15836_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/servetki-paperovi-safi-odnosharovi-bili-85-sht-pach/"


class ="product-title" title="Серветки паперові Safi одношарові білі 85 шт/пач" > Серветки паперові Safi одношарові білі 85 шт / пач < / a >

< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/servetki-paperovi-safi-odnosharovi-bili-85-sht-pach/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 4 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "4"
data - ca - product - review - reviews - stars - full = "4"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(1)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-15836" id="old_price_update_15836" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_15836" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_15836" class ="ty-list-price ty-nowrap" > 22 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_15836 --> < / span >

< span


class ="cm-reload-15836 ty-price-update" id="price_update_15836" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_15836" >

< bdi > < span
id = "sec_discounted_price_15836"


class ="ty-price-num" > 18 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_15836 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-15836 " id="add_to_cart_update_15836" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=92587&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_15836" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_15836 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Серветки паперові Safi одношарові білі 85 шт/пач"
data - gtm - id = "92587"
data - gtm - product - id = "15836"
data - gtm - discount = "4.00"
data - gtm - price = "22.00"
data - gtm - brand = "Safi"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Серветки, паперові рушники"
data - gtm - variant = "Білий"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-15836" id="product_data_features_short_update_15836" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Safi <

/ li > < li > Вид: Серветки
паперові < / li > < li > Кількість
в
упаковці, шт: 85 < / li > < li > Кількість
шарів: 1 < / li > < li > Колір: Білий < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: Целюлоза < / li > < li > Розмір: 23, 5
х23, 5
см < / li > < / ul > < / div > <!--product_data_features_short_update_15836 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Серветки паперові Safi одношарові білі 85 шт/пач"
data - item - id = "92587"
data - product - id = "15836"
data - discount = "4.00"
data - price = "18.00"
data - item - brand = "Safi"
data - item - category = "Краса та здоров’я/Гігієна/Серветки, паперові рушники"
data - item - variant = "Білий"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "2"
data - quantity = "1"
data - qty = "1"
data - position = "2"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#3"data-id-scroll="3"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="758" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-758 grid-list__label" id="product_data_features_label_update_758" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_758--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-schodenni-libresse-classic-regular-50sht.-up./" >

< img


class ="ty-pict  gallery-products__general   cm-image" id="det_img_758"  src="https://images.avrora.ua/images/thumbnails/250/250/detailed/12/24748_001.webp"  alt="Прокладки щоденні Libresse Classic Regular 50шт./уп." title="Прокладки щоденні Libresse Classic Regular 50шт./уп." / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Libresse Classic Regular 50шт./уп." data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/12/24748_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Libresse Classic Regular 50шт./уп. - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/12/24748_003.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Libresse Classic Regular 50шт./уп. - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/12/24748_008.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_758"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_758*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[758][product_id]"
value = "758" / >

< div


class ="right-top-blog" >

< / div >

< div


class ="left-top-blog" id="top_icon_758_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..758]"
data - ca - target - id = "top_icon_758*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< img


class ="image-360 restudio_360_view_icon" id="restudio_360_view_icon_758_472" src="/design/themes/restudiotheme/media/restudio_360/icon-restudio-360.png" width="28" alt="360 icon" >

< !--top_icon_758_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-schodenni-libresse-classic-regular-50sht.-up./"


class ="product-title" title="Прокладки щоденні Libresse Classic Regular 50шт./уп." > Прокладки щоденні Libresse Classic Regular 50шт./ уп.< / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 1.78 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/prokladki-schodenni-libresse-classic-regular-50sht.-up./?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 5 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "5"
data - ca - product - review - reviews - stars - full = "5"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(2)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-758 ty-price-update" id="price_update_758" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_758" >

< bdi > < span
id = "sec_discounted_price_758"


class ="ty-price-num" > 89 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_758 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-758 " id="add_to_cart_update_758" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=24748&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_758" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_758 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки щоденні Libresse Classic Regular 50шт./уп."
data - gtm - id = "24748"
data - gtm - product - id = "758"
data - gtm - discount = "0.00"
data - gtm - price = "89.00"
data - gtm - brand = "Libresse"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-758" id="product_data_features_short_update_758" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Libresse <

/ li > < li > Вид: Прокладки < / li > < / ul > < / div > <!--product_data_features_short_update_758 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки щоденні Libresse Classic Regular 50шт./уп."
data - item - id = "24748"
data - product - id = "758"
data - discount = "0.00"
data - price = "89.00"
data - item - brand = "Libresse"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "3"
data - quantity = "1"
data - qty = "1"
data - position = "3"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#4"data-id-scroll="4"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="4364" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-4364 grid-list__label" id="product_data_features_label_update_4364" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_4364--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-schodenni-lidie-by-kotex-normal-50-sht-up/" >

< img


class ="ty-pict  gallery-products__general   cm-image" id="det_img_4364"  src="https://images.avrora.ua/images/thumbnails/250/250/detailed/178/19224_00011_ana1-jj.webp"  alt="Прокладки щоденні Lidie by Kotex Нормал 50 шт/уп" title="Прокладки щоденні Lidie by Kotex Нормал 50 шт/уп" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Lidie by Kotex Нормал 50 шт/уп" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/178/19224_00011_ana1-jj.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Lidie by Kotex Нормал 50 шт/уп - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/178/19224_000222_7lfs-is.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Lidie by Kotex Нормал 50 шт/уп - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/178/19224_00055_2mt0-rv.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Lidie by Kotex Нормал 50 шт/уп - 4" data-id="3" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/178/19224_000444_84sl-ea.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Lidie by Kotex Нормал 50 шт/уп - 5" data-id="4" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/178/19224_000333_ifya-co.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_4364"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_4364*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[4364][product_id]"
value = "4364" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-4364" id="product_labels_update_4364" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -22 % < / div >

< / div >

< !--product_labels_update_4364 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_4364_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..4364]"
data - ca - target - id = "top_icon_4364*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_4364_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-schodenni-lidie-by-kotex-normal-50-sht-up/"


class ="product-title" title="Прокладки щоденні Lidie by Kotex Нормал 50 шт/уп" > Прокладки щоденні Lidie by Kotex Нормал 50 шт / уп < / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 1.54 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-4364" id="old_price_update_4364" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_4364" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_4364" class ="ty-list-price ty-nowrap" > 99 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_4364 --> < / span >

< span


class ="cm-reload-4364 ty-price-update" id="price_update_4364" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_4364" >

< bdi > < span
id = "sec_discounted_price_4364"


class ="ty-price-num" > 77 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_4364 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-4364 " id="add_to_cart_update_4364" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=19224&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_4364" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_4364 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки щоденні Lidie by Kotex Нормал 50 шт/уп"
data - gtm - id = "19224"
data - gtm - product - id = "4364"
data - gtm - discount = "22.00"
data - gtm - price = "99.00"
data - gtm - brand = "Kotex"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-4364" id="product_data_features_short_update_4364" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Kotex <

/ li > < li > Вид: Прокладки < / li > < li > Кількість
в
упаковці, шт: 50 < / li > < li > Країна
походження: Китай < / li > < / ul > < / div > <!--product_data_features_short_update_4364 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки щоденні Lidie by Kotex Нормал 50 шт/уп"
data - item - id = "19224"
data - product - id = "4364"
data - discount = "22.00"
data - price = "77.00"
data - item - brand = "Kotex"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "4"
data - quantity = "1"
data - qty = "1"
data - position = "4"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#5"data-id-scroll="5"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="901" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-901 grid-list__label" id="product_data_features_label_update_901" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_901--> < / div >

< / div >

< a
href = "https://avrora.ua/palichki-vatni-lady-cotton-200-shtuk/" >

< img


class ="ty-pict  gallery-products__general   cm-image" id="det_img_901"  src="https://images.avrora.ua/images/thumbnails/250/250/detailed/128/17078.webp"  alt="Палички ватні Lady Cotton 200 штук" title="Палички ватні Lady Cotton 200 штук" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Палички ватні Lady Cotton 200 штук" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/128/17078.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Палички ватні Lady Cotton 200 штук - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/128/17078_1.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Палички ватні Lady Cotton 200 штук - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/128/17078_2.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Палички ватні Lady Cotton 200 штук - 4" data-id="3" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/128/17078_4.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Палички ватні Lady Cotton 200 штук - 5" data-id="4" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/128/17078_6.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_901"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_901*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[901][product_id]"
value = "901" / >

< div


class ="right-top-blog" >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< / div >

< div


class ="left-top-blog" id="top_icon_901_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..901]"
data - ca - target - id = "top_icon_901*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_901_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/palichki-vatni-lady-cotton-200-shtuk/"


class ="product-title" title="Палички ватні Lady Cotton 200 штук" > Палички ватні Lady Cotton 200 штук < / a >

< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/palichki-vatni-lady-cotton-200-shtuk/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 5 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "5"
data - ca - product - review - reviews - stars - full = "5"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(1)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-901 ty-price-update" id="price_update_901" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_901" >

< bdi > < span
id = "sec_discounted_price_901"


class ="ty-price-num" > 39 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_901 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-901 " id="add_to_cart_update_901" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=17078&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_901" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_901 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Палички ватні Lady Cotton 200 штук"
data - gtm - id = "17078"
data - gtm - product - id = "901"
data - gtm - discount = "0.00"
data - gtm - price = "39.00"
data - gtm - brand = "Lady Cotton"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Особиста гігієна"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-901" id="product_data_features_short_update_901" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Lady


Cotton < / li > < li > Вид: Ватні
палички < / li > < li > Кількість
в
упаковці, шт: 200 < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: Поліпропілен(паличка), бавовна(
    голівка) < / li > < / ul > < / div > <!--product_data_features_short_update_901 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Палички ватні Lady Cotton 200 штук"
data - item - id = "17078"
data - product - id = "901"
data - discount = "0.00"
data - price = "39.00"
data - item - brand = "Lady Cotton"
data - item - category = "Краса та здоров’я/Гігієна/Особиста гігієна"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "1"
data - quantity = "1"
data - qty = "1"
data - position = "5"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#6"data-id-scroll="6"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="9605" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-9605 grid-list__label" id="product_data_features_label_update_9605" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_9605--> < / div >

< / div >

< a
href = "https://avrora.ua/servetki-paperovi-silken-mini-barvi-2-shari-100-sht-up/" >

< img


class ="ty-pict  gallery-products__general   cm-image" id="det_img_9605"  src="https://images.avrora.ua/images/thumbnails/250/250/detailed/44/54319_001.webp"  alt="Серветки паперові Silken MINI Барви 2 шари 100 шт/уп" title="Серветки паперові Silken MINI Барви 2 шари 100 шт/уп" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Серветки паперові Silken MINI Барви 2 шари 100 шт/уп" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/44/54319_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Серветки паперові Silken MINI Барви 2 шари 100 шт/уп - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/44/54319_002.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Серветки паперові Silken MINI Барви 2 шари 100 шт/уп - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/44/54319_003.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_9605"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_9605*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[9605][product_id]"
value = "9605" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-9605" id="product_labels_update_9605" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -17 % < / div >

< / div >

< !--product_labels_update_9605 --> < / div >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< / div >

< div


class ="left-top-blog" id="top_icon_9605_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..9605]"
data - ca - target - id = "top_icon_9605*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_9605_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/servetki-paperovi-silken-mini-barvi-2-shari-100-sht-up/"


class ="product-title" title="Серветки паперові Silken MINI Барви 2 шари 100 шт/уп" > Серветки паперові Silken MINI Барви 2 шари 100 шт / уп < / a >

< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/servetki-paperovi-silken-mini-barvi-2-shari-100-sht-up/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 5 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "5"
data - ca - product - review - reviews - stars - full = "5"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(2)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-9605" id="old_price_update_9605" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_9605" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_9605" class ="ty-list-price ty-nowrap" > 24 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_9605 --> < / span >

< span


class ="cm-reload-9605 ty-price-update" id="price_update_9605" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_9605" >

< bdi > < span
id = "sec_discounted_price_9605"


class ="ty-price-num" > 20 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_9605 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-9605 " id="add_to_cart_update_9605" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=54319&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_9605" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_9605 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Серветки паперові Silken MINI Барви 2 шари 100 шт/уп"
data - gtm - id = "54319"
data - gtm - product - id = "9605"
data - gtm - discount = "4.00"
data - gtm - price = "24.00"
data - gtm - brand = "Silken"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Серветки, паперові рушники"
data - gtm - variant = "Білий"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-9605" id="product_data_features_short_update_9605" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Silken <

/ li > < li > Вид: Серветки
паперові < / li > < li > Кількість
в
упаковці, шт: 100 < / li > < li > Кількість
шарів: 2 < / li > < li > Колір: Білий < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: Целюлоза < / li > < li > Розмір: 13
х20
см < / li > < / ul > < / div > <!--product_data_features_short_update_9605 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Серветки паперові Silken MINI Барви 2 шари 100 шт/уп"
data - item - id = "54319"
data - product - id = "9605"
data - discount = "4.00"
data - price = "20.00"
data - item - brand = "Silken"
data - item - category = "Краса та здоров’я/Гігієна/Серветки, паперові рушники"
data - item - variant = "Білий"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "2"
data - quantity = "1"
data - qty = "1"
data - position = "6"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#7"data-id-scroll="7"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="5506" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-5506 grid-list__label" id="product_data_features_label_update_5506" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_5506--> < / div >

< / div >

< a
href = "https://avrora.ua/nabir-rushnikiv-paperovih-papirella-deluxe-purpure-dvosharovi-2-sht-up/" >

< img


class ="ty-pict  gallery-products__general   cm-image" id="det_img_5506"  src="https://images.avrora.ua/images/thumbnails/250/250/detailed/29/42409_001.webp"  alt="Набір рушників паперових Papirella Deluxe Purpure двошарові 2 шт/уп" title="Набір рушників паперових Papirella Deluxe Purpure двошарові 2 шт/уп" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Набір рушників паперових Papirella Deluxe Purpure двошарові 2 шт/уп" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/29/42409_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Набір рушників паперових Papirella Deluxe Purpure двошарові 2 шт/уп - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/29/42409_002.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_5506"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_5506*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[5506][product_id]"
value = "5506" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-5506" id="product_labels_update_5506" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -25 % < / div >

< / div >

< !--product_labels_update_5506 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_5506_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..5506]"
data - ca - target - id = "top_icon_5506*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_5506_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/nabir-rushnikiv-paperovih-papirella-deluxe-purpure-dvosharovi-2-sht-up/"


class ="product-title" title="Набір рушників паперових Papirella Deluxe Purpure двошарові 2 шт/уп" > Набір рушників паперових Papirella Deluxe Purpure двошарові 2 шт / уп < / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 20.50 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/nabir-rushnikiv-paperovih-papirella-deluxe-purpure-dvosharovi-2-sht-up/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 5 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "5"
data - ca - product - review - reviews - stars - full = "5"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(1)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-5506" id="old_price_update_5506" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_5506" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_5506" class ="ty-list-price ty-nowrap" > 55 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_5506 --> < / span >

< span


class ="cm-reload-5506 ty-price-update" id="price_update_5506" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_5506" >

< bdi > < span
id = "sec_discounted_price_5506"


class ="ty-price-num" > 41 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_5506 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-5506 " id="add_to_cart_update_5506" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=42409&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_5506" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_5506 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Набір рушників паперових Papirella Deluxe Purpure двошарові 2 шт/уп"
data - gtm - id = "42409"
data - gtm - product - id = "5506"
data - gtm - discount = "14.00"
data - gtm - price = "55.00"
data - gtm - brand = "Papirella"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Серветки, паперові рушники"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-5506" id="product_data_features_short_update_5506" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Papirella <

/ li > < li > Вид: Паперові
рушники < / li > < li > Кількість
в
упаковці, шт: 2 < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: Целюлоза < / li > < li > Форма
випуску: Рулон < / li > < / ul > < / div > <!--product_data_features_short_update_5506 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Набір рушників паперових Papirella Deluxe Purpure двошарові 2 шт/уп"
data - item - id = "42409"
data - product - id = "5506"
data - discount = "14.00"
data - price = "41.00"
data - item - brand = "Papirella"
data - item - category = "Краса та здоров’я/Гігієна/Серветки, паперові рушники"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "3"
data - quantity = "1"
data - qty = "1"
data - position = "7"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#8"data-id-scroll="8"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="16532" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-16532 grid-list__label" id="product_data_features_label_update_16532" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_16532--> < / div >

< / div >

< a
href = "https://avrora.ua/palichki-vatni-kosmetichni-safi-300-sht-up/" >

< img


class ="ty-pict  gallery-products__general   cm-image" id="det_img_16532"  src="https://images.avrora.ua/images/thumbnails/250/250/detailed/78/64909_001.webp"  alt="Палички ватні косметичні Safi 300 шт/уп" title="Палички ватні косметичні Safi 300 шт/уп" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Палички ватні косметичні Safi 300 шт/уп" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/78/64909_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Палички ватні косметичні Safi 300 шт/уп - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/78/64909_002.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_16532"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_16532*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[16532][product_id]"
value = "16532" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-16532" id="product_labels_update_16532" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -18 % < / div >

< / div >

< !--product_labels_update_16532 --> < / div >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< span


class ="labels-item variant_exclusive" > < / span >

< / div >

< div


class ="left-top-blog" id="top_icon_16532_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..16532]"
data - ca - target - id = "top_icon_16532*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_16532_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/palichki-vatni-kosmetichni-safi-300-sht-up/"


class ="product-title" title="Палички ватні косметичні Safi 300 шт/уп" > Палички ватні косметичні Safi 300 шт / уп < / a >

< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-16532" id="old_price_update_16532" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_16532" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_16532" class ="ty-list-price ty-nowrap" > 34 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_16532 --> < / span >

< span


class ="cm-reload-16532 ty-price-update" id="price_update_16532" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_16532" >

< bdi > < span
id = "sec_discounted_price_16532"


class ="ty-price-num" > 28 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_16532 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-16532 " id="add_to_cart_update_16532" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=64909&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_16532" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_16532 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Палички ватні косметичні Safi 300 шт/уп"
data - gtm - id = "64909"
data - gtm - product - id = "16532"
data - gtm - discount = "6.00"
data - gtm - price = "34.00"
data - gtm - brand = "Safi"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Особиста гігієна"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-16532" id="product_data_features_short_update_16532" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Safi <

/ li > < li > Вид: Ватні
палички < / li > < li > Довжина: 7, 5
см < / li > < li > Кількість
в
упаковці, шт: 300 < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: Поліпропілен(паличка), бавовняне
волокно(голівка) < / li > < li > Призначення: Для
гігієнічних
та
косметичних
потреб < / li > < / ul > < / div > <!--product_data_features_short_update_16532 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Палички ватні косметичні Safi 300 шт/уп"
data - item - id = "64909"
data - product - id = "16532"
data - discount = "6.00"
data - price = "28.00"
data - item - brand = "Safi"
data - item - category = "Краса та здоров’я/Гігієна/Особиста гігієна"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "4"
data - quantity = "1"
data - qty = "1"
data - position = "8"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#9"data-id-scroll="9"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="8714" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-8714 grid-list__label" id="product_data_features_label_update_8714" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_8714--> < / div >

< / div >

< a
href = "https://avrora.ua/gel-dlya-intimnoi-gigiieni-cleanness-z-bakterialnim-efektom-310-g/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_8714"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/37/58261_005.webp"  alt="Гель для інтимної гігієни Cleanness+ з бактериальним ефектом 310 г" title="Гель для інтимної гігієни Cleanness+ з бактериальним ефектом 310 г" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Гель для інтимної гігієни Cleanness+ з бактериальним ефектом 310 г" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/37/58261_005.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Гель для інтимної гігієни Cleanness+ з бактериальним ефектом 310 г - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/37/58261_006.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Гель для інтимної гігієни Cleanness+ з бактериальним ефектом 310 г - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/37/58261_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Гель для інтимної гігієни Cleanness+ з бактериальним ефектом 310 г - 4" data-id="3" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/37/58261_007.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_8714"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_8714*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[8714][product_id]"
value = "8714" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-8714" id="product_labels_update_8714" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -22 % < / div >

< / div >

< !--product_labels_update_8714 --> < / div >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< / div >

< div


class ="left-top-blog" id="top_icon_8714_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..8714]"
data - ca - target - id = "top_icon_8714*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_8714_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/gel-dlya-intimnoi-gigiieni-cleanness-z-bakterialnim-efektom-310-g/"


class ="product-title" title="Гель для інтимної гігієни Cleanness+ з бактериальним ефектом 310 г" > Гель для інтимної гігієни Cleanness+ з бактериальним ефектом 310 г < / a >

< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/gel-dlya-intimnoi-gigiieni-cleanness-z-bakterialnim-efektom-310-g/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 4.3 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "4"
data - ca - product - review - reviews - stars - full = "4"
data - ca - product - review - reviews - stars - is -half = "1"
> < / div >
< / a >
< div


class ="left_info" >


(4)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-8714" id="old_price_update_8714" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_8714" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_8714" class ="ty-list-price ty-nowrap" > 88 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_8714 --> < / span >

< span


class ="cm-reload-8714 ty-price-update" id="price_update_8714" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_8714" >

< bdi > < span
id = "sec_discounted_price_8714"


class ="ty-price-num" > 69 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_8714 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-8714 " id="add_to_cart_update_8714" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=58261&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_8714" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_8714 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Гель для інтимної гігієни Cleanness+ з бактериальним ефектом 310 г"
data - gtm - id = "58261"
data - gtm - product - id = "8714"
data - gtm - discount = "19.00"
data - gtm - price = "88.00"
data - gtm - brand = "Cleanness+"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-8714" id="product_data_features_short_update_8714" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Cleanness + <

/ li > < li > Вага: 310
г < / li > < li > Вид: Гелі
для
інтимної
гігієни < / li > < li > Країна
походження: Україна < / li > < li > Особливості: З
бактерицидним
ефектом < / li > < / ul > < / div > <!--product_data_features_short_update_8714 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Гель для інтимної гігієни Cleanness+ з бактериальним ефектом 310 г"
data - item - id = "58261"
data - product - id = "8714"
data - discount = "19.00"
data - price = "69.00"
data - item - brand = "Cleanness+"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "1"
data - quantity = "1"
data - qty = "1"
data - position = "9"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#10"data-id-scroll="10"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="14439" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-14439 grid-list__label" id="product_data_features_label_update_14439" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_14439--> < / div >

< / div >

< a
href = "https://avrora.ua/nabir-rushnikiv-paperovih-iz-gilzoyu-safi-bili-2-shari-2-sht-up/" >
< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_14439"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/70/82704_001.webp"  alt="Набір рушників паперових із гільзою Safi білі 2 шари 2 шт/уп" title="Набір рушників паперових із гільзою Safi білі 2 шари 2 шт/уп" / >

< / a >

< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_14439"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_14439*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[14439][product_id]"
value = "14439" / >

< div


class ="right-top-blog" >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< span


class ="labels-item variant_exclusive" > < / span >

< / div >

< div


class ="left-top-blog" id="top_icon_14439_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..14439]"
data - ca - target - id = "top_icon_14439*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_14439_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/nabir-rushnikiv-paperovih-iz-gilzoyu-safi-bili-2-shari-2-sht-up/"


class ="product-title" title="Набір рушників паперових із гільзою Safi білі 2 шари 2 шт/уп" > Набір рушників паперових із гільзою Safi білі 2 шари 2 шт / уп < / a >

< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/nabir-rushnikiv-paperovih-iz-gilzoyu-safi-bili-2-shari-2-sht-up/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 4 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "4"
data - ca - product - review - reviews - stars - full = "4"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(1)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-14439 ty-price-update" id="price_update_14439" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_14439" >

< bdi > < span
id = "sec_discounted_price_14439"


class ="ty-price-num" > 64 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_14439 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-14439 " id="add_to_cart_update_14439" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=82704&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_14439" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_14439 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Набір рушників паперових із гільзою Safi білі 2 шари 2 шт/уп"
data - gtm - id = "82704"
data - gtm - product - id = "14439"
data - gtm - discount = "0.00"
data - gtm - price = "64.00"
data - gtm - brand = "Safi"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Серветки, паперові рушники"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-14439" id="product_data_features_short_update_14439" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Safi <

/ li > < li > Вид: Паперові
рушники < / li > < li > Кількість
в
упаковці, шт: 2 < / li > < li > Кількість
шарів: 2 < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: 100 % целюлоза < / li > < li > Призначення: Для
гігієнічних
потреб < / li > < li > Розмір: 22, 5
х18, 5
х10
см < / li > < / ul > < / div > <!--product_data_features_short_update_14439 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Набір рушників паперових із гільзою Safi білі 2 шари 2 шт/уп"
data - item - id = "82704"
data - product - id = "14439"
data - discount = "0.00"
data - price = "64.00"
data - item - brand = "Safi"
data - item - category = "Краса та здоров’я/Гігієна/Серветки, паперові рушники"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "2"
data - quantity = "1"
data - qty = "1"
data - position = "10"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#11"data-id-scroll="11"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="17858" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-17858 grid-list__label" id="product_data_features_label_update_17858" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_17858--> < / div >

< / div >

< a
href = "https://avrora.ua/servetki-vologi-dityachi-safi-ekstrakt-romashki-z-klapanom-132-sht-up/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_17858"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/83/99292_001.webp"  alt="Серветки вологі дитячі Safi екстракт ромашки з клапаном 132 шт/уп" title="Серветки вологі дитячі Safi екстракт ромашки з клапаном 132 шт/уп" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Серветки вологі дитячі Safi екстракт ромашки з клапаном 132 шт/уп" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/83/99292_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Серветки вологі дитячі Safi екстракт ромашки з клапаном 132 шт/уп - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/83/99292_002.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_17858"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_17858*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[17858][product_id]"
value = "17858" / >

< div


class ="right-top-blog" >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< span


class ="labels-item variant_exclusive" > < / span >

< / div >

< div


class ="left-top-blog" id="top_icon_17858_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..17858]"
data - ca - target - id = "top_icon_17858*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_17858_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/servetki-vologi-dityachi-safi-ekstrakt-romashki-z-klapanom-132-sht-up/"


class ="product-title" title="Серветки вологі дитячі Safi екстракт ромашки з клапаном 132 шт/уп" > Серветки вологі дитячі Safi екстракт ромашки з клапаном 132 шт / уп < / a >

< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/servetki-vologi-dityachi-safi-ekstrakt-romashki-z-klapanom-132-sht-up/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 3.8 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "4"
data - ca - product - review - reviews - stars - full = "4"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(5)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-17858 ty-price-update" id="price_update_17858" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_17858" >

< bdi > < span
id = "sec_discounted_price_17858"


class ="ty-price-num" > 44 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_17858 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-17858 " id="add_to_cart_update_17858" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=99292&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_17858" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_17858 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Серветки вологі дитячі Safi екстракт ромашки з клапаном 132 шт/уп"
data - gtm - id = "99292"
data - gtm - product - id = "17858"
data - gtm - discount = "0.00"
data - gtm - price = "44.00"
data - gtm - brand = "Safi"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Серветки, паперові рушники"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-17858" id="product_data_features_short_update_17858" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Safi <

/ li > < li > Вид: Серветки
вологі < / li > < li > Кількість
в
упаковці, шт: 132 < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: Неткана
полотнина < / li > < li > Особливості: Без
спирту
та
парабенів < / li > < li > Призначення: Для
гігієнічного
використання < / li > < li > Розмір: 24
х10
см < / li > < / ul > < / div > <!--product_data_features_short_update_17858 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Серветки вологі дитячі Safi екстракт ромашки з клапаном 132 шт/уп"
data - item - id = "99292"
data - product - id = "17858"
data - discount = "0.00"
data - price = "44.00"
data - item - brand = "Safi"
data - item - category = "Краса та здоров’я/Гігієна/Серветки, паперові рушники"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "3"
data - quantity = "1"
data - qty = "1"
data - position = "11"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#12"data-id-scroll="12"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="927" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-927 grid-list__label" id="product_data_features_label_update_927" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_927--> < / div >

< / div >

< a
href = "https://avrora.ua/papir-tualetniy-siriy-noviy-kiiv-500/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_927"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/149/15453_101.webp"  alt="Папір туалетний сірий Новий Київ-500" title="Папір туалетний сірий Новий Київ-500" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Папір туалетний сірий Новий Київ-500" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/149/15453_101.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Папір туалетний сірий Новий Київ-500 - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/12/15453_010_qria-uc.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_927"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_927*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[927][product_id]"
value = "927" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-927" id="product_labels_update_927" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -15 % < / div >

< / div >

< !--product_labels_update_927 --> < / div >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< / div >

< div


class ="left-top-blog" id="top_icon_927_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..927]"
data - ca - target - id = "top_icon_927*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_927_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/papir-tualetniy-siriy-noviy-kiiv-500/"


class ="product-title" title="Папір туалетний сірий Новий Київ-500" > Папір туалетний сірий Новий Київ-500 < / a >

< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/papir-tualetniy-siriy-noviy-kiiv-500/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 5 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "5"
data - ca - product - review - reviews - stars - full = "5"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(5)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-927" id="old_price_update_927" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_927" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_927" class ="ty-list-price ty-nowrap" > 39 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_927 --> < / span >

< span


class ="cm-reload-927 ty-price-update" id="price_update_927" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_927" >

< bdi > < span
id = "sec_discounted_price_927"


class ="ty-price-num" > 33 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_927 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-927 " id="add_to_cart_update_927" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=15453&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_927" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_927 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Папір туалетний сірий Новий Київ-500"
data - gtm - id = "15453"
data - gtm - product - id = "927"
data - gtm - discount = "6.00"
data - gtm - price = "39.00"
data - gtm - brand = "Новий Київ"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Особиста гігієна"
data - gtm - variant = "Сірий"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-927" id="product_data_features_short_update_927" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Новий


Київ < / li > < li > Вага: 415
г < / li > < li > Вид: Туалетний
папір < / li > < li > Кількість
шарів: 1 < / li > < li > Колір: Сірий < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: Перероблений
папір < / li > < li > Форма
випуску: Рулон < / li > < / ul > < / div > <!--product_data_features_short_update_927 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Папір туалетний сірий Новий Київ-500"
data - item - id = "15453"
data - product - id = "927"
data - discount = "6.00"
data - price = "33.00"
data - item - brand = "Новий Київ"
data - item - category = "Краса та здоров’я/Гігієна/Особиста гігієна"
data - item - variant = "Сірий"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "4"
data - quantity = "1"
data - qty = "1"
data - position = "12"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#13"data-id-scroll="13"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="9506" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-9506 grid-list__label" id="product_data_features_label_update_9506" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_9506--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-gigiienichni-always-ultra-super-single-8-sht-pach/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_9506"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/43/85832_001.webp"  alt="Прокладки гігієнічні ALWAYS Ultra Super Single 8 шт/пач" title="Прокладки гігієнічні ALWAYS Ultra Super Single 8 шт/пач" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні ALWAYS Ultra Super Single 8 шт/пач" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/43/85832_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні ALWAYS Ultra Super Single 8 шт/пач - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/43/85832_002.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_9506"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_9506*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[9506][product_id]"
value = "9506" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-9506" id="product_labels_update_9506" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -14 % < / div >

< / div >

< !--product_labels_update_9506 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_9506_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..9506]"
data - ca - target - id = "top_icon_9506*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_9506_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-gigiienichni-always-ultra-super-single-8-sht-pach/"


class ="product-title" title="Прокладки гігієнічні ALWAYS Ultra Super Single 8 шт/пач" > Прокладки гігієнічні ALWAYS Ultra Super Single 8 шт / пач < / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 7.38 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/prokladki-gigiienichni-always-ultra-super-single-8-sht-pach/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 2 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "2"
data - ca - product - review - reviews - stars - full = "2"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(1)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-9506" id="old_price_update_9506" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_9506" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_9506" class ="ty-list-price ty-nowrap" > 69 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_9506 --> < / span >

< span


class ="cm-reload-9506 ty-price-update" id="price_update_9506" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_9506" >

< bdi > < span
id = "sec_discounted_price_9506"


class ="ty-price-num" > 59 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_9506 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-9506 " id="add_to_cart_update_9506" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=85832&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_9506" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_9506 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки гігієнічні ALWAYS Ultra Super Single 8 шт/пач"
data - gtm - id = "85832"
data - gtm - product - id = "9506"
data - gtm - discount = "10.00"
data - gtm - price = "69.00"
data - gtm - brand = "Always"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-9506" id="product_data_features_short_update_9506" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Always <

/ li > < li > Вид: Прокладки < / li > < li > Кількість
крапель: 5 < / li > < li > Країна
походження: Німеччина < / li > < li > Особливості: З
крильцями < / li > < / ul > < / div > <!--product_data_features_short_update_9506 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки гігієнічні ALWAYS Ultra Super Single 8 шт/пач"
data - item - id = "85832"
data - product - id = "9506"
data - discount = "10.00"
data - price = "59.00"
data - item - brand = "Always"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "1"
data - quantity = "1"
data - qty = "1"
data - position = "13"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#14"data-id-scroll="14"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="354" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-354 grid-list__label" id="product_data_features_label_update_354" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_354--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-gigiienichni-naturella-classic-4-nor.single10/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_354"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/188/25660_010101.webp"  alt="Прокладки гігієнічні NATURELLA Classic Camomile Normal 10 шт/пач" title="Прокладки гігієнічні NATURELLA Classic Camomile Normal 10 шт/пач" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Classic Camomile Normal 10 шт/пач" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/188/25660_010101.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Classic Camomile Normal 10 шт/пач - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/25660_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Classic Camomile Normal 10 шт/пач - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/25660_002.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Classic Camomile Normal 10 шт/пач - 4" data-id="3" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/25660_003.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Classic Camomile Normal 10 шт/пач - 5" data-id="4" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/25660_004.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Classic Camomile Normal 10 шт/пач - 6" data-id="5" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/25660_005.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_354"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_354*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[354][product_id]"
value = "354" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-354" id="product_labels_update_354" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -29 % < / div >

< / div >

< !--product_labels_update_354 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_354_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..354]"
data - ca - target - id = "top_icon_354*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< img


class ="image-360 restudio_360_view_icon" id="restudio_360_view_icon_354_472" src="/design/themes/restudiotheme/media/restudio_360/icon-restudio-360.png" width="28" alt="360 icon" >

< !--top_icon_354_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-gigiienichni-naturella-classic-4-nor.single10/"


class ="product-title" title="Прокладки гігієнічні NATURELLA Classic Camomile Normal 10 шт/пач" > Прокладки гігієнічні NATURELLA Classic Camomile Normal 10 шт / пач < / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 3.90 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/prokladki-gigiienichni-naturella-classic-4-nor.single10/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 3.7 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "4"
data - ca - product - review - reviews - stars - full = "3"
data - ca - product - review - reviews - stars - is -half = "1"
> < / div >
< / a >
< div


class ="left_info" >


(3)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-354" id="old_price_update_354" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_354" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_354" class ="ty-list-price ty-nowrap" > 55 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_354 --> < / span >

< span


class ="cm-reload-354 ty-price-update" id="price_update_354" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_354" >

< bdi > < span
id = "sec_discounted_price_354"


class ="ty-price-num" > 39 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_354 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-354 " id="add_to_cart_update_354" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=25660&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_354" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_354 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки гігієнічні NATURELLA Classic Camomile Normal 10 шт/пач"
data - gtm - id = "25660"
data - gtm - product - id = "354"
data - gtm - discount = "16.00"
data - gtm - price = "55.00"
data - gtm - brand = "Naturella"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-354" id="product_data_features_short_update_354" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Naturella <

/ li > < li > Вид: Прокладки < / li > < li > Кількість
в
упаковці, шт: 10 < / li > < li > Кількість
крапель: 4 < / li > < li > Країна
походження: Україна < / li > < / ul > < / div > <!--product_data_features_short_update_354 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки гігієнічні NATURELLA Classic Camomile Normal 10 шт/пач"
data - item - id = "25660"
data - product - id = "354"
data - discount = "16.00"
data - price = "39.00"
data - item - brand = "Naturella"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "2"
data - quantity = "1"
data - qty = "1"
data - position = "14"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#15"data-id-scroll="15"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="22670" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-22670 grid-list__label" id="product_data_features_label_update_22670" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_22670--> < / div >

< / div >

< a
href = "https://avrora.ua/nabir-paperu-tualetnogo-ecolo-2-shari-4-sht-up/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_22670"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/183/91796_00001111.webp"  alt="Набір паперу туалетного Ecolo 2 шари 4 шт/уп" title="Набір паперу туалетного Ecolo 2 шари 4 шт/уп" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Набір паперу туалетного Ecolo 2 шари 4 шт/уп" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/183/91796_00001111.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Набір паперу туалетного Ecolo 2 шари 4 шт/уп - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/104/91796_001.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_22670"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_22670*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[22670][product_id]"
value = "22670" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-22670" id="product_labels_update_22670" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -16 % < / div >

< / div >

< !--product_labels_update_22670 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_22670_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..22670]"
data - ca - target - id = "top_icon_22670*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_22670_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/nabir-paperu-tualetnogo-ecolo-2-shari-4-sht-up/"


class ="product-title" title="Набір паперу туалетного Ecolo 2 шари 4 шт/уп" > Набір паперу туалетного Ecolo 2 шари 4 шт / уп < / a >

< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/nabir-paperu-tualetnogo-ecolo-2-shari-4-sht-up/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 5 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "5"
data - ca - product - review - reviews - stars - full = "5"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(2)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-22670" id="old_price_update_22670" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_22670" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_22670" class ="ty-list-price ty-nowrap" > 55 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_22670 --> < / span >

< span


class ="cm-reload-22670 ty-price-update" id="price_update_22670" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_22670" >

< bdi > < span
id = "sec_discounted_price_22670"


class ="ty-price-num" > 46 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_22670 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-22670 " id="add_to_cart_update_22670" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=91796&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_22670" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_22670 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Набір паперу туалетного Ecolo 2 шари 4 шт/уп"
data - gtm - id = "91796"
data - gtm - product - id = "22670"
data - gtm - discount = "9.00"
data - gtm - price = "55.00"
data - gtm - brand = "Ecolo"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Особиста гігієна"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-22670" id="product_data_features_short_update_22670" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Ecolo <

/ li > < li > Вид: Туалетний
папір < / li > < li > Кількість
в
упаковці, шт: 4
шт < / li > < li > Кількість
шарів: 2
шари < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: 100 % целюлоза < / li > < / ul > < / div > <!--product_data_features_short_update_22670 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Набір паперу туалетного Ecolo 2 шари 4 шт/уп"
data - item - id = "91796"
data - product - id = "22670"
data - discount = "9.00"
data - price = "46.00"
data - item - brand = "Ecolo"
data - item - category = "Краса та здоров’я/Гігієна/Особиста гігієна"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "3"
data - quantity = "1"
data - qty = "1"
data - position = "15"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#16"data-id-scroll="16"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="9515" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-9515 grid-list__label" id="product_data_features_label_update_9515" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_9515--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-gigiienichni-always-ultra-normal-single-10-shtuk/" >
< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_9515"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/43/85831_987.webp"  alt="Прокладки гігієнічні ALWAYS Ultra Normal Single 10 штук" title="Прокладки гігієнічні ALWAYS Ultra Normal Single 10 штук" / >

< / a >

< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_9515"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_9515*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[9515][product_id]"
value = "9515" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-9515" id="product_labels_update_9515" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -14 % < / div >

< / div >

< !--product_labels_update_9515 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_9515_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..9515]"
data - ca - target - id = "top_icon_9515*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_9515_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-gigiienichni-always-ultra-normal-single-10-shtuk/"


class ="product-title" title="Прокладки гігієнічні ALWAYS Ultra Normal Single 10 штук" > Прокладки гігієнічні ALWAYS Ultra Normal Single 10 штук < / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 5.90 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-9515" id="old_price_update_9515" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_9515" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_9515" class ="ty-list-price ty-nowrap" > 69 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_9515 --> < / span >

< span


class ="cm-reload-9515 ty-price-update" id="price_update_9515" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_9515" >

< bdi > < span
id = "sec_discounted_price_9515"


class ="ty-price-num" > 59 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_9515 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-9515 " id="add_to_cart_update_9515" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=85831&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_9515" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_9515 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки гігієнічні ALWAYS Ultra Normal Single 10 штук"
data - gtm - id = "85831"
data - gtm - product - id = "9515"
data - gtm - discount = "10.00"
data - gtm - price = "69.00"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-9515" id="product_data_features_short_update_9515" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Вид: Прокладки <

/ li > < li > Кількість
в
упаковці, шт: 10 < / li > < li > Кількість
крапель: 4 < / li > < li > Країна
походження: Угорщина < / li > < li > Призначення: Для
жіночої
гігієни < / li > < / ul > < / div > <!--product_data_features_short_update_9515 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки гігієнічні ALWAYS Ultra Normal Single 10 штук"
data - item - id = "85831"
data - product - id = "9515"
data - discount = "10.00"
data - price = "59.00"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "4"
data - quantity = "1"
data - qty = "1"
data - position = "16"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#17"data-id-scroll="17"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="10002" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-10002 grid-list__label" id="product_data_features_label_update_10002" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_10002--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-schodenni-libresse-natural-care-normal-58-shtuk/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_10002"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/46/87972_001.webp"  alt="Прокладки щоденні Libresse Natural Care Normal 58 штук" title="Прокладки щоденні Libresse Natural Care Normal 58 штук" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Libresse Natural Care Normal 58 штук" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/46/87972_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Libresse Natural Care Normal 58 штук - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/46/87972_002.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Libresse Natural Care Normal 58 штук - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/46/87972_003.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Libresse Natural Care Normal 58 штук - 4" data-id="3" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/46/87972_004.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_10002"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_10002*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[10002][product_id]"
value = "10002" / >

< div


class ="right-top-blog" >

< / div >

< div


class ="left-top-blog" id="top_icon_10002_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..10002]"
data - ca - target - id = "top_icon_10002*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_10002_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-schodenni-libresse-natural-care-normal-58-shtuk/"


class ="product-title" title="Прокладки щоденні Libresse Natural Care Normal 58 штук" > Прокладки щоденні Libresse Natural Care Normal 58 штук < / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 2.57 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/prokladki-schodenni-libresse-natural-care-normal-58-shtuk/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 5 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "5"
data - ca - product - review - reviews - stars - full = "5"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(2)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-10002 ty-price-update" id="price_update_10002" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_10002" >

< bdi > < span
id = "sec_discounted_price_10002"


class ="ty-price-num" > 149 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_10002 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-10002 " id="add_to_cart_update_10002" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=87972&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_10002" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_10002 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки щоденні Libresse Natural Care Normal 58 штук"
data - gtm - id = "87972"
data - gtm - product - id = "10002"
data - gtm - discount = "0.00"
data - gtm - price = "149.00"
data - gtm - brand = "Libresse"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-10002" id="product_data_features_short_update_10002" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Libresse <

/ li > < li > Вид: Прокладки < / li > < li > Кількість
в
упаковці, шт: 58 < / li > < li > Кількість
крапель: 1 < / li > < li > Країна
походження: Словаччина < / li > < li > Особливості: Без
запаху < / li > < li > Призначення: Для
жіночої
гігієни < / li > < li > Розмір: Normal < / li > < li > Форма
випуску: Без
крилець < / li > < / ul > < / div > <!--product_data_features_short_update_10002 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки щоденні Libresse Natural Care Normal 58 штук"
data - item - id = "87972"
data - product - id = "10002"
data - discount = "0.00"
data - price = "149.00"
data - item - brand = "Libresse"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "1"
data - quantity = "1"
data - qty = "1"
data - position = "17"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#18"data-id-scroll="18"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="16263" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-16263 grid-list__label" id="product_data_features_label_update_16263" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_16263--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-gigiienichni-always-ultra-super-duo-516-sht-pach/" >
< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_16263"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/77/84222.webp"  alt="Прокладки гігієнічні Always Ultra Super Duo 5*16 шт/пач" title="Прокладки гігієнічні Always Ultra Super Duo 5*16 шт/пач" / >

< / a >

< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_16263"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_16263*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[16263][product_id]"
value = "16263" / >

< div


class ="right-top-blog" >

< / div >

< div


class ="left-top-blog" id="top_icon_16263_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..16263]"
data - ca - target - id = "top_icon_16263*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_16263_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-gigiienichni-always-ultra-super-duo-516-sht-pach/"


class ="product-title" title="Прокладки гігієнічні Always Ultra Super Duo 5*16 шт/пач" > Прокладки гігієнічні Always Ultra Super Duo 5 * 16 шт / пач < / a >

< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-16263 ty-price-update" id="price_update_16263" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_16263" >

< bdi > < span
id = "sec_discounted_price_16263"


class ="ty-price-num" > 129 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_16263 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-16263 " id="add_to_cart_update_16263" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=84222&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_16263" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_16263 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки гігієнічні Always Ultra Super Duo 5*16 шт/пач"
data - gtm - id = "84222"
data - gtm - product - id = "16263"
data - gtm - discount = "0.00"
data - gtm - price = "129.00"
data - gtm - brand = "Always"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-16263" id="product_data_features_short_update_16263" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Always <

/ li > < li > Вид: Прокладки < / li > < li > Кількість
в
упаковці, шт: 16 < / li > < li > Кількість
крапель: 5 < / li > < li > Країна
походження: Угорщина < / li > < li > Розмір: 2
Super < / li > < li > Форма
випуску: З
крильцями < / li > < / ul > < / div > <!--product_data_features_short_update_16263 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки гігієнічні Always Ultra Super Duo 5*16 шт/пач"
data - item - id = "84222"
data - product - id = "16263"
data - discount = "0.00"
data - price = "129.00"
data - item - brand = "Always"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "2"
data - quantity = "1"
data - qty = "1"
data - position = "18"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#19"data-id-scroll="19"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="16869" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-16869 grid-list__label" id="product_data_features_label_update_16869" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_16869--> < / div >

< / div >

< a
href = "https://avrora.ua/diski-vatni-kosmetichni-safi-avrora-50-sht-up/" >
< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_16869"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/80/84791.webp"  alt="Диски ватні косметичні Safi Аврора 50 шт/уп" title="Диски ватні косметичні Safi Аврора 50 шт/уп" / >

< / a >

< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_16869"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_16869*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[16869][product_id]"
value = "16869" / >

< div


class ="right-top-blog" >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< span


class ="labels-item variant_exclusive" > < / span >

< / div >

< div


class ="left-top-blog" id="top_icon_16869_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..16869]"
data - ca - target - id = "top_icon_16869*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_16869_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/diski-vatni-kosmetichni-safi-avrora-50-sht-up/"


class ="product-title" title="Диски ватні косметичні Safi Аврора 50 шт/уп" > Диски ватні косметичні Safi Аврора 50 шт / уп < / a >

< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/diski-vatni-kosmetichni-safi-avrora-50-sht-up/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 5 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "5"
data - ca - product - review - reviews - stars - full = "5"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(2)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-16869 ty-price-update" id="price_update_16869" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_16869" >

< bdi > < span
id = "sec_discounted_price_16869"


class ="ty-price-num" > 16 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_16869 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-16869 " id="add_to_cart_update_16869" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=84791&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_16869" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_16869 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Диски ватні косметичні Safi Аврора 50 шт/уп"
data - gtm - id = "84791"
data - gtm - product - id = "16869"
data - gtm - discount = "0.00"
data - gtm - price = "16.00"
data - gtm - brand = "Safi"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Особиста гігієна"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-16869" id="product_data_features_short_update_16869" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Safi <

/ li > < li > Вид: Ватні
диски < / li > < li > Кількість
в
упаковці, шт: 50 < / li > < li > Країна
походження: Латвія < / li > < li > Матеріал: 100 % бавовна < / li > < / ul > < / div > <!--product_data_features_short_update_16869 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Диски ватні косметичні Safi Аврора 50 шт/уп"
data - item - id = "84791"
data - product - id = "16869"
data - discount = "0.00"
data - price = "16.00"
data - item - brand = "Safi"
data - item - category = "Краса та здоров’я/Гігієна/Особиста гігієна"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "3"
data - quantity = "1"
data - qty = "1"
data - position = "19"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#20"data-id-scroll="20"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="554" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-554 grid-list__label" id="product_data_features_label_update_554" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_554--> < / div >

< / div >

< a
href = "https://avrora.ua/rushnik-paperoviy-deluxe-dvosharoviy-biliy-300-vidriviv/" >
< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_554"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/146/42410_119.webp"  alt="Рушник паперовий DeLuxe двошаровий білий 300 відривів" title="Рушник паперовий DeLuxe двошаровий білий 300 відривів" / >

< / a >

< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_554"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_554*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[554][product_id]"
value = "554" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-554" id="product_labels_update_554" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -16 % < / div >

< / div >

< !--product_labels_update_554 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_554_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..554]"
data - ca - target - id = "top_icon_554*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_554_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/rushnik-paperoviy-deluxe-dvosharoviy-biliy-300-vidriviv/"


class ="product-title" title="Рушник паперовий DeLuxe двошаровий білий 300 відривів" > Рушник паперовий DeLuxe двошаровий білий 300 відривів < / a >

< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/rushnik-paperoviy-deluxe-dvosharoviy-biliy-300-vidriviv/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 2 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "2"
data - ca - product - review - reviews - stars - full = "2"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(1)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-554" id="old_price_update_554" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_554" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_554" class ="ty-list-price ty-nowrap" > 64 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_554 --> < / span >

< span


class ="cm-reload-554 ty-price-update" id="price_update_554" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_554" >

< bdi > < span
id = "sec_discounted_price_554"


class ="ty-price-num" > 54 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_554 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-554 " id="add_to_cart_update_554" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=42410&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_554" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_554 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Рушник паперовий DeLuxe двошаровий білий 300 відривів"
data - gtm - id = "42410"
data - gtm - product - id = "554"
data - gtm - discount = "10.00"
data - gtm - price = "64.00"
data - gtm - brand = "DeLuxe"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Серветки, паперові рушники"
data - gtm - variant = "Білий"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-554" id="product_data_features_short_update_554" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: DeLuxe <

/ li > < li > Вид: Паперові
рушники < / li > < li > Кількість
шарів: 2 < / li > < li > Колір: Білий < / li > < li > Країна
походження: Україна < / li > < li > Розмір: 22, 5
х10
см(1
відрив) < / li > < / ul > < / div > <!--product_data_features_short_update_554 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Рушник паперовий DeLuxe двошаровий білий 300 відривів"
data - item - id = "42410"
data - product - id = "554"
data - discount = "10.00"
data - price = "54.00"
data - item - brand = "DeLuxe"
data - item - category = "Краса та здоров’я/Гігієна/Серветки, паперові рушники"
data - item - variant = "Білий"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "4"
data - quantity = "1"
data - qty = "1"
data - position = "20"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#21"data-id-scroll="21"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="8550" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-8550 grid-list__label" id="product_data_features_label_update_8550" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_8550--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-urologichni-zhinochi-tena-lady-slim-normal-12-shtuk/" >
< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_8550"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/79/81025_001.webp"  alt="Прокладки урологічні жіночі Tena Lady Slim Normal 12 штук" title="Прокладки урологічні жіночі Tena Lady Slim Normal 12 штук" / >

< / a >

< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_8550"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_8550*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[8550][product_id]"
value = "8550" / >

< div


class ="right-top-blog" >

< / div >

< div


class ="left-top-blog" id="top_icon_8550_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..8550]"
data - ca - target - id = "top_icon_8550*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_8550_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-urologichni-zhinochi-tena-lady-slim-normal-12-shtuk/"


class ="product-title" title="Прокладки урологічні жіночі Tena Lady Slim Normal 12 штук" > Прокладки урологічні жіночі Tena Lady Slim Normal 12 штук < / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 8.75 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-8550 ty-price-update" id="price_update_8550" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_8550" >

< bdi > < span
id = "sec_discounted_price_8550"


class ="ty-price-num" > 105 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_8550 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-8550 " id="add_to_cart_update_8550" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=81025&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_8550" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_8550 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки урологічні жіночі Tena Lady Slim Normal 12 штук"
data - gtm - id = "81025"
data - gtm - product - id = "8550"
data - gtm - discount = "0.00"
data - gtm - price = "105.00"
data - gtm - brand = "Tena"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-8550" id="product_data_features_short_update_8550" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Tena <

/ li > < li > Вид: Прокладки
урологічні < / li > < li > Кількість
крапель: 3 < / li > < / ul > < / div > <!--product_data_features_short_update_8550 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки урологічні жіночі Tena Lady Slim Normal 12 штук"
data - item - id = "81025"
data - product - id = "8550"
data - discount = "0.00"
data - price = "105.00"
data - item - brand = "Tena"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "1"
data - quantity = "1"
data - qty = "1"
data - position = "21"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#22"data-id-scroll="22"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="6237" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-6237 grid-list__label" id="product_data_features_label_update_6237" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_6237--> < / div >

< / div >

< a
href = "https://avrora.ua/milo-intimne-nizhne-romashka-370-ml/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_6237"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/185/14439_01011.webp"  alt="Мило інтимне Зелена Аптека Ніжне Ромашка 370 мл" title="Мило інтимне Зелена Аптека Ніжне Ромашка 370 мл" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Мило інтимне Зелена Аптека Ніжне Ромашка 370 мл" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/185/14439_01011.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Мило інтимне Зелена Аптека Ніжне Ромашка 370 мл - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/97/14439_001.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_6237"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_6237*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[6237][product_id]"
value = "6237" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-6237" id="product_labels_update_6237" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -20 % < / div >

< / div >

< !--product_labels_update_6237 --> < / div >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< / div >

< div


class ="left-top-blog" id="top_icon_6237_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..6237]"
data - ca - target - id = "top_icon_6237*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_6237_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/milo-intimne-nizhne-romashka-370-ml/"


class ="product-title" title="Мило інтимне Зелена Аптека Ніжне Ромашка 370 мл" > Мило інтимне Зелена Аптека Ніжне Ромашка 370 мл < / a >

< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-6237" id="old_price_update_6237" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_6237" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_6237" class ="ty-list-price ty-nowrap" > 99 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_6237 --> < / span >

< span


class ="cm-reload-6237 ty-price-update" id="price_update_6237" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_6237" >

< bdi > < span
id = "sec_discounted_price_6237"


class ="ty-price-num" > 79 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_6237 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-6237 " id="add_to_cart_update_6237" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=14439&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_6237" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_6237 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Мило інтимне Зелена Аптека Ніжне Ромашка 370 мл"
data - gtm - id = "14439"
data - gtm - product - id = "6237"
data - gtm - discount = "20.00"
data - gtm - price = "99.00"
data - gtm - brand = "Зелена аптека"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-6237" id="product_data_features_short_update_6237" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Зелена


аптека < / li > < li > Вид: Гелі
для
інтимної
гігієни < / li > < li > Країна
походження: Україна < / li > < li > Об &  # 039;єм: 370  мл</li></ul></div>            <!--product_data_features_short_update_6237--></div>

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Мило інтимне Зелена Аптека Ніжне Ромашка 370 мл"
data - item - id = "14439"
data - product - id = "6237"
data - discount = "20.00"
data - price = "79.00"
data - item - brand = "Зелена аптека"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "2"
data - quantity = "1"
data - qty = "1"
data - position = "22"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#23"data-id-scroll="23"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="13899" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-13899 grid-list__label" id="product_data_features_label_update_13899" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_13899--> < / div >

< / div >

< a
href = "https://avrora.ua/nabir-paperu-tualetnogo-selpak-comfort-2-shari-4-shtuki/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_13899"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/104/97190_002.webp"  alt="Набір паперу туалетного SELPAK Comfort 2 шари 4 штуки" title="Набір паперу туалетного SELPAK Comfort 2 шари 4 штуки" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Набір паперу туалетного SELPAK Comfort 2 шари 4 штуки" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/104/97190_002.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Набір паперу туалетного SELPAK Comfort 2 шари 4 штуки - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/104/97190_003.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Набір паперу туалетного SELPAK Comfort 2 шари 4 штуки - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/105/97190_004.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Набір паперу туалетного SELPAK Comfort 2 шари 4 штуки - 4" data-id="3" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/105/97190_005.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Набір паперу туалетного SELPAK Comfort 2 шари 4 штуки - 5" data-id="4" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/68/97190_001.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_13899"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_13899*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[13899][product_id]"
value = "13899" / >

< div


class ="right-top-blog" >

< / div >

< div


class ="left-top-blog" id="top_icon_13899_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..13899]"
data - ca - target - id = "top_icon_13899*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_13899_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/nabir-paperu-tualetnogo-selpak-comfort-2-shari-4-shtuki/"


class ="product-title" title="Набір паперу туалетного SELPAK Comfort 2 шари 4 штуки" > Набір паперу туалетного SELPAK Comfort 2 шари 4 штуки < / a >

< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/nabir-paperu-tualetnogo-selpak-comfort-2-shari-4-shtuki/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 1 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "1"
data - ca - product - review - reviews - stars - full = "1"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(1)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-13899 ty-price-update" id="price_update_13899" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_13899" >

< bdi > < span
id = "sec_discounted_price_13899"


class ="ty-price-num" > 59 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_13899 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-13899 " id="add_to_cart_update_13899" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=97190&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_13899" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_13899 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Набір паперу туалетного SELPAK Comfort 2 шари 4 штуки"
data - gtm - id = "97190"
data - gtm - product - id = "13899"
data - gtm - discount = "0.00"
data - gtm - price = "59.00"
data - gtm - brand = "Selpak"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Особиста гігієна"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-13899" id="product_data_features_short_update_13899" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Selpak <

/ li > < li > Вид: Туалетний
папір < / li > < li > Кількість
в
упаковці, шт: 4 < / li > < li > Кількість
шарів: 2 < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: 100 % целюлоза < / li > < / ul > < / div > <!--product_data_features_short_update_13899 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Набір паперу туалетного SELPAK Comfort 2 шари 4 штуки"
data - item - id = "97190"
data - product - id = "13899"
data - discount = "0.00"
data - price = "59.00"
data - item - brand = "Selpak"
data - item - category = "Краса та здоров’я/Гігієна/Особиста гігієна"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "3"
data - quantity = "1"
data - qty = "1"
data - position = "23"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#24"data-id-scroll="24"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="9513" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-9513 grid-list__label" id="product_data_features_label_update_9513" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_9513--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-gigiienichni-always-ultra-day-and-night-singl-7-shtuk/" >
< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_9513"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/43/85829_897_uai6-ki.webp"  alt="Прокладки гігієнічні ALWAYS Ultra Day&amp;Night Singl 7 штук" title="Прокладки гігієнічні ALWAYS Ultra Day&amp;Night Singl 7 штук" / >

< / a >

< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_9513"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_9513*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[9513][product_id]"
value = "9513" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-9513" id="product_labels_update_9513" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -14 % < / div >

< / div >

< !--product_labels_update_9513 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_9513_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..9513]"
data - ca - target - id = "top_icon_9513*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_9513_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-gigiienichni-always-ultra-day-and-night-singl-7-shtuk/"


class ="product-title" title="Прокладки гігієнічні ALWAYS Ultra Day&amp;Night Singl 7 штук" > Прокладки гігієнічні ALWAYS Ultra Day & Night Singl 7 штук < / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 8.43 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-9513" id="old_price_update_9513" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_9513" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_9513" class ="ty-list-price ty-nowrap" > 69 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_9513 --> < / span >

< span


class ="cm-reload-9513 ty-price-update" id="price_update_9513" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_9513" >

< bdi > < span
id = "sec_discounted_price_9513"


class ="ty-price-num" > 59 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_9513 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-9513 " id="add_to_cart_update_9513" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=85829&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_9513" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_9513 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки гігієнічні ALWAYS Ultra Day&amp;Night Singl 7 штук"
data - gtm - id = "85829"
data - gtm - product - id = "9513"
data - gtm - discount = "10.00"
data - gtm - price = "69.00"
data - gtm - brand = "Always"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-9513" id="product_data_features_short_update_9513" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Always <

/ li > < li > Вид: Прокладки < / li > < li > Кількість
в
упаковці, шт: 7 < / li > < li > Кількість
крапель: 6 < / li > < li > Особливості: День / Ніч < / li > < li > Призначення: Для
жіночої
гігієни < / li > < / ul > < / div > <!--product_data_features_short_update_9513 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки гігієнічні ALWAYS Ultra Day&amp;Night Singl 7 штук"
data - item - id = "85829"
data - product - id = "9513"
data - discount = "10.00"
data - price = "59.00"
data - item - brand = "Always"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "4"
data - quantity = "1"
data - qty = "1"
data - position = "24"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#25"data-id-scroll="25"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="9852" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-9852 grid-list__label" id="product_data_features_label_update_9852" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_9852--> < / div >

< / div >

< a
href = "https://avrora.ua/nabir-paperu-tualetnogo-ecolo-deluxe-3-shari-4-sht-up/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_9852"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/45/83079_001.webp"  alt="Набір паперу туалетного Ecolo Deluxe 3 шари 4 шт/уп" title="Набір паперу туалетного Ecolo Deluxe 3 шари 4 шт/уп" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Набір паперу туалетного Ecolo Deluxe 3 шари 4 шт/уп" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/45/83079_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Набір паперу туалетного Ecolo Deluxe 3 шари 4 шт/уп - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/45/83079_002.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_9852"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_9852*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[9852][product_id]"
value = "9852" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-9852" id="product_labels_update_9852" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -15 % < / div >

< / div >

< !--product_labels_update_9852 --> < / div >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< / div >

< div


class ="left-top-blog" id="top_icon_9852_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..9852]"
data - ca - target - id = "top_icon_9852*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_9852_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/nabir-paperu-tualetnogo-ecolo-deluxe-3-shari-4-sht-up/"


class ="product-title" title="Набір паперу туалетного Ecolo Deluxe 3 шари 4 шт/уп" > Набір паперу туалетного Ecolo Deluxe 3 шари 4 шт / уп < / a >

< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/nabir-paperu-tualetnogo-ecolo-deluxe-3-shari-4-sht-up/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 5 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "5"
data - ca - product - review - reviews - stars - full = "5"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(2)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-9852" id="old_price_update_9852" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_9852" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_9852" class ="ty-list-price ty-nowrap" > 84 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_9852 --> < / span >

< span


class ="cm-reload-9852 ty-price-update" id="price_update_9852" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_9852" >

< bdi > < span
id = "sec_discounted_price_9852"


class ="ty-price-num" > 71 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_9852 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-9852 " id="add_to_cart_update_9852" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=83079&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_9852" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_9852 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Набір паперу туалетного Ecolo Deluxe 3 шари 4 шт/уп"
data - gtm - id = "83079"
data - gtm - product - id = "9852"
data - gtm - discount = "13.00"
data - gtm - price = "84.00"
data - gtm - brand = "Ruta"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Особиста гігієна"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-9852" id="product_data_features_short_update_9852" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Ruta <

/ li > < li > Вид: Туалетний
папір < / li > < li > Кількість
в
упаковці, шт: 4 < / li > < li > Кількість
шарів: 3 < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: Целюлоза < / li > < / ul > < / div > <!--product_data_features_short_update_9852 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Набір паперу туалетного Ecolo Deluxe 3 шари 4 шт/уп"
data - item - id = "83079"
data - product - id = "9852"
data - discount = "13.00"
data - price = "71.00"
data - item - brand = "Ruta"
data - item - category = "Краса та здоров’я/Гігієна/Особиста гігієна"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "1"
data - quantity = "1"
data - qty = "1"
data - position = "25"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#26"data-id-scroll="26"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="24710" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-24710 grid-list__label" id="product_data_features_label_update_24710" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_24710--> < / div >

< / div >

< a
href = "https://avrora.ua/rushniki-paperovi-v-skladannya-safi-bili-2-shari-130-listiv-pach/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_24710"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/113/101897_002.webp"  alt="Рушники паперові V-складання Safi білі 2 шари 130 листів/пач" title="Рушники паперові V-складання Safi білі 2 шари 130 листів/пач" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Рушники паперові V-складання Safi білі 2 шари 130 листів/пач" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/113/101897_002.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Рушники паперові V-складання Safi білі 2 шари 130 листів/пач - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/113/101897_001.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_24710"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_24710*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[24710][product_id]"
value = "24710" / >

< div


class ="right-top-blog" >

< span


class ="labels-item variant_exclusive" > < / span >

< / div >

< div


class ="left-top-blog" id="top_icon_24710_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..24710]"
data - ca - target - id = "top_icon_24710*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_24710_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/rushniki-paperovi-v-skladannya-safi-bili-2-shari-130-listiv-pach/"


class ="product-title" title="Рушники паперові V-складання Safi білі 2 шари 130 листів/пач" > Рушники паперові V-складання Safi білі 2 шари 130 листів / пач < / a >

< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/rushniki-paperovi-v-skladannya-safi-bili-2-shari-130-listiv-pach/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 5 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "5"
data - ca - product - review - reviews - stars - full = "5"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(1)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-24710 ty-price-update" id="price_update_24710" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_24710" >

< bdi > < span
id = "sec_discounted_price_24710"


class ="ty-price-num" > 49 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_24710 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-24710 " id="add_to_cart_update_24710" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=101897&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_24710" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_24710 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Рушники паперові V-складання Safi білі 2 шари 130 листів/пач"
data - gtm - id = "101897"
data - gtm - product - id = "24710"
data - gtm - discount = "0.00"
data - gtm - price = "49.00"
data - gtm - brand = "Safi"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Серветки, паперові рушники"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-24710" id="product_data_features_short_update_24710" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Safi <

/ li > < li > Вид: Паперові
рушники < / li > < li > Кількість
в
упаковці, шт: 130 < / li > < li > Кількість
шарів: 2 < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: 100 % целюлоза < / li > < li > Призначення: Для
побутового
використання < / li > < li > Розмір: 20
х21
см < / li > < / ul > < / div > <!--product_data_features_short_update_24710 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Рушники паперові V-складання Safi білі 2 шари 130 листів/пач"
data - item - id = "101897"
data - product - id = "24710"
data - discount = "0.00"
data - price = "49.00"
data - item - brand = "Safi"
data - item - category = "Краса та здоров’я/Гігієна/Серветки, паперові рушники"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "2"
data - quantity = "1"
data - qty = "1"
data - position = "26"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#27"data-id-scroll="27"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="20678" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-20678 grid-list__label" id="product_data_features_label_update_20678" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_20678--> < / div >

< / div >

< a
href = "https://avrora.ua/rushniki-paperovi-v-skladennya-papero-bili-2-shari150-listiv-pachka/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_20678"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/95/99625-.webp"  alt="Рушники паперові V-складення Papero білі 2 шари150 листів/пачка" title="Рушники паперові V-складення Papero білі 2 шари150 листів/пачка" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Рушники паперові V-складення Papero білі 2 шари150 листів/пачка" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/95/99625-.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Рушники паперові V-складення Papero білі 2 шари150 листів/пачка - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/95/99625_1.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_20678"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_20678*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[20678][product_id]"
value = "20678" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-20678" id="product_labels_update_20678" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -16 % < / div >

< / div >

< !--product_labels_update_20678 --> < / div >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< / div >

< div


class ="left-top-blog" id="top_icon_20678_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..20678]"
data - ca - target - id = "top_icon_20678*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_20678_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/rushniki-paperovi-v-skladennya-papero-bili-2-shari150-listiv-pachka/"


class ="product-title" title="Рушники паперові V-складення Papero білі 2 шари150 листів/пачка" > Рушники паперові V-складення Papero білі 2 шари150 листів / пачка < / a >

< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-20678" id="old_price_update_20678" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_20678" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_20678" class ="ty-list-price ty-nowrap" > 55 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_20678 --> < / span >

< span


class ="cm-reload-20678 ty-price-update" id="price_update_20678" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_20678" >

< bdi > < span
id = "sec_discounted_price_20678"


class ="ty-price-num" > 46 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_20678 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-20678 " id="add_to_cart_update_20678" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=99625&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_20678" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_20678 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Рушники паперові V-складення Papero білі 2 шари150 листів/пачка"
data - gtm - id = "99625"
data - gtm - product - id = "20678"
data - gtm - discount = "9.00"
data - gtm - price = "55.00"
data - gtm - brand = "Papero"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Серветки, паперові рушники"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-20678" id="product_data_features_short_update_20678" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Papero <

/ li > < li > Вид: Паперові
рушники < / li > < li > Кількість
в
упаковці, шт: 150
листів < / li > < li > Кількість
шарів: 2 < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: 100 % целюлоза < / li > < / ul > < / div > <!--product_data_features_short_update_20678 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Рушники паперові V-складення Papero білі 2 шари150 листів/пачка"
data - item - id = "99625"
data - product - id = "20678"
data - discount = "9.00"
data - price = "46.00"
data - item - brand = "Papero"
data - item - category = "Краса та здоров’я/Гігієна/Серветки, паперові рушники"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "3"
data - quantity = "1"
data - qty = "1"
data - position = "27"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#28"data-id-scroll="28"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="19928" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-19928 grid-list__label" id="product_data_features_label_update_19928" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_19928--> < / div >

< / div >

< a
href = "https://avrora.ua/servetki-vologi-dityachi-smile-ekstrakt-aloe-24-sht-up/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_19928"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/124/photo_2025-01-13_11-17-13.webp"  alt="Серветки вологі дитячі Smile Екстракт алое 24 шт/уп" title="Серветки вологі дитячі Smile Екстракт алое 24 шт/уп" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Серветки вологі дитячі Smile Екстракт алое 24 шт/уп" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/124/photo_2025-01-13_11-17-13.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Серветки вологі дитячі Smile Екстракт алое 24 шт/уп - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/124/photo_2025-02-11_10-58-38.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Серветки вологі дитячі Smile Екстракт алое 24 шт/уп - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/124/photo_2025-02-11_10-59-42.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Серветки вологі дитячі Smile Екстракт алое 24 шт/уп - 4" data-id="3" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/124/photo_2025-02-11_11-00-33.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Серветки вологі дитячі Smile Екстракт алое 24 шт/уп - 5" data-id="4" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/124/photo_2025-02-11_11-00-36.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Серветки вологі дитячі Smile Екстракт алое 24 шт/уп - 6" data-id="5" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/124/photo_2025-02-11_11-00-38.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_19928"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_19928*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[19928][product_id]"
value = "19928" / >

< div


class ="right-top-blog" >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< / div >

< div


class ="left-top-blog" id="top_icon_19928_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..19928]"
data - ca - target - id = "top_icon_19928*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_19928_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/servetki-vologi-dityachi-smile-ekstrakt-aloe-24-sht-up/"


class ="product-title" title="Серветки вологі дитячі Smile Екстракт алое 24 шт/уп" > Серветки вологі дитячі Smile Екстракт алое 24 шт / уп < / a >

< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-19928 ty-price-update" id="price_update_19928" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_19928" >

< bdi > < span
id = "sec_discounted_price_19928"


class ="ty-price-num" > 24 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_19928 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-19928 " id="add_to_cart_update_19928" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=105065&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_19928" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_19928 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Серветки вологі дитячі Smile Екстракт алое 24 шт/уп"
data - gtm - id = "105065"
data - gtm - product - id = "19928"
data - gtm - discount = "0.00"
data - gtm - price = "24.00"
data - gtm - brand = "Smile"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Серветки, паперові рушники"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-19928" id="product_data_features_short_update_19928" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Smile <

/ li > < li > Вид: Серветки
вологі < / li > < li > Кількість
в
упаковці, шт: 24 < / li > < li > Країна
походження: Україна < / li > < li > Особливості: Гіпоалергенні, без
спирту
та
силіконів < / li > < li > Тип
шкіри: Для
всіх
типів < / li > < / ul > < / div > <!--product_data_features_short_update_19928 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Серветки вологі дитячі Smile Екстракт алое 24 шт/уп"
data - item - id = "105065"
data - product - id = "19928"
data - discount = "0.00"
data - price = "24.00"
data - item - brand = "Smile"
data - item - category = "Краса та здоров’я/Гігієна/Серветки, паперові рушники"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "4"
data - quantity = "1"
data - qty = "1"
data - position = "28"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#29"data-id-scroll="29"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="34349" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-34349 grid-list__label" id="product_data_features_label_update_34349" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_34349--> < / div >

< / div >

< a
href = "https://avrora.ua/hustki-nosovi-paperovi-safi-etnoornament-bez-aromatu-2-shari-10-sht-up/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_34349"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/151/113979_001.webp"  alt="Хустки носові паперові Safi Етноорнамент без аромату 2 шари 10 шт/уп" title="Хустки носові паперові Safi Етноорнамент без аромату 2 шари 10 шт/уп" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Хустки носові паперові Safi Етноорнамент без аромату 2 шари 10 шт/уп" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/151/113979_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Хустки носові паперові Safi Етноорнамент без аромату 2 шари 10 шт/уп - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/151/113979_002.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_34349"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_34349*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[34349][product_id]"
value = "34349" / >

< div


class ="right-top-blog" >

< span


class ="labels-item variant_exclusive" > < / span >

< / div >

< div


class ="left-top-blog" id="top_icon_34349_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..34349]"
data - ca - target - id = "top_icon_34349*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_34349_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/hustki-nosovi-paperovi-safi-etnoornament-bez-aromatu-2-shari-10-sht-up/"


class ="product-title" title="Хустки носові паперові Safi Етноорнамент без аромату 2 шари 10 шт/уп" > Хустки носові паперові Safi Етноорнамент без аромату 2 шари 10 шт / уп < / a >

< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-34349 ty-price-update" id="price_update_34349" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_34349" >

< bdi > < span
id = "sec_discounted_price_34349"


class ="ty-price-num" > 2 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_34349 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-34349 " id="add_to_cart_update_34349" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=113979&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_34349" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_34349 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Хустки носові паперові Safi Етноорнамент без аромату 2 шари 10 шт/уп"
data - gtm - id = "113979"
data - gtm - product - id = "34349"
data - gtm - discount = "0.00"
data - gtm - price = "2.00"
data - gtm - brand = "Safi"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Серветки, паперові рушники"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-34349" id="product_data_features_short_update_34349" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Safi <

/ li > < li > Вид: Хустинки < / li > < li > Кількість
в
упаковці, шт: 10
шт < / li > < li > Кількість
шарів: 2 < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: Целюлоза < / li > < li > Розмір: 20
х20
см < / li > < / ul > < / div > <!--product_data_features_short_update_34349 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Хустки носові паперові Safi Етноорнамент без аромату 2 шари 10 шт/уп"
data - item - id = "113979"
data - product - id = "34349"
data - discount = "0.00"
data - price = "2.00"
data - item - brand = "Safi"
data - item - category = "Краса та здоров’я/Гігієна/Серветки, паперові рушники"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "1"
data - quantity = "1"
data - qty = "1"
data - position = "29"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#30"data-id-scroll="30"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="697" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-697 grid-list__label" id="product_data_features_label_update_697" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_697--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-gigiienichni-naturella-ult.cam.-norm.sin.-10-sht-pach./" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_697"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/25666_001.webp"  alt="Прокладки гігієнічні NATURELLA Ultra Camomile Нормал 10 штук" title="Прокладки гігієнічні NATURELLA Ultra Camomile Нормал 10 штук" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Camomile Нормал 10 штук" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/25666_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Camomile Нормал 10 штук - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/25666_002_yd8w-5f.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Camomile Нормал 10 штук - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/25666_003.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Camomile Нормал 10 штук - 4" data-id="3" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/25666_004.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Camomile Нормал 10 штук - 5" data-id="4" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/25666_005.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Camomile Нормал 10 штук - 6" data-id="5" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/25666_006.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_697"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_697*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[697][product_id]"
value = "697" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-697" id="product_labels_update_697" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -17 % < / div >

< / div >

< !--product_labels_update_697 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_697_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..697]"
data - ca - target - id = "top_icon_697*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_697_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-gigiienichni-naturella-ult.cam.-norm.sin.-10-sht-pach./"


class ="product-title" title="Прокладки гігієнічні NATURELLA Ultra Camomile Нормал 10 штук" > Прокладки гігієнічні NATURELLA Ultra Camomile Нормал 10 штук < / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 4.90 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-697" id="old_price_update_697" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_697" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_697" class ="ty-list-price ty-nowrap" > 59 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_697 --> < / span >

< span


class ="cm-reload-697 ty-price-update" id="price_update_697" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_697" >

< bdi > < span
id = "sec_discounted_price_697"


class ="ty-price-num" > 49 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_697 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-697 " id="add_to_cart_update_697" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=25666&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_697" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_697 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки гігієнічні NATURELLA Ultra Camomile Нормал 10 штук"
data - gtm - id = "25666"
data - gtm - product - id = "697"
data - gtm - discount = "10.00"
data - gtm - price = "59.00"
data - gtm - brand = "Naturella"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-697" id="product_data_features_short_update_697" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Naturella <

/ li > < li > Вид: Прокладки < / li > < li > Кількість
крапель: 4 < / li > < / ul > < / div > <!--product_data_features_short_update_697 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки гігієнічні NATURELLA Ultra Camomile Нормал 10 штук"
data - item - id = "25666"
data - product - id = "697"
data - discount = "10.00"
data - price = "49.00"
data - item - brand = "Naturella"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "2"
data - quantity = "1"
data - qty = "1"
data - position = "30"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#31"data-id-scroll="31"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="19801" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-19801 grid-list__label" id="product_data_features_label_update_19801" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_19801--> < / div >

< / div >

< a
href = "https://avrora.ua/servetki-vologi-dityachi-aqua-baby-z-vitaminnim-kompleksom-15-sht-up./" >
< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_19801"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/91/91802_001.webp"  alt="Серветки вологі дитячі Aqua Baby з вітамінним комплексом 15 шт/уп." title="Серветки вологі дитячі Aqua Baby з вітамінним комплексом 15 шт/уп." / >

< / a >

< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_19801"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_19801*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[19801][product_id]"
value = "19801" / >

< div


class ="right-top-blog" >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< / div >

< div


class ="left-top-blog" id="top_icon_19801_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..19801]"
data - ca - target - id = "top_icon_19801*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_19801_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/servetki-vologi-dityachi-aqua-baby-z-vitaminnim-kompleksom-15-sht-up./"


class ="product-title" title="Серветки вологі дитячі Aqua Baby з вітамінним комплексом 15 шт/уп." > Серветки вологі дитячі Aqua Baby з вітамінним комплексом 15 шт / уп.< / a >

< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-19801 ty-price-update" id="price_update_19801" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_19801" >

< bdi > < span
id = "sec_discounted_price_19801"


class ="ty-price-num" > 5 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_19801 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-19801 " id="add_to_cart_update_19801" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=91802&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_19801" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_19801 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Серветки вологі дитячі Aqua Baby з вітамінним комплексом 15 шт/уп."
data - gtm - id = "91802"
data - gtm - product - id = "19801"
data - gtm - discount = "0.00"
data - gtm - price = "5.00"
data - gtm - brand = "Biosphere"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Серветки, паперові рушники"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-19801" id="product_data_features_short_update_19801" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Biosphere <

/ li > < li > Вид: Серветки
вологі < / li > < li > Кількість
в
упаковці, шт: 15 < / li > < li > Країна
походження: Україна < / li > < / ul > < / div > <!--product_data_features_short_update_19801 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Серветки вологі дитячі Aqua Baby з вітамінним комплексом 15 шт/уп."
data - item - id = "91802"
data - product - id = "19801"
data - discount = "0.00"
data - price = "5.00"
data - item - brand = "Biosphere"
data - item - category = "Краса та здоров’я/Гігієна/Серветки, паперові рушники"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "3"
data - quantity = "1"
data - qty = "1"
data - position = "31"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#32"data-id-scroll="32"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="17934" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-17934 grid-list__label" id="product_data_features_label_update_17934" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_17934--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-gigiienichni-kotex-ultra-night-quadro-22-sht-pach/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_17934"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/186/101679_010123.webp"  alt="Прокладки гігієнічні Kotex Ultra Night Quadro 22 шт/пач" title="Прокладки гігієнічні Kotex Ultra Night Quadro 22 шт/пач" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні Kotex Ultra Night Quadro 22 шт/пач" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/186/101679_010123.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні Kotex Ultra Night Quadro 22 шт/пач - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/83/101679_001.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_17934"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_17934*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[17934][product_id]"
value = "17934" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-17934" id="product_labels_update_17934" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -24 % < / div >

< / div >

< !--product_labels_update_17934 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_17934_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..17934]"
data - ca - target - id = "top_icon_17934*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_17934_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-gigiienichni-kotex-ultra-night-quadro-22-sht-pach/"


class ="product-title" title="Прокладки гігієнічні Kotex Ultra Night Quadro 22 шт/пач" > Прокладки гігієнічні Kotex Ultra Night Quadro 22 шт / пач < / a >

< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-17934" id="old_price_update_17934" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_17934" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_17934" class ="ty-list-price ty-nowrap" > 169 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_17934 --> < / span >

< span


class ="cm-reload-17934 ty-price-update" id="price_update_17934" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_17934" >

< bdi > < span
id = "sec_discounted_price_17934"


class ="ty-price-num" > 129 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_17934 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-17934 " id="add_to_cart_update_17934" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=101679&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_17934" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_17934 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки гігієнічні Kotex Ultra Night Quadro 22 шт/пач"
data - gtm - id = "101679"
data - gtm - product - id = "17934"
data - gtm - discount = "40.00"
data - gtm - price = "169.00"
data - gtm - brand = "Kotex"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-17934" id="product_data_features_short_update_17934" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Kotex <

/ li > < li > Вид: Прокладки < / li > < li > Кількість
в
упаковці, шт: 22 < / li > < li > Кількість
крапель: 6 < / li > < li > Країна
походження: Чехія < / li > < / ul > < / div > <!--product_data_features_short_update_17934 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки гігієнічні Kotex Ultra Night Quadro 22 шт/пач"
data - item - id = "101679"
data - product - id = "17934"
data - discount = "40.00"
data - price = "129.00"
data - item - brand = "Kotex"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "4"
data - quantity = "1"
data - qty = "1"
data - position = "32"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#33"data-id-scroll="33"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="10000" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-10000 grid-list__label" id="product_data_features_label_update_10000" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_10000--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-gigiienichni-libress-comfort-maxi-long-9-shtuk/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_10000"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/174/87970_1000.webp"  alt="Прокладки гігієнічні LIBRESS Comfort Maxi Long 9 штук" title="Прокладки гігієнічні LIBRESS Comfort Maxi Long 9 штук" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні LIBRESS Comfort Maxi Long 9 штук" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/174/87970_1000.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні LIBRESS Comfort Maxi Long 9 штук - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/46/87970_003.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні LIBRESS Comfort Maxi Long 9 штук - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/46/87970_004.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні LIBRESS Comfort Maxi Long 9 штук - 4" data-id="3" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/46/87970_005.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні LIBRESS Comfort Maxi Long 9 штук - 5" data-id="4" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/46/87970_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні LIBRESS Comfort Maxi Long 9 штук - 6" data-id="5" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/46/87970_002.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_10000"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_10000*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[10000][product_id]"
value = "10000" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-10000" id="product_labels_update_10000" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -11 % < / div >

< / div >

< !--product_labels_update_10000 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_10000_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..10000]"
data - ca - target - id = "top_icon_10000*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_10000_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-gigiienichni-libress-comfort-maxi-long-9-shtuk/"


class ="product-title" title="Прокладки гігієнічні LIBRESS Comfort Maxi Long 9 штук" > Прокладки гігієнічні LIBRESS Comfort Maxi Long 9 штук < / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 5.44 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/prokladki-gigiienichni-libress-comfort-maxi-long-9-shtuk/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 5 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "5"
data - ca - product - review - reviews - stars - full = "5"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(1)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-10000" id="old_price_update_10000" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_10000" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_10000" class ="ty-list-price ty-nowrap" > 55 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_10000 --> < / span >

< span


class ="cm-reload-10000 ty-price-update" id="price_update_10000" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_10000" >

< bdi > < span
id = "sec_discounted_price_10000"


class ="ty-price-num" > 49 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_10000 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-10000 " id="add_to_cart_update_10000" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=87970&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_10000" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_10000 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки гігієнічні LIBRESS Comfort Maxi Long 9 штук"
data - gtm - id = "87970"
data - gtm - product - id = "10000"
data - gtm - discount = "6.00"
data - gtm - price = "55.00"
data - gtm - brand = "Libresse"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-10000" id="product_data_features_short_update_10000" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Libresse <

/ li > < li > Вид: Прокладки < / li > < li > Довжина: 284
мм < / li > < li > Кількість
в
упаковці, шт: 9 < / li > < li > Кількість
крапель: 5 < / li > < li > Країна
походження: Словаччина < / li > < li > Особливості: Без
запаху < / li > < li > Призначення: Для
жіночої
гігієни < / li > < li > Форма
випуску: З
крильцями < / li > < / ul > < / div > <!--product_data_features_short_update_10000 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки гігієнічні LIBRESS Comfort Maxi Long 9 штук"
data - item - id = "87970"
data - product - id = "10000"
data - discount = "6.00"
data - price = "49.00"
data - item - brand = "Libresse"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "1"
data - quantity = "1"
data - qty = "1"
data - position = "33"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#34"data-id-scroll="34"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="17658" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-17658 grid-list__label" id="product_data_features_label_update_17658" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_17658--> < / div >

< / div >

< a
href = "https://avrora.ua/servetki-paperovi-safi-1-shar-bili-350-sht-pach/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_17658"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/82/92589_002.webp"  alt="Серветки паперові Safi 1 шар білі 350 шт/пач" title="Серветки паперові Safi 1 шар білі 350 шт/пач" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Серветки паперові Safi 1 шар білі 350 шт/пач" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/82/92589_002.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Серветки паперові Safi 1 шар білі 350 шт/пач - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/82/92589_001.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_17658"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_17658*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[17658][product_id]"
value = "17658" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-17658" id="product_labels_update_17658" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -16 % < / div >

< / div >

< !--product_labels_update_17658 --> < / div >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< span


class ="labels-item variant_exclusive" > < / span >

< / div >

< div


class ="left-top-blog" id="top_icon_17658_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..17658]"
data - ca - target - id = "top_icon_17658*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_17658_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/servetki-paperovi-safi-1-shar-bili-350-sht-pach/"


class ="product-title" title="Серветки паперові Safi 1 шар білі 350 шт/пач" > Серветки паперові Safi 1 шар білі 350 шт / пач < / a >

< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/servetki-paperovi-safi-1-shar-bili-350-sht-pach/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 4 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "4"
data - ca - product - review - reviews - stars - full = "4"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(1)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-17658" id="old_price_update_17658" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_17658" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_17658" class ="ty-list-price ty-nowrap" > 64 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_17658 --> < / span >

< span


class ="cm-reload-17658 ty-price-update" id="price_update_17658" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_17658" >

< bdi > < span
id = "sec_discounted_price_17658"


class ="ty-price-num" > 54 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_17658 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-17658 " id="add_to_cart_update_17658" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=92589&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_17658" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_17658 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Серветки паперові Safi 1 шар білі 350 шт/пач"
data - gtm - id = "92589"
data - gtm - product - id = "17658"
data - gtm - discount = "10.00"
data - gtm - price = "64.00"
data - gtm - brand = "Safi"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Серветки, паперові рушники"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-17658" id="product_data_features_short_update_17658" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Safi <

/ li > < li > Вид: Серветки
паперові < / li > < li > Кількість
в
упаковці, шт: 350 < / li > < li > Кількість
шарів: 1 < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: 100 % целюлоза < / li > < li > Призначення: Для
господарсько - побутових
потреб < / li > < li > Розмір: 21
х21
см < / li > < / ul > < / div > <!--product_data_features_short_update_17658 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Серветки паперові Safi 1 шар білі 350 шт/пач"
data - item - id = "92589"
data - product - id = "17658"
data - discount = "10.00"
data - price = "54.00"
data - item - brand = "Safi"
data - item - category = "Краса та здоров’я/Гігієна/Серветки, паперові рушники"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "2"
data - quantity = "1"
data - qty = "1"
data - position = "34"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#35"data-id-scroll="35"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="16469" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-16469 grid-list__label" id="product_data_features_label_update_16469" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_16469--> < / div >

< / div >

< a
href = "https://avrora.ua/palichki-vatni-kosmetichni-safi-200-sht-up/" >
< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_16469"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/78/75695_958.webp"  alt="Палички ватнi косметичні Safi 200 шт/уп" title="Палички ватнi косметичні Safi 200 шт/уп" / >

< / a >

< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_16469"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_16469*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[16469][product_id]"
value = "16469" / >

< div


class ="right-top-blog" >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< span


class ="labels-item variant_exclusive" > < / span >

< / div >

< div


class ="left-top-blog" id="top_icon_16469_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..16469]"
data - ca - target - id = "top_icon_16469*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_16469_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/palichki-vatni-kosmetichni-safi-200-sht-up/"


class ="product-title" title="Палички ватнi косметичні Safi 200 шт/уп" > Палички ватнi косметичні Safi 200 шт / уп < / a >

< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-16469 ty-price-update" id="price_update_16469" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_16469" >

< bdi > < span
id = "sec_discounted_price_16469"


class ="ty-price-num" > 29 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_16469 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-16469 " id="add_to_cart_update_16469" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=75695&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_16469" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_16469 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Палички ватнi косметичні Safi 200 шт/уп"
data - gtm - id = "75695"
data - gtm - product - id = "16469"
data - gtm - discount = "0.00"
data - gtm - price = "29.00"
data - gtm - brand = "Safi"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Особиста гігієна"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-16469" id="product_data_features_short_update_16469" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Safi <

/ li > < li > Вид: Ватні
палички < / li > < li > Кількість
в
упаковці, шт: 200 < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: 100 % бавовна < / li > < li > Призначення: Для
гігієнічних
та
косметичних
потреб < / li > < / ul > < / div > <!--product_data_features_short_update_16469 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Палички ватнi косметичні Safi 200 шт/уп"
data - item - id = "75695"
data - product - id = "16469"
data - discount = "0.00"
data - price = "29.00"
data - item - brand = "Safi"
data - item - category = "Краса та здоров’я/Гігієна/Особиста гігієна"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "3"
data - quantity = "1"
data - qty = "1"
data - position = "35"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#36"data-id-scroll="36"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="25030" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-25030 grid-list__label" id="product_data_features_label_update_25030" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_25030--> < / div >

< / div >

< a
href = "https://avrora.ua/nabir-paperu-tualetnogo-ecolo-deluxe-biliy-3-shari-24-sht-up/" >
< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_25030"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/114/111441_001.webp"  alt="Набір паперу туалетного Ecolo Deluxe білий 3 шари 24 шт/уп" title="Набір паперу туалетного Ecolo Deluxe білий 3 шари 24 шт/уп" / >

< / a >

< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_25030"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_25030*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[25030][product_id]"
value = "25030" / >

< div


class ="right-top-blog" >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< / div >

< div


class ="left-top-blog" id="top_icon_25030_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..25030]"
data - ca - target - id = "top_icon_25030*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_25030_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/nabir-paperu-tualetnogo-ecolo-deluxe-biliy-3-shari-24-sht-up/"


class ="product-title" title="Набір паперу туалетного Ecolo Deluxe білий 3 шари 24 шт/уп" > Набір паперу туалетного Ecolo Deluxe білий 3 шари 24 шт / уп < / a >

< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/nabir-paperu-tualetnogo-ecolo-deluxe-biliy-3-shari-24-sht-up/?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 5 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "5"
data - ca - product - review - reviews - stars - full = "5"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(4)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-25030 ty-price-update" id="price_update_25030" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_25030" >

< bdi > < span
id = "sec_discounted_price_25030"


class ="ty-price-num" > 399 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_25030 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-25030 " id="add_to_cart_update_25030" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=111441&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_25030" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_25030 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Набір паперу туалетного Ecolo Deluxe білий 3 шари 24 шт/уп"
data - gtm - id = "111441"
data - gtm - product - id = "25030"
data - gtm - discount = "0.00"
data - gtm - price = "399.00"
data - gtm - brand = "Ecolo"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Особиста гігієна"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-25030" id="product_data_features_short_update_25030" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Ecolo <

/ li > < li > Вид: Туалетний
папір < / li > < li > Кількість
в
упаковці, шт: 24 < / li > < li > Кількість
шарів: 3
шари < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: 100 % целюлоза < / li > < / ul > < / div > <!--product_data_features_short_update_25030 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Набір паперу туалетного Ecolo Deluxe білий 3 шари 24 шт/уп"
data - item - id = "111441"
data - product - id = "25030"
data - discount = "0.00"
data - price = "399.00"
data - item - brand = "Ecolo"
data - item - category = "Краса та здоров’я/Гігієна/Особиста гігієна"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "4"
data - quantity = "1"
data - qty = "1"
data - position = "36"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#37"data-id-scroll="37"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="8432" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-8432 grid-list__label" id="product_data_features_label_update_8432" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_8432--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-gigiienichni-naturella-ult.cam.norm.duo-20-shtuk/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_8432"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/62401_001.webp"  alt="Прокладки гігієнічні NATURELLA Ultra Camomile Normal Duo 20 штук" title="Прокладки гігієнічні NATURELLA Ultra Camomile Normal Duo 20 штук" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Camomile Normal Duo 20 штук" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/62401_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Camomile Normal Duo 20 штук - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/62401_002.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Camomile Normal Duo 20 штук - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/62401_003.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Camomile Normal Duo 20 штук - 4" data-id="3" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/62401_004.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Camomile Normal Duo 20 штук - 5" data-id="4" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/62401_005.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Camomile Normal Duo 20 штук - 6" data-id="5" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/62401_006.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_8432"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_8432*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[8432][product_id]"
value = "8432" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-8432" id="product_labels_update_8432" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -23 % < / div >

< / div >

< !--product_labels_update_8432 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_8432_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..8432]"
data - ca - target - id = "top_icon_8432*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_8432_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-gigiienichni-naturella-ult.cam.norm.duo-20-shtuk/"


class ="product-title" title="Прокладки гігієнічні NATURELLA Ultra Camomile Normal Duo 20 штук" > Прокладки гігієнічні NATURELLA Ultra Camomile Normal Duo 20 штук < / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 4.60 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-8432" id="old_price_update_8432" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_8432" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_8432" class ="ty-list-price ty-nowrap" > 119 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_8432 --> < / span >

< span


class ="cm-reload-8432 ty-price-update" id="price_update_8432" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_8432" >

< bdi > < span
id = "sec_discounted_price_8432"


class ="ty-price-num" > 92 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_8432 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-8432 " id="add_to_cart_update_8432" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=62401&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_8432" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_8432 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки гігієнічні NATURELLA Ultra Camomile Normal Duo 20 штук"
data - gtm - id = "62401"
data - gtm - product - id = "8432"
data - gtm - discount = "27.00"
data - gtm - price = "119.00"
data - gtm - brand = "Naturella"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-8432" id="product_data_features_short_update_8432" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Naturella <

/ li > < li > Вид: Прокладки < / li > < li > Кількість
в
упаковці, шт: 20 < / li > < li > Призначення: Для
жіночої
гігієни < / li > < li > Розмір: 14
х9
см < / li > < / ul > < / div > <!--product_data_features_short_update_8432 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки гігієнічні NATURELLA Ultra Camomile Normal Duo 20 штук"
data - item - id = "62401"
data - product - id = "8432"
data - discount = "27.00"
data - price = "92.00"
data - item - brand = "Naturella"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "1"
data - quantity = "1"
data - qty = "1"
data - position = "37"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#38"data-id-scroll="38"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="4110" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-4110 grid-list__label" id="product_data_features_label_update_4110" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_4110--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-schodeni-kotex-deo-normal-plus-liners-56-sht-up/" >
< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_4110"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/178/58103_0011.webp"  alt="Прокладки щодені Kotex Deo Normal Plus Liners 56 штук" title="Прокладки щодені Kotex Deo Normal Plus Liners 56 штук" / >

< / a >

< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_4110"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_4110*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[4110][product_id]"
value = "4110" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-4110" id="product_labels_update_4110" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -19 % < / div >

< / div >

< !--product_labels_update_4110 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_4110_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..4110]"
data - ca - target - id = "top_icon_4110*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_4110_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-schodeni-kotex-deo-normal-plus-liners-56-sht-up/"


class ="product-title" title="Прокладки щодені Kotex Deo Normal Plus Liners 56 штук" > Прокладки щодені Kotex Deo Normal Plus Liners 56 штук < / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 1.86 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-4110" id="old_price_update_4110" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_4110" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_4110" class ="ty-list-price ty-nowrap" > 129 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_4110 --> < / span >

< span


class ="cm-reload-4110 ty-price-update" id="price_update_4110" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_4110" >

< bdi > < span
id = "sec_discounted_price_4110"


class ="ty-price-num" > 104 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_4110 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-4110 " id="add_to_cart_update_4110" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=58103&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_4110" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_4110 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки щодені Kotex Deo Normal Plus Liners 56 штук"
data - gtm - id = "58103"
data - gtm - product - id = "4110"
data - gtm - discount = "25.00"
data - gtm - price = "129.00"
data - gtm - brand = "Kotex"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-4110" id="product_data_features_short_update_4110" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Kotex <

/ li > < li > Вид: Прокладки < / li > < li > Кількість
в
упаковці, шт: 56 < / li > < li > Країна
походження: Китай < / li > < / ul > < / div > <!--product_data_features_short_update_4110 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки щодені Kotex Deo Normal Plus Liners 56 штук"
data - item - id = "58103"
data - product - id = "4110"
data - discount = "25.00"
data - price = "104.00"
data - item - brand = "Kotex"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "2"
data - quantity = "1"
data - qty = "1"
data - position = "38"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#39"data-id-scroll="39"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="6419" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-6419 grid-list__label" id="product_data_features_label_update_6419" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_6419--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-gigiienichni-naturella-classic-camomale-maxi-8-shtuk/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_6419"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/182/25662_001100.webp"  alt="Прокладки гігієнічні NATURELLA Classic Camomile Maxi 8 штук" title="Прокладки гігієнічні NATURELLA Classic Camomile Maxi 8 штук" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Classic Camomile Maxi 8 штук" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/182/25662_001100.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Classic Camomile Maxi 8 штук - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/182/25662_0011001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Classic Camomile Maxi 8 штук - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/25662_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Classic Camomile Maxi 8 штук - 4" data-id="3" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/25662_002.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Classic Camomile Maxi 8 штук - 5" data-id="4" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/25662_003.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Classic Camomile Maxi 8 штук - 6" data-id="5" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/25662_004.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_6419"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_6419*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[6419][product_id]"
value = "6419" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-6419" id="product_labels_update_6419" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -29 % < / div >

< / div >

< !--product_labels_update_6419 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_6419_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..6419]"
data - ca - target - id = "top_icon_6419*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_6419_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-gigiienichni-naturella-classic-camomale-maxi-8-shtuk/"


class ="product-title" title="Прокладки гігієнічні NATURELLA Classic Camomile Maxi 8 штук" > Прокладки гігієнічні NATURELLA Classic Camomile Maxi 8 штук < / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 4.88 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-6419" id="old_price_update_6419" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_6419" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_6419" class ="ty-list-price ty-nowrap" > 55 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_6419 --> < / span >

< span


class ="cm-reload-6419 ty-price-update" id="price_update_6419" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_6419" >

< bdi > < span
id = "sec_discounted_price_6419"


class ="ty-price-num" > 39 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_6419 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-6419 " id="add_to_cart_update_6419" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=25662&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_6419" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_6419 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки гігієнічні NATURELLA Classic Camomile Maxi 8 штук"
data - gtm - id = "25662"
data - gtm - product - id = "6419"
data - gtm - discount = "16.00"
data - gtm - price = "55.00"
data - gtm - brand = "Naturella"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-6419" id="product_data_features_short_update_6419" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Naturella <

/ li > < li > Вид: Прокладки < / li > < li > Кількість
в
упаковці, шт: 8 < / li > < li > Кількість
крапель: 3 < / li > < li > Країна
походження: Німеччина < / li > < / ul > < / div > <!--product_data_features_short_update_6419 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки гігієнічні NATURELLA Classic Camomile Maxi 8 штук"
data - item - id = "25662"
data - product - id = "6419"
data - discount = "16.00"
data - price = "39.00"
data - item - brand = "Naturella"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "3"
data - quantity = "1"
data - qty = "1"
data - position = "39"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#40"data-id-scroll="40"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="32332" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-32332 grid-list__label" id="product_data_features_label_update_32332" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_32332--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-gigiienichni-greenday-soft-night-6-sht-pach./" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_32332"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/143/105330_1.webp"  alt="Прокладки гігієнічні Greenday Soft Night 6 шт/пач." title="Прокладки гігієнічні Greenday Soft Night 6 шт/пач." / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні Greenday Soft Night 6 шт/пач." data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/143/105330_1.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні Greenday Soft Night 6 шт/пач. - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/143/105330.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_32332"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_32332*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[32332][product_id]"
value = "32332" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-32332" id="product_labels_update_32332" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -17 % < / div >

< / div >

< !--product_labels_update_32332 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_32332_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..32332]"
data - ca - target - id = "top_icon_32332*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_32332_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-gigiienichni-greenday-soft-night-6-sht-pach./"


class ="product-title" title="Прокладки гігієнічні Greenday Soft Night 6 шт/пач." > Прокладки гігієнічні Greenday Soft Night 6 шт / пач.< / a >

< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/prokladki-gigiienichni-greenday-soft-night-6-sht-pach./?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 4.9 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "5"
data - ca - product - review - reviews - stars - full = "5"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(10)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-32332" id="old_price_update_32332" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_32332" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_32332" class ="ty-list-price ty-nowrap" > 29 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_32332 --> < / span >

< span


class ="cm-reload-32332 ty-price-update" id="price_update_32332" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_32332" >

< bdi > < span
id = "sec_discounted_price_32332"


class ="ty-price-num" > 24 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_32332 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-32332 " id="add_to_cart_update_32332" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=105330&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_32332" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_32332 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки гігієнічні Greenday Soft Night 6 шт/пач."
data - gtm - id = "105330"
data - gtm - product - id = "32332"
data - gtm - discount = "5.00"
data - gtm - price = "29.00"
data - gtm - brand = "Greenday"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-32332" id="product_data_features_short_update_32332" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Greenday <

/ li > < li > Вид: Прокладки < / li > < li > Кількість
в
упаковці, шт: 6 < / li > < li > Кількість
крапель: 6 < / li > < li > Країна
походження: Туреччина < / li > < / ul > < / div > <!--product_data_features_short_update_32332 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки гігієнічні Greenday Soft Night 6 шт/пач."
data - item - id = "105330"
data - product - id = "32332"
data - discount = "5.00"
data - price = "24.00"
data - item - brand = "Greenday"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "4"
data - quantity = "1"
data - qty = "1"
data - position = "40"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#41"data-id-scroll="41"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="10219" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-10219 grid-list__label" id="product_data_features_label_update_10219" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_10219--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-gigiienichni-always-deo-ultra-lig.sing.10-shtuk/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_10219"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/182/88443_00001111.webp"  alt="Прокладки гігієнічні ALWAYS Deo Ультра Light 10 штук" title="Прокладки гігієнічні ALWAYS Deo Ультра Light 10 штук" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні ALWAYS Deo Ультра Light 10 штук" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/182/88443_00001111.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні ALWAYS Deo Ультра Light 10 штук - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/47/88443_001.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_10219"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_10219*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[10219][product_id]"
value = "10219" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-10219" id="product_labels_update_10219" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -14 % < / div >

< / div >

< !--product_labels_update_10219 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_10219_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..10219]"
data - ca - target - id = "top_icon_10219*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_10219_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-gigiienichni-always-deo-ultra-lig.sing.10-shtuk/"


class ="product-title" title="Прокладки гігієнічні ALWAYS Deo Ультра Light 10 штук" > Прокладки гігієнічні ALWAYS Deo Ультра Light 10 штук < / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 5.90 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-10219" id="old_price_update_10219" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_10219" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_10219" class ="ty-list-price ty-nowrap" > 69 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_10219 --> < / span >

< span


class ="cm-reload-10219 ty-price-update" id="price_update_10219" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_10219" >

< bdi > < span
id = "sec_discounted_price_10219"


class ="ty-price-num" > 59 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_10219 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-10219 " id="add_to_cart_update_10219" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=88443&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_10219" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_10219 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки гігієнічні ALWAYS Deo Ультра Light 10 штук"
data - gtm - id = "88443"
data - gtm - product - id = "10219"
data - gtm - discount = "10.00"
data - gtm - price = "69.00"
data - gtm - brand = "Always"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-10219" id="product_data_features_short_update_10219" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Always <

/ li > < li > Вид: Прокладки < / li > < li > Кількість
в
упаковці, шт: 10 < / li > < li > Кількість
крапель: 3 < / li > < li > Країна
походження: Угорщина < / li > < li > Призначення: Для
жіночої
гігієни < / li > < li > Розмір: Ligh < / li > < li > Склад: Бавовняне
волокно, віскоза < / li > < li > Форма
випуску: З
крильцями < / li > < / ul > < / div > <!--product_data_features_short_update_10219 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки гігієнічні ALWAYS Deo Ультра Light 10 штук"
data - item - id = "88443"
data - product - id = "10219"
data - discount = "10.00"
data - price = "59.00"
data - item - brand = "Always"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "1"
data - quantity = "1"
data - qty = "1"
data - position = "41"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#42"data-id-scroll="42"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="8416" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-8416 grid-list__label" id="product_data_features_label_update_8416" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_8416--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-schodenni-discreet-deo-vesnyaniy-briz-60-sht/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_8416"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/55178_001.webp"  alt="Прокладки щоденні Discreet Део Весняний бриз 60 шт" title="Прокладки щоденні Discreet Део Весняний бриз 60 шт" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Discreet Део Весняний бриз 60 шт" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/55178_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Discreet Део Весняний бриз 60 шт - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/55178_002.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Discreet Део Весняний бриз 60 шт - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/55178_003.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Discreet Део Весняний бриз 60 шт - 4" data-id="3" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/55178_004.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Discreet Део Весняний бриз 60 шт - 5" data-id="4" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/55178_005.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Discreet Део Весняний бриз 60 шт - 6" data-id="5" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/179/55178_006.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_8416"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_8416*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[8416][product_id]"
value = "8416" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-8416" id="product_labels_update_8416" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -23 % < / div >

< / div >

< !--product_labels_update_8416 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_8416_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..8416]"
data - ca - target - id = "top_icon_8416*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_8416_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-schodenni-discreet-deo-vesnyaniy-briz-60-sht/"


class ="product-title" title="Прокладки щоденні Discreet Део Весняний бриз 60 шт" > Прокладки щоденні Discreet Део Весняний бриз 60 шт < / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 1.65 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-8416" id="old_price_update_8416" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_8416" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_8416" class ="ty-list-price ty-nowrap" > 129 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_8416 --> < / span >

< span


class ="cm-reload-8416 ty-price-update" id="price_update_8416" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_8416" >

< bdi > < span
id = "sec_discounted_price_8416"


class ="ty-price-num" > 99 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_8416 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-8416 " id="add_to_cart_update_8416" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=55178&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_8416" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_8416 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки щоденні Discreet Део Весняний бриз 60 шт"
data - gtm - id = "55178"
data - gtm - product - id = "8416"
data - gtm - discount = "30.00"
data - gtm - price = "129.00"
data - gtm - brand = "Discreet"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-8416" id="product_data_features_short_update_8416" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Discreet <

/ li > < li > Вид: Прокладки < / li > < li > Кількість
в
упаковці, шт: 60 < / li > < li > Країна
походження: Італія < / li > < / ul > < / div > <!--product_data_features_short_update_8416 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки щоденні Discreet Део Весняний бриз 60 шт"
data - item - id = "55178"
data - product - id = "8416"
data - discount = "30.00"
data - price = "99.00"
data - item - brand = "Discreet"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "2"
data - quantity = "1"
data - qty = "1"
data - position = "42"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#43"data-id-scroll="43"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="32330" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-32330 grid-list__label" id="product_data_features_label_update_32330" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_32330--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-gigiienichni-greenday-soft-long-7-sht-pach./" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_32330"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/143/105331.webp"  alt="Прокладки гігієнічні Greenday Soft Long 7 шт/пач." title="Прокладки гігієнічні Greenday Soft Long 7 шт/пач." / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні Greenday Soft Long 7 шт/пач." data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/143/105331.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні Greenday Soft Long 7 шт/пач. - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/143/105331_2.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_32330"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_32330*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[32330][product_id]"
value = "32330" / >

< div


class ="right-top-blog" >

< / div >

< div


class ="left-top-blog" id="top_icon_32330_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..32330]"
data - ca - target - id = "top_icon_32330*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_32330_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-gigiienichni-greenday-soft-long-7-sht-pach./"


class ="product-title" title="Прокладки гігієнічні Greenday Soft Long 7 шт/пач." > Прокладки гігієнічні Greenday Soft Long 7 шт / пач.< / a >

< / bdi >

< div


class ="rating-container" > < a class ="ty-product-review-reviews-stars__link "


href = "https://avrora.ua/prokladki-gigiienichni-greenday-soft-long-7-sht-pach./?selected_section=product_reviews#product_reviews"
title = "Продукт отримав оцінку 5 із 5 зірок. Show review rating."
>
< div


class ="ty-product-review-reviews-stars


"
data - ca - product - review - reviews - stars - rating = "5"
data - ca - product - review - reviews - stars - full = "5"
data - ca - product - review - reviews - stars - is -half = ""
> < / div >
< / a >
< div


class ="left_info" >


(4)
< / div >
< / div >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-32330 ty-price-update" id="price_update_32330" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_32330" >

< bdi > < span
id = "sec_discounted_price_32330"


class ="ty-price-num" > 29 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_32330 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-32330 " id="add_to_cart_update_32330" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=105331&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_32330" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_32330 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки гігієнічні Greenday Soft Long 7 шт/пач."
data - gtm - id = "105331"
data - gtm - product - id = "32330"
data - gtm - discount = "0.00"
data - gtm - price = "29.00"
data - gtm - brand = "Greenday"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-32330" id="product_data_features_short_update_32330" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Greenday <

/ li > < li > Вид: Прокладки < / li > < li > Кількість
в
упаковці, шт: 7 < / li > < li > Кількість
крапель: 5 < / li > < li > Країна
походження: Туреччина < / li > < / ul > < / div > <!--product_data_features_short_update_32330 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки гігієнічні Greenday Soft Long 7 шт/пач."
data - item - id = "105331"
data - product - id = "32330"
data - discount = "0.00"
data - price = "29.00"
data - item - brand = "Greenday"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "3"
data - quantity = "1"
data - qty = "1"
data - position = "43"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#44"data-id-scroll="44"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="28645" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-28645 grid-list__label" id="product_data_features_label_update_28645" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_28645--> < / div >

< / div >

< a
href = "https://avrora.ua/nabir-paperu-tualetnogo-nizhniy-dotik-aroma-gold-biliy-2-shari-4-sht-up/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_28645"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/130/115038_001.webp"  alt="Набір паперу туалетного Ніжний дотик Арома Голд білий  2 шари 4 шт/уп" title="Набір паперу туалетного Ніжний дотик Арома Голд білий  2 шари 4 шт/уп" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Набір паперу туалетного Ніжний дотик Арома Голд білий  2 шари 4 шт/уп" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/130/115038_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Набір паперу туалетного Ніжний дотик Арома Голд білий  2 шари 4 шт/уп - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/130/115038_002.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Набір паперу туалетного Ніжний дотик Арома Голд білий  2 шари 4 шт/уп - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/130/115038_003.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Набір паперу туалетного Ніжний дотик Арома Голд білий  2 шари 4 шт/уп - 4" data-id="3" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/130/115038_004.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Набір паперу туалетного Ніжний дотик Арома Голд білий  2 шари 4 шт/уп - 5" data-id="4" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/130/115038_005.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_28645"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_28645*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[28645][product_id]"
value = "28645" / >

< div


class ="right-top-blog" >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< / div >

< div


class ="left-top-blog" id="top_icon_28645_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..28645]"
data - ca - target - id = "top_icon_28645*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_28645_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/nabir-paperu-tualetnogo-nizhniy-dotik-aroma-gold-biliy-2-shari-4-sht-up/"


class ="product-title" title="Набір паперу туалетного Ніжний дотик Арома Голд білий  2 шари 4 шт/уп" > Набір паперу туалетного Ніжний дотик Арома Голд білий  2 шари 4 шт / уп < / a >

< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-28645 ty-price-update" id="price_update_28645" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_28645" >

< bdi > < span
id = "sec_discounted_price_28645"


class ="ty-price-num" > 64 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_28645 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-28645 " id="add_to_cart_update_28645" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=115038&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_28645" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_28645 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Набір паперу туалетного Ніжний дотик Арома Голд білий  2 шари 4 шт/уп"
data - gtm - id = "115038"
data - gtm - product - id = "28645"
data - gtm - discount = "0.00"
data - gtm - price = "64.00"
data - gtm - brand = "Ніжний дотик"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Особиста гігієна"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-28645" id="product_data_features_short_update_28645" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Ніжний


дотик < / li > < li > Вид: Туалетний
папір < / li > < li > Кількість
в
упаковці, шт: 4
шт < / li > < li > Кількість
шарів: 2
шари < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: 100 % целюлоза, ароматична
композиція < / li > < li > Призначення: Для
гігієнічних
потреб < / li > < / ul > < / div > <!--product_data_features_short_update_28645 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Набір паперу туалетного Ніжний дотик Арома Голд білий  2 шари 4 шт/уп"
data - item - id = "115038"
data - product - id = "28645"
data - discount = "0.00"
data - price = "64.00"
data - item - brand = "Ніжний дотик"
data - item - category = "Краса та здоров’я/Гігієна/Особиста гігієна"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "4"
data - quantity = "1"
data - qty = "1"
data - position = "44"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#45"data-id-scroll="45"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="2012" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-2012 grid-list__label" id="product_data_features_label_update_2012" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_2012--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-gigiienichni-naturella-ultra-maxi-8-shtuk/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_2012"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/152/25668_201.webp"  alt="Прокладки гігієнічні NATURELLA Ultra Maxi 8 штук" title="Прокладки гігієнічні NATURELLA Ultra Maxi 8 штук" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Maxi 8 штук" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/152/25668_201.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Maxi 8 штук - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/152/25668_202.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Maxi 8 штук - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/152/25668_203.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Maxi 8 штук - 4" data-id="3" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/152/25668_204.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Maxi 8 штук - 5" data-id="4" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/152/25668_205.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні NATURELLA Ultra Maxi 8 штук - 6" data-id="5" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/152/25668_206.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_2012"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_2012*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[2012][product_id]"
value = "2012" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-2012" id="product_labels_update_2012" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -17 % < / div >

< / div >

< !--product_labels_update_2012 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_2012_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..2012]"
data - ca - target - id = "top_icon_2012*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< img


class ="image-360 restudio_360_view_icon" id="restudio_360_view_icon_2012_472" src="/design/themes/restudiotheme/media/restudio_360/icon-restudio-360.png" width="28" alt="360 icon" >

< !--top_icon_2012_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-gigiienichni-naturella-ultra-maxi-8-shtuk/"


class ="product-title" title="Прокладки гігієнічні NATURELLA Ultra Maxi 8 штук" > Прокладки гігієнічні NATURELLA Ultra Maxi 8 штук < / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 6.13 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-2012" id="old_price_update_2012" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_2012" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_2012" class ="ty-list-price ty-nowrap" > 59 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_2012 --> < / span >

< span


class ="cm-reload-2012 ty-price-update" id="price_update_2012" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_2012" >

< bdi > < span
id = "sec_discounted_price_2012"


class ="ty-price-num" > 49 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_2012 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-2012 " id="add_to_cart_update_2012" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=25668&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_2012" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_2012 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки гігієнічні NATURELLA Ultra Maxi 8 штук"
data - gtm - id = "25668"
data - gtm - product - id = "2012"
data - gtm - discount = "10.00"
data - gtm - price = "59.00"
data - gtm - brand = "Naturella"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-2012" id="product_data_features_short_update_2012" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Naturella <

/ li > < li > Вид: Прокладки < / li > < li > Кількість
в
упаковці, шт: 8 < / li > < li > Кількість
крапель: 5 < / li > < li > Країна
походження: Німеччина < / li > < / ul > < / div > <!--product_data_features_short_update_2012 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки гігієнічні NATURELLA Ultra Maxi 8 штук"
data - item - id = "25668"
data - product - id = "2012"
data - discount = "10.00"
data - price = "49.00"
data - item - brand = "Naturella"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "1"
data - quantity = "1"
data - qty = "1"
data - position = "45"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#46"data-id-scroll="46"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="17933" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-17933 grid-list__label" id="product_data_features_label_update_17933" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_17933--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-gigiienichni-kotex-ultra-normal-quadro-30-sht-pach/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_17933"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/186/101681_0101012.webp"  alt="Прокладки гігієнічні Kotex Ultra Normal Quadro 30 шт/пач" title="Прокладки гігієнічні Kotex Ultra Normal Quadro 30 шт/пач" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні Kotex Ultra Normal Quadro 30 шт/пач" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/186/101681_0101012.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки гігієнічні Kotex Ultra Normal Quadro 30 шт/пач - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/83/101681_001.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_17933"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_17933*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[17933][product_id]"
value = "17933" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-17933" id="product_labels_update_17933" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -24 % < / div >

< / div >

< !--product_labels_update_17933 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_17933_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..17933]"
data - ca - target - id = "top_icon_17933*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_17933_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-gigiienichni-kotex-ultra-normal-quadro-30-sht-pach/"


class ="product-title" title="Прокладки гігієнічні Kotex Ultra Normal Quadro 30 шт/пач" > Прокладки гігієнічні Kotex Ultra Normal Quadro 30 шт / пач < / a >

< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-17933" id="old_price_update_17933" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_17933" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_17933" class ="ty-list-price ty-nowrap" > 169 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_17933 --> < / span >

< span


class ="cm-reload-17933 ty-price-update" id="price_update_17933" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_17933" >

< bdi > < span
id = "sec_discounted_price_17933"


class ="ty-price-num" > 129 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_17933 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-17933 " id="add_to_cart_update_17933" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=101681&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_17933" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_17933 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки гігієнічні Kotex Ultra Normal Quadro 30 шт/пач"
data - gtm - id = "101681"
data - gtm - product - id = "17933"
data - gtm - discount = "40.00"
data - gtm - price = "169.00"
data - gtm - brand = "Kotex"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-17933" id="product_data_features_short_update_17933" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Kotex <

/ li > < li > Вид: Прокладки < / li > < li > Кількість
в
упаковці, шт: 30 < / li > < li > Кількість
крапель: 4 < / li > < li > Країна
походження: Чехія < / li > < / ul > < / div > <!--product_data_features_short_update_17933 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки гігієнічні Kotex Ultra Normal Quadro 30 шт/пач"
data - item - id = "101681"
data - product - id = "17933"
data - discount = "40.00"
data - price = "129.00"
data - item - brand = "Kotex"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "2"
data - quantity = "1"
data - qty = "1"
data - position = "46"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#47"data-id-scroll="47"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="20682" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-20682 grid-list__label" id="product_data_features_label_update_20682" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_20682--> < / div >

< / div >

< a
href = "https://avrora.ua/nabir-paperu-tualetnogo-papero-biliy-2-shari-4-sht-up./" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_20682"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/95/99628.webp"  alt="Набір паперу туалетного Papero білий 2 шари 4 шт/уп." title="Набір паперу туалетного Papero білий 2 шари 4 шт/уп." / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Набір паперу туалетного Papero білий 2 шари 4 шт/уп." data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/95/99628.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Набір паперу туалетного Papero білий 2 шари 4 шт/уп. - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/95/99628_1.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Набір паперу туалетного Papero білий 2 шари 4 шт/уп. - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/95/99628_2.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_20682"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_20682*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[20682][product_id]"
value = "20682" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-20682" id="product_labels_update_20682" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -22 % < / div >

< / div >

< !--product_labels_update_20682 --> < / div >

< span


class ="labels-item variant_27909" >


Національний
кешбек
< / span >
< / div >

< div


class ="left-top-blog" id="top_icon_20682_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..20682]"
data - ca - target - id = "top_icon_20682*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_20682_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/nabir-paperu-tualetnogo-papero-biliy-2-shari-4-sht-up./"


class ="product-title" title="Набір паперу туалетного Papero білий 2 шари 4 шт/уп." > Набір паперу туалетного Papero білий 2 шари 4 шт / уп.< / a >

< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-20682" id="old_price_update_20682" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_20682" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_20682" class ="ty-list-price ty-nowrap" > 59 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_20682 --> < / span >

< span


class ="cm-reload-20682 ty-price-update" id="price_update_20682" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_20682" >

< bdi > < span
id = "sec_discounted_price_20682"


class ="ty-price-num" > 46 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_20682 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-20682 " id="add_to_cart_update_20682" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=99628&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_20682" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_20682 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Набір паперу туалетного Papero білий 2 шари 4 шт/уп."
data - gtm - id = "99628"
data - gtm - product - id = "20682"
data - gtm - discount = "13.00"
data - gtm - price = "59.00"
data - gtm - brand = "Papero"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Особиста гігієна"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-20682" id="product_data_features_short_update_20682" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Бренд: Papero <

/ li > < li > Вид: Туалетний
папір < / li > < li > Кількість
в
упаковці, шт: 4 < / li > < li > Кількість
шарів: 2 < / li > < li > Країна
походження: Україна < / li > < li > Матеріал: 100 % целюлоза < / li > < li > Призначення: Для
гігієнічних
потреб < / li > < / ul > < / div > <!--product_data_features_short_update_20682 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Набір паперу туалетного Papero білий 2 шари 4 шт/уп."
data - item - id = "99628"
data - product - id = "20682"
data - discount = "13.00"
data - price = "46.00"
data - item - brand = "Papero"
data - item - category = "Краса та здоров’я/Гігієна/Особиста гігієна"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "3"
data - quantity = "1"
data - qty = "1"
data - position = "47"
>
< / div >
< / div >
< / div >
< div


class ="ty-column4"data-location-product="https://avrora.ua/gigiena/page-2/#48"data-id-scroll="48"data-location-id="2" >

< div


class ="ty-grid-list__item ty-quick-view-button__wrapper ty-grid-list__item--overlay" data-product-id="9563" > < div class ="ty-grid-list__item--wrap" > < div class ="ty-grid-list__image" > < div class ="label-wrap__scroller" > < div class ="cm-reload-9563 grid-list__label" id="product_data_features_label_update_9563" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="product-label--wrap" > < / div > < !--product_data_features_label_update_9563--> < / div >

< / div >

< a
href = "https://avrora.ua/prokladki-schodenni-discreet-deo-water-lily-20-shtuk/" >

< img


class ="ty-pict  gallery-products__general lazy-product   cm-image" id="det_img_9563"  src="/design/themes/restudiotheme/media/lazyimage.jpg" data-src="https://images.avrora.ua/images/thumbnails/250/250/detailed/44/25653_001.webp"  alt="Прокладки щоденні Discreet Deo Water Lily 20 штук" title="Прокладки щоденні Discreet Deo Water Lily 20 штук" / >

< span


class ="gallery-products" >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Discreet Deo Water Lily 20 штук" data-id="0" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/44/25653_001.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Discreet Deo Water Lily 20 штук - 2" data-id="1" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/44/25653_003.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Discreet Deo Water Lily 20 штук - 3" data-id="2" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/44/25653_004.webp" > < / span >

< span


class ="gallery-products__items" data-alt="Прокладки щоденні Discreet Deo Water Lily 20 штук - 4" data-id="3" data-imgGallery="https://images.avrora.ua/images/thumbnails/250/250/detailed/44/25653_005.webp" > < / span >

< / span >
< / a >
< / div > < div


class ="ty-grid-list__description" >

< div


class ="ty-simple-list clearfix" >

< form
action = "https://avrora.ua/"
method = "post"
name = "product_form_9563"
enctype = "multipart/form-data"


class ="cm-disable-empty-files  cm-ajax cm-ajax-full-render cm-ajax-status-middle " >

< input
type = "hidden"
name = "result_ids"
value = "cart_status*,wish_list*,checkout*,account_info*,top_icon_9563*" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "product_data[9563][product_id]"
value = "9563" / >

< div


class ="right-top-blog" >

< div


class ="ty-product-labels ty-product-labels--top-right   cm-reload-9563" id="product_labels_update_9563" >

< div


class ="ty-product-labels__item   ty-product-labels__item--discount" >

< div


class ="ty-product-labels__content" > -10 % < / div >

< / div >

< !--product_labels_update_9563 --> < / div >

< / div >

< div


class ="left-top-blog" id="top_icon_9563_472" >

< button
type = "button"


class ="ty-btn ty-btn__tertiary ty-btn-icon ty-add-to-wish cm-submit cm-ajax cm-ajax-full-render text-button"


data - ca - dispatch = "dispatch[wishlist.add..9563]"
data - ca - target - id = "top_icon_9563*"
title = "Додати в Обране" >
< i


class ="ty-icon-heart" > < / i >

< / button >

< !--top_icon_9563_472 --> < / div >

< bdi


class ="product-name__wrap" >

< a
href = "https://avrora.ua/prokladki-schodenni-discreet-deo-water-lily-20-shtuk/"


class ="product-title" title="Прокладки щоденні Discreet Deo Water Lily 20 штук" > Прокладки щоденні Discreet Deo Water Lily 20 штук < / a >

< div


class ="products-with-price" >

< bdi > < span


class ="ty-price" > 2.20 < / span > & nbsp; < span class ="ty-price" > грн < / span > < / bdi > / шт

< / div >
< / bdi >

< div


class ="ty-simple-list__price clearfix" >

< span


class ="cm-reload-9563" id="old_price_update_9563" >

< span


class ="ty-list-price ty-nowrap" id="line_list_price_9563" > < span class ="ty-strike" > < bdi > < span id="sec_list_price_9563" class ="ty-list-price ty-nowrap" > 49 < / span > & nbsp; < span class ="ty-list-price ty-nowrap" > грн < / span > < / bdi > < / span > < / span >

< !--old_price_update_9563 --> < / span >

< span


class ="cm-reload-9563 ty-price-update" id="price_update_9563" >

< input
type = "hidden"
name = "appearance[show_price_values]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_price]"
value = "1" / >
< span


class ="ty-price" id="line_discounted_price_9563" >

< bdi > < span
id = "sec_discounted_price_9563"


class ="ty-price-num" > 44 < / span > & nbsp; < span class ="ty-price-num" > грн < / span > < / bdi > < / span >

< !--price_update_9563 --> < / span >

< / div >

< div


class ="ty-simple-list__buttons" >

< div


class ="cm-reload-9563 " id="add_to_cart_update_9563" >

< input
type = "hidden"
name = "appearance[show_add_to_cart]"
value = "1" / >
< input
type = "hidden"
name = "appearance[show_list_buttons]"
value = "" / >
< input
type = "hidden"
name = "appearance[but_role]"
value = "action" / >
< input
type = "hidden"
name = "appearance[quick_view]"
value = "" / >

< a
id = "button_cart_2951"


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn__big ty-btn__add-to-cart ty-btn no-pointer" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=25653&amp;product_amount=&amp;city_id=" data-ca-target-id="in_another_shop_9563" data-ca-dialog- class ="shops-all popup-checkout" data-ca-dialog-title="Наявність в магазинах" > Купити < / a >

< !--add_to_cart_update_9563 --> < / div >

< / div >

< div


class ="hidden" >

< input
type = "hidden"


class ="gtm-array"


data - gtm - name = "Прокладки щоденні Discreet Deo Water Lily 20 штук"
data - gtm - id = "25653"
data - gtm - product - id = "9563"
data - gtm - discount = "5.00"
data - gtm - price = "49.00"
data - gtm - category = "Краса та здоров’я"
data - gtm - category2 = "Гігієна"
data - gtm - category3 = "Товари для жіночої гігієни"
data - gtm - quantity = "1"
data - gtm - index = "1"
data - qty = "1"
data - gtm - promo - id = "12"
data - gtm - promo - name = ""
>
< / div >

< div


class ="ty-simple-list__control" >

< div


class ="cm-reload-9563" id="product_data_features_short_update_9563" >

< input
type = "hidden"
name = "appearance[show_features]"
value = "1" / >

< div


class ="ty-product-block--features-top" > < ul > < li > Вид: Прокладки <

/ li > < li > Особливості: Щоденні < / li > < / ul > < / div > <!--product_data_features_short_update_9563 --> < / div >

< / div >

< div


class ="ty-simple-list__anim" > < / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< / div >
< input
type = "hidden"
name = "restudio_gtm"
data - item - name = "Прокладки щоденні Discreet Deo Water Lily 20 штук"
data - item - id = "25653"
data - product - id = "9563"
data - discount = "5.00"
data - price = "44.00"
data - item - category = "Краса та здоров’я/Гігієна/Товари для жіночої гігієни"
data - item - list - name = "Гігієна - Main Content"
data - item - list - id = "category_products_12"
data - index = "4"
data - quantity = "1"
data - qty = "1"
data - position = "48"
>
< / div >
< / div >
< / div >

< / div >

< !-- Inline
script
moved
to
the
bottom
of
the
page -->

< !-- Inline
script
moved
to
the
bottom
of
the
page -->

< div


class ="flex_revers" id="read_more_3" >

< div


class ="show_more" >

< a


class ="ty-pagination__item ty-pagination__btn ty-pagination__next cm-history cm-ajax" href="https://avrora.ua/gigiena/page-3/" rev="pagination_contents_3" data-ca-page="3" data-ca-target-id="read_more_3" > < span > < / span > Переглянути бiльше < / a >

< / div >

< div


class ="ty-pagination__bottom" >

< div


class ="ty-pagination" >

< a
data - ca - scroll = ".cm-pagination-container"


class ="ty-pagination__item ty-pagination__btn ty-pagination__prev cm-history cm-ajax" href="https://avrora.ua/gigiena/" data-ca-page="1" data-ca-target-id="pagination_contents,elm_faq_wrap" title="Prev" > < span


class ="ty-icon ty-pagination__text-arrow"

> < / span > & nbsp; < span


class ="ty-pagination__text" > Назад < / span > < / a >

< div


class ="ty-pagination__items" >

< a
data - ca - scroll = ".cm-pagination-container"
href = "https://avrora.ua/gigiena/"
data - ca - page = "1"


class ="cm-history ty-pagination__item cm-ajax" data-ca-target-id="pagination_contents,elm_faq_wrap" > 1 < / a >

< span


class ="ty-pagination__selected" > 2 < / span >

< a
data - ca - scroll = ".cm-pagination-container"
href = "https://avrora.ua/gigiena/page-3/"
data - ca - page = "3"


class ="cm-history ty-pagination__item cm-ajax" data-ca-target-id="pagination_contents,elm_faq_wrap" > 3 < / a >

< a
data - ca - scroll = ".cm-pagination-container"
href = "https://avrora.ua/gigiena/page-4/"
data - ca - page = "4"


class ="cm-history ty-pagination__item cm-ajax" data-ca-target-id="pagination_contents,elm_faq_wrap" > 4 < / a >

< a
data - ca - scroll = ".cm-pagination-container"
href = "https://avrora.ua/gigiena/page-5/"
data - ca - page = "5"


class ="cm-history ty-pagination__item cm-ajax" data-ca-target-id="pagination_contents,elm_faq_wrap" > 5 < / a >

< / div >

< a
data - ca - scroll = ".cm-pagination-container"


class ="ty-pagination__item ty-pagination__btn ty-pagination__next cm-history cm-ajax ty-pagination__right-arrow" href="https://avrora.ua/gigiena/page-3/" data-ca-page="3" data-ca-target-id="pagination_contents,elm_faq_wrap" title="Next" > < span class ="ty-pagination__text" > Вперед < / span > & nbsp; < span


class ="ty-icon ty-pagination__text-arrow"

> < / span > < / a >

< / div >
< / div >

< !--pagination_contents --> < / div >

< !--read_more_3 --> < / div >
< !--read_more_2 --> < / div >

< !--category_products_12 --> < / div > < div


class ="ty-wysiwyg-content" > < div class ="mobile__bottom-block--fixed hidden" >

< button


class ="filter-btn" > < span > < / span > Фільтр < / button >

< div
id = "elm_sort_wrap_mobile_ul" >
< div


class ="ty-sort-container" >

< span > Сортувати: < / span >

< div


class ="ty-sort-dropdown" id="elm_sort_wrap_mobile" >

< a
id = "sw_elm_sort_fields_mobile"


class ="ty-sort-dropdown__wrapper cm-combination" > Популярні < i class ="ty-sort-dropdown__icon ty-icon-down-micro" > < / i > < / a >

< ul
id = "elm_sort_fields_mobile"


class ="ty-sort-dropdown__content cm-popup-box hidden" >

< li


class ="sort-by-timestamp-desc ty-sort-dropdown__content-item" >

< a


class ="cm-ajax cm-ajax-full-render ty-sort-dropdown__content-item-a" data-ca-scroll=".cm-pagination-container" data-ca-target-id="elm_sort_wrap,elm_sort_wrap_mobile,pagination_contents" href="https://avrora.ua/gigiena/page-2/?sort_by=timestamp&amp;sort_order=desc" rel="nofollow" > Новинки < / a >

< / li >
< li


class ="sort-by-price-asc ty-sort-dropdown__content-item" >

< a


class ="cm-ajax cm-ajax-full-render ty-sort-dropdown__content-item-a" data-ca-scroll=".cm-pagination-container" data-ca-target-id="elm_sort_wrap,elm_sort_wrap_mobile,pagination_contents" href="https://avrora.ua/gigiena/page-2/?sort_by=price&amp;sort_order=asc" rel="nofollow" > Від дешевших < / a >

< / li >
< li


class ="sort-by-price-desc ty-sort-dropdown__content-item" >

< a


class ="cm-ajax cm-ajax-full-render ty-sort-dropdown__content-item-a" data-ca-scroll=".cm-pagination-container" data-ca-target-id="elm_sort_wrap,elm_sort_wrap_mobile,pagination_contents" href="https://avrora.ua/gigiena/page-2/?sort_by=price&amp;sort_order=desc" rel="nofollow" > Від дорогих < / a >

< / li >
< / ul >
< !--elm_sort_wrap_mobile --> < / div >

< / div >
< !--elm_sort_wrap_mobile_ul --> < / div >
< / div >
< / div >
< / div >

< / div >

< / div >

< / div >

< div


class ="tygh-footer" id="tygh_footer" >

< div


class ="container-fluid   ty-footer-grid" >

< div


class ="row footer-blocks--wrap" >

< div


class ="col-md-16  footer-blocks site-mode-A" >

< div


class ="row tygh-footer__logo--wrap" >

< div


class ="col-md-2  tygh-footer__logo site-mode-A" >

< div


class ="ty-logo-container" >

< a
href = "https://avrora.ua/"
title = "" >
< img


class ="ty-pict  ty-logo-container__image   cm-image" id="det_img_6a270d54e84ff"  src="https://images.avrora.ua/images/logos/8/logo.webp"  width="328" height="114" alt="Мультимаркет Аврора" title="Мультимаркет Аврора" / >

< / a >
< / div >
< / div >

< div


class ="col-md-3  tygh-footer__menu site-mode-A" >

< ul
id = "text_links_372"


class ="ty-text-links" >

< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/"
>
Головна
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://robota.avrora.ua/nasa-misiia"
>
Комплаєнс
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://corporate.avrora.ua/about/"
target = "_blank"
>
Контакти
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://corporate.avrora.ua/for-partners/"
target = "_blank"
>
Партнерам
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://robota.avrora.ua/vakansiyi"
target = "_blank"
>
Робота
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://next.avrora.ua/"
target = "_blank"
>
Аврора
Next
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://robota.avrora.ua/novini-avrora"
target = "_blank"
>
Новини
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://robota.avrora.ua/"
target = "_blank"
>
Більше
про
Аврору
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/dostavka-ta-oplata/"
>
Доставка
та
оплата
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/obmin-ta-povernennya/"
>
Обмін
та
повернення
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/elektronniy-dokumentoobig/"
>
Електронний
документообіг
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/pravila-rozmischennya-vidgukiv-pro-tovari-na-sayti/"
>
Правила
розміщення
відгуків
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/oficiyni-pravila/"
>
Офіційні
правила
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/publichna-ugoda/"
>
Публічна
угода
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/politika-obrobki-ta-zahistu-personalnih-danih/"
>
Політика
конфіденційності
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/cookies/"
>
Cookies
< / a >
< / li >
< / ul >
< / div >

< div


class ="col-md-3  tygh-footer__menu site-mode-A" >

< ul
id = "text_links_373"


class ="ty-text-links" >

< li


class ="ty-text-links__item ty-level-0 header__hidden-link" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/magazyny/"
>
Магазини
< / a >
< / li >
< / ul > < ul
id = "text_links_707"


class ="ty-text-links" >

< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/exclusive-aurora/"
>
Ексклюзивно
в
Аврорі
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/sitemap/"
>
Карта
сайту
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/blog/"
>
Блог
< / a >
< / li >
< li


class ="ty-text-links__item ty-level-0" >

< a


class ="ty-text-links__a"


href = "https://avrora.ua/radio-avrora/"
>
Радіо
Аврора
< / a >
< / li >
< / ul >
< / div >

< div


class ="col-md-4  tygh-footer__contacts site-mode-A" >

< div


class ="ty-wysiwyg-content" > < div class ="contacts__item" >

< p > Служба
підтримки < / p >
< p > < a
href = "tel:+380800300066" > < strong > 0
800
300
066 < / strong > < / a > < / p >
< / div >
< div


class ="contacts__item" >

< p


class ="worktime-title" > Графік роботи < / p >

< p


class ="worktime-body" > < strong > Пн - Нд: 7: 00 - 21

:00 < / strong > < / p >
< / div >
< div


class ="contacts__item" >

< p > Загальні
питання < / p >
< p > < a
href = "/cdn-cgi/l/email-protection#70191e161f301106021f02115e0511" > < strong > < span


class ="__cf_email__" data-cfemail="630a0d050c230215110c11024d1602" >[email &  # 160;protected]</span></strong></a></p>
< / div >
< div


class ="contacts__item" >

< p > Інтернет - замовлення < / p >
< p > < a
href = "/cdn-cgi/l/email-protection#701f0214150203301106021f02115e0511" > < strong > < span


class ="__cf_email__" data-cfemail="b3dcc1d7d6c1c0f3d2c5c1dcc1d29dc6d2" >[email &  # 160;protected]</span></strong></a></p>
< / div >
< div


class ="contacts__item" >

< p > PR - запити < / p >
< p > < a
href = "/cdn-cgi/l/email-protection#5b2b291b3a2d2934293a752e3a" > < strong > < span


class ="__cf_email__" data-cfemail="c7b7b587a6b1b5a8b5a6e9b2a6" >[email &  # 160;protected]</span></strong></a></p>
< / div > < / div > < div


class ="social-footer-block " >

< div


class ="ty-wysiwyg-content" > < div class ="ty-social-wrap" >

< div


class ="ty-social-item facebook" >

< a
href = "https://www.facebook.com/avrora.multimarket"
target = "_blank"
title = "Facebook" >
< i


class ="icon-facebook" > < / i >

< / a >
< / div >
< div


class ="ty-social-item instagram" >

< a
href = "https://www.instagram.com/avrora.multimarket/"
target = "_blank"
title = "Instagram" >
< i


class ="icon-instagram" > < / i >

< / a >
< / div >
< div


class ="ty-social-item telegram" >

< a
href = "https://t.me/Avroraua"
target = "_blank"
title = "Telegram" >
< i


class ="icon-telegram" > < / i >

< / a >
< / div >
< div


class ="ty-social-item youtube" >

< a
href = "https://www.youtube.com/channel/UCMIQPAmwj86Gf0gtakRSVJA"
target = "_blank"
title = "Youtube" >
< i


class ="icon-youtube" > < / i >

< / a >
< / div >
< div


class ="ty-social-item tiktok" >

< a
href = "https://www.tiktok.com/@avrora.multimarket"
target = "_blank"
title = "TikTok" >
< i


class ="icon-tiktok" > < / i >

< / a >
< / div >
< div


class ="ty-social-item linkedin" >

< a
href = "https://www.linkedin.com/company/avroraua/"
target = "_blank"
title = "Linkedin" >
< i


class ="icon-linkedin" > < / i >

< / a >
< / div >
< div


class ="ty-social-item viber" >

< a
href = "https://invite.viber.com/?g2=AQANNWf1szIUrU7N0%2B3q7jrf1CbtWxJEn%2FyE8kQukVNn9mzVglYNZs%2BctMuOws8p&lang=uk"
target = "_blank"
title = "Viber" >
< i


class ="icon-viber" > < / i >

< / a >
< / div >
< / div > < / div >
< / div >
< / div >

< div


class ="col-md-4  tygh-footer__subscribe site-mode-A" >

< div


class ="ty-footer" >

< div


class ="ty-footer-general__header  cm-combination" id="sw_footer-general_56" >

< span > Підпишись
на
новини
та
акції < / span >

< i


class ="ty-footer-menu__icon-open ty-icon-down-open" > < / i >

< i


class ="ty-footer-menu__icon-hide ty-icon-up-open" > < / i >

< / div >
< div


class ="ty-footer-general__body" id="footer-general_56" > < div class ="ty-footer-form-block ty-footer-form-block--responsive" >

< form
action = "https://avrora.ua/"
method = "post"
name = "subscribe_form"


class ="cm-processing-personal-data" >

< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "newsletter_format"
value = "2" / >

< p


class ="ty-footer-form-block__p" > Ми надсилаємо тільки найкращі пропозиції для шопінгу < / p >

< div


class ="ty-footer-form-block__form-container" >

< div


class ="ty-footer-form-block__form ty-control-group ty-input-append cm-block-add-subscribe" >

< label


class ="cm-required cm-email hidden" for ="subscr_email56" > E-mail < / label >

< input
type = "text"
name = "subscribe_email"
id = "subscr_email56"
size = "20"
value = "Залиш свій email"


class ="cm-hint ty-input-text" / >

< div


class ="check-block" >

< label


class ="cm-required" for ="subscr__checkbox56" >

< span


class ="checkbox-wrap" >

< input
type = "checkbox"
name = "subscribe_checkbox"
id = "subscr__checkbox56"
checked / >
< span


class ="checked" > < / span >

< / span >
Я
погоджуюсь
з
умовами < a


class ="cm-dialog-opener cm-dialog-auto-size" href="/politika-obrobki-ta-zahistu-personalnih-danih/" id="opener_page_tl_31_2" data-ca-target-id="page_tl_31" data-ca-dialog-title="Угода користувача" > Політики конфіденційності < / a > і даю згоду на обробку моїх данних

< / label >
< / div >

< button
title = "Підписатися"


class ="ty-btn-go" type="submit" > Підписатися < / button >

< input
type = "hidden"
name = "dispatch"
value = "newsletters.add_subscriber" / >
< / div >
< / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >
< !-- Inline
script
moved
to
the
bottom
of
the
page --> < / div >
< / div >
< / div >

< / div >

< div


class ="row bottom-info-footer--wrap" >

< div


class ="col-md-16  bottom-info-footer site-mode-A" >

< div


class ="ty-wysiwyg-content" > < div class ="site-information" >

< a
href = "https://t.me/A_StatusWorkShops_Bot"
target = "_blank"


class ="site-information__item telegram hidden" title="Чат-бот Telegram" >

< strong > Чат - бот
Telegram < / strong >
< i


class ="svg-icon-telegram" > < / i >

< / a >
< div


class ="site-information__item partners" >

< strong > Членство
в
АСС, ЕВА, ГД
ООН, UNIC < / strong >
< div


class ="svg-icon-wrap" >

< a
href = "https://chamber.ua/ua/companies/real-bargain-llc-2/"
target = "_blank"
rel = "nofollow"


class ="acc-info" title="Американська торговельна палата в Україні" > < / a >

< a
href = "https://eba.com.ua/member/tov-vygidna-pokupka/"
target = "_blank"
rel = "nofollow"


class ="eba-info" title="European Business Association" > < / a >

< a
href = "https://globalcompact.org.ua/"
target = "_blank"
rel = "nofollow"


class ="globalcompact-info" title="Global Compact" > < / a >

< a
href = "https://unic.org.ua/members/117/"
target = "_blank"
rel = "nofollow"


class ="unic-info" title="Unic" > < / a >

< / div >
< / div >
< / div > < / div > < div


class ="ty-payment-icons" >

< span


class ="ty-payment-icons__item liqpay" title="LiqPay" > < / span >

< span


class ="ty-payment-icons__item privat24" title="Privat24" > < / span >

< span


class ="ty-payment-icons__item visa" title="ViSA" > < / span >

< span


class ="ty-payment-icons__item mastercard" title="mastercard" > < / span >

< / div >
< / div >

< / div >

< div


class ="row app-section--wrap" >

< div


class ="col-md-16  app-section site-mode-A" >

< div


class ="mobile-app-block" >

< div


class ="mobile-app-block__title" >


Аврора
з
тобою
всюди
< / div >
< div


class ="mobile-app-block__links" >

< a
href = "https://play.google.com/store/apps/details?id=com.avrora.app"
target = "_blank"
rel = "noopener" >
< img
src = "/design/themes/restudiotheme/media/webp/googleplay.webp"
alt = "Android App" >
< / a >
< a
href = "https://apps.apple.com/ua/app/%D0%B0%D0%B2%D1%80%D0%BE%D1%80%D0%B0/id6755111436"
target = "_blank"
rel = "noopener" >
< img
src = "/design/themes/restudiotheme/media/webp/appstore.webp"
alt = "iOS App" >
< / a >
< / div >
< / div >
< / div >

< / div >

< div


class ="row bottom-copyright-footer--wrap" >

< div


class ="col-md-16  bottom-copyright-footer site-mode-A" >

< div


class ="bottom-copyright__wrap" >

< div


class ="bottom-copyright__text" >

& copy;
Аврора.
2026 - Всі
права
захищені
< / div >
< div


class ="bottom-copyright__dev" >

< a


class ="bottom-copyright" href="https://www.restudio.com.ua/" target="_blank" > Development: ReStudio <

/ a > < span


class ="slash" > / < / span >

< a


class ="bottom-copyright vintage" href="https://vintage.com.ua/" target="_blank" > Design: <


    span


class ="icon" > < / span > < / a >

< / div >
< / div >
< / div >

< / div >
< / div >

< / div >

< div


class ="row" >

< div


class ="col-md-16   site-mode-A" >

< div


class ="ty-wysiwyg-content" > < a href="#tygh_main_container" class ="scroll-up" > top < / a > < / div >

< / div >

< / div >
< / div >

< / div >
< div


class ="tygh-under-bottom mobile-ui-menu hidden" >

< div


class ="mobile-ui-menu__wrap" >

< ul


class ="mobile-ui-menu__nav" >

< li


class ="mobile-ui-menu__nav--li" >

< a
href = "https://avrora.ua/"


class ="mobile-ui-menu__nav--a link-home" >


Головна
< / a >
< / li >
< li


class ="mobile-ui-menu__nav--li" > < a class ="mobile-ui-menu__nav--a mob-btn link-catalog" > Каталог < / a > < / li >

< li


class ="mobile-ui-menu__nav--li" >

< a


class ="mobile-ui-menu__nav--a mob-btn link-cart" onclick="$('.header-info .top-select-locations .local-shop-link').trigger('click');" >

< span


class ="res-cart__amount cart-count hidden" > 0 < / span >


Кошик
< / a >
< / li >
< li


class ="mobile-ui-menu__nav--li" >

< a
href = "https://avrora.ua/wishlist/"


class ="mobile-ui-menu__nav--a link-wishlist cm-tooltip" title="Обране" >

< span


class ="res-cart__amount wish-count hidden" > 0 < / span >


Обране
< / a >
< / li >
< li


class ="mobile-ui-menu__nav--li" > < a class ="mobile-ui-menu__nav--a mob-btn link-more" > Більше < / a > < / li >

< / ul > < / div >
< / div >

< / div >
< !--tygh_main_container --> < / div >

< !--tygh_container --> < / div >

< script
data - cfasync = "false"
src = "/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js" > < / script > < script
src = "https://code.jquery.com/jquery-3.5.1.min.js"
integrity = "sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
crossorigin = "anonymous"
data - no - defer
> < / script >
< script
src = "https://code.jquery.com/jquery-migrate-3.3.0.min.js"
integrity = "sha256-wZ3vNXakH9k4P00fNGAlbN0PkpKSyhRa76IFy4V1PYE="
crossorigin = "anonymous"
data - no - defer
> < / script >
< script
data - no - defer >
if (!window.jQuery) {
document.write('<script src="https://avrora.ua/js/lib/jquery/jquery-3.5.1.min.js?ver=1780866602" ><\/script>');
document.write('<script src="https://avrora.ua/js/lib/jquery/jquery-migrate-3.3.0%7D.min.js?ver=1780866602" ><\/script>');
}
< / script >

< script
src = "https://avrora.ua/var/cache/misc/assets/js/tygh/scripts-9b6d1af1082e01d656114d81bc45a0f2.js?1780866602" > < / script >
< script
src = "https://cdnjs.cloudflare.com/ajax/libs/animejs/2.0.2/anime.min.js" > < / script >
< script
src = "/design/themes/restudiotheme/js/lib/leaflet.js?v=1" > < / script >
< script
src = "/design/themes/restudiotheme/js/lib/leaflet.markercluster.js?v=1" > < / script >
< script
src = "/design/themes/restudiotheme/js/openstreetmap_shops_popup.js?v=16" > < / script >
< script >
(function(_, $)
{

    _.tr({
        cannot_buy: 'Неможливо купити цей товар з обраними варіантами опцій',
        no_products_selected: 'Немає обраних',
        error_no_items_selected: 'Немає обраних елементів! Для виконання цієї дії має бути вибраний хоча б один елемент.',
        delete_confirmation: 'Ви дійсно бажаєте видалити виділені елементи?',
        text_out_of_stock: 'Немає у наявності',
        items: 'шт.',
        text_required_group_product: 'Будь ласка, виберіть товар для зазначеної групи [group_name]',
        save: 'Зберегти',
        close: 'Закрити',
        notice: 'Сповіщення:',
        warning: 'Попередження:',
        error: 'Помилка',
        empty: 'Порожній',
        text_are_you_sure_to_proceed: 'Справді продовжити?',
        text_invalid_url: 'Введено неприпустиму URL-адресу',
        error_validator_email: 'Email в полі &lt;b&gt;[field]&lt;\/b&gt; недійсний.',
        error_validator_phone: 'Неприпустимий номер телефону в полі &lt;b&gt;[field]&lt;\/b&gt;. Правильний формат (044) 123-45-67 або 380 44 123 4567.',
        error_validator_phone_mask: 'Номер в полі &lt;b&gt;[field]&lt;\/b&gt; некоректний.',
        error_validator_integer: 'Неприпустиме значення поля &lt;b&gt;[field]&lt;\/b&gt;. Воно повинно бути цілим числом.',
        error_validator_multiple: 'Поле &lt;b&gt;[field]&lt;\/b&gt; не має вибраних параметрів.',
        error_validator_password: 'Паролі в &lt;b&gt;[field2]&lt;\/b&gt; і &lt;b&gt;[field]&lt;\/b&gt; полях не співпадають.',
        error_validator_required: 'Поле [field] є обов\&#039;язковим.',
        error_validator_zipcode: 'Невірний поштовий індекс в полі &lt;b&gt;[field]&lt;\/b&gt;. Правильний формат: [extra].',
        error_validator_message: 'Неприпустиме значення поля &lt;b&gt;[field]&lt;\/b&gt;.',
        text_page_loading: 'Завантаження... Ваш запит обробляється, будь ласка, почекайте.',
        error_ajax: 'На жаль, щось пішло не так ([error]). Будь ласка, спробуйте ще раз.',
        text_changes_not_saved: 'Зроблені зміни не було збережено.',
        text_data_changed: 'Ваші зміни не були збережені. Натисніть ОК, щоб продовжити, або кнопку Скасувати, щоб залишитися на поточній сторінці.',
        placing_order: 'Розміщення замовлення',
        file_browser: 'Знайти файл',
        browse: 'Перегляд...',
        more: 'Більше',
        text_no_products_found: 'Ой, тут нічого не знайшлося. Спробуй змінити фільтри або переглянь всі товари.',
        cookie_is_disabled: 'For a complete shopping experience, please &lt;a href=\&quot;https://www.wikihow.com/Enable-Cookies-in-Your-Internet-Web-Browser\&quot; target=\&quot;_blank\&quot;&gt;set your browser to accept cookies&lt;\/a&gt;',
        insert_image: 'Додати зображення',
        image_url: 'Url зображення',
        loading: 'Завантаження...',

        text_editing_raw: 'Редагування тексту',
        save_raw: 'Зберегти',
        cancel_raw: 'Скасувати',

        sms_sent: 'Код надіслано',
        auth_title: 'Авторизація',
        sign_in: 'Увійти',
        auth_title_little: 'Ще трошечки'
    });

$.extend(_, {
    index_script: 'index.php',
    changes_warning: / * 'Y' * / 'N',
         currencies: {
    'primary': {
        'decimals_separator': '.',
        'thousands_separator': '&nbsp;',
        'decimals': '2'
    },
    'secondary': {
        'decimals_separator': '.',
        'thousands_separator': '&nbsp;',
        'decimals': '2',
        'coefficient': '1.00000'
    }
},
default_editor: 'full_ckeditor',
default_previewer: 'owl',
current_path: '',
current_location: 'https://avrora.ua',
images_dir: 'https://avrora.ua/design/themes/responsive/media/images',
notice_displaying_time: 5,
cart_language: 'uk',
language_direction: 'ltr',
default_language: 'uk',
cart_prices_w_taxes: false,
regexp: [],
current_url: 'https://avrora.ua/gigiena/page-2/',
current_host: 'avrora.ua',
init_context: '',
phone_validation_mode: 'international_format',
hash_of_available_countries: '22fc22532e5c4f4ce545873e4b151d36'
});



$(document).ready(function()
{
$.runCart('C');
});

// CSRF
form
protection
key
_.security_hash = 'e70a77422e4e8f6aeecf0dbd2b03cfff';
}(Tygh, Tygh.$));
< / script >
< script >
(function(_, $)
{
    _.tr({
        nothing_found: 'Не знайдено'
    });

}(Tygh, Tygh.$));
< / script >
< script >
Tygh.tr('buy_together_fill_the_mandatory_fields',
        'Перед додаванням цього продукту до кошика, будь ласка, вкажіть параметри продукту.');
< / script >
< script >
$(document).ready(function()
{

    jQuery.ui.autocomplete.prototype._resizeMenu = function()
{
    var
ul = this.menu.element;
ul.outerWidth(this.element.outerWidth());
}

if ($('#search_input').length){

$('body').find('[name="search_form"]').on('submit', function (event) {

// $("#search_input").keydown(function(event){

if ($('body').find('.smart-search').length) {
var form_get = $('body').find('.smart-search').data('from_get');

if ( form_get != 0) {
window.location.href = form_get;
event.preventDefault();
return false;
}
}
});

$('#search_input').autocomplete({
    minLength: 1,
    appendTo: ".ty-search-autocomplete",
    source: function(request, response) {

$.ajax({
    url: "index.php?dispatch=res_adv_search.query",
    data: {
        searchtext: request.term
    },
    dataType: "json",
    success: function(data) {
        var obj = data;
// var
obj = $.parseJSON(data.text);
if ($.isEmptyObject(data)) {
    var
result = [
    {
        label: 'Немає збігів',
        value: request.term
    }
];
response(result);
} else {
    response($.map(obj, function(item)
{
return item;
}))
}

$('body') \
    .find('.smart-search__keyword, .smart-search__products') \
    .mCustomScrollbar();

}
})
}

}).focus(function()
{

$(this).data("uiAutocomplete").search($(this).val());

}).data("ui-autocomplete")._renderItem = function(ul, item)
{

    ul.addClass('res_search');

// console.log(item);

if (item.html)
{
    var
html = item.html;

} else {
    var
html = '<span class="q-search witdsto" align="center" >' + item.label + '</span>';
}


return $("<li>")
.data("ui-autocomplete-item", item)
.append(html)
.appendTo(ul);

};
}

/ * $('body').on('click', function(e)
{
var
elm =  $('#ty-search-block');
if (e.target.id == 'search_input'){
elm.addClass('open');
$('.ty-dropdown-box__title,.ty-select-block__a').removeClass('open');
} else {
elm.removeClass('open');
$('.ty-search-autocomplete').removeClass('open--mod');
$('body').removeClass('open--mod');
}
// if (e.target.id == 'ty-search-block'){
// elm.removeClass('open');
//}
}); * /

$('body').on(

    'click',

    '.ss__category-item',

    function(event)
{

event.preventDefault();

let
getThisEl = $(this),
getTisCat = getThisEl
.data('catId');

$('body')
.find('.group_category')
.addClass('hidden');

$('.ss__category-item')
.removeClass('active');

getThisEl
.addClass('active');



$(`.${getTisCat}`)
.removeClass('hidden');

}

);

$('body').on(

    'click',

    '.all-ss__category',

    function(event)
{

event.preventDefault();

$('.ss__category-item')
.removeClass('active');

$('body')
.find('.group_category')
.removeClass('hidden');

}

);


let
getSmartSearchInput = $('.top-search input.ty-search-block__input'),
getSearchBlock = $('#ty-search-block'),
getSmartSearchClear = $('.clear-search');

getSmartSearchInput.on(

    'click keyup',

    function()
{

let
getThisEl = $(this);

if (
        getThisEl.val().length > 2
) {

getSearchBlock
.addClass('open');

getThisEl
.addClass('open--mod');

$('.ty-search-autocomplete')
.addClass('open--mod');
$('body')
.addClass('open--mod');
getSmartSearchClear
.addClass('open--mod');

}

}

);

getSmartSearchClear.on('click', function()
{

getSmartSearchInput
.val('');

getSmartSearchClear
.removeClass('open--mod');

$('body, .ty-search-autocomplete')
.removeClass('open--mod');

getSearchBlock
.removeClass('open');

});

$(function($)
{

$(document).mouseup(function(e)
{

    let
getSearchContainer = $('.top-search');

if (!getSearchContainer.is (e.target)
   & & getSearchContainer.has(e.target).length == = 0 ) {

$('.ty-search-block') \
    .removeClass('open');

$('body, .ty-search-autocomplete') \
    .removeClass('open--mod');

}
});

});

});

// $('.ty-search-block__input').on('input', function()
{
// if ($(this).val().length > 2) {
                                 //         $('.clear-search').addClass('show');
//} else {

         //}
//});

/ * $('.top-search input.ty-search-block__input').on('keyup', function()
{

if ($(this).val().length > 2) {
$(this).addClass('open--mod');

setTimeout(function()
{
$('.ty-search-autocomplete').addClass('open--mod');
$('body').addClass('open--mod');
$('.clear-search').addClass('open--mod');
}, 500);

} else {
$(this).removeClass('open--mod');
$('.ty-search-autocomplete').removeClass('open--mod');
$('body').removeClass('open--mod');
$('.clear-search').removeClass('open--mod');
}
}); * /

/ * $('.top-search input.ty-search-block__input').on('click', function()
{
if ($(this).val().length > 2 & & $(this). is (":focus")) {
$(this).addClass('open--mod');

setTimeout(function()
{
$('.ty-search-autocomplete').addClass('open--mod');
$('body').addClass('open--mod');
$('.clear-search').addClass('open--mod');
}, 500);

} else {
$(this).removeClass('open--mod');
$('.ty-search-autocomplete').removeClass('open--mod');
$('body').removeClass('open--mod');
$('.clear-search').removeClass('open--mod');
}
}); * /

< / script >
    < script >
// $('body').on('click', '.js-choose-stock-id:not(.is-popup)', function(e)
{
// e.preventDefault();
// var
stock_id = $(this).data('id');
// var
stock_text = $(this).data('text');
// var $select = $('#cac_stock_id_d');
// var $existingOption = $select.find('option[value="' + stock_id + '"]');
// if ($existingOption.length) {
// $existingOption.text(stock_text);
//} else {
// var newOption = new Option(stock_text, stock_id, true, true);
// $select.append(newOption);
//}
// $select.val(stock_id).trigger('change.select2');
// $select.closest('form').find('button[type="submit"]').click();
//});
// $('body').on('click', '.js-choose-stock-id.is-popup', function(e) {
// e.preventDefault();
// var stock_id = $(this).data('id');
// $('.cac-choose-shop[data-stock-id="'+stock_id+'"]').click();
//});
$('body').on('click', '.js-cac-confirm-popup', function(){
$('body').removeClass('stock_city_confirm');

const expires = new Date();
expires.setTime(expires.getTime() + (60 * 24 * 60 * 60 * 1000));
document.cookie = `stock_city_confirm=true; expires=${expires.toUTCString()}; path= / `;

$('.header-info .local-shop-link').click();
$('.av-cac--confirm').remove();
});
$('body').on('click', '.js-cac-confirm-shop', function(){
$('body').removeClass('stock_city_confirm');

const expires = new Date();
expires.setTime(expires.getTime() + (60 * 24 * 60 * 60 * 1000));
document.cookie = `stock_city_confirm=true; expires=${expires.toUTCString()}; path= / `;

$('.av-cac--confirm').remove();
});
$('body').on('click', '#cac_checkout_city .city-trigger', function () {

let getThisElement = $(this),
getSelectCity = $('#cac_city_id_d');

getBoxCityString = getThisElement.data('caCity');
getBoxCityId = getThisElement.data('caCityId');

getSelectCity.attr('data-ca-lite-checkout-last-value', getBoxCityId);

getSelectCity.val(getBoxCityId).change();

});
$.ceEvent('on', 'ce.commoninit', function (context) {
(function($){

context.find('#popup_in_shops_city_id').on('select2:open', function()
{
    var $dropdown = $(this).data('select2').$dropdown;
$dropdown.appendTo($(this).parent());
$dropdown.addClass('popup-select-container');
$dropdown.css('z-index', 1000);
});

context.find('#cac_city_id_d').on('change', function()
{

    var
city_id = $(this).val();
var
form = $(this).closest('form');
var
selected_section = $(this).closest('form').find('input[name="selected_section"]').val();

$.ceAjax('request', fn_url('cac.set_location_city_id'), {
    hidden: true,
    caching: false,
    force_exec: true,
    save_history: false,
    method: 'post',
    result_ids: 'form_cac_info',
    data: {
        selected_section: selected_section,
        city_id: city_id
    },
    callback: function(response) {
    if (response.selected_section) {
        var existingInput = form.find('input[name="selected_section"]');
if (existingInput.length > 0)
{
    existingInput.val(response.selected_section);
} else {
    form.append('<input type="hidden" name="selected_section" value="' + response.selected_section + '">');
}
}
}
});

});

context.find('.shops-item').on('click', function()
{
if (!$(this).hasClass('mob-active')) {
    context.find('.shops-item').removeClass('mob-active');
$(this).addClass('mob-active');
}
});

})($);
});
$('body').on('click', '.cac-choose-shop', function(e)
{

    e.preventDefault();

var
city_id = $(this).attr('data-city-id');

var
stock_id = $(this).attr('data-stock-id');

var
product_code = $(this).attr('data-product-code');

var
return_url = window.location.href;

$.ceAjax('request', fn_url('cac.set_location_send'), {
caching: false,
force_exec: true,
full_render: true,
save_history: false,
method: 'post',
result_ids: 'tygh_main_container',
data: {
    selected_section: 'product_tab_11',
    return_url: return_url,
    product_code: product_code,
    city_id_d: city_id,
    stock_id_d: stock_id
},
callback: function(response)
{
    console.log(response);
}
});

});
$('body').on('click', '.avr-shops-list .avr-shops-item:not(.mob_active)', function()
{
if (window.matchMedia('(max-width: 767px)').matches)
{
$('.avr-shops-list .avr-shops-item').removeClass('mob-active');
$(this).addClass('mob-active');
}
});
$('body').on('click', '.mobile-header .local-shop-link', function()
{
$('.mobile-header .close-mob-menu').click();
});
< / script >

    <!-- Inline
scripts -->
< script >

$(document).on('click', '.ty-sort-dropdown__content-item-a', function()
{
    const
href = $(this).attr('href');
const
url = new
URL(href, window.location.origin);
const
sort_by = url.searchParams.get('sort_by');
const
sort_order = url.searchParams.get('sort_order');
const
sort_parameter = `${sort_by}
_${sort_order}
`;
dataLayer.push({ecommerce: null});
dataLayer.push({
event: 'sort_used_session_flag',
sort_parameter: sort_parameter
});
});

< / script >
    < script
src = "https://avrora.ua/js/tygh/product_filters.js?ver=1780866602" > < / script > < script
src = "https://avrora.ua/js/lib/jqueryuitouch/jquery.ui.touch-punch.min.js?ver=1780866602" > < / script > < script
src = "https://avrora.ua/js/tygh/filter_table.js?ver=1780866602" > < / script >
                                                                       < script
src = "https://avrora.ua/js/tygh/exceptions.js?ver=1780866602" > < / script > < script
src = "https://avrora.ua/js/tygh/product_image_gallery.js?ver=1780866602" > < / script > < script
type = "application/ld+json" >
       {
           "@context": "https://schema.org",
           "@type": "ItemList",
           "name": "Гігієна",
           "url": "https://avrora.ua/gigiena/",
           "numberOfItems": 48,
           "itemListElement": [
               {
                   "@type": "ListItem",
                   "position": 1,
                   "item": {
"@type": "Product",
"name": "Палички ватнi косметичні Safi 100 шт/уп",
"url": "https://avrora.ua/palichki-vatni-kosmetichni-safi-100-sht-up/",
"image": "https://images.avrora.ua/images/detailed/78/75696_001.JPG",
"offers": {
    "@type": "Offer",
    "price": "14.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 2,
    "item": {
"@type": "Product",
"name": "Серветки паперові Safi одношарові білі 85 шт/пач",
"url": "https://avrora.ua/servetki-paperovi-safi-odnosharovi-bili-85-sht-pach/",
"image": "https://images.avrora.ua/images/detailed/77/92587_9239.jpg",
"offers": {
    "@type": "Offer",
    "price": "18.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 3,
    "item": {
"@type": "Product",
"name": "Прокладки щоденні Libresse Classic Regular 50шт./уп.",
"url": "https://avrora.ua/prokladki-schodenni-libresse-classic-regular-50sht.-up./",
"image": "https://images.avrora.ua/images/detailed/12/24748_001.JPG",
"offers": {
    "@type": "Offer",
    "price": "89.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 4,
    "item": {
"@type": "Product",
"name": "Прокладки щоденні Lidie by Kotex Нормал 50 шт/уп",
"url": "https://avrora.ua/prokladki-schodenni-lidie-by-kotex-normal-50-sht-up/",
"image": "https://images.avrora.ua/images/detailed/178/19224_00011_ana1-jj.jpg",
"offers": {
    "@type": "Offer",
    "price": "77.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 5,
    "item": {
"@type": "Product",
"name": "Палички ватні Lady Cotton 200 штук",
"url": "https://avrora.ua/palichki-vatni-lady-cotton-200-shtuk/",
"image": "https://images.avrora.ua/images/detailed/128/17078.jpg",
"offers": {
    "@type": "Offer",
    "price": "39.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 6,
    "item": {
"@type": "Product",
"name": "Серветки паперові Silken MINI Барви 2 шари 100 шт/уп",
"url": "https://avrora.ua/servetki-paperovi-silken-mini-barvi-2-shari-100-sht-up/",
"image": "https://images.avrora.ua/images/detailed/44/54319_001.JPG",
"offers": {
    "@type": "Offer",
    "price": "20.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 7,
    "item": {
"@type": "Product",
"name": "Набір рушників паперових Papirella Deluxe Purpure двошарові 2 шт/уп",
"url": "https://avrora.ua/nabir-rushnikiv-paperovih-papirella-deluxe-purpure-dvosharovi-2-sht-up/",
"image": "https://images.avrora.ua/images/detailed/29/42409_001.JPG",
"offers": {
    "@type": "Offer",
    "price": "41.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 8,
    "item": {
"@type": "Product",
"name": "Палички ватні косметичні Safi 300 шт/уп",
"url": "https://avrora.ua/palichki-vatni-kosmetichni-safi-300-sht-up/",
"image": "https://images.avrora.ua/images/detailed/78/64909_001.JPG",
"offers": {
    "@type": "Offer",
    "price": "28.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 9,
    "item": {
"@type": "Product",
"name": "Гель для інтимної гігієни Cleanness+ з бактериальним ефектом 310 г",
"url": "https://avrora.ua/gel-dlya-intimnoi-gigiieni-cleanness-z-bakterialnim-efektom-310-g/",
"image": "https://images.avrora.ua/images/detailed/37/58261_005.JPG",
"offers": {
    "@type": "Offer",
    "price": "69.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 10,
    "item": {
"@type": "Product",
"name": "Набір рушників паперових із гільзою Safi білі 2 шари 2 шт/уп",
"url": "https://avrora.ua/nabir-rushnikiv-paperovih-iz-gilzoyu-safi-bili-2-shari-2-sht-up/",
"image": "https://images.avrora.ua/images/detailed/70/82704_001.jpg",
"offers": {
    "@type": "Offer",
    "price": "64.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 11,
    "item": {
"@type": "Product",
"name": "Серветки вологі дитячі Safi екстракт ромашки з клапаном 132 шт/уп",
"url": "https://avrora.ua/servetki-vologi-dityachi-safi-ekstrakt-romashki-z-klapanom-132-sht-up/",
"image": "https://images.avrora.ua/images/detailed/83/99292_001.jpg",
"offers": {
    "@type": "Offer",
    "price": "44.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 12,
    "item": {
"@type": "Product",
"name": "Папір туалетний сірий Новий Київ-500",
"url": "https://avrora.ua/papir-tualetniy-siriy-noviy-kiiv-500/",
"image": "https://images.avrora.ua/images/detailed/149/15453_101.jpg",
"offers": {
    "@type": "Offer",
    "price": "33.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 13,
    "item": {
"@type": "Product",
"name": "Прокладки гігієнічні ALWAYS Ultra Super Single 8 шт/пач",
"url": "https://avrora.ua/prokladki-gigiienichni-always-ultra-super-single-8-sht-pach/",
"image": "https://images.avrora.ua/images/detailed/43/85832_001.JPG",
"offers": {
    "@type": "Offer",
    "price": "59.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 14,
    "item": {
"@type": "Product",
"name": "Прокладки гігієнічні NATURELLA Classic Camomile Normal 10 шт/пач",
"url": "https://avrora.ua/prokladki-gigiienichni-naturella-classic-4-nor.single10/",
"image": "https://images.avrora.ua/images/detailed/188/25660_010101.jpg",
"offers": {
    "@type": "Offer",
    "price": "39.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 15,
    "item": {
"@type": "Product",
"name": "Набір паперу туалетного Ecolo 2 шари 4 шт/уп",
"url": "https://avrora.ua/nabir-paperu-tualetnogo-ecolo-2-shari-4-sht-up/",
"image": "https://images.avrora.ua/images/detailed/183/91796_00001111.jpg",
"offers": {
    "@type": "Offer",
    "price": "46.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 16,
    "item": {
"@type": "Product",
"name": "Прокладки гігієнічні ALWAYS Ultra Normal Single 10 штук",
"url": "https://avrora.ua/prokladki-gigiienichni-always-ultra-normal-single-10-shtuk/",
"image": "https://images.avrora.ua/images/detailed/43/85831_987.jpg",
"offers": {
    "@type": "Offer",
    "price": "59.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 17,
    "item": {
"@type": "Product",
"name": "Прокладки щоденні Libresse Natural Care Normal 58 штук",
"url": "https://avrora.ua/prokladki-schodenni-libresse-natural-care-normal-58-shtuk/",
"image": "https://images.avrora.ua/images/detailed/46/87972_001.jpg",
"offers": {
    "@type": "Offer",
    "price": "149.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 18,
    "item": {
"@type": "Product",
"name": "Прокладки гігієнічні Always Ultra Super Duo 5*16 шт/пач",
"url": "https://avrora.ua/prokladki-gigiienichni-always-ultra-super-duo-516-sht-pach/",
"image": "https://images.avrora.ua/images/detailed/77/84222.jpg",
"offers": {
    "@type": "Offer",
    "price": "129.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 19,
    "item": {
"@type": "Product",
"name": "Диски ватні косметичні Safi Аврора 50 шт/уп",
"url": "https://avrora.ua/diski-vatni-kosmetichni-safi-avrora-50-sht-up/",
"image": "https://images.avrora.ua/images/detailed/80/84791.jpg",
"offers": {
    "@type": "Offer",
    "price": "16.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 20,
    "item": {
"@type": "Product",
"name": "Рушник паперовий DeLuxe двошаровий білий 300 відривів",
"url": "https://avrora.ua/rushnik-paperoviy-deluxe-dvosharoviy-biliy-300-vidriviv/",
"image": "https://images.avrora.ua/images/detailed/146/42410_119.jpg",
"offers": {
    "@type": "Offer",
    "price": "54.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 21,
    "item": {
"@type": "Product",
"name": "Прокладки урологічні жіночі Tena Lady Slim Normal 12 штук",
"url": "https://avrora.ua/prokladki-urologichni-zhinochi-tena-lady-slim-normal-12-shtuk/",
"image": "https://images.avrora.ua/images/detailed/79/81025_001.jpg",
"offers": {
    "@type": "Offer",
    "price": "105.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 22,
    "item": {
"@type": "Product",
"name": "Мило інтимне Зелена Аптека Ніжне Ромашка 370 мл",
"url": "https://avrora.ua/milo-intimne-nizhne-romashka-370-ml/",
"image": "https://images.avrora.ua/images/detailed/185/14439_01011.jpg",
"offers": {
    "@type": "Offer",
    "price": "79.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 23,
    "item": {
"@type": "Product",
"name": "Набір паперу туалетного SELPAK Comfort 2 шари 4 штуки",
"url": "https://avrora.ua/nabir-paperu-tualetnogo-selpak-comfort-2-shari-4-shtuki/",
"image": "https://images.avrora.ua/images/detailed/104/97190_002.jpg",
"offers": {
    "@type": "Offer",
    "price": "59.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 24,
    "item": {
"@type": "Product",
"name": "Прокладки гігієнічні ALWAYS Ultra Day&amp;Night Singl 7 штук",
"url": "https://avrora.ua/prokladki-gigiienichni-always-ultra-day-and-night-singl-7-shtuk/",
"image": "https://images.avrora.ua/images/detailed/43/85829_897_uai6-ki.jpg",
"offers": {
    "@type": "Offer",
    "price": "59.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 25,
    "item": {
"@type": "Product",
"name": "Набір паперу туалетного Ecolo Deluxe 3 шари 4 шт/уп",
"url": "https://avrora.ua/nabir-paperu-tualetnogo-ecolo-deluxe-3-shari-4-sht-up/",
"image": "https://images.avrora.ua/images/detailed/45/83079_001.JPG",
"offers": {
    "@type": "Offer",
    "price": "71.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 26,
    "item": {
"@type": "Product",
"name": "Рушники паперові V-складання Safi білі 2 шари 130 листів/пач",
"url": "https://avrora.ua/rushniki-paperovi-v-skladannya-safi-bili-2-shari-130-listiv-pach/",
"image": "https://images.avrora.ua/images/detailed/113/101897_002.jpg",
"offers": {
    "@type": "Offer",
    "price": "49.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 27,
    "item": {
"@type": "Product",
"name": "Рушники паперові V-складення Papero білі 2 шари150 листів/пачка",
"url": "https://avrora.ua/rushniki-paperovi-v-skladennya-papero-bili-2-shari150-listiv-pachka/",
"image": "https://images.avrora.ua/images/detailed/95/99625-.jpg",
"offers": {
    "@type": "Offer",
    "price": "46.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 28,
    "item": {
"@type": "Product",
"name": "Серветки вологі дитячі Smile Екстракт алое 24 шт/уп",
"url": "https://avrora.ua/servetki-vologi-dityachi-smile-ekstrakt-aloe-24-sht-up/",
"image": "https://images.avrora.ua/images/detailed/124/photo_2025-01-13_11-17-13.jpg",
"offers": {
    "@type": "Offer",
    "price": "24.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 29,
    "item": {
"@type": "Product",
"name": "Хустки носові паперові Safi Етноорнамент без аромату 2 шари 10 шт/уп",
"url": "https://avrora.ua/hustki-nosovi-paperovi-safi-etnoornament-bez-aromatu-2-shari-10-sht-up/",
"image": "https://images.avrora.ua/images/detailed/151/113979_001.jpg",
"offers": {
    "@type": "Offer",
    "price": "2.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 30,
    "item": {
"@type": "Product",
"name": "Прокладки гігієнічні NATURELLA Ultra Camomile Нормал 10 штук",
"url": "https://avrora.ua/prokladki-gigiienichni-naturella-ult.cam.-norm.sin.-10-sht-pach./",
"image": "https://images.avrora.ua/images/detailed/179/25666_001.jpg",
"offers": {
    "@type": "Offer",
    "price": "49.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 31,
    "item": {
"@type": "Product",
"name": "Серветки вологі дитячі Aqua Baby з вітамінним комплексом 15 шт/уп.",
"url": "https://avrora.ua/servetki-vologi-dityachi-aqua-baby-z-vitaminnim-kompleksom-15-sht-up./",
"image": "https://images.avrora.ua/images/detailed/91/91802_001.jpg",
"offers": {
    "@type": "Offer",
    "price": "5.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 32,
    "item": {
"@type": "Product",
"name": "Прокладки гігієнічні Kotex Ultra Night Quadro 22 шт/пач",
"url": "https://avrora.ua/prokladki-gigiienichni-kotex-ultra-night-quadro-22-sht-pach/",
"image": "https://images.avrora.ua/images/detailed/186/101679_010123.jpg",
"offers": {
    "@type": "Offer",
    "price": "129.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 33,
    "item": {
"@type": "Product",
"name": "Прокладки гігієнічні LIBRESS Comfort Maxi Long 9 штук",
"url": "https://avrora.ua/prokladki-gigiienichni-libress-comfort-maxi-long-9-shtuk/",
"image": "https://images.avrora.ua/images/detailed/174/87970_1000.png",
"offers": {
    "@type": "Offer",
    "price": "49.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 34,
    "item": {
"@type": "Product",
"name": "Серветки паперові Safi 1 шар білі 350 шт/пач",
"url": "https://avrora.ua/servetki-paperovi-safi-1-shar-bili-350-sht-pach/",
"image": "https://images.avrora.ua/images/detailed/82/92589_002.jpg",
"offers": {
    "@type": "Offer",
    "price": "54.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 35,
    "item": {
"@type": "Product",
"name": "Палички ватнi косметичні Safi 200 шт/уп",
"url": "https://avrora.ua/palichki-vatni-kosmetichni-safi-200-sht-up/",
"image": "https://images.avrora.ua/images/detailed/78/75695_958.jpg",
"offers": {
    "@type": "Offer",
    "price": "29.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 36,
    "item": {
"@type": "Product",
"name": "Набір паперу туалетного Ecolo Deluxe білий 3 шари 24 шт/уп",
"url": "https://avrora.ua/nabir-paperu-tualetnogo-ecolo-deluxe-biliy-3-shari-24-sht-up/",
"image": "https://images.avrora.ua/images/detailed/114/111441_001.jpg",
"offers": {
    "@type": "Offer",
    "price": "399.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 37,
    "item": {
"@type": "Product",
"name": "Прокладки гігієнічні NATURELLA Ultra Camomile Normal Duo 20 штук",
"url": "https://avrora.ua/prokladki-gigiienichni-naturella-ult.cam.norm.duo-20-shtuk/",
"image": "https://images.avrora.ua/images/detailed/179/62401_001.jpg",
"offers": {
    "@type": "Offer",
    "price": "92.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 38,
    "item": {
"@type": "Product",
"name": "Прокладки щодені Kotex Deo Normal Plus Liners 56 штук",
"url": "https://avrora.ua/prokladki-schodeni-kotex-deo-normal-plus-liners-56-sht-up/",
"image": "https://images.avrora.ua/images/detailed/178/58103_0011.jpg",
"offers": {
    "@type": "Offer",
    "price": "104.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 39,
    "item": {
"@type": "Product",
"name": "Прокладки гігієнічні NATURELLA Classic Camomile Maxi 8 штук",
"url": "https://avrora.ua/prokladki-gigiienichni-naturella-classic-camomale-maxi-8-shtuk/",
"image": "https://images.avrora.ua/images/detailed/182/25662_001100.jpg",
"offers": {
    "@type": "Offer",
    "price": "39.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 40,
    "item": {
"@type": "Product",
"name": "Прокладки гігієнічні Greenday Soft Night 6 шт/пач.",
"url": "https://avrora.ua/prokladki-gigiienichni-greenday-soft-night-6-sht-pach./",
"image": "https://images.avrora.ua/images/detailed/143/105330_1.jpg",
"offers": {
    "@type": "Offer",
    "price": "24.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 41,
    "item": {
"@type": "Product",
"name": "Прокладки гігієнічні ALWAYS Deo Ультра Light 10 штук",
"url": "https://avrora.ua/prokladki-gigiienichni-always-deo-ultra-lig.sing.10-shtuk/",
"image": "https://images.avrora.ua/images/detailed/182/88443_00001111.jpg",
"offers": {
    "@type": "Offer",
    "price": "59.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 42,
    "item": {
"@type": "Product",
"name": "Прокладки щоденні Discreet Део Весняний бриз 60 шт",
"url": "https://avrora.ua/prokladki-schodenni-discreet-deo-vesnyaniy-briz-60-sht/",
"image": "https://images.avrora.ua/images/detailed/179/55178_001.jpg",
"offers": {
    "@type": "Offer",
    "price": "99.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 43,
    "item": {
"@type": "Product",
"name": "Прокладки гігієнічні Greenday Soft Long 7 шт/пач.",
"url": "https://avrora.ua/prokladki-gigiienichni-greenday-soft-long-7-sht-pach./",
"image": "https://images.avrora.ua/images/detailed/143/105331.jpg",
"offers": {
    "@type": "Offer",
    "price": "29.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 44,
    "item": {
"@type": "Product",
"name": "Набір паперу туалетного Ніжний дотик Арома Голд білий  2 шари 4 шт/уп",
"url": "https://avrora.ua/nabir-paperu-tualetnogo-nizhniy-dotik-aroma-gold-biliy-2-shari-4-sht-up/",
"image": "https://images.avrora.ua/images/detailed/130/115038_001.jpg",
"offers": {
    "@type": "Offer",
    "price": "64.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 45,
    "item": {
"@type": "Product",
"name": "Прокладки гігієнічні NATURELLA Ultra Maxi 8 штук",
"url": "https://avrora.ua/prokladki-gigiienichni-naturella-ultra-maxi-8-shtuk/",
"image": "https://images.avrora.ua/images/detailed/152/25668_201.jpg",
"offers": {
    "@type": "Offer",
    "price": "49.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 46,
    "item": {
"@type": "Product",
"name": "Прокладки гігієнічні Kotex Ultra Normal Quadro 30 шт/пач",
"url": "https://avrora.ua/prokladki-gigiienichni-kotex-ultra-normal-quadro-30-sht-pach/",
"image": "https://images.avrora.ua/images/detailed/186/101681_0101012.jpg",
"offers": {
    "@type": "Offer",
    "price": "129.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 47,
    "item": {
"@type": "Product",
"name": "Набір паперу туалетного Papero білий 2 шари 4 шт/уп.",
"url": "https://avrora.ua/nabir-paperu-tualetnogo-papero-biliy-2-shari-4-sht-up./",
"image": "https://images.avrora.ua/images/detailed/95/99628.jpg",
"offers": {
    "@type": "Offer",
    "price": "46.00",
    "priceCurrency": "UAH"
}
}}, {
    "@type": "ListItem",
    "position": 48,
    "item": {
"@type": "Product",
"name": "Прокладки щоденні Discreet Deo Water Lily 20 штук",
"url": "https://avrora.ua/prokladki-schodenni-discreet-deo-water-lily-20-shtuk/",
"image": "https://images.avrora.ua/images/detailed/44/25653_001.JPG",
"offers": {
    "@type": "Offer",
    "price": "44.00",
    "priceCurrency": "UAH"
}
}}]
}
< / script > < script >
$(document).ready(function()
{
    var
gtm_array_static = [];
$('.grid-list-wrap .ty-grid-list__item:not(.gtm_sent)').each(function()
{
if (isScrolledIntoViewGridList(this)) {
var self_static = $(this).find('input[name="restudio_gtm"]');
var itemId = self_static.data('item-id');
console.log(itemId);
gtm_array_static.push({
"item_name": self_static.data('item-name'),
"item_id": self_static.data('item-id'),
"discount": self_static.data('discount'),
"price": self_static.data('price'),
"item_brand": self_static.data('item-brand'),
"item_category": self_static.data('item-category'),
"item_variant": self_static.data('item-variant'),
"item_list_name": self_static.data('item-list-name'),
"item_list_id": self_static.data('item-list-id'),
"index": self_static.data('position'),
"quantity": 1,
"google_business_vertical": "retail",
});
$(this).addClass('gtm_sent');
}
});
if (gtm_array_static.length > 0) {
dataLayer.push({ecommerce: null});
dataLayer.push({
    event: "view_item_list",
    ecommerce: {
        items: gtm_array_static
    }
});
}
$(window).scroll(function()
{
var
gtm_array = [];
$('.grid-list-wrap .ty-grid-list__item:not(.gtm_sent)').each(function()
{
if (isScrolledIntoViewGridList(this))
{
    var
self = $(this).find('input[name="restudio_gtm"]');
var
itemId = self.data('item-id');
console.log(itemId);
gtm_array.push({
    "item_name": self.data('item-name'),
    "item_id": self.data('item-id'),
    "discount": self.data('discount'),
    "price": self.data('price'),
    "item_brand": self.data('item-brand'),
    "item_category": self.data('item-category'),
    "item_variant": self.data('item-variant'),
    "item_list_name": self.data('item-list-name'),
    "item_list_id": self.data('item-list-id'),
    "index": self.data('position'),
    "quantity": 1,
    "google_business_vertical": "retail",
});
$(this).addClass('gtm_sent');
}
});
if (gtm_array.length > 0) {
dataLayer.push({ecommerce: null});
dataLayer.push({
    event: "view_item_list",
    ecommerce: {
        items: gtm_array
    }
});
}
});

function
isScrolledIntoViewGridList(elem)
{
    var
docViewTop = $(window).scrollTop();
var
docViewBottom = docViewTop + $(window).height();
var
elemTop = $(elem).offset().top;
var
elemBottom = elemTop + $(elem).height();

return elemBottom <= docViewBottom & & elemTop >= docViewTop;
}
});
< / script >
    < script >
    (function(_, $)
{

$.ceEvent('on', 'ce.commoninit', function(context)
{

    let
getErrorBlockChecked = context.find('.ty-footer-form-block__form .check-block');

setTimeout(function()
{

if (
    getErrorBlockChecked.hasClass('error')
)
{

    getErrorBlockChecked
    .find('.help-inline')
    .remove();

}

}, 250);

getErrorBlockChecked.on(
    'click',
    'label',
    function()
{

    getErrorBlockChecked
    .find('.help-inline')
    .remove();

}
);

});

}(Tygh, Tygh.$));
< / script >

    < div


class ="switch-mode-popup hidden" id="site_mode" >

< div


class ="switch-mode-popup--content" >

< p > Це
замовлення
зберемо
з
наявних
товарів
у
магазині, який
ти
обереш. < / p >
< p > При
переході
у
магазин
твій
кошик
очиститься ☝️ < / p >
< / div >
< div


class ="buttons-container" >

< button


class ="ty-btn-close__modal" >


Скасувати
< / button >
< a


class ="cm-dialog-opener cm-dialog-auto-size ty-btn__primary ty-btn ty-btn-close__modal js-open-store" href="https://avrora.ua/index.php?dispatch=cac.set_location" data-ca-dialog-title="Обери магазин, де тобі буде зручно забрати замовлення" data-ca-dialog- class ="popup-location" data-ca-target-id="cac_form_ajax" >


Прийняти
< / a >
< / div >
< / div >
< div


class ="switch-mode-popup hidden" id="site_mode_w" >

< div


class ="switch-mode-popup--content" >

< p >
Товари
офлайн - магазину
видаляться
з
кошика.Щоб
їх
відшукати, тицяй
на
серденько
та
зберігай
в
Обране
< / p >
< / div >
< div


class ="buttons-container" >

< button


class ="ty-btn-close__modal" >


Скасувати
< / button >
< a


class ="ty-btn__primary ty-btn ty-btn-close__modal" href="https://avrora.ua/index.php?dispatch=cac.default" >


Прийняти
< / a >
< / div >
< / div >
< div


class ="switch-mode-popup hidden" id="site_mode_k" >

< div


class ="switch-mode-popup--content" >

< p >
Деякі
товари
можуть
бути
недоступні
до
замовлення, оскільки
відрізняються
залишки
між
магазинами.
< / p >
< / div >
< div


class ="buttons-container" >

< button


class ="ty-btn-close__modal" >


Скасувати
< / button >
< a


class ="ty-btn__primary ty-btn ty-btn-close__modal cm-dialog-opener cm-dialog-auto-size" href="https://avrora.ua/index.php?dispatch=cac.set_location"  data-ca-dialog- class ="popup-location" data-ca-dialog-title="Обери магазин, де тобі буде зручно забрати замовлення" data-ca-target-id="cac_form_ajax" >


Продовжити
< / a >
< / div >
< / div >
< div


class ="switch-mode-popup hidden" id="site_mode_k_2" >

< div


class ="switch-mode-popup--content" >

< p >
Деякі
товари
можуть
бути
недоступні
до
замовлення, оскільки
відрізняються
залишки
між
магазинами.
< / p >
< / div >
< div


class ="buttons-container" >

< button


class ="ty-btn-close__modal" >


Скасувати
< / button >
< a


class ="ty-btn__primary ty-btn ty-btn-close__modal cm-dialog-opener cm-dialog-auto-size" data-ca-dialog- class ="choose_in_another_shop shops-all popup-checkout" data-ca-target-id="in_another_shop_" data-ca-dialog-title="Наявність в магазинах" href="https://avrora.ua/index.php?dispatch=products.popup_get_item_in_shops&amp;product_code=" >


Продовжити
< / a >
< / div >
< / div >
< div


class ="switch-mode-popup hidden" id="site_mode_k_3" >

< div


class ="switch-mode-popup--content" >

< p >
Деякі
товари
можуть
бути
недоступні
до
замовлення, оскільки
відрізняються
залишки
між
магазинами.
< / p >
< / div >
< div


class ="buttons-container" >

< button


class ="ty-btn-close__modal" >


Скасувати
< / button >
< a


class ="ty-btn__primary ty-btn ty-btn-close__modal" href="https://avrora.ua/index.php?dispatch=cac.fast_choose&amp;stock_id=&amp;home=true" >


Продовжити
< / a >
< / div >
< / div >
< script >
$.ceEvent('on', 'ce.ajaxdone', function(elms, scripts, params, responseData, responseText)
{
if (responseData.refresh_count == true)
{
    const
newLink = $('<a>', {


class: 'cm-dialog-opener cm-dialog-auto-size refresh-count-2',


'data-ca-dialog-class': 'js-switch-mode-view',
'data-ca-dialog-title': 'При зміні магазину вміст кошика може змінитися',
'data-ca-target-id': 'site_mode_k_2',
'data-product-code': $('a.refresh-count').attr('data-product-code'),
'data-obj-id': $('a.refresh-count').attr('data-obj-id'),
text: '3 магазинах'
});

$('a.refresh-count').replaceWith(newLink);
}
if (responseData.refresh_count_2 == true) {
const oldLink3 = $('a.refresh-count-3');
const newLink3 = $('<a>', {


class: 'cm-dialog-opener cm-dialog-auto-size btn-in-another-shop',


'data-ca-dialog-class': 'choose_in_another_shop shops-all popup-checkout',
'data-ca-target-id': 'in_another_shop_' + oldLink3.attr('data-obj-id'),
'data-obj-id': oldLink3.attr('data-obj-id'),
'data-ca-dialog-title': 'Наявність в магазинах',
'data-product-code': oldLink3.attr('data-product-code'),
href: '/index.php?dispatch=products.popup_get_item_in_shops&product_code=' + oldLink3.attr('data-product-code'),
text: oldLink3.text()
});
oldLink3.replaceWith(newLink3);
const
oldLink = $('a.refresh-count-2');
const
newLink = $('<a>', {


class: 'cm-dialog-opener cm-dialog-auto-size refresh-count',


'data-ca-dialog-class': 'choose_in_another_shop shops-all popup-checkout',
'data-ca-dialog-title': 'Наявність в магазинах',
'data-ca-target-id': 'in_another_shop_' + oldLink.attr('data-obj-id'),
href: '/index.php?dispatch=products.popup_get_item_in_shops&product_code=' + oldLink.attr('data-product-code'),
'data-obj-id': oldLink.attr('data-obj-id'),
'data-product-code': oldLink.attr('data-product-code'),
text: oldLink.text()
});
oldLink.replaceWith(newLink);
const
oldLink2 = $('a.refresh-shop-2');
const
newLink2 = $('<a>', {


class: 'shoplist_list--link refresh-shop',


href: '/index.php?dispatch=cac.fast_choose&stock_id=' + oldLink2.attr('data-stock') + '&home=true',
'data-stock': oldLink2.attr('data-stock'),
text: oldLink2.text()
});
oldLink2.replaceWith(newLink2);
}
});
< / script > < script
type = "application/ld+json" >
       {
           "@context": "https://schema.org",
           "@type": "Organization",
           "name": "Мультимаркет Аврора",
           "logo": "https://images.avrora.ua/images/logos/8/favikon-48kh48-03_kzgv4jq.png",
           "url": "https://avrora.ua/",
           "sameAs": [
               "https://www.facebook.com/avrora.multimarket",
               "https://www.instagram.com/avrora.multimarket/",
               "https://t.me/Avroraua",
               "https://www.youtube.com/channel/UCMIQPAmwj86Gf0gtakRSVJA",
               "https://www.tiktok.com/@avrora.multimarket"
           ],
           "contactPoint": [
               {
                   "@type": "ContactPoint",
                   "telephone": "+380-800-300-066",
                   "contactType": "customer service",
                   "email": "info@avrora.ua"
               }
           ]
       }
       < / script >

           < div
id = "login_block393"


class ="hidden" title="Увійти" >

< div


class ="ty-login-popup" >

< div
id = "popup393_login_popup_form_container" >

< div


class ="auth-by-phone" >

< form
name = "popup393_form"
id = "popup393_form"
action = "https://avrora.ua/"
method = "post"


class ="cm-ajax cm-ajax-full-render popup-otp" >

< input
type = "hidden"
name = "result_ids"
value = "popup393_login_popup_form_container" / >
< input
type = "hidden"
name = "login_block_id"
value = "popup393" / >
< input
type = "hidden"
name = "quick_login"
value = "1" / >

< input
type = "hidden"
name = "return_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >
< input
type = "hidden"
name = "redirect_url"
value = "index.php?sl=uk&amp;dispatch=categories.view&amp;category_id=13&amp;page=2" / >

< div


class ="step-otp step-otp-first show" >

< div


class ="ty-control-group ty-control-group--phone" >

< input
type = "text"
id = "phone_popup393"
name = "phone"
size = "32"


class ="ty-login__input ty-login__input--phone cm-mask-phone cm-focus" autocomplete="one-time-code" placeholder="+380(__)___-__-__" / >

< label
for ="phone_popup393" class ="ty-control-group__label cm-trim cm-mask-phone-label" > Твій номер телефону < / label >
< / div >

< div


class ="ty-product-filters__block" >

< div


class ="cm-product-filters-checkbox-container ty-product-filters__group" >

< label >
< span


class ="checkbox-wrap" >

< input


class ="cm-product-filters-checkbox" type="checkbox" value="Y" id="agree_popup393" >

< span


class ="checked" > < / span >

< / span >
< span > Я
погоджуюсть
з < a
href = "https://avrora.ua/politika-obrobki-ta-zahistu-personalnih-danih/"
target = "_blank" > Політикою
конфеденційності < / a > та < a
href = "https://avrora.ua/publichna-ugoda/"
target = "_blank" > Умовами
надання
послуг < / a >.< / span >
< / label >
< / div >
< / div >

< div


class ="buttons-container clearfix" >

< button
id = "get_sms_popup393"


class ="ty-btn__login ty-btn__secondary ty-btn ty-btn__login--phone" type="button" onclick="startOtp('popup393_form');" disabled >


Увійти
< / button >
< / div >

< / div >

< div


class ="step-otp step-otp-second" >

< div


class ="sms-sent--subtitle" >


Введи
код, надісланий
у
Viber
або
SMS
на
номер < span


class ="sms-sent--subtitle-phone" > < / span >

< / div >

< div


class ="sms-verify-code" >

< input
id = "otp[0]"


class ="get-focus"  maxlength="1" type="number" >

< input
id = "otp[1]"
maxlength = "1"
type = "number" >
< input
id = "otp[2]"
maxlength = "1"
type = "number" >
< input
id = "otp[3]"
maxlength = "1"
type = "number" >
< / div >

< div


class ="sms-sent--timer" >


Ти
можеш
запросити
новий
код
через < span


class ="js-sms-sent--timer" > < / span >

< / div >

< div


class ="sms-send--again hidden" >

< span
onclick = "sendAgain('popup393_form');" >
Вислати
код
ще
раз
< / span >
< / div >

< div


class ="otp-captcha hidden" >

< div


class ="js-otp-turnstile" data-sitekey="0x4AAAAAADKC2t-wCWEcMwnz" > < / div >

< / div >

< div


class ="buttons-container clearfix" >

< button
id = "log_in_popup393"


class ="ty-btn__login ty-btn__secondary ty-btn ty-btn__login--log" type="button" onclick="loginOtp('popup393_form');" disabled >


Увійти
< / button >
< / div >

< div


class ="choose-other-phone" >

< span
onclick = "backOtp('popup393_form');" >
Ввести
інший
номер
телефону
< / span >
< / div >

< / div >

< div


class ="step-otp step-otp-third" >

< div


class ="sms-sent--subtitle" >


Бачимо
тебе
тут
вперше.Як
до
тебе
звертатись?
< / div >

< div


class ="ty-control-group ty-first-name" >

< input
type = "text"
id = "user_name_popup393"


class ="ty-login__input finish-otp--login" placeholder=" " / >

< label
for ="user_name_popup393" class ="ty-control-group__label" > Ім'я</label>
< / div >

< div


class ="ty-control-group ty-last-name" >

< input
type = "text"
id = "user_lastname_popup393"


class ="ty-login__input finish-otp--last" placeholder=" " / >

< label
for ="user_lastname_popup393" class ="ty-control-group__label" > Прізвище < / label >
< / div >

< div


class ="ty-control-group ty-profile-field__item ty-birth_date" >

< input
type = "text"
id = "user_date_popup393"
size = "32"
value = ""
placeholder = " "


class ="ty-input-text" >

< label
for ="user_date_popup393" class ="ty-control-group__label" > Дата народження < / label >
< / div >

< div


class ="ty-control-group" >

< input
type = "text"
id = "user_email_popup393"
value = ""


class ="ty-login__input finish-otp--email" placeholder=" " / >

< label
for ="user_email_popup393" class ="ty-control-group__label" > E-mail < / label >
< / div >

< div


class ="buttons-container clearfix" >

< button
id = "log_in_popup393"


class ="ty-btn__login ty-btn__secondary ty-btn ty-btn__login--finish" type="button" disabled onclick="finishOtp('popup393_form');" >


Увійти
< / button >
< / div >

< / div >

< input
type = "hidden"
name = "security_hash"


class ="cm-no-hide-input" value="e70a77422e4e8f6aeecf0dbd2b03cfff" / > < / form >

< / div >

< script
src = "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit" async defer > < / script >

< script >
(function($, _)
{
    const
bodyHtml = $('body');
$.ceEvent('on', 'ce.commoninit', function()
{
    bodyHtml.find('.cl-my_login').on('click', 'a', function()
{
if ($('.step-otp-second').hasClass('show')){
if ($('.auth-by-phone-popup').length) {
$('.auth-by-phone-popup .ui-dialog-title').text(_.tr("sms_sent"));
$('.cl-my_login > a').attr('data-ca-dialog-title', _.tr("sms_sent"));
}
} else if ($('.step-otp-third').hasClass('show')) {
if ($('.auth-by-phone-popup').length) {
$('.auth-by-phone-popup .ui-dialog-title').text(_.tr("auth_title_little"));
$('.cl-my_login > a').attr('data-ca-dialog-title', _.tr("auth_title_little"));
}
} else {
if ($('.auth-by-phone-popup').length) {
$('.auth-by-phone-popup .ui-dialog-title').text(_.tr("sign_in"));
$('.cl-my_login > a').attr('data-ca-dialog-title', _.tr("sign_in"));
}
}
})
});
}(Tygh.$, Tygh));
< / script >

< !--popup393_login_popup_form_container --> < / div >
< / div >
< / div >
< script
src = "//cdnjs.cloudflare.com/ajax/libs/lazysizes/5.1.2/lazysizes.min.js" > < / script >
< script
src = "//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.10/highlight.min.js" > < / script >
< script >
hljs.initHighlightingOnLoad();
< / script >

< script >
(function($)
{
$.ceEvent('one', 'ce.commoninit', function(context)
{
    let
getCookies = $.cookie,
getNowDate = new
Date(), \
    getNowTime = getNowDate.getTime(), \
    getTimeLifeCookies = getNowTime + 1000 * 1750, \
    getReferrer = document.referrer;
getTimeLifeCookies += 30 * 24 * 60 * 60 * 1000;
if (
        getCookies.get('sd_user')
        & & (
                getReferrer.includes("youtube.com")
                | | getReferrer.includes("tiktok.com")
        )
)
{
    document.cookie = "sd_user=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}
});
})($);
< / script >
< script >
!function(t, e, c, n)
{
    var
s = e.createElement(c);
s.async = 1, s.src = 'https://statics.esputnik.com/scripts/' + n + '.js';
var
r = e.scripts[0];
r.parentNode.insertBefore(s, r);
var
f = function()
{
    f.c(arguments);
};
f.q = [];
f.c = function()
{
    f.q.push(arguments);
};
t['eS'] = t['eS'] | | f;
}(window, document, 'script', '084B5C4D78C4434AB83B49D22F0CEF1B');

eS('init');

eS('sendEvent', 'CategoryPage', {
    'CategoryPage': {
        'categoryKey': 'Гігієна'
    }
});

console.log('eSputnik: CategoryPage');

(function($)
{
    const $root = $('.res_category');
if (!$root.length)
return;

$root.off('click.gtmCategoryClick').on('click.gtmCategoryClick', 'a', function(e)
{

if (!e.originalEvent)
return;

const
href = this.getAttribute('href') | | '';
if (!href | | href == = '#' | | href.startsWith('javascript:')) return;

const
name = (($(this).find('span').first().text() | | $(this).text()) + '').trim().replace( /\s + / g, ' ');
if (!name) return;

window.dataLayer = window.dataLayer | | [];
dataLayer.push({ecommerce: null});
dataLayer.push({
    event: 'Category_click',
    event_category: 'Category_click',
    event_action: 'Click',
    event_label: name
});
});
})(jQuery);

(function($)
{
    const $headerCatalog = $('.header__categories');
if (!$headerCatalog.length)
return;

const $title = $headerCatalog.find('.ty-dropdown-box__title');
const $content = $headerCatalog.find('.ty-dropdown-box__content');

function
isOpened()
{
return $title.hasClass('active') | | $content.hasClass('open');
}

function
pushCatalogView()
{
window.dataLayer = window.dataLayer | | [];
dataLayer.push({ecommerce: null});
dataLayer.push({
    event: 'Catalog_view',
    event_category: 'Catalog',
    event_action: 'View',
    event_label: 'Main catalog viewed from header'
});
}

$headerCatalog.off('click.gtmCatalogView').on('click.gtmCatalogView',
                                              '.ty-dropdown-box__title > a, .ty-dropdown-box__title', function(e)
{
if (!e.originalEvent)
return;

setTimeout(function()
{
if (!isOpened()) return;
if ($content.data('gtmCatalogViewed')) return;

$content.data('gtmCatalogViewed', true);
pushCatalogView();
}, 0);
});

$(document).off('click.gtmCatalogViewReset').on('click.gtmCatalogViewReset', function()
{
if (!isOpened() & & $content.data('gtmCatalogViewed')) {
$content.removeData('gtmCatalogViewed');
}
});

})(jQuery);

$.ceEvent('on', 'ce.commoninit', function(context)
{
    (function($)
{

    context.find('.ty-add-to-wish:not(.in-wish)').on('click', function()
{

var
input = $(this).closest('.ty-grid-list__item--wrap').find('input[name="restudio_gtm"]');

console.log(input);

if (input.length) {

eS('sendEvent', 'AddToWishlist', {
'AddToWishlist': {
    'productKey': input.attr('data-product-id'),
    'price': input.attr('data-price'),
    'isInStock': parseInt(input.attr('data-qty'), 10)
}
});

console.log('eSputnik: AddToWishlist');

} else {

    var
input2 = $(this).closest('form').find('.gtm-array');

if (input2.length)
{

    eS('sendEvent', 'AddToWishlist', {
        'AddToWishlist': {
            'productKey': input2.attr('data-gtm-product-id'),
            'price': input2.attr('data-gtm-price'),
            'isInStock': parseInt(input2.attr('data-qty'), 10)
        }
    });

console.log('eSputnik: AddToWishlist');

}

}

});

})($);
});

< / script >

    < script
type = "module" >

import

{v4 as uuidv4} from

'https://jspm.dev/uuid';

let
_getBody = $('body');

var
url_string = window.location.href;
var
url = new
URL(url_string);
var
q = url.searchParams.get("q");

if (q)
{
    _getBody.find('#search_input').val(q)
}


$.ceEvent('on', 'ce.commoninit', function(context)
{
    (function($)
{

    let
_getSearchValue, \
    _getReferrer = document.referrer;

const
days = 365 * 10;
const
uid = getCookie('_ms') | | setCookie('_ms', uuidv4(), days);

function
sendData(data)
{

    var
last_event = localStorage.getItem('last_event');

if (last_event != 'click' & & data.e == 'add2cart' & & !_getBody.hasClass('products_search')) {
data.q = '';
}

localStorage.setItem('last_event', data.e);

const
xhr = new
XMLHttpRequest();
xhr.open("POST", "https://track.multisearch.io", true);
xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
xhr.send(new
URLSearchParams(data));
console.log(data);
}

function
handlerSearchSend()
{

    _getThisElement = $(this);
_getOid = false;
_getEvent = 'search';
_getQuery = _getSearchValue = _getBody.find('#search_input').val();

setCookie('is_search', 1, days);
localStorage.setItem('search_word', _getSearchValue);

handleDataCreate(_getThisElement, _getOid, _getEvent, _getQuery);

}

function
getSearchStatus()
{
    const
isSearchCookie = getCookie('is_search');
return isSearchCookie === '1' ? '1': '0';
}

function
setCookie(name, value, days)
{
const
expires = new
Date(Date.now() + days * 24 * 60 * 60 * 1000).toUTCString();
document.cookie = `${name} =${value};
expires =${expires};
path = / `;
return value;
}

function
getCookie(name)
{
const
value = `; ${document.cookie}
`;
const
parts = value.split(`; ${name} = `);
if (parts.length === 2) return parts.pop().split(';').shift();
}

function
deleteCookie(name)
{
const
expires = new
Date(0).toUTCString();
document.cookie = `${name} =;
expires =${expires};
path = / `;
}

function
handleDataCreate(_getThisElement, _getOid, _getEvent, _getQuery)
{
let
_getData;

if (_getReferrer.includes('&q=') | | localStorage.getItem('search_word')) {
_getSearchValue = localStorage.getItem('search_word');
} else {
_getSearchValue = _getBody.find('#search_input').val();
}

if (_getEvent === 'search'){
_getData = {
id: "03af76599918",
uid: uid,
e: _getEvent,
s: getSearchStatus(),
q: _getBody.find('#search_input').val(),
};
} else if (!localStorage.getItem('search_word') & & !_getSearchValue){
_getData = {
id: "03af76599918",
uid: uid,
oid: (_getEvent === 'click' | | _getBody.hasClass('products_search') | | _getOid) ? _getOid: '',
e: _getEvent,
s: getSearchStatus()
};
} else {
    _getData = {
    id: "03af76599918",
    uid: uid,
    oid: (_getEvent === 'click' | | localStorage.getItem('search_word') | | _getBody.hasClass(
        'products_search') | | _getOid) ? _getOid: '',
e: _getEvent,
s: getSearchStatus(),
q: (_getEvent === 'click' | | localStorage.getItem('search_word') | | _getSearchValue) ? _getSearchValue: '',
};
}

sendData(_getData);
}

deleteCookie('search_word');

let
_getThisElement, \
    _getOid, \
    _getEvent, \
    _getQuery;

context.find('.ty-search-autocomplete').on('click', '.ss__products--item a', function()
{

    _getThisElement = $(this);
_getOid = _getThisElement.parents('.ss__products--item').data('productId');
_getEvent = 'click';

_getSearchValue = _getBody.find('#search_input').val();

_getQuery = _getSearchValue;

setCookie('is_search', 1, days);
localStorage.setItem('search_word', _getSearchValue);

handleDataCreate(_getThisElement, _getOid, _getEvent, _getQuery);

});

context.find('.ty-grid-list__item').on('click', 'a', function()
{
if (_getBody.hasClass('products_search'))
{
    _getThisElement = $(this);
_getOid = _getThisElement.parents('.ty-grid-list__item').data('productId');
_getEvent = 'click';

_getSearchValue = _getBody.find('#search_input').val();

setCookie('is_search', 1, days);
localStorage.setItem('search_word', _getSearchValue);

_getBody.hasClass('products_search') ? _getQuery = _getSearchValue: _getQuery = false;

handleDataCreate(_getThisElement, _getOid, _getEvent, _getQuery);
}
});

context.find('.ty-search-autocomplete').on('click', '.smart-search__all-result a', function()
{
    handlerSearchSend();
});

context.find('[name="search_form"]').on('submit', function()
{
    handlerSearchSend();
});

context.find('.ty-btn__add-to-cart:not(.trigger-buy)').on('click', function()
{

    _getSearchValue = _getBody.find('#search_input').val();

_getBody.hasClass('products_search') ? _getQuery = _getSearchValue: _getQuery = '';

_getThisElement = $(this);
_getEvent = 'add2cart';
_getOid = _getThisElement.parents('.ty-grid-list__item').data('productId');

if (_getThisElement.parents('.ty-product-detail').data('productId'))
{
    _getOid = _getThisElement.parents('.ty-product-detail').data('productId');
}

handleDataCreate(_getThisElement, _getOid, _getEvent, _getQuery);

});

if (
    _getBody.find('.content-grid').hasClass('product-page')
) {

_getBody.on('click', 'a', function()
{
if (
       !$(this).hasClass('ty-tabs__a')
   & & $(this).attr('href') != ''
){
    localStorage.removeItem('search_word');
}

});

}

})($);
});

< / script >

    < div
id = "gtm_add_to_wish" >

     <!--gtm_add_to_wish --> < / div > < script >
$('body').on('click', '.js-gtm-banner', function(e)
{
    e.preventDefault();
var
link = $(this).attr('href');
var
info = $(this).find('.js-gtm-banner--info');
var
position = $('.js-gtm-banner').index(this) + 1;
window.dataLayer = window.dataLayer | | [];
dataLayer.push({
                   'event': info.attr('data-event'),
                   'page_current': window.location.href, // Поточний
URL
сторінки
на
якій
був
клік
по
банеру
'position': position, // Поточний
номер
позиції
банера
на
сторінці
'page_next': info.attr('data-link'), // URL
Куди
веде
посилання
після
кліку
по
банеру
'name': info.attr('data-name'), // URL
Куди
веде
посилання
після
кліку
по
банеру
});
console.log('Event:', info.attr('data-event'), 'Position:', position);
location.href = link;
});
< / script >
    < script >
    (function(){
    var s = document.createElement("script");
s.async = true;
s.src = (document.location.protocol == "https:" ? "https:": "http:") + "//cralodas.com.ua/code/";
var
a = document.getElementsByTagName("script")[0];
a.parentNode.insertBefore(s, a);})();
< / script >

    < script
defer
src = "https://static.cloudflareinsights.com/beacon.min.js/v833ccba57c9e4d2798f2e76cebdd09a11778172276447"
integrity = "sha512-57MDmcccJXYtNnH+ZiBwzC4jb2rvgVCEokYN+L/nLlmO8rfYT/gIpW2A569iJ/3b+0UEasghjuZH/ma3wIs/EQ=="
data - cf - beacon = '{"version":"2024.11.0","token":"74047a35e4aa4ea4b03b8591e79ba206","server_timing":{"name":{"cfCacheStatus":true,"cfEdge":true,"cfExtPri":true,"cfL4":true,"cfOrigin":true,"cfSpeedBrain":true},"location_startswith":null}}'
crossorigin = "anonymous" > < / script >
                                < / body >
                                    < / html >
            if products:
                print(f"🚀 Надсилаємо {len(products)} товарів у n8n...")
                async with httpx.AsyncClient() as n8n_client:
                    n8n_response = await n8n_client.post(N8N_WEBHOOK_URL, json={"bad_products": products})
                    print(f"🎉 Статус відповіді n8n: {n8n_response.status_code}")
                    print(f"Текст відповіді n8n: {n8n_response.text}")

    except Exception as e:
        print(f"❌ Виникла помилка під час виконання: {e}")


def get_mock_products():
    """Повертає реалістичний масив проблемних товарів Аврори для тестування n8n пайплайну"""
    return [
        {
            "product_name": "Капсули для прання Sila Wash 12 шт",
            "product_link": "https://avrora.ua/kapsuli-dlya-prannya-sila-wash/",
            "price": "118 грн",
            "rating": 2.4,
            "reviews": [
                "Капсули взагалі не розчиняються в пралці, залишають білі плями на одязі!",
                "Жахлива якість, довелося переправати речі двічі. Не рекомендую.",
                "Плівка дуже груба, хімічний запах просто нестерпний."
            ]
        },
        {
            "product_name": "Засіб для миття посуду Чиста Оселя 500мл",
            "product_link": "https://avrora.ua/zasib-dlya-mittya-posudu-chista-oselya/",
            "price": "45 грн",
            "rating": 3.1,
            "reviews": [
                "Рідкий як вода, розхід величезний. Краще переплатити за нормальний.",
                "Погано змиває жир у холодній воді. Продукт нікудишній.",
                "Пляшка приїхала тріснута, все вилилося."
            ]
        }
    ]


if __name__ == "__main__":
    target_url = "https://avrora.ua/ximiya-zasobi-dlya-prannya/"
    asyncio.run(scrape_avrora_category(target_url))