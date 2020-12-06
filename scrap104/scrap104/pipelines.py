# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class Scrap104Pipeline:
    def process_item(self, item, spider):
        item['title'] = item['title'].replace(',', '')
        item['salary'] = item['salary'].replace(',', '')
        
        with open(r"D:\104data.csv", 'a') as file:  
            file.write('%s,' %item['title'])
            file.write('%s,' %item['company'])
            file.write('%s,' %item['region'])
            file.write('%s,' %item['salary'])
            file.write('%s,' %item['competitor'])
            file.write('%s\n' %item['link'])
        
        return item
    
    
    
    
    
    
    
    
    
    
    
    
    

