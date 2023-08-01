import csv
from fastapi import HTTPException, FastAPI
from utils import Table, get_timezone_difference, get_northern_city


app = FastAPI()

db = {}
with open('RU.txt', encoding='utf-8') as file:
    data = csv.reader(file, delimiter='\t')
    for row in data:
        db.update({row[0]: Table.build_data(row[1:])})


@app.get('/geoinfo/{geoname_id}')
def get_city_info(geoname_id: str):
    if geoname_id in db.keys():
        return db[geoname_id]
    raise HTTPException(status_code=404, detail='city not found')


@app.get('/page/page_number={page_number}/offset={offset}')
def get_page_cities(page_number: int, offset: int):
    if page_number > 0 and offset > 0:
        first_city = (page_number - 1) * offset
        last_city = page_number * offset
        return [{key: value} for key, value in list(db.items())[first_city:last_city]]
    raise HTTPException(status_code=404, detail='enter the correct page number and/or number of cities')


@app.get('/two_cities')
def get_two_cities(first: str, second: str):
    if first is None or second is None:
        raise HTTPException(status_code=404, detail='enter two cities')

    first_name = first.lower()
    second_name = second.lower()
    list_first_cities = []
    list_second_cities = []
    for value in db.values():
        if first_name in value['ALTERNATE_NAMES'].lower().split(','):
            list_first_cities.append(value)
        if second_name in value['ALTERNATE_NAMES'].lower().split(','):
            list_second_cities.append(value)

    list_first_cities.sort(key=lambda x: int(x['POPULATION']), reverse=True)
    list_second_cities.sort(key=lambda x: int(x['POPULATION']), reverse=True)
    first_city = list_first_cities[0] if len(list_first_cities) else {}
    second_city = list_second_cities[0] if len(list_second_cities) else {}

    northern_city = get_northern_city(first_name, second_name, first_city, second_city)
    time_diff = get_timezone_difference(first_city['TIMEZONE'] if first_city else '',
                                        second_city['TIMEZONE'] if second_city else '')
    return {
        'first_city': first_city if first_city else 'not found',
        'second_city': second_city if second_city else 'not found',
        'northern': northern_city,
        'timezone_difference': False if time_diff == 0 else True,
        'the_difference_in_hours': time_diff
    }


@app.get('/name_matches')
def name_matches(subname: str):
    if subname is None:
        raise HTTPException(status_code=404, detail='enter city')

    all_matches = set()
    subname = subname.lower()
    for value in db.values():
        for i in value['ALTERNATE_NAMES'].lower().split(','):
            if i.startswith(subname):
                all_matches.add(str(value['NAME']))
    return list(all_matches)
