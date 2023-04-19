from __future__ import absolute_import, unicode_literals
from celery import shared_task
from instagram import insta_selenium


@shared_task
def hello_world():
    link = 'http://www.instagram.com'
    username = 'napoli123milan'
    password = 'italia123koma'
    insta_selenium.InstaSelenium(link, username, password)
    print('salam yeti')

