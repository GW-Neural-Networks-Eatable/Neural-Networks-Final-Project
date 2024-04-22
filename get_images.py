from playwright.async_api import async_playwright
import sqlite3
from sqlite3 import Error
from array import array
import requests 
from PIL import Image
import os


async def get_images(dish_data, conn) -> None:


    ctr = 6800

    for dish in dish_data:
        
        url = dish[2]
        # print('url: ', url[0])
        if url[0] != 'h': #if we have already converted an image continue through the loop 
            continue
        data = requests.get(url).content

        check = len(url) - 15

        if(url[check] == 'p'):

            path = "Images!/" + str(ctr) + ".png"

        else:
            
            path = "Images!/" + str(ctr) + ".jpg"
        
        
        file = open(path, "wb")
        file.write(data)

        #replace url with file path 
        with conn:
            cur = conn.cursor()
            sql = '''UPDATE Dish SET PATH = ? WHERE RESTAURANT = ? AND DISH_NAME = ?'''
            cur.execute(sql, (path, dish[0], dish[1]))
            conn.commit()
        file.close()

        ctr = ctr + 1