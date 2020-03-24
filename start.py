import browser
import video
import time
import description
import abunda
import json
import setup

def getLinks(id, video_url):

    driver = browser.createBrowser(setup.local())

    JSON = json.dumps({'id': id, 'abunda_links': "error"})

    if video.get(driver, video_url):

        amazon_links = description.getLinks(driver)
        abunda_links = abunda.convertLinks(driver, amazon_links)

        JSON = json.dumps({'id': id, 'abunda_links': abunda_links})

        print("")
        print(JSON)
        print("")
        print("Found {} abunda links(s)".format(len(abunda_links)))

        return JSON
    else:
        print("failed to load video")
        
        return JSON
    
    driver.quit()