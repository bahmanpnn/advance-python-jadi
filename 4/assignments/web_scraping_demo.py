import requests
import mysql.connector
from bs4 import BeautifulSoup


# send request with user agent to prevent blocking from website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url,headers=headers)

# بررسی موفقیت دریافت اطلاعات
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # find countries
    # countries = soup.find_all('div', class_="country")
    countries = soup.find_all('div', attrs={'class':'country'},limit=20)

    try:
        print('connecting to database...')
        cnx=mysql.connector.connect(user="root",
                                    password="123",
                                    host="localhost",
                                    database="test_database")

        print('connected successfully')

        cursor=cnx.cursor()
        sql="CREATE TABLE IF NOT EXISTS Country(\
            id INT AUTO_INCREMENT PRIMARY KEY,\
            country_name VARCHAR(127) NOT NULL,\
            capital_name VARCHAR(127) NOT NULL,\
            population INT,\
            area INT\
        );"
        cursor.execute(sql)
        cnx.commit()
        countries_data=[]
        
        for country in countries:
            # find country name
            country_name = country.find('h3', class_="country-name")
            name = country_name.text.strip() if country_name else "بدون اسم"
            # print(name)

            # find country capital
            country_capital = country.find('span', class_="country-capital")
            capital = country_capital.text.strip() if country_capital else "بدون اسم"
            # print(capital)

            # find country population
            country_population = country.find('span', class_="country-population")
            population = country_population.text.strip() if country_population else "بدون اسم"
            # print(population)

            # find country area
            country_area = country.find('span', class_="country-area")
            area = country_area.text.strip() if country_area else "بدون اسم"
            # print(area)

            # append a country values to countries_data list
            countries_data.append((name,capital,population,area)) 
        
        # insert countries data to database
        sql = "INSERT INTO Country (country_name, capital_name, population,area) VALUES (%s, %s, %s, %s)"
        cursor.executemany(sql, countries_data)
        cnx.commit()

        print("data added to database successfully;")

    except Exception as e:
        print(f"Unexpected error: {e}")

    finally:
        if "cursor" in locals():
            cursor.close()
        if "cnx" in locals():
            cnx.close()

else:
    print(f"error for fetching data: {response.status_code}")




"""

    delete rows of table
    cursor.execute("DELETE FROM Country")
    cnx.commit()

    print("All test data deleted.")


    cursor.execute("ALTER TABLE Country MODIFY COLUMN area FLOAT")
    cnx.commit()

"""
