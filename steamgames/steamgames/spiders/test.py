# -*- coding: utf-8 -*-
import scrapy
from steamgames.items import SteamgamesItem


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['store.steampowered.com']
    start_urls = ['https://store.steampowered.com/search/?filter=globaltopsellers&os=win']

    def parse(self, response):
        node_list = response.xpath("//*[@id='search_resultsRows']/a")
        print(node_list)
        for node in node_list:
            item = SteamgamesItem()
            name = node.xpath("./div[2]/div[1]/span/text()").extract()
            link = node.xpath("./@href").extract()
            time = [i.replace(","," ") for i in node.xpath("./div[2]/div[2]/text()").extract()]
            evaluate = [j.replace(","," ") for j in [i.replace("<br>",",") for i in node.xpath("./div[2]/div[3]/span/@data-tooltip-html").extract()]]
            discount = node.xpath("./div[2]/div[4]/div[1]/span/text()").extract()
            price = [i.replace(",","") for i in node.xpath('normalize-space(./div[2]/div[4]/div[2])').extract()]

            item['name'] = name[0]
            item['link'] = link[0]
            try:
                item['time'] = time[0]
            except:
                item['time'] = 'See link for details'
            item['evaluate'] = evaluate[0]
            try:
                item['discount'] = discount[0]
            except:
                item['discount'] = 'No discount for now'
            item['price'] = price[0].strip()


            yield item

