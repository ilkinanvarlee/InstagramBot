from __future__ import absolute_import, unicode_literals
from celery import shared_task
from instagram import insta_selenium
from instagram.models import Instagram


"""
@shared_task
def hello_world():
    link = 'http://www.instagram.com'
    username = 'napoli123milan'
    password = 'italia123koma'
    insta_selenium.InstaSelenium(link, username, password)
    print('All Right')
"""


@shared_task
def hello_world():
    link = 'http://www.instagram.com'

    for i in Instagram.objects.all():
        username = i.instagram_username
        password = i.instagram_password
        insta_selenium.InstaSelenium(link, username, password)
    print('All Right')
