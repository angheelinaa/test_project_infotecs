from abc import ABC
from pytz import timezone
from datetime import datetime


class Table(ABC):
    NAME = 0
    ASCII_NAME = 1
    ALTERNATE_NAMES = 2
    LATITUDE = 3
    LONGITUDE = 4
    FEATURE_CLASS = 5
    FEATURE_CODE = 6
    COUNTRY_CODE = 7
    CC2 = 8
    ADMIN1_CODE = 9
    ADMIN2_CODE = 10
    ADMIN3_CODE = 11
    ADMIN4_CODE = 12
    POPULATION = 13
    ELEVATION = 14
    DEM = 15
    TIMEZONE = 16
    MODIFICATION_DATE = 17
    fields = {
        'NAME': 0,
        'ASCII_NAME': 1,
        'ALTERNATE_NAMES': 2,
        'LATITUDE': 3,
        'LONGITUDE': 4,
        'FEATURE_CLASS': 5,
        'FEATURE_CODE': 6,
        'COUNTRY_CODE': 7,
        'CC2': 8,
        'ADMIN1_CODE': 9,
        'ADMIN2_CODE': 10,
        'ADMIN3_CODE': 11,
        'ADMIN4_CODE': 12,
        'POPULATION': 13,
        'ELEVATION': 14,
        'DEM': 15,
        'TIMEZONE': 16,
        'MODIFICATION_DATE': 17
    }

    @classmethod
    def build_data(cls, row: list):
        result = {}
        for key, index in cls.fields.items():
            result.update({key: row[int(index)]})
        return result


def get_timezone_difference(tz1, tz2):
    if tz1 and tz2:
        time = datetime.now()
        return abs(timezone(tz2).localize(time) - timezone(tz1).localize(time)).seconds / 3600
    return 'no info'


def get_northern_city(first_name: str, second_name: str, first_city: dict, second_city: dict):
    if first_city and not second_city:
        return first_name.capitalize()
    if second_city and not first_city:
        return second_name.capitalize()
    if first_city and second_city:
        if float(first_city['LATITUDE']) > float(second_city['LATITUDE']):
            return first_name.capitalize()
        elif float(first_city['LATITUDE']) == float(second_city['LATITUDE']):
            return 'same latitude'
        return second_name.capitalize()
    return 'no info'
