import asyncio
import csv
from get_menu import get_restaurant_menu
from get_restaurants import get_restaurants
from playwright.async_api import async_playwright

# Get restaurants
city = "Washington"
state = "DC"
url = "https://www.toasttab.com/local/search?filters=eyJ1c2VyU3RyZWV0IjoiIiwidXNlck5laWdoYm9yaG9vZCI6IiIsInVzZXJDaXR5IjoiV2FzaGluZ3RvbiIsInVzZXJTdGF0ZSI6IkRDIiwidXNlckxhdCI6MzguOTA1OTg0OSwidXNlckxvbmciOi03Ny4wMzM0MTc5MDAwMDAwMiwiY3Vpc2luZUlkIjpudWxsfQ%3D%3D&pg=1"
restaurants = "restaurants.csv"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context("browser", slow_mo=50)
        page = await browser.new_page()

        await get_restaurants(page, url, city, state, restaurants)

        # Get menus, for each restaurant
        with open(restaurants, "r") as file:
            reader = csv.reader(file)
            next(reader) # Skip header

            for row in reader:
                restaurant, menu_city, menu_state, menu_url = row
                await get_restaurant_menu(page, menu_url, restaurant, menu_city, menu_state, "items.csv")

        # Close browser
        await browser.close()

asyncio.run(main())