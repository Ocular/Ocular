# -*- encoding: utf-8 -*-
# Author: Epix
import scrapy
from Ocular import accounts
from scrapy.http.request.form import FormRequest
from scrapy.contrib.spiders.crawl import CrawlSpider
from Ocular.items import OcularItem
from scrapy.utils.response import get_base_url
from urlparse import urljoin


class pixiv(CrawlSpider):
    name = 'pixiv'
    # start_urls = ['http://www.pixiv.net/member_illust.php?id=154294']
    # headers={'Content-Type':'application/x-www-form-url'}

    def __init__(self, ids):
        self.start_urls = ['http://www.pixiv.net/member_illust.php?id=%s' % id for id in ids]
        print(self.start_urls)

    def start_requests(self):
        return [FormRequest('https://www.secure.pixiv.net/login.php',
                            formdata={'mode': 'login', 'pixiv_id': accounts.pixiv_pixiv_id, 'pass': accounts.pixiv_pass,
                                      'skip': '1'},
                            callback=self.after_login)]

    def after_login(self, response):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)
