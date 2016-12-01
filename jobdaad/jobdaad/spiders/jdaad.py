# -*- coding: utf-8 -*-
import linecache

import scrapy
from jobdaad.items import JobdaadItem
import json

class JdaadSpider(scrapy.Spider):
    name = "jdaad"
    #allowed_domains = ["https://www.daad.de/bundles/daadphdgermanyrise/data/js/offers.js?cb=20161126110000"]
    start_urls = ['https://www.daad.de/bundles/daadphdgermanyrise/data/js/offers.js?/']

    def parse(self, response):
       # fp = open('1.html','w')
       # fp.write(response.body.replace('var offers = TAFFY(', '').replace(');', ''))
       # fp.close()
       item = JobdaadItem()
       jtaffy = response.body.replace('var offers = TAFFY(', '').replace(');', '')

       with open('data2.json', 'w') as fout:
           fout.write(jtaffy)
       fout.close()

       with open('data2.json', 'r') as fin:
           # data = f.readlines()
           data = json.load(fin)
       fin.close
       # count = linecache.getlines('data2.json')
       # linecache.clearcache()
       # data = json.load('data2.json')
       for each in data:
           print each['code']
           item['code'] = each['code']
           item['created'] = each['created']
           item['contactadresszusatz'] = each['contactadresszusatz']
           item['contactasprache'] = each['contactasprache']
           item['contactasprache_key'] = each['contactasprache_key']
           item['contactasprache_value'] = each['contactasprache_value']
           item['contactdsprache'] = each['contactdsprache']
           item['contactdsprache_key'] = each['contactdsprache_key']
           item['contactdsprache_value'] = each['contactdsprache_value']
           item['contactemail'] = each['contactemail']
           item['contactfax'] = each['contactfax']
           item['contactfirstname'] = each['contactfirstname']
           item['contactinstitution'] = each['contactinstitution']
           item['contactlastname'] = each['contactlastname']
           item['contactlogo'] = each['contactlogo']
           item['contactorganisation'] = each['contactorganisation']
           item['contactort'] = each['contactort']
           item['contactplz'] = each['contactplz']
           item['contactposition'] = each['contactposition']
           item['contactstrasse'] = each['contactstrasse']
           item['contacttelefon'] = each['contacttelefon']
           item['contacttitel'] = each['contacttitel']
           item['contactunterlagen'] = each['contactunterlagen']
           item['contactunterlagen_key'] = each['contactunterlagen_key']
           item['contactunterlagen_value'] = each['contactunterlagen_value']
           item['contactunterlagenotherde'] = each['contactunterlagenotherde']
           item['contactunterlagenotheren'] = each['contactunterlagenotheren']
           item['contacturl'] = each['contacturl']
           item['contactvoraussetzungde'] = each['contactvoraussetzungde']
           item['contactvoraussetzungen'] = each['contactvoraussetzungen']
           item['created'] = each['created']
           item['created_key'] = each['created_key']
           item['offerangebotsurl'] = each['offerangebotsurl']
           item['offeranzahl'] = each['offeranzahl']
           item['offerbeginn'] = each['offerbeginn']
           item['offerbeginn_key'] = each['offerbeginn_key']
           item['offerbeginn_value'] = each['offerbeginn_value']
           item['offerbeschreibungde'] = each['offerbeschreibungde']
           item['offerbeschreibungen'] = each['offerbeschreibungen']
           item['offerdauer'] = each['offerdauer']
           item['offerdauerde'] = each['offerdauerde']
           item['offerdaueren'] = each['offerdaueren']
           item['offerdeadline'] = each['offerdeadline']
           item['offerdeadline_key'] = each['offerdeadline_key']
           item['offerdeadline_value'] = each['offerdeadline_value']
           item['offerfachgebietde'] = each['offerfachgebietde']
           item['offerfachgebieten'] = each['offerfachgebieten']
           item['offerfachrichtung'] = each['offerfachrichtung']
           item['offerfachrichtung_key'] = each['offerfachrichtung_key']
           item['offerfachrichtung_value'] = each['offerfachrichtung_value']
           item['offerfinanzierung'] = each['offerfinanzierung']
           item['offerfinanzierung_key'] = each['offerfinanzierung_key']
           item['offerfinanzierung_value'] = each['offerfinanzierung_value']
           item['offerpromotion'] = each['offerpromotion']
           item['offerpromotion_key'] = each['offerpromotion_key']
           item['offerpromotion_value'] = each['offerpromotion_value']
           item['offertitelde'] = each['offertitelde']
           item['offertitelen'] = each['offertitelen']
           item['updated'] = each['updated']
           item['updated_key'] = each['updated_key']
           yield item