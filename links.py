import time
import buddon

def filter(driver, sus_links):

    black_list = ["youtube", "twitter", "facebook", "goo.gl", "kit.co", "discord", "banggood", "tubebuddy", "gearbest", "spinning" "mikesunboxing", "knockies", "abunda"]
    amazon_links = []

    original_handle = driver.current_window_handle

    for link in sus_links:

        driver.switch_to.window(original_handle)

        if "http" in link.text:
            check = any(x in link.text for x in black_list)
            if not check:

                buddon.click(driver,link)
            
                handle = driver.window_handles[-1]
                driver.switch_to.window(handle)

                while driver.current_url in "about:blank":
                    time.sleep(0.5)

                if "amazon.com" in driver.current_url:
                    if "amazonprime" not in driver.current_url:
                        if "shop" not in driver.current_url:                            
                            amazon_links.append(driver.current_url)
                
                for handle in driver.window_handles:
                    if handle != original_handle:
                        driver.switch_to.window(handle)
                        driver.close()

    return amazon_links