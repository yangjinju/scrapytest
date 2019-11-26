# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class ScrapytestPipeline(object):
    def __init__(self):
        self.f = open("豆瓣TOP250.csv", "w", newline="")
        self.writer = csv.writer(self.f)
        self.writer.writerow(["title", "img", "评分"])

    def process_item(self, item, spider):
        # 保存到csv文件中
        title = item["title"]
        img = item["img"]
        rating_num = item["rating_num"]
        self.writer.writerow([title, img, rating_num])
        return item

