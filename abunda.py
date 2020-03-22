from selenium.webdriver.common.keys import Keys

def convertLinks(driver, amazon_links):
    abunda_links = []

    for link in amazon_links:

        driver.get("https://shopabunda.com")

        search_bar = driver.find_elements_by_xpath("//input[@id='bc-sf-search-box-2']") 
        if search_bar:
            search_bar[0].clear()
            search_bar[0].send_keys(link)
            search_bar[0].send_keys(Keys.RETURN)

            price = driver.find_elements_by_xpath("//div[@class='sc-iBEsjs lphJbu pf-b7257e67']/div")

            if price:
                price = price[0].text
                price = price.split("$")[1]
                price = price.split(".")[0]
                if "," in price:
                    price = price.replace(',', '')

                if int(price) >= 50:
                    abunda_links.append(driver.current_url) 
                    

    return abunda_links
