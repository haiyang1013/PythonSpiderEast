# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

from EastSpider.items import EastspiderItem


class eastspider(scrapy.spiders.CrawlSpider):
    name = 'eastspider'
    allowed_domains = ['eastbay.com']
    start_urls = ['https://www.eastbay.com/category/sale.html?query=sale%3Arelevance%3AstyleDiscountPercent%3ASALE%3Agender%3AMen%27s%3Abrand%3AASICS+Tiger']
    rules = (
        Rule(LinkExtractor(allow='/product/asics-tiger.+.html$'), callback='parseContent', follow=True),
    )

    def parseContent(self, response):
        print("----------已爬取成功--------------")
        print(response.url)
        # 创建item字段对象， 用来存储信息
        item = EastspiderItem()
        title = response.xpath("//span[@class='ProductName-primary']/text()").extract_first()
        price_final = response.xpath("//span[@class='ProductPrice-final']/text()").extract_first()
        price_original = response.xpath("//span[@class='ProductPrice-original']/text()").extract_first()
        color = response.xpath("//p[@class='ProductDetails-form__label']/text()").extract_first()
        size = response.xpath("//div[@class='ProductSize']/label/span/text()").extract()
        sku = response.xpath("//div[@id='ProductDetails-tabs-details-panel']/text()").extract()
        details = response.xpath("//div[@class='ProductDetails-description']").extract()
        img_urls = response.xpath("//span[@class='c-image--square']/span/img/@src").extract()

        item['title'] = title
        item['price_final'] = price_final
        item['price_original'] = price_original
        item['color'] = color
        item['size'] = size
        item['sku'] = "#"+sku[1]
        item['details'] = details
        item['img_urls'] = img_urls

        # 返回提取到的每一个item数据 给管道文件处理，同时还会回来继续执行后面的代码
        yield item


