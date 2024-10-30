"""Модуль установок."""
from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']

NEWSPIDER_MODULE = SPIDER_MODULES

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).resolve().parent.parent

RESULTS = 'results'

results_dir = BASE_DIR / RESULTS
results_dir.mkdir(exist_ok=True)

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
