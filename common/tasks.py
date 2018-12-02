import os
import time
from worker import celery
from scrapper import scraper
import dal
import datetime


@celery.task()
def scrap_task(url):
    url_data = dal.Stories.get_by(url=url)
    try:
        new_data = scraper(url)
        url_data.status = 'done'
        url_data.data = new_data
    except:
        url_data.status = 'failed'
        raise
    finally:
        url_data.updated_time = datetime.datetime.utcnow()
        url_data.save()

  
