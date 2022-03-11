import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"

    def start_requests(self):
        urls = [
            'https://www.naturalnews.com/all-posts.html'

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for post in response.css('div.f-tabbed-list-content'):
            yield {
                'headline': post.css('h2::text').get(),
                'article_link': post.css('h2 a::attr(href)').get(),
                'is_fake': 1
            }

        next_page = response.css('.pagination-next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)