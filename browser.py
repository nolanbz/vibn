from selenium import webdriver 
import os
import setup


def createBrowser(local):

    bin = os.environ.get("GOOGLE_CHROME_BIN")
    path = os.environ.get("CHROMEDRIVER_PATH")

    if local:
        bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        path = "/Users/nolan/Python/vibn/chromedriver"

    option = webdriver.ChromeOptions()
    option.binary_location = bin
    option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')
    
    browser = webdriver.Chrome(executable_path=path, options=option)

    return browser