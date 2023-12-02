from typing import Iterable
from jobber.items import JobItem
import scrapy
from scrapy import Request
import csv


class JobbermanSpider(scrapy.Spider):
    name = "jobber"
    allowed_domains = ["www.jobberman.com"]

    def start_requests(self):
        urls = []
        with open('jobber/spiders/link.csv', 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                urls.append(row[0])
            for url in urls:
                yield scrapy.Request(str(url), callback=self.parse)

    def parse(self, response):
        item = JobItem()
        try:
            item['job_tittle'] = response.xpath('//*[@data-cy="title-job"]/text()').get()
            item['commpany_Name'] = response.css('h2.pb-1 a::text').get()
            item['sector'] = response.xpath('//h2[@class="text-sm font-normal"]/a/text()').get()
            item['pay'] = response.xpath('//span[@class="text-sm font-normal"]/text()').get()
            item['minimum_qualification'] = response.xpath('//span[@class="pb-1 text-gray-500"]/text()').get()
            item['experience_level'] = response.xpath('//li[2]/span[@class="pb-1 text-gray-500"]/text()').get()
            item['experience_length'] = response.xpath('//li[3]/span[@class="pb-1 text-gray-500"]/text()').get()
            item['responsibilities'] = response.xpath('//ul[1]/li[@style="word-break: break-word;"]/text()').getall()
            item['requirements'] = response.xpath('//ul[2]/li[@style="word-break: break-word;"]/text()').getall()
            yield item
        except:
            pass
