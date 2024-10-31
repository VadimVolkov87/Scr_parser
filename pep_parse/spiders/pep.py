"""Модуль парсера приложения."""
import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Класс паука приложения."""

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        """Метод парсинга ссылок на страницы Pep."""
        for pep_link in response.css('tbody tr td a::attr(href)').getall():
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Метод для парсинга страниц Pep."""
        number_names = ' '.join(t.strip() for t in response.css(
            'h1.page-title::text'
        ).getall()).strip().split(' – ')
        yield PepParseItem(
            number=number_names[0].split()[1],
            name=number_names[1],
            status=response.css('dl dd abbr::text').get(),
        )
