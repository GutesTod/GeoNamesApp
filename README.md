# TestTaskInfotecs
__Программа для тестового задания "Программист Python" в "Инфотекс"__
## Установка
1. Клонируйте репозиторий на свой компьютер: `git clone https://github.com/GutesTod/TestTaskInfotecs.git`
2. Установите необходимые зависимости: `pip install -r requirements.txt`
3. Запустите скрипт: `python script.py`
## API
Основная задача API - предоставления информации по географическим объектам. Данные взять из географической базы данных GeoNames
### Описание методов
|Метод|Описание метода|Пример|
| ----- | --------------- | ------ |
|GET /api/city/<int:geonameid>|Возвращение информации о городе по идентификатору geonameid|http://localhost:8000/api/city/10106491
| `GET /api/cities?page=__?__&per_page=__?__` | Возвращание списка городов с их информацией, принимая параметры: page - страница, per_page - количество отображаемых на странице городов | http://localhost:8000/api/cities?page=1&per_page=10 |
| `GET /api/two-cities?city1_name=__?__&city2_name=__?__` | Получение информации о городах из параметров city1_name и city2_name, а также указывает какой из них расположен севернее и одинаковая ли у них временная зона | http://localhost:8000/api//api/two-cities?city1_name=Москва&city2_name=Уфа |
| `GET /api/suggest-city?name=__?__` | Возращание вариантов городов, которые начинаются с заданной подстроки | http://localhost:8000/api/suggest-city?name=Мос |
