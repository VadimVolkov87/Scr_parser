"""Модуль для определения items приложения."""
import scrapy


class PepParseItem(scrapy.Item):
    """Класс для определения атрибутов item."""

    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
