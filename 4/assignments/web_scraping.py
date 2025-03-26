import requests
import mysql.connector
from bs4 import BeautifulSoup

# تنظیمات درخواست HTTP
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://www.scrapethissite.com/pages/simple/"

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Error fetching data: {e}")
    exit(1)

# پردازش HTML
soup = BeautifulSoup(response.text, 'html.parser')
countries = soup.find_all('div', class_="country", limit=20)  # فقط ۲۰ کشور اول

# اتصال به دیتابیس
try:
    print('Connecting to database...')
    with mysql.connector.connect(user="root",
                                 password="123",
                                 host="localhost",
                                 database="test_database") as cnx:
        print('Connected successfully')
        with cnx.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Country(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    country_name VARCHAR(127) NOT NULL UNIQUE,
                    capital_name VARCHAR(127) NOT NULL,
                    population INT,
                    area FLOAT
                )
            """)

            # حذف کل داده‌ها برای جایگزینی جدید
            cursor.execute("DELETE FROM Country")
            cnx.commit()
            print("Old data deleted.")

            # استخراج اطلاعات کشورها
            countries_data = []
            for country in countries:
                name = country.find('h3', class_="country-name")
                capital = country.find('span', class_="country-capital")
                population = country.find('span', class_="country-population")
                area = country.find('span', class_="country-area")

                name = name.text.strip() if name else "بدون اسم"
                capital = capital.text.strip() if capital else "بدون پایتخت"
                try:
                    population = int(population.text.strip().replace(',', '')) if population else None
                except ValueError:
                    population = None
                try:
                    area = float(area.text.strip().replace(',', '')) if area else None
                except ValueError:
                    area = None

                countries_data.append((name, capital, population, area))

            # درج اطلاعات جدید در دیتابیس
            sql_insert = "INSERT INTO Country (country_name, capital_name, population, area) VALUES (%s, %s, %s, %s)"
            cursor.executemany(sql_insert, countries_data)
            cnx.commit()

            print(f"{len(countries_data)} new records added successfully.")

except mysql.connector.Error as db_err:
    print(f"Database error: {db_err}")

except Exception as e:
    print(f"Unexpected error: {e}")
