"""Модуль установок."""
from pep_parse.pipelines import RESULTS

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']

NEWSPIDER_MODULE = SPIDER_MODULES[0]

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    f'{RESULTS}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
