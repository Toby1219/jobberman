from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from jobber.spiders.jobberman import JobbermanSpider


def main():
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    process.crawl(JobbermanSpider)
    process.start()


if __name__ == '__main__':
    print('Waiting')
    #  schedule.every(2).seconds.do(main)
    # while True:
    #    schedule.run_pending()
    #    time.sleep(1)
    main()
