import os
import sqlite3
import shutil
import imghdr

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

# We'll need to ensure images are accepted by TF, so we'll store the image types accepted
img_type_accepted_by_tf = ["bmp", "gif", "jpeg", "png"] # https://stackoverflow.com/a/68192520

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
        if imghdr.what(item[0]) in img_type_accepted_by_tf: # https://stackoverflow.com/a/68192520
            shutil.copy(item[0], f"{image_folder}/{min}_{max}")     
