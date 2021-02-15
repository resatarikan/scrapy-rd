# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:52:10 2021

@author: Richard Gold
"""

import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.ckitchen.com/allpoints-fmp/parts-a-to-z/a.html']

    def parse(self, response):
        for title in response.css('.oxy-post-title'):
            yield {'title': title.css('::text').get()}
            

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)