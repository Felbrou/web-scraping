import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/notebooks"]

    def parse(self, response):
        
        products = response.css("div.ui-search-result__wrapper")

        for product in products:
            yield {
                'brand': product.css("span.poly-component__brand::text").get(),
                'name': product.css("a.poly-component__title::text").get()
            }