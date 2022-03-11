import scrapy
valid = True
offset = 1


class NewsSpider(scrapy.Spider):
    name = "news"

    def start_requests(self):
        global valid
        urls = [
            'https://weeklyworldnews.com/category/headlines/'
        ]

        for url in urls:
            valid = True
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        global offset
        allLinks = response.css('.entry-title a::attr(href)').getall()

        for each_link in allLinks:
            yield scrapy.Request(each_link, callback=self.parse_href)

        if valid:
            next_page = 'https://weeklyworldnews.com/category/headlines/page/'
            offset += 1
            next_page = next_page + str(offset) + '/'
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_href(self, response):
        global valid
        yearsList = ['2021', '2020', '2019', '2018']
        available = False
        date = response.css('.entry-date::text').get()
        if date is not None:
            for year in yearsList:
                if year in date:
                    available = True
                    break
        if available:
            title = response.css('.entry-title::text').get()
            title = title.replace('\n', '')
            title = title.replace('\t', '')
            paragraph = response.css('.entry-content p::text').getall()
            text = ''
            count = 0
            for sentence in paragraph:
                if count == 3:
                    break
                sentence = sentence.replace('\xa0', '')
                sentence = sentence.replace('\n', '')
                sentence = sentence.replace('\r', '')
                sentence = sentence.replace('\t', '')
                if sentence != "":
                    text = text + sentence
                    count += 1
            yield {
                'date': date,
                'title': title,
                'text': text,
                'is_fake': 1
            }
        elif date is not None:
            valid = False
