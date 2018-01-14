# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy.mail import MailSender
from secrets import mail_username, mail_password


class AvtonetspiderPipeline(object):

    def open_spider(self, spider):
        self.file = open('db/' + spider.name, 'a+')
        self.known_cars = set()
        self.new_cars = []
        for line in self.file:
            self.known_cars.add(line.split('|')[0])

    def process_item(self, item, spider):
        if item['id'] in self.known_cars:
            raise DropItem("Known car found: %s" % item['id'])
        else:
            self.new_cars.append(item['link'])
            line = item['id'] + '|' + item['link'] + "\n"
            self.file.write(line)
            return item

    def close_spider(self, spider):
        self.file.close()
        mailer = MailSender(
            mailfrom=mail_username,
            smtphost="smtp.gmail.com",
            smtpport=465,
            smtpuser=mail_username,
            smtppass=mail_password,
            smtpssl=True
        )
        if len(self.new_cars) > 0:
			links = '\n'.join(self.new_cars)
            mailer.send(
                to=[spider.mail_to],
                subject="New cars for you - " + str(len(self.new_cars)) + " - " + spider.name,
                body=links + "----------------------------\n" + "All cars from this category: " + spider.start_urls[0]
            )
