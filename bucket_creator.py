import os
import sqlite3
import shutil

# Config
database = "testDB.db"
database_table = "Dish"
database_img_col = "PATH"
database_price_col = "PRICE"
image_folder = "buckets"
bucket_range = 5
bucket_min = 10
bucket_max = 50

# You should not need to change anything below this line
# -------------------------------------------------------

# Generate buckets. List of tuples (min, max)
buckets = [(x, x + bucket_range) for x in range(bucket_min, bucket_max, bucket_range)] 

# Open db connection
conn = sqlite3.connect(database)
cursor = conn.cursor()

# Empty `images` folder
shutil.rmtree(image_folder, ignore_errors=True)

# Create, populate buckets
for bucket in buckets:
    min, max = bucket

    # Create folder for bucket
    os.makedirs(f"{image_folder}/{min}_{max}", exist_ok=True)

    # Get data
    cursor.execute(f"SELECT {database_img_col} FROM {database_table} WHERE {database_price_col} >= {min} AND {database_price_col} < {max}")
    items = cursor.fetchall()

    # Copy images to bucket folder
    for item in items:
        shutil.copy(item[0], f"{image_folder}/{min}_{max}")     
