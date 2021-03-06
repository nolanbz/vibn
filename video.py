from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException


def get(driver, video_url):

    driver.get(video_url)
    button_class_name = "more-button"
    video_path = "//yt-formatted-string[@class='style-scope ytd-video-primary-info-renderer']"

    

    try:
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, video_path)))
        
        try:
            show_more_button = driver.find_element_by_class_name(button_class_name)
            show_more_button.click()
            return True
        except:
            return False

    except TimeoutException:
        print("Timed out waiting for video to load")

        return False

