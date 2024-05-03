from playwright.async_api import async_playwright
import sqlite3
from get_menu import get_restaurant_menu
from sqlite3 import Error


def connection(database):
    #get connection 
    conn = None 
    try: 
        conn = sqlite3.connect(database)
    except Error as e: 
        print(e)
    return conn

async def get_restaurants(page, url: str, city: str, state: str) -> None:
    async with async_playwright() as p:
        await page.goto(url)

        # Get all restaurants
        restaurants = await page.query_selector_all(".restaurants > .rx-card-container")

        # Write to CSV (append mode)
        #connect to the database 
        database = 'prices.db'
        conn = connection(database)
        with conn: 
            for r in restaurants:
                name = await r.query_selector(".rx-name")
                name = await name.inner_text() if name else ""
                name = name.replace(",", " ") # Replace comma with space

                menu_url = await r.query_selector("a.link-to-rx-profile")
                menu_url = await menu_url.get_attribute("href") if menu_url else None

                if not menu_url:
                    continue

                # Convert relative URL to absolute URL
                menu_url = f"https://www.toasttab.com{menu_url}"

                #insert into database
                sql = '''INSERT INTO Restaurant(NAME,URL,CITY,STATE)values(?,?,?,?)'''
                cur = conn.cursor()
                cur.execute(sql, (name, menu_url, city, state))
                conn.commit()
                