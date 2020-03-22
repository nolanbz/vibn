from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from sys import platform

def clickLink(driver, link):
    
    if platform == "darwin":
        ActionChains(driver) \
            .key_down(Keys.COMMAND) \
            .click(link) \
            .key_up(Keys.COMMAND) \
            .perform()
    else:
        ActionChains(driver) \
            .key_down(Keys.CONTROL) \
            .click(link) \
            .key_up(Keys.CONTROL) \
            .perform()