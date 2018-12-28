import time
import scrapy
from scrapy.contrib.spiders import CrawlSpider
from ..items import TestItem


class TestSpider(CrawlSpider):
    name = 'test'
    t = {'html': []}
    start_urls = ['https://www.dior.com/it_it',
                  'https://www.dior.com/fr_fr',
                  'https://www.dior.com/en_us',
                  'https://www.dior.com/nl_be',
                  'https://www.dior.com/fr_be',
                  'https://www.dior.com/nl_nl',
                  'https://www.dior.com/de_de',
                  'https://www.dior.com/es_es',
                  ]
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'test.json'
    }


    def parse(self, response):
        for i in response.css('a.navigation-item-link::attr(href)').extract():
            print(i)
            yield scrapy.Request('https://www.dior.com'+i, callback=self.parse_html)

    def parse_html(self, response):
        value = ['€', '$']
        for div in response.css(
                'li.grid-view-element.is-product.one-column.legend-bottom'
                ' div.product.product-legend-bottom.product--cdcbase '):
            item = TestItem()
            i = div.css('a::attr(href)').extract()[0]
            item['region'] = str(response).split('/')[3]
            item['ierarch'] = str(response).split(item['region'])[-1]
            item['price'] = ''.join(div.css('span.price-line::text').extract()).replace('\xa0', '')
            item['valute'] = ''.join([i if i in item['price'] else '' for i in value])
            item['name'] = div.css('span.multiline-text::text').extract()
            start = time.time()
            request = scrapy.Request('https://www.dior.com' + i, callback=self.parse_item)
            request.meta['item'] = item
            request.meta['start'] = start
            yield request

    def parse_item(self, response):
        item = response.meta['item']
        item['description'] = response.css('div.product-tab-html::text').extract_first()
        item['article'] = response.url.split('-')[1]
        item['html'] = response.url
        item['time'] = str(time.time() - response.meta['start'])
        self.t['html'].append(item['html'])
        return item
