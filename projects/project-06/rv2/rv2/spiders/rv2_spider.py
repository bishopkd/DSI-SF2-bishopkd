from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy

# item models
from rv2.items import RV2Item

class RV2Spider(CrawlSpider):

	name = "rv2"
	allowed_domains = ["craigslist.org"]
	start_urls = [
      'https://newyork.craigslist.org/search/sss?query=rv',
      'https://losangeles.craigslist.org/search/sss?query=rv',
      'https://chicago.craigslist.org/search/sss?query=rv',
      'https://houston.craigslist.org/search/sss?query=rv',
      'https://philadelphia.craigslist.org/search/sss?query=rv',
      'https://phoenix.craigslist.org/search/sss?query=rv',
      'https://sanantonio.craigslist.org/search/sss?query=rv',
      'https://sandiego.craigslist.org/search/sss?query=rv',
      'https://dallas.craigslist.org/search/sss?query=rv',
      'https://austin.craigslist.org/search/sss?query=rv',
      'https://jacksonville.craigslist.org/search/sss?query=rv',
      'https://sanfrancisco.craigslist.org/search/sss?query=rv',
      'https://indianapolis.craigslist.org/search/sss?query=rv',
      'https://columbus.craigslist.org/search/sss?query=rv',
      'https://charlotte.craigslist.org/search/sss?query=rv',
      'https://detroit.craigslist.org/search/sss?query=rv',
      'https://elpaso.craigslist.org/search/sss?query=rv',
      'https://seattle.craigslist.org/search/sss?query=rv'
	]

	rules = (
		Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback="parse_search", follow = True),

	)


	def parse_search(self, response):


        	for sel in response.xpath("//div[@class='rows']"):

	            item = RV2Item()
	            item['title'] =  sel.xpath("//span[@class='price']/text()").extract()[0]
	            item['price'] =  sel.xpath('//a[@class="hdrlnk"]/text()').extract()[0]
	            yield item

