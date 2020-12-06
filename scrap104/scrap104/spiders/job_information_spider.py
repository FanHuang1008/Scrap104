# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 13:37:32 2020

@author: 黃凡
"""
# job_information_spider

import scrapy
from scrap104.items import Scrap104Item

key_word = '數據分析'  
class JobInfSpider(scrapy.Spider):
    name = 'JobInf_list'  
    allowed_domains = ['www.104.com.tw']
    start_urls = ['https://www.104.com.tw/jobs/search/?keyword=%s&area=6001001000&page=1&jobsource=2018indexpoc&ro=0' %key_word]
    
    def parse(self, response):
        
        articles = response.xpath("//article[@class='b-block--top-bord job-list-item b-clearfix js-job-item ']")
        for article in articles:            
            Information = Scrap104Item()
            
            Information['title'] = article.attrib['data-job-name']
            Information['company'] = article.attrib['data-cust-name']
            Information['region'] = article.xpath(".//div[@class='b-block__left']//ul[@class='b-list-inline b-clearfix job-list-intro b-content']//li/text()").extract_first()
            Information['salary'] = article.xpath(".//div[@class='b-block__left']//div//span/text()").extract_first()
            Information['competitor'] = article.xpath(".//div[@class='b-block__right b-pos-relative']//a/text()").extract_first()
            Information['link'] = article.xpath(".//div[@class='b-block__left']//h2//a").attrib['href']
            yield Information
        
        # different pages
        for i in range(2,21):    
            url = 'https://www.104.com.tw/jobs/search/?keyword=%s&area=6001001000&page=%s&jobsource=2018indexpoc&ro=0' %(key_word, str(i))
            yield scrapy.Request(url, self.parse)
            
            
            
  
            
