# -*- coding: utf-8 -*-
import scrapy

from scrapytest import items

'''
豆瓣 Top 250
https://movie.douban.com/top250?start=0&filter=
'''

domain = "https://movie.douban.com/top250"


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['movie.douban.com']
    start_urls = [domain + '?start=0&filter=']  ## 可以分析是否有下一页

    # 获取到网页返回的数据
    def parse(self, response):
        li_list = response.xpath("//ol[contains(@class,'grid_view')]/li")
        print("长度：", len(li_list))
        for li in li_list:
            item = items.MovieItem()
            title = li.xpath(".//div[@class='item']/div[@class='info']/div[@class='hd']/a/span/text()").extract_first()
            img = li.xpath(".//div[@class='item']/div[@class='pic']/a/img/@src").extract_first()
            rating_num = str(li.xpath(
                ".//div[@class='item']/div[@class='info']/div[@class='bd']/div/span[@class='rating_num']/text()").extract_first()).strip()

            print("title:", title)
            print("img:", img)
            print("rating_num:", rating_num)
            item['title'] = title
            item['img'] = img
            item['rating_num'] = rating_num
            yield item

            # 获取下一页在超链接
            # nextUrl = response.xpath("//*[@id='page-container']/div/ul/li[7]/a").extract_first()
        nextUrl = response.xpath("//span[contains(@class,'next')]/a/@href").extract_first()
        print("nextUrl", nextUrl)
        if nextUrl != "javascript:;":
            yield scrapy.Request(url=domain + nextUrl, callback=self.parse)
