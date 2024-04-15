from playwright.async_api import async_playwright
import sqlite3
from sqlite3 import Error
from array import array

def connection(database):
    #get connection 
    conn = None 
    try: 
        conn = sqlite3.connect(database)
    except Error as e: 
        print(e)
    return conn

async def get_restaurant_menu(page, url: str, restaurant: str, city: str, state: str) -> None:
    async with async_playwright() as p:
        await page.goto(url)
        
        # Get all items
        items = await page.query_selector_all(".itemSection > .item")
         #connect to the database 
        database = 'testDB.db'
        conn = connection(database)
        with conn: 
            for item in items:
                name = await item.query_selector(".itemHeader")
                name = await name.inner_text() if name else ""

                price = await item.query_selector(".price")
                price = await price.inner_text() if price else None
                price = price.replace("$","")

                image = await item.query_selector("img.itemImage")
                image = await image.get_attribute("src") if image else None

                if not price or not image:
                    continue
                sql = '''SELECT RESTAURANT, DISH_NAME FROM DISH WHERE RESTAURANT = ? AND DISH_NAME = ?'''
                cur = conn.cursor()
                result = list(cur.execute(sql, (restaurant, name)))
                # conn.commit()
                
                if len(result)== 0: 
                    #insert into db 
                    sql = '''INSERT INTO Dish(RESTAURANT,DISH_NAME,PATH,PRICE)values(?,?,?,?)'''
                    cur = conn.cursor()
                    cur.execute(sql, (restaurant, name, image, price))
                    conn.commit()



        # Write to CSV (append mode)
        # with open(csv, "a") as file:
        #     for item in items:
        #         name = await item.query_selector(".itemHeader")
        #         name = await name.inner_text() if name else ""

        #         price = await item.query_selector(".price")
        #         price = await price.inner_text() if price else None

        #         image = await item.query_selector("img.itemImage")
        #         image = await image.get_attribute("src") if image else None

        #         if not price or not image:
        #             continue

        #         # Write to CSV
        #         file.write(f"{restaurant},{city},{state},{name},{price},{image}\n")
