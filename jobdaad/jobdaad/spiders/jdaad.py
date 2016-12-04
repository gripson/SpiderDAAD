# -*- coding: utf-8 -*-
import linecache

import scrapy
from scrapy import Selector
from scrapy.http import Request
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.contrib.linkextractors import LinkExtractor
from w3lib.url import url_query_parameter

from jobdaad.items import JobdaadItem
import json

class JdaadSpider(scrapy.Spider):
    name = "jdaad"
    #allowed_domains = ["https://www.daad.de/bundles/daadphdgermanyrise/data/js/offers.js?cb=20161126110000"]
    start_urls = ['https://www.daad.de/deutschland/promotion/phd/en/13306-phdgermany-database/']
    # start_urls = ['https://www.daad.de/bundles/daadphdgermanyrise/data/js/offers.js?/']

    # rules = (
        # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
        # Rule(LinkExtractor(allow=('category\.php',), deny=('subsection\.php',))),

        # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
        # Rule(LinkExtractor(allow=('offers\.js',)), callback='parse_offers'),
    # )

    # def parse_offers(self, response):
    #     yield Request(response.url, callback=self.parse)

    def parse(self, response):
        selector = Selector(response)
        # url = selector.xpath("//script").extract()
        # print url
        # url = selector.xpath('//script[re:test(@src, "/bundles/daadphdgermanyrise/data/js/offers.js?cb=\s$")]').extract()
        url= selector.xpath('//script[contains(@src, "offers")]/@src').extract()
        url_offers = 'https://www.daad.de' + url[0]
        print url_offers
        return Request(url_offers, callback=self.parse_offers)


    def parse_offers(self, response):
       # fp = open('1.html','w')
       # fp.write(response.body.replace('var offers = TAFFY(', '').replace(');', ''))
       # fp.close()
       url = response.url
       date = url_query_parameter(url, "cb")
       filename = "daadphd%s.json"% date

       item = JobdaadItem()
       jtaffy = response.body.replace('var offers = TAFFY(', '').replace(');', '')

       with open(filename, 'w') as fout:
           fout.write(jtaffy)
       fout.close()

       with open(filename, 'r') as fin:
           # data = f.readlines()
           data = json.load(fin)
       fin.close
       # count = linecache.getlines('data2.json')
       # linecache.clearcache()
       # data = json.load('data2.json')
       for each in data:
           print each['code']
           item['code'] = each['code'].encode('utf-8')
           item['contactadresszusatz'] = each['contactadresszusatz'].encode('utf-8')
           item['contactasprache'] = each['contactasprache'].encode('utf-8')
           item['contactasprache_key'] = each['contactasprache_key'].encode('utf-8')
           item['contactasprache_value'] = each['contactasprache_value'].encode('utf-8')
           item['contactdsprache'] = each['contactdsprache'].encode('utf-8')
           item['contactdsprache_key'] = each['contactdsprache_key'].encode('utf-8')
           item['contactdsprache_value'] = each['contactdsprache_value'].encode('utf-8')
           item['contactemail'] = each['contactemail'].encode('utf-8')
           item['contactfax'] = each['contactfax'].encode('utf-8')
           item['contactfirstname'] = each['contactfirstname'].encode('utf-8')
           item['contactinstitution'] = each['contactinstitution'].encode('utf-8')
           item['contactlastname'] = each['contactlastname'].encode('utf-8')
           item['contactlogo'] = each['contactlogo'].encode('utf-8')
           item['contactorganisation'] = each['contactorganisation'].encode('utf-8')
           item['contactort'] = each['contactort'].encode('utf-8')
           item['contactplz'] = each['contactplz'].encode('utf-8')
           item['contactposition'] = each['contactposition'].encode('utf-8')
           item['contactstrasse'] = each['contactstrasse'].encode('utf-8')
           item['contacttelefon'] = each['contacttelefon'].encode('utf-8')
           item['contacttitel'] = each['contacttitel'].encode('utf-8')
           item['contactunterlagen'] = each['contactunterlagen'].encode('utf-8')
           item['contactunterlagen_key'] = each['contactunterlagen_key'].encode('utf-8')
           item['contactunterlagen_value'] = each['contactunterlagen_value'].encode('utf-8')
           item['contactunterlagenotherde'] = each['contactunterlagenotherde'].encode('utf-8')
           item['contactunterlagenotheren'] = each['contactunterlagenotheren'].encode('utf-8')
           item['contacturl'] = each['contacturl'].encode('utf-8')
           item['contactvoraussetzungde'] = each['contactvoraussetzungde'].encode('utf-8')
           item['contactvoraussetzungen'] = each['contactvoraussetzungen'].encode('utf-8')
           item['created'] = each['created'].encode('utf-8')
           item['created_key'] = each['created_key'].encode('utf-8')
           item['offerangebotsurl'] = each['offerangebotsurl'].encode('utf-8')
           item['offeranzahl'] = each['offeranzahl'].encode('utf-8')
           item['offerbeginn'] = each['offerbeginn'].encode('utf-8')
           item['offerbeginn_key'] = each['offerbeginn_key'].encode('utf-8')
           item['offerbeginn_value'] = each['offerbeginn_value'].encode('utf-8')
           item['offerbeschreibungde'] = each['offerbeschreibungde'].encode('utf-8')
           item['offerbeschreibungen'] = each['offerbeschreibungen'].encode('utf-8')
           item['offerdauer'] = each['offerdauer'].encode('utf-8')
           item['offerdauerde'] = each['offerdauerde'].encode('utf-8')
           item['offerdaueren'] = each['offerdaueren'].encode('utf-8')
           item['offerdeadline'] = each['offerdeadline'].encode('utf-8')
           item['offerdeadline_key'] = each['offerdeadline_key'].encode('utf-8')
           item['offerdeadline_value'] = each['offerdeadline_value'].encode('utf-8')
           item['offerfachgebietde'] = each['offerfachgebietde'].encode('utf-8')
           item['offerfachgebieten'] = each['offerfachgebieten'].encode('utf-8')
           item['offerfachrichtung'] = each['offerfachrichtung'].encode('utf-8')
           item['offerfachrichtung_key'] = each['offerfachrichtung_key'].encode('utf-8')
           item['offerfachrichtung_value'] = each['offerfachrichtung_value'].encode('utf-8')
           item['offerfinanzierung'] = each['offerfinanzierung'].encode('utf-8')
           item['offerfinanzierung_key'] = each['offerfinanzierung_key'].encode('utf-8')
           item['offerfinanzierung_value'] = each['offerfinanzierung_value'].encode('utf-8')
           item['offerpromotion'] = each['offerpromotion'].encode('utf-8')
           item['offerpromotion_key'] = each['offerpromotion_key'].encode('utf-8')
           item['offerpromotion_value'] = each['offerpromotion_value'].encode('utf-8')
           item['offertitelde'] = each['offertitelde'].encode('utf-8')
           item['offertitelen'] = each['offertitelen'].encode('utf-8')
           item['updated'] = each['updated'].encode('utf-8')
           item['updated_key'] = each['updated_key'].encode('utf-8')
           yield item