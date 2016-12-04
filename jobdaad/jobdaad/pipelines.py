# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as pymysql


def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='****',
        charset='utf8',
        use_unicode=False
    )
    return conn

class JobdaadPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        sql
        return item
