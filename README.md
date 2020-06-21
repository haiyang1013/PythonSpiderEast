# PythonSpiderEast
用Python通过 scrapy 实现网页信息爬取和采集。
windows环境，已安装Python-38
1.升级python pip :
python -m pip install --upgrade pip
2.通过pip安装Scrapy：
pip install Scrapy

报异常
pip install F:\Users\Desktop\Twisted-20.3.0-cp38-cp38-win32.whl

3.创建Scrapy项目

scrapy startproject EastSpider

在当前目录下创建scrapy项目

4.创建写爬虫的文件
scrapy genspider eastspider "eastbay.com"

5.分析、解析网页
观察网页，通过浏览器得出他们是这样子的结构，并且我们运用强大的xpath解析方式解析：

6.编写代码

需要编写四个相关联的文件： itcast.py    items.py    settings.py    pipelines.py (管道文件)

7.结果展示
执行文命令行： scrapy crawl  + 爬虫文件的名称(eastspider)


爬取数据遇到的部分问题
1.反机器人爬取
# Obey robots.txt rules settings.py
ROBOTSTXT_OBEY = False
2.爬取页面是Http Status 403
# Crawl responsibly by identifying yourself (and your website) on the user-agent settings.py
USER_AGENT = 'EastSpider (+https://www.eastbay.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
3.多个网页爬取，spider需继承
