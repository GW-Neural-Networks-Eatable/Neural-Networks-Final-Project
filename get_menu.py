from playwright.async_api import async_playwright

async def get_restaurant_menu(page, url: str, restaurant: str, city: str, state: str, csv: str) -> None:
    async with async_playwright() as p:
        await page.goto(url)

        # Get all items
        items = await page.query_selector_all(".itemSection > .item")

        # Write to CSV (append mode)
        with open(csv, "a") as file:
            for item in items:
                name = await item.query_selector(".itemHeader")
                name = await name.inner_text() if name else ""

                price = await item.query_selector(".price")
                price = await price.inner_text() if price else None

                image = await item.query_selector("img.itemImage")
                image = await image.get_attribute("src") if image else None

                if not price or not image:
                    continue

                # Write to CSV
                file.write(f"{restaurant},{city},{state},{name},{price},{image}\n")
