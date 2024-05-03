## Install Dependencies
```bash
pip install -r requirements.txt
playwright install
```

## Web Scraping
To scrape data using the url provided in main.py, the url is provided for everything except for the pages you desire. Edit the loop for the number of pages you would like to scrape.

## Training the model
To train the model, run the cells in the `model_reg.ipynb` (regression; exact price predictions) or `model_cat.ipynb` (classification into price buckets) notebook. The notebook will save the model(s) in the `models` directory.

## Running the Flask app
To run the Flask app, run the following command in the terminal (in your virtual environment):
```bash
flask run
```
The app will be available at `http://127.0.0.1:5000` (or whatever URL is returned in the URL), where an image can be uploaded to get a price prediction.

## Generating, publishing the paper
In the `main` branch, run the following commands to generate the paper:
```bash
quarto publish gh-pages paper.qmd
```
