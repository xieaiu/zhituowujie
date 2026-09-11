import scrapy
import re


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["www.cosrx.com"]
    start_urls = ["https://www.cosrx.com/collections/all"]

    def parse(self, response):
        #用最后一页的页码确定总页数，并拼接链接
        last_page = response.xpath('//div[@class="container pagination-row"]/div/span[last()-1]/a[1]/text()').extract_first()
        for page in range(int(last_page)+1):
            page_href = self.start_urls[0] + f'?page={page}'
            yield scrapy.Request(url=page_href, callback=self.parse_goods)

    def parse_goods(self, response):
        #解析每一页的商品链接
        goods_href_list = response.xpath('//div[@class="product-info"]/div/div/a[@class="product-link"]/@href').extract()
        for good_href in goods_href_list:
            goods_href = response.urljoin(good_href)
            # print(goods_href)
            yield scrapy.Request(url=goods_href, callback=self.parse_goods_details)

    def parse_goods_details(self, response):
        name = response.xpath('//h1[@class="title"]/text()').extract_first()
        price = response.xpath('//span[@class="current-price theme-money"]/text()').extract_first()
        image_list = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " main-image ")]'
            '//div[contains(concat(" ", normalize-space(@class), " "), " product-media--image ")]'
            '/ancestor::a[contains(concat(" ", normalize-space(@class), " "), " show-gallery ")][1]/@href'
        ).getall()
        video_templates = response.xpath(
            '//div[contains(concat(" ", normalize-space(@class), " "), " main-image ")]'
            '//script[contains(concat(" ", normalize-space(@class), " "), " product-media__video-template ")]/text()'
        ).getall()
        video_html = ''.join(video_templates)
        video_list = re.findall(r'<source[^>]+src=["\']([^"\']+)["\']', video_html)
        video_imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', video_html)
        image_list.extend(video_imgs)
        details_text = '\n'.join(response.xpath('//main//p//text()').getall())
        key_ingredients = re.search(r'Key Ingredients?\s*:\s*([^\r\n]+)', details_text, re.I)
        size = re.search(r'Size\s*:\s*([^\r\n]+)', details_text, re.I)
        key_ingredients = key_ingredients.group(1).strip() if key_ingredients else None
        size = size.group(1).strip() if size else None
        yield {
            'name': name,
            'price': price,
            'image_list': image_list,
            'video_list': video_list,
            'key_ingredients': key_ingredients,
            'size': size
        }
