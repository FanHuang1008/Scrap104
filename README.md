# Scrap104
Since collecting job description or internship information from the internet can be time-consuming and boring, I decided to create a web crawler to do this task for me.

Before I modified the JobdesSpider, I defined what kind of data I wanted to extract. I opened the items.py file and added six fields under the Item class.

Although I had a hard time finding the link for next page, I realized that I can jump to whichever page I want by changing the parameter ‘page’ in the url, so I used a for loop to go through the first twenty pages. In addition, I assigned the keyword to the key_word variable so that I don’t have to modify the start_urls in the future. 

There were two sections I modified in the settings.py file. First, I set FEED_EXPORT_ENCODING to utf-8 to solve the Chinese encoding problem. Second, I changed the value of ITEM_PIPELINES to 300 to enable the pipelines.py file. 

In the pipelines.py file, I removed the comma in both job title and salary. 
