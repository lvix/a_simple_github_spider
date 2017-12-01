#!/usr/bin/env python3 

import scrapy 

class simple_github_spider(scrapy.Spider):

    name = 'simpe_github_spider'

    @property
    def start_urls(self):
        
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,4))

    def parse(self, response):
        for item in response.xpath('//*[@id="user-repositories-list"]/ul/li'):
            yield{
                "name": item.xpath('div[1]/h3/a/text()').re_first('[\s*](\S.*)'),
                "update_time": item.xpath("div[3]/relative-time/@datetime").extract_first()
                }

