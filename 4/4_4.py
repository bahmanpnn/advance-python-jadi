"""
    working with requests package is good more for apis not scraping.
    so we need to another tools to scrap and fetch data from html(or other type of files) and pages of website.

    https://pypi.org/project/beautifulsoup4/
    that tool is beautifulsoup package.
    we can use regex too but this package is better and helps us more.
    rule==> BeautifulSoup(page(or file(html(r.text))),how)
"""
import requests
from bs4 import BeautifulSoup


r=requests.get("https://divar.ir/s/mashhad/rent-residential?credit=0-50000000&rent=0-5000000")
# print(r.text)

soup=BeautifulSoup(r.text,'html.parser')
# print(soup)

# val=soup.find('article')
# print(val)
# print(val.attrs)


values=soup.find_all("article")
# print(values)
# print(values[1])
val1=values[1]
val2=values[2]
print(val1.attrs)
print(val2.attrs)


print(soup.find('article',attrs={'class':['kt-post-card', 'kt-post-card--outlined', 'kt-post-card']}))
# print(soup.find('article',attrs={'class':['unsafe-kt-post-card', 'unsafe-kt-post-card--outlined', 'unsafe-kt-post-card']}))

# *** we can combine regex and beautiful soup together.like using sub method for removing spaces or something==>
 