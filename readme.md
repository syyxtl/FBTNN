大标题  
===================================  
大标题一般显示工程名,类似html的\<h1\><br />  
你只要在标题下面跟上=====即可  
      
        
中标题  
-----------------------------------  
中标题一般显示重点项,类似html的\<h2\><br />  
你只要在标题下面输入------即可  
   
## 每级标题
用1～6个#加上空格代表没级标题 ，例如：

## 二级标题
### 三级标题
#### 四级表题
##### 五级标题
###### 六级标题
      
### 注意!!!下面所有语法的提示我都先用3级小标题提醒了!!!   
      
### The data are crawled in the following website   
    这是一个单行的文本框,只要两个Tab再输入文字即可  

# DATA      
## SOURCE
### The data are crawled in the following website     
    https://sh.meituan.com/ ：SERVICE DATA
    https://www.dianping.com/ ：SERVICE DATA
    https://sh.lianjia.com/ ：HOUSE DATA  
    https://map.baidu.com/ ：COMMUTE DATA  
    MS DATA is relative secrecy

## python scrapy
scrapy is used to crawl the data(https://scrapy.org/)

The example is in the folder : "spider"

Considering that some websites like ‘https://sh.meituan.com/’ may set a series of anti-crawl mechanism, we suggest that you have the following work before you start to scrwal you own data

https://github.com/Python3WebSpider/ProxyPool


