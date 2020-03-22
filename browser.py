from selenium import webdriver 


def createBrowser(headless):

    GOOGLE_CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    CHROME_DRIVER = "/Users/nolan/Python/vibn/chromedriver"

    option = webdriver.ChromeOptions()
    option.binary_location = GOOGLE_CHROME_BIN
    option.add_argument('--log-level=3')
    option.add_argument("--incognito")
    option.add_argument("--mute-audio")
    option.add_argument('--disable-gpu')
    option.add_argument('--no-sandbox')
    option.add_argument("--disable-popup-blocking")
    option.add_argument("--disable-extensions")
    option.add_argument("--disable-application-cache")
    
    
    if headless:
        option.add_argument("--headless")

    browser = webdriver.Chrome(executable_path=CHROME_DRIVER, options=option)

    return browser