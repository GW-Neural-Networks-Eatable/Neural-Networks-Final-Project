from playwright.async_api import async_playwright

async def get_restaurants(page, url: str, city: str, state: str, csv: str) -> None:
    async with async_playwright() as p:
        await page.goto(url)

        # Get all restaurants
        restaurants = await page.query_selector_all(".restaurants > .rx-card-container")

        # Write to CSV (append mode)
        with open(csv, "a") as file:
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

                # Write to CSV
                file.write(f"{name},{city},{state},{menu_url}\n")
                