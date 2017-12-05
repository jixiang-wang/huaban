
根据自定义关键词，下载图片

今天我们来爬取一个图片网站花瓣网，写一个比较简单的图片下载的爬虫;   
    
    
![image](https://github.com/xiangge93/huaban/raw/master/images/迪丽热巴.png)
    
    
图片太多了，只截了这些图片，大概几千张；
对，没错，就是你们喜欢的胖迪，
1、首先分析一下花瓣网图片的加载方式
打开花瓣网首页，搜索“迪丽热巴”，
![image](https://github.com/xiangge93/huaban/raw/master/images/第一页加载的20张图片.png)    



下拉加载出第二页的图片时弹出登录框，只有登录账号才可以继续加载后面的所有图片；   
![image](https://github.com/xiangge93/huaban/raw/master/images/第二页加载的20张图片.png)    

    
    
可以看出，花瓣网的图片加载是异步加载的方式，这时我们可以选择selenium模拟登录网页模仿浏览器的操作不断的下拉加载出所有的图片；
2、主要思想：
首先要登录账号，输入要搜索的图片，每次下拉加载出当前页面的图片后，提取对于图片的url存到一个列表里，由于每页图片是20张，所以我这里在下载图片的时候也是每次存20个url就去下载对应的这20张图片；
3、准备工作：
安装selenium的库，pip或者下载到本地安装都OK；
下面是安装Phantomjs或者Chrome      
chromedriver的安装路径：     

![image](https://github.com/xiangge93/huaban/raw/master/images/chromedriver的安装路径.png)     


phantomjs的安装路径：     
![image](https://github.com/xiangge93/huaban/raw/master/images/phantomjs的安装路径.png)         

具体下载可自行百度，或者参考下面的博客，这里感谢这位博主      

[在Windows下安装PIP+Phantomjs+Selenium](http://blog.csdn.net/eastmount/article/details/47785123）
