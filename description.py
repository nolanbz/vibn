import links


def getLinks(driver):

    link_path = "//a[@class='yt-simple-endpoint style-scope yt-formatted-string']"

    description_links = driver.find_elements_by_xpath(link_path)

    description_links = links.filter(driver, description_links)

    return description_links