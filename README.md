# Виджет банковских операций

## Описание
Проект предназначен для фильтрации и сортировки банковских операций клиента. Он предоставляет инструменты для обработки данных в формате JSON (списки словарей).

## Установка
1. Клонируйте репозиторий:
   git clone https://github.com
2. Установите зависимости (если появятся в будущем):
   pip install -r requirements.txt

## Использование

### Фильтрация по статусу
Позволяет получить список операций с конкретным статусом (например, только успешные).

python
from src.processing import filter_by_state

data = [{'id': 1, 'state': 'EXECUTED'}, {'id': 2, 'state': 'CANCELED'}]
print(filter_by_state(data))  # По умолчанию EXECUTED
print(filter_by_state(data, 'CANCELED'))


### Сортировка по дате
Позволяет упорядочить операции от новых к старым или наоборот.

python
from src.processing import sort_by_date

data = [{'date': '2019-07-01'}, {'date': '2023-01-01'}]
print(sort_by_date(data)) # Сначала новые
