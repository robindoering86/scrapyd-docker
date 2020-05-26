# -*- coding: utf-8 -*-

# Scrapy settings for cloud_test project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'cloud_test'

SPIDER_MODULES = ['cloud_test.spiders']
NEWSPIDER_MODULE = 'cloud_test.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cloud_test (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'cloud_test.middlewares.CloudTestSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'cloud_test.middlewares.CloudTestDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'cloud_test.pipelines.CloudTestPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

DOWNLOADER_MIDDLEWARES = {
    'scrapoxy.downloadmiddlewares.proxy.ProxyMiddleware': 100,
    'scrapoxy.downloadmiddlewares.wait.WaitMiddleware': 101,
    'scrapoxy.downloadmiddlewares.scale.ScaleMiddleware': 102,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 700,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 701,
}

ITEM_PIPELINES = {
    'cloud_test.pipelines.MongoPipeline': 300,
}

MONGO_USER = os.getenv('MONGO_USER')
MONGO_PW = os.getenv('MONGO_PW')
MONGO_DATABASE = os.getenv('MONGO_DATABASE')
MONGO_URI = f"mongodb+srv://{MONGO_USER}:{MONGO_PW}@cluster0-vshap.mongodb.net/csrdata?retryWrites=true&w=majority"
CONCURRENT_REQUESTS_PER_DOMAIN = 1
RETRY_TIMES = 0

PROXY = os.getenv('PROXY')
#PROXY = 'http://18.197.33.132:8888/?noconnect'
#PROXY = 'http://localhost:8888/?noconnect'

API_SCRAPOXY = os.getenv('API_SCRAPOXY')
#API_SCRAPOXY = 'http://18.197.33.132:8889/api'
#API_SCRAPOXY = 'http://localhost:8889/api'

API_SCRAPOXY_PASSWORD = os.getenv('API_SCRAPOXY_PASSWORD')


