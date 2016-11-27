# -*- coding: utf-8 -*-
import scrapy
import json
import urlopen

class JdaadSpider(scrapy.Spider):
    name = "jdaad"
    #allowed_domains = ["https://www.daad.de/bundles/daadphdgermanyrise/data/js/offers.js?cb=20161126110000"]
    start_urls = ['https://www.daad.de/bundles/daadphdgermanyrise/data/js/offers.js?cb=20161126110000/']

    def parse(self, response):
       fp = open('1.html','w')
       fp.write(response.body)
       fp.close()

        # jdict = json.loads(response.body)
        # jtaffy = jdict["Taffy"]
        # for each in jtaffy:
        #     print each['code']
        #     print each['contactemail']
        #     print each['offertitelen']
        #     print response.body