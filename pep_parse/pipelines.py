"""Модуль пайплайна для обработки результатов."""
import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS = 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    """Класс пайплайна для обработки результатов парсинга."""

    def open_spider(self, spider):
        """Функция создания словаря для результатов."""
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        """Функция подсчета статусов."""
        self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        """Функция записи результатов в файл."""
        results_dir = BASE_DIR / RESULTS
        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            csv.writer(f, dialect=csv.unix_dialect, quoting=csv.QUOTE_NONE
                       ).writerows((('Статус', 'Количество'),
                                   *self.results.items(),
                                   ('Итого', sum(self.results.values())), ))
