"""
   https://www.freeformatter.com/html-formatter.html#google_vignette

   <article class="kt-post-card kt-post-card--outlined kt-post-card--has-chat kt-post-card">
      <a class="kt-post-card__action" href="/v/اکسیژن-ساز-اجاره-ای-سوشیا-۱۰-لیتری-فروش-خرید/wZ_0UJa7">
         <div class="kt-post-card__body">
            <div class="kt-post-card__info">
               <h2 class="kt-post-card__title">اکسیژن ساز اجاره ای سوشیا ۱۰ لیتری فروش خرید</h2>
               <div class="kt-post-card__description">کارکرده</div>
               <div class="kt-post-card__description">۲۷,۰۰۰,۰۰۰ تومان</div>
               <div class="kt-post-card__bottom"><span class="kt-post-card__red-text">پله شده | فروشگاه</span><span class="kt-post-card__bottom-description kt-text-truncate" title="در نواب">در نواب</span></div>
            </div>
            <div class="kt-post-card__features"><i class="kt-icon kt-icon-chat-bubble" title="با امکان چت"></i></div>
            <div class="kt-post-card-thumbnail">
               <div>
                  <picture class="kt-image-block kt-image-block--radius-sm" style="padding-bottom: 100%;"><img decoding="auto" fetchpriority="auto" class="kt-image-block__image kt-image-block__image--fading kt-image-block__image--lazy-loaded" data-src="https://s100.divarcdn.com/static/photo/afra/webp_thumbnail/_0rPJAVytXCXJ_Jc5dljgg/b6415f05-2039-40c1-9468-0d60a0be6d15.webp" src="https://s100.divarcdn.com/static/photo/afra/webp_thumbnail/_0rPJAVytXCXJ_Jc5dljgg/b6415f05-2039-40c1-9468-0d60a0be6d15.webp" alt="اکسیژن ساز اجاره ای سوشیا ۱۰ لیتری فروش خرید"></picture>
               </div>
               <div data-has-skeleton="true" class="kt-tag kt-tag--overlay kt-tag--small kt-post-card-thumbnail__tag"><i class="kt-icon kt-icon--xs kt-tag__icon" style="background-image: url(&quot;https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/stairs.png&quot;);"></i><span data-has-skeleton="true" class="kt-tag__text kt-text-truncate">پله</span></div>
            </div>
         </div>
      </a>
   </article>

"""


import requests
from bs4 import BeautifulSoup

# ارسال درخواست به همراه User-Agent برای جلوگیری از بلاک شدن
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# url = "https://divar.ir/s/mashhad"
# url = "https://divar.ir/s/tehran"
url = "https://divar.ir/s/tehran?q=%D8%AA%D9%88%D8%A7%D9%81%D9%82%DB%8C"

response = requests.get(url, headers=headers)

# بررسی موفقیت دریافت اطلاعات
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # پیدا کردن تمام آگهی‌ها
   #  ads = soup.find_all('article')
    ads = soup.find_all('article', class_="kt-post-card")

    for ad in ads:
        # پیدا کردن عنوان آگهی
        title_tag = ad.find('h2', class_="kt-post-card__title")
        title = title_tag.text.strip() if title_tag else "بدون عنوان"

        # پیدا کردن قیمت
        price_tag = ad.find('div', class_="kt-post-card__description")
        price = price_tag.text.strip() if price_tag else "نامشخص"

        # فیلتر کردن آگهی‌هایی که قیمت آن‌ها توافقی است یا در محتوای آن توافقی یافت میشود
        # if "توافقی" in price:
        if "توافقی" in price or "توافقی" in title:
            print(f"عنوان: {title}, قیمت: {price}")

else:
   print(f"خطا در دریافت اطلاعات! کد وضعیت: {response.status_code}")
