"""Модуль парсера приложения."""
import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Класс паука приложения."""

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Функция парсинга ссылок на страницы Pep."""
        pep_links = response.css('tbody tr td a::attr(href)').getall()
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Функция для парсинга страниц Pep."""
        number_name = ' '.join(t.strip() for t in response.css(
            'h1.page-title::text'
        ).getall()).strip().split(' – ')
        data = {
            'number': number_name[0].split()[1],
            'name': number_name[1],
            'status': response.css('dl dd abbr::text').get()
        }
        yield PepParseItem(data)
