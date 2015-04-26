# -*- encoding: utf-8 -*-
# Author: Epix
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from Ocular.spiders.pixiv import pixiv
from scrapy.utils.project import get_project_settings

spider = pixiv([154294, 296720])
settings = get_project_settings()
crawler = Crawler(settings)
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start()
reactor.run()
