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
    option.add_argument("--incognito")
    option.add_argument("--mute-audio")
    option.add_argument("--disable-popup-blocking")
    option.add_argument("--disable-extensions")
    option.add_argument("--disable-application-cache")
    
    browser = webdriver.Chrome(executable_path=path, options=option)

    return browser