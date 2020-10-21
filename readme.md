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
Information entropy is used in the paper to release the problem of consistency of distribution of data, Researchers can collect their data in their own distribution under our definition of features. <br>
The raw data which calculated with information entropy are store in "data"

## Install

numpy 1.18.5 <br>
openv-python 4.4.0 <br>
tensorflow 2.3.1 <br>
keras 2.4.3 <br>

### Extract prior konwledge from multiple linear regression, Exmaple
      run inputs_train.py
      
### Feature Transfer, Example
      run FBTNN.py
      
### Eval data, Example
      run eval.py

### Expansibility
the well trained model is store in data. <br>
the work you should do is write a model in mmodel.py and extend the model(we have three models for you to learn). Simply, you can do the following things to get a new model
      step 1: collect the data and calculte the information entropy under our definition of features.
      step 2: find the folloing code in FBTNN.py - Line 62 
      base_model = load_model('./model/three_scale_sh_h3.h5').get_layer(index=0)  # please change the model-name to "*_tl_*_l.h5" in /FBTNN/model/
      step 3: find the folloing code in FBTNN.py - Line 89 
      model.save("three_scale_tl_h2_l.h5") # please change the model-name as you want

Alternative, you can feed your own data in the "FBTNN.py" can also get a good result.
