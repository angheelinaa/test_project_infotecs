# Project Geonames API

This is a FastAPI application that provides an API for retrieving information from the Geonames database. It utilizes a CSV file (`RU.txt`) as a mock database containing geographical data.

## Setup

1. Make sure you have Python and pip installed on your system.
2. Clone this repository to your local machine.
3. Install the required dependencies by running `pip install -r requirements.txt`.

## Running the Application

To start the FastAPI server, run the following command:

```bash
uvicorn main:app --reload
```

The server will be up and running at `http://localhost:8000`.

## Endpoints

1. `/geoinfo/{geoname_id}` - Get information about a city by its `geoname_id`.
2. `/page/page_number={page_number}/offset={offset}` - Get a paginated list of cities.
3. `/two_cities` - Get information about two cities, which of them is located to the north and whether they have the same time zone (their time difference).
4. `/name_matches` - Get  information about possible options for the continuation of the entered part of the city name

## How to Use

### Getting City Information by ID

Send a GET request to `/geoinfo/{geoname_id}`, where `geoname_id` is the ID of the city you want to retrieve information for.

#### Example

Request URL `http://127.0.0.1:8000/geoinfo/524894`

Response body:
```json
{
  "NAME": "Moskva",
  "ASCII_NAME": "Moskva",
  "ALTERNATE_NAMES": "Maskva,Moscou,Moscow,Moscu,Moscú,Moskau,Moskou,Moskovu,Moskva,Məskeu,Москва,Мәскеу",
  "LATITUDE": "55.76167",
  "LONGITUDE": "37.60667",
  "FEATURE_CLASS": "A",
  "FEATURE_CODE": "ADM1",
  "COUNTRY_CODE": "RU",
  "CC2": "",
  "ADMIN1_CODE": "48",
  "ADMIN2_CODE": "",
  "ADMIN3_CODE": "",
  "ADMIN4_CODE": "",
  "POPULATION": "13010112",
  "ELEVATION": "",
  "DEM": "161",
  "TIMEZONE": "Europe/Moscow",
  "MODIFICATION_DATE": "2023-01-12"
}
```

### Getting a Paginated List of Cities

Send a GET request to `/page/page_number={page_number}/offset={offset}`, providing the `page_number` and `offset` parameters for pagination.

#### Example

Request URL `http://127.0.0.1:8000/page/page_number=20/offset=4`

Response body:
```json
[
  {
    "451823": {
      "NAME": "Stupnevo",
      "ASCII_NAME": "Stupnevo",
      "ALTERNATE_NAMES": "Stupnevo,Ступнево",
      "LATITUDE": "57.08113",
      "LONGITUDE": "34.57708",
      "FEATURE_CLASS": "P",
      "FEATURE_CODE": "PPL",
      "COUNTRY_CODE": "RU",
      "CC2": "",
      "ADMIN1_CODE": "77",
      "ADMIN2_CODE": "",
      "ADMIN3_CODE": "",
      "ADMIN4_CODE": "",
      "POPULATION": "0",
      "ELEVATION": "",
      "DEM": "196",
      "TIMEZONE": "Europe/Moscow",
      "MODIFICATION_DATE": "2012-01-16"
    }
  },
  {
    "451824": {
      "NAME": "Stukshino",
      "ASCII_NAME": "Stukshino",
      "ALTERNATE_NAMES": "Stukshino,Стукшино",
      "LATITUDE": "56.68851",
      "LONGITUDE": "34.78528",
      "FEATURE_CLASS": "P",
      "FEATURE_CODE": "PPL",
      "COUNTRY_CODE": "RU",
      "CC2": "",
      "ADMIN1_CODE": "77",
      "ADMIN2_CODE": "",
      "ADMIN3_CODE": "",
      "ADMIN4_CODE": "",
      "POPULATION": "0",
      "ELEVATION": "",
      "DEM": "175",
      "TIMEZONE": "Europe/Moscow",
      "MODIFICATION_DATE": "2012-01-16"
    }
  },
  {
    "451825": {
      "NAME": "Strubishche",
      "ASCII_NAME": "Strubishche",
      "ALTERNATE_NAMES": "Strubishche,Strubishhe,Струбище",
      "LATITUDE": "57.16038",
      "LONGITUDE": "34.64929",
      "FEATURE_CLASS": "P",
      "FEATURE_CODE": "PPL",
      "COUNTRY_CODE": "RU",
      "CC2": "",
      "ADMIN1_CODE": "77",
      "ADMIN2_CODE": "",
      "ADMIN3_CODE": "",
      "ADMIN4_CODE": "",
      "POPULATION": "0",
      "ELEVATION": "",
      "DEM": "180",
      "TIMEZONE": "Europe/Moscow",
      "MODIFICATION_DATE": "2012-01-16"
    }
  },
  {
    "451826": {
      "NAME": "Stroyevichi",
      "ASCII_NAME": "Stroyevichi",
      "ALTERNATE_NAMES": "Stroevichi,Stroyevichi,Строевичи",
      "LATITUDE": "56.82265",
      "LONGITUDE": "34.80191",
      "FEATURE_CLASS": "P",
      "FEATURE_CODE": "PPL",
      "COUNTRY_CODE": "RU",
      "CC2": "",
      "ADMIN1_CODE": "77",
      "ADMIN2_CODE": "",
      "ADMIN3_CODE": "",
      "ADMIN4_CODE": "",
      "POPULATION": "0",
      "ELEVATION": "",
      "DEM": "197",
      "TIMEZONE": "Europe/Moscow",
      "MODIFICATION_DATE": "2012-01-16"
    }
  }
]
```

