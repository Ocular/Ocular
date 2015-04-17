# -*- encoding: utf-8 -*-
# Author: Epix
import scrapy
from .. import accounts
from scrapy.http.request.form import FormRequest


class pixiv(scrapy.Spider):
    name = 'pixiv'
    start_urls = ['http://www.pixiv.net/member_illust.php?id=154294']
    # headers={'Content-Type':'application/x-www-form-url'}

    def start_requests(self):
        return [FormRequest('https://www.secure.pixiv.net/login.php',
                            formdata={'mode': 'login', 'pixiv_id': accounts.pixiv_pixiv_id, 'pass': accounts.pixiv_pass,
                                      'skip': '1'},
                            callback=self.after_login)]

    def after_login(self, response):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        print(response.css('title'))
