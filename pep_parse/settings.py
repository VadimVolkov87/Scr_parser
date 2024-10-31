"""Модуль установок."""
from pathlib import Path

BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'

SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).resolve().parent.parent

RESULTS = 'results'

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
