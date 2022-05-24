import scrapy
from apkmirror.items import ApkmirrorItem


class ApkmirrorSpider(scrapy.Spider):
    name = 'apkmirror_spider'
    allowed_domains = ['apkmirror.com']
    start_urls = ['https://www.apkmirror.com/uploads/page/1/']

    def parse(self, response):
        apk_links = response.xpath(
            '//a[@class="fontBlack"]/@href').extract()
        if apk_links:
            page_num = response.meta.get('page_num')
            if page_num is None:
                next_page_link = response.url + '/page/2/'
                page_num = 2
            else:
                page_num += 1
                splitted = response.url.split('/')[:5]
                splitted.append(str(page_num))
                next_page_link = '/'.join(splitted)
            yield response.follow(
                next_page_link,
                callback=self.parse,
                meta={
                    'page_num': page_num,
                 },
            )
        for apk_link in apk_links:
            yield response.follow(
                apk_link,
                callback=self.parse_apk_details,
            )

    def parse_apk_details(self, response):
        apk_item = ApkmirrorItem()
        apk_link = response.url

        download_link = response.xpath(
            '///a[@class="downloadLink"]/@href').extract_first()

        array_of_data = response.xpath(
            '//div[@class="infoSlide t-height"]/'
            'p/span[@class="infoSlide-value"]/text()').extract()
        if len(array_of_data) >= 4:
            for data in array_of_data[:4]:
                if 'mb' in data.lower():
                    apk_item['file_size'] = data
                elif 'gmt' in data.lower():
                    apk_item['uploaded'] = data
                elif data.count('.') >= 2:
                    apk_item['version'] = data
                else:
                    apk_item['downloads'] = data

        apk_item['apk_link'] = apk_link
        apk_item['download_link'] = download_link
        yield apk_item
