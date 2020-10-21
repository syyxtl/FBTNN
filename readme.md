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

## FBTNN， a model focus on residential location choice both in- and inter- cities
## Information entropy
information entropy is used in the paper to release the problem of consistency of distribution of data, Researchers can collect their data in their own distribution under our definition of features. 
## Install

numpy 1.18.5
openv-python 4.4.0
tensorflow 2.3.1
keras 2.4.3

### Extract prior konwledge from multiple linear regression, Exmaple
      run inputs_train.py
      
### Feature Transfer, Example
      run FBTNN.py
      
### Eval data, Example
      run eval.py

### Expansibility
the well trained model is store in data(we recommand three_scale_sh_h3.h5)
the work you should do is write a model in mmodel.py and extend the model(we have three models for you to learn)