### Getting Information about Two Cities

Send a GET request to `/two_cities`, providing the names of the two cities you want to compare. The API will return information about the two cities and:

* `northern` - the city that is located to the north
* `timezone_difference` - True if the timezones of the cities differ; False if the timezones of cities are the same
* `the_difference_in_hours` - time difference between two cities in hours

#### Example

Request URL `http://127.0.0.1:8000/two_cities?first=Москва&second=Владивосток`

Response body:
```json
{
  "first_city": {
    "NAME": "Moskva",
    "ASCII_NAME": "Moskva",
    "ALTERNATE_NAMES": "Maskva,Moscou,Moscow,Moscu,Moscú,Moskau,Moskou,Moskovu,Moskva,Məskeu,Москва,Мәскеу",
    "LATITUDE": "55.76167",
    "LONGITUDE": "37.60667",
    "FEATURE_CLASS": "A",
    "FEATURE_CODE": "ADM1",
    "COUNTRY_CODE": "RU",
    "CC2": "",
    "ADMIN1_CODE": "48",
    "ADMIN2_CODE": "",
    "ADMIN3_CODE": "",
    "ADMIN4_CODE": "",
    "POPULATION": "13010112",
    "ELEVATION": "",
    "DEM": "161",
    "TIMEZONE": "Europe/Moscow",
    "MODIFICATION_DATE": "2023-01-12"
  },
  "second_city": {
    "NAME": "Vladivostok",
    "ASCII_NAME": "Vladivostok",
    "ALTERNATE_NAMES": "Bladibostok,Uladzivastok,VVO,Vladivostok,Vladivostoka,Vladivostokas,Vladivostokium,Vlagyivosztok,Wladiwostok,Wladywostok,Władywostok,beulladiboseutokeu,fladyfwstwk,hai can wai,hai can wei,urajiosutoku,vilativostok,vladivastak,vladivostoka,w la di wx s txkh,wladywstwk,wldywwstwq,Βλαδιβοστόκ,Владивосток,Уладзівасток,Վլադիվոստոկ,וולאדיוואסטאק,ולדיווסטוק,فلاديفوستوك,ولادیوستوک,ولادی‌وؤستؤک,ولادی‌وستوک,ولاڈیووسٹوک,व्लादिवोस्तॉक,व्लादिवोस्तोक,விலாடிவொஸ்டொக்,ವ್ಲಾಡಿವಾಸ್ಟಾಕ್,วลาดีวอสตอค,ვლადივოსტოკი,ウラジオストク,海参崴,海參崴,블라디보스토크",
    "LATITUDE": "43.10562",
    "LONGITUDE": "131.87353",
    "FEATURE_CLASS": "P",
    "FEATURE_CODE": "PPLA",
    "COUNTRY_CODE": "RU",
    "CC2": "",
    "ADMIN1_CODE": "59",
    "ADMIN2_CODE": "",
    "ADMIN3_CODE": "",
    "ADMIN4_CODE": "",
    "POPULATION": "604901",
    "ELEVATION": "",
    "DEM": "40",
    "TIMEZONE": "Asia/Vladivostok",
    "MODIFICATION_DATE": "2022-09-17"
  },
  "northern": "Москва",
  "timezone_difference": true,
  "the_difference_in_hours": 7
}
```

### Get a hint with possible options for continuing the name of the city 

Send a GET request to `/name_matches`.  The API will return a list with hints

#### Example

Request URL `http://127.0.0.1:8000/name_matches?subname=Екат`

Response body:
```json
[
  "Yekaterinovskiy Rayon",
  "Yekaterinoslavka",
  "Yekaterina",
  "Yekaterinino",
  "Vtoraya Yekaterinovka",
  "Derevnya Yekaterinovka",
  "Yekaterinovskiy",
  "Yekaterinki",
  "Yekaterinopol’ye",
  "Yekaterininskiy Kanal",
  "Yekaterinburg",
  "Yekaterinogradskaya",
  "Yekaterinoslavskiy",
  "Yekaterino-Nikol’skoye",
  "Yekateringof",
  "Yekaterinovskiy Plodopitomnik",
  "Yekaterinovka",
  "Yekaterinkino",
  "Yekaterininskoye",
  "Yekaterinskoye",
  "Yekaterininka",
  "Yekaterinovskaya"
]
```

## Note

For more convenient access to the above functions after starting the FastAPI server, you can open the automatic interactive API documentation (provided by Swagger UI). To do this, go to ` http://127.0.0.1:8000/docs`