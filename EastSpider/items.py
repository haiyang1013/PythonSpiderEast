# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EastspiderItem(scrapy.Item):
    # define the fields for your item here like:

    # 与eastspider.py 定义的一一对应
    title = scrapy.Field() #标题
    price_final = scrapy.Field() #价格
    price_original = scrapy.Field()  # 原价格
    color = scrapy.Field() #颜色
    size = scrapy.Field() #尺码
    sku = scrapy.Field() #网站货号
    details = scrapy.Field() #详情
    img_urls = scrapy.Field() #大图的URL

    # pass
