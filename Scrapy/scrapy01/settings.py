# Scrapy settings for scrapy01 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy01'

SPIDER_MODULES = ['scrapy01.spiders']
NEWSPIDER_MODULE = 'scrapy01.spiders'

DATABASE={'drivername':'xxx','username':'tony','password':'violin','database':'aaa'}

ITEM_PIPELINES={'scrapy01.pipelines.Scrapy01Pipeline':300}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy01 (+http://www.yourdomain.com)'
