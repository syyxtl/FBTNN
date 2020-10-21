# DATA      
## SOURCE, The data are crawled in the following website
    https://sh.meituan.com/ ：SERVICE DATA
    https://www.dianping.com/ ：SERVICE DATA
    https://sh.lianjia.com/ ：HOUSE DATA  
    https://map.baidu.com/ ：COMMUTE DATA  
    MS DATA is relative secrecy

## Crawl the data with python & scrapy
scrapy is used to crawl the data(https://scrapy.org/)

The example is in the folder : "spider"

Considering that some websites like ‘https://sh.meituan.com/’ may set a series of anti-crawl mechanism, we suggest that you have the following work before you start to scrwal you own data

https://github.com/Python3WebSpider/ProxyPool

# Extract prior konwledge from multiple linear regression
      run inputs_train.py
      
# Feature Transfer
      run FBTNN.py
      
# Eval data
      run eval.py
