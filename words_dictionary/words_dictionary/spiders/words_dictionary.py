#!/usr/bin/env python
# coding: utf-8

# In[35]:

import scrapy

class wordsForGame(scrapy.Spider):
    name = 'words_bank'
    
    start_urls = ['https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/']
    
    def parse(self, response):
        
        temp = response.css('div.field-item.even') # focus only on the part of site that holds the words
        wordList = temp.css('p::text').getall()
        wordList.remove('a')
        for word in wordList:
            yield{"word" : word}
        

# In[ ]:







