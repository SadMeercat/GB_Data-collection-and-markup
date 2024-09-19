import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.xpath('//article[@class="product_pod"]')
        for book in books:
            yield {
                'title': book.xpath('.//h3/a/@title').get(),
                'price': book.xpath('.//div[@class="product_price"]/p[@class="price_color"]/text()').get(),
                'availability': book.xpath('.//div[@class="product_price"]/p[@class="instock availability"]/text()').getall()[-1].strip(),
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

        # scrapy crawl books -o books.json

