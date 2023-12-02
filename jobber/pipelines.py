# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JobberPipeline:
    def process_item(self, item, spider):
        return item


class CleanJob:
    def process_item(self, item, spider):
        item['job_tittle'] = self.clean_data(item['job_tittle'])
        item['commpany_Name'] = self.clean_data(item['commpany_Name'])
        item['sector'] = self.clean_data(item['sector'])
        item['pay'] = self.clean_data(item['pay'])
        item['minimum_qualification'] = self.clean_data(item['minimum_qualification'])
        item['experience_level'] = self.clean_data(item['experience_level'])
        item['experience_length'] = self.clean_data(item['experience_length'])
        item['responsibilities'] = self.clean_data(item['responsibilities'])
        item['requirements'] = self.clean_data(item['requirements'])
        return item

    def clean_data(self, text):
        try:
            chars = ['\n', '#', '$']
            for char in chars:
                if char in text:
                    value = text.replace(char, '').strip()
                    return value
                else:
                    return text
        except:
            pass