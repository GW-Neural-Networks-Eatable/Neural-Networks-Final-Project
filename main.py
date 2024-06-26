import asyncio
import csv
from get_menu import get_restaurant_menu
from get_restaurants import get_restaurants
from get_images import get_images
from playwright.async_api import async_playwright
import sqlite3
from sqlite3 import Error


# Get restaurants
city = "Washington"
state = "DC"
url = "https://www.toasttab.com/local/search?filters=eyJ1c2VyU3RyZWV0IjoiIiwidXNlck5laWdoYm9yaG9vZCI6IiIsInVzZXJDaXR5IjoiV2FzaGluZ3RvbiIsInVzZXJTdGF0ZSI6IkRDIiwidXNlckxhdCI6MzguOTA1OTg0OSwidXNlckxvbmciOi03Ny4wMzM0MTc5MDAwMDAwMiwiY3Vpc2luZUlkIjpudWxsfQ%3D%3D&pg="
# restaurants = "restaurants.csv"

# def connection(database):
    


async def main():
    database = 'prices.db'
    #get connection 
    conn = None 
    try: 
        conn = sqlite3.connect(database)
    except Error as e: 
        print(e)

        
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context("browser", slow_mo=50, headless = False)
        page = await browser.new_page()
        
        #connect to the database
        # conn = connection(database)
        with conn:
        #do the dang thing
        #get the restaurants

            for i in range(12,16):

                earl = url + str(i)

                await get_restaurants(page, earl, city, state)

            #gonna need a a select statement 
            cur = conn.cursor()
            sql = '''SELECT * from Restaurant'''
            cur.execute(sql)
            rests = cur.fetchall()
            # print(rests)
            for l in rests:
               await get_restaurant_menu(page, l[1], l[0], city, state)
    
            # Get menus, for each restaurant
            # with open(restaurants, "r") as file:
            #     reader = csv.reader(file)
            #     next(reader) # Skip header

            #     for row in reader:
            #         restaurant, menu_city, menu_state, menu_url = row
            #         await get_restaurant_menu(page, menu_url, restaurant, menu_city, menu_state, "items.csv")
        # Close browser
        await browser.close()
        with conn: 
            cur = conn.cursor()
            sql = '''SELECT * FROM DISH'''
            cur.execute(sql)
            dishes = cur.fetchall()
            await get_images(dishes, conn)
        

asyncio.run(main())
###test
# def main():
#     database = 'testDB.db'
#     conn = connection(database)
#     with conn:
#         sql = '''INSERT INTO Restaurant(NAME,CITY)values(?,?)'''
#         cur = conn.cursor()
#         cur.execute(sql, ('SEH', 'DC'))
#         conn.commit()

# if __name__ == '__main__':
#     main()