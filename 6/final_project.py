"""
    train an ai model to get population of country from database data and predict area of input
    1-first most scrap and fetch data from website.
    2-insert data to database.
    3-read all data from database and train model.
    4-now test it and give population and get prediction of area.
"""

import requests
import mysql.connector
from bs4 import BeautifulSoup
from sklearn import tree


def collect_data_from_site():
    # send request with user agent to prevent blocking from website
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    url = "https://www.scrapethissite.com/pages/simple/"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        countries = soup.find_all('div', attrs={'class': 'country'})

        try:
            print('Connecting to database...')
            cnx = mysql.connector.connect(
                user="root",
                password="123",
                host="localhost",
                database="test_database",
                charset="utf8mb4",
                collation="utf8mb4_unicode_ci"
            )
            print('Connected successfully')

            cursor = cnx.cursor()
            cursor.execute("DROP TABLE IF EXISTS Country")
            
            sql = """
                CREATE TABLE Country (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    country_name VARCHAR(127) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL UNIQUE,
                    capital_name VARCHAR(127) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
                    population INT,
                    area FLOAT
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
                """
            cursor.execute(sql)
            print("Table 'Country' created successfully.")

            countries_data = []
            for country in countries:
                country_name = country.find('h3', class_="country-name")
                name = country_name.text.strip() if country_name else "بدون اسم"

                country_capital = country.find('span', class_="country-capital")
                capital = country_capital.text.strip() if country_capital else "بدون اسم"

                country_population = country.find('span', class_="country-population")
                population = int(country_population.text.strip()) if country_population else None

                country_area = country.find('span', class_="country-area")
                area = float(country_area.text.strip()) if country_area else None

                countries_data.append((name, capital, population, area))

            sql = "INSERT INTO Country (country_name, capital_name, population, area) VALUES (%s, %s, %s, %s)"
            cursor.executemany(sql, countries_data)
            cnx.commit()

            print("New data added to database successfully.")

        except Exception as e:
            print(f"Unexpected error: {e}")

        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'cnx' in locals():
                cnx.close()

    else:
        print(f"Error fetching data: {response.status_code}")


def train_model():
    try:
        # connect to database
        print('Connecting to database...')
        cnx = mysql.connector.connect(
            user="root",
            password="123",
            host="localhost",
            database="test_database",
            charset="utf8mb4",
            collation="utf8mb4_unicode_ci"
        )
        print('Connected successfully')

        # fetch all countries and rows from country table
        cursor = cnx.cursor()
        # cursor.execute("SELECT * FROM Country")
        cursor.execute("SELECT population, area FROM Country WHERE population IS NOT NULL AND area IS NOT NULL")
        country_list=cursor.fetchall()

        if not country_list:
            print(" There is no valid data for training!!")
            return None

        # تبدیل داده‌ها برای مدل
        x = [[row[0]] for row in country_list]  # جمعیت (یک آرایه دو بعدی)
        y = [row[1] for row in country_list]  # مساحت (یک آرایه یک بعدی)

        # train model with x,y lists that have countires data
        model = tree.DecisionTreeRegressor()
        model.fit(x, y)

        print("Model trained successfully!")

        return model

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals():
            cnx.close()


if __name__ == "__main__":
    # fetch data from website and insert into database with collect data from site function
    # collect_data_from_site()
    
    # read all data from database and train an ai model
    trained_model=train_model()

    if trained_model:
        prediction = trained_model.predict([[1500]])  # باید دو‌بعدی باشه
        print(f"Predicted area for 1500 population: {prediction[0]}")





"""
    def train_model_way2():
    try:
        # connect to database
        print('Connecting to database...')
        cnx = mysql.connector.connect(
            user="root",
            password="123",
            host="localhost",
            database="test_database",
            charset="utf8mb4",
            collation="utf8mb4_unicode_ci"
        )
        print('Connected successfully')

        # fetch all countries and rows from country table
        cursor = cnx.cursor()
        # cursor.execute("SELECT population, area FROM Country WHERE population IS NOT NULL AND area IS NOT NULL")
        cursor.execute("SELECT * FROM Country")
        country_list=cursor.fetchall()

        filtered_countries = [row for row in country_list if row[3] is not None and row[4] is not None]
        if not filtered_countries :
            print(" There is no valid data for training!!")
            return None
        
        x = [[row[3]] for row in filtered_countries]  # جمعیت به عنوان ورودی
        y = [row[4] for row in filtered_countries]    # مساحت به عنوان خروجی

        # train model with x,y lists that have countires data
        model = tree.DecisionTreeRegressor()
        model.fit(x, y)

        print("Model trained successfully!")

        return model

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals():
            cnx.close()

            
====================================================

    x=[]
    y=[]

    # append countries data to x,y list
    for country in country_list:
        # print('country population: ',country[3]," | country area: ",country[4])
        x.append(country[0])
        y.append(country[1])

"""