import browser
import video
import time
import description
import abunda
import json
import os
import requests
from celery import Celery

app = Celery()
app.conf.broker_url = os.environ.get('REDISTOGO_URL','redis://localhost:6379/0')

@app.task
def returnLinks(id, video_url):
    driver = browser.createBrowser()

    JSON = {"id": id, "abunda_links": "error"}

    print(id, video_url)

    if video.get(driver, video_url):

        amazon_links = description.getLinks(driver)
        abunda_links = abunda.convertLinks(driver, amazon_links)

        JSON = {"id": id, "abunda_links": abunda_links}

        requests.post('https://admin:55092473B@4fa9162f.ngrok.io/video_callbacks/receive_data', json=JSON)
        driver.quit()
        return JSON
    else:
        print("failed to load video")
        
        requests.post('https://admin:55092473B@4fa9162f.ngrok.io/video_callbacks/receive_data', json=JSON)
        driver.quit()
        return JSON
    
    
