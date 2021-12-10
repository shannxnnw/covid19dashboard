import csv

def parse_csv_data():
    """ opens,reads and outputs the csv file containing national covid stats """
    with open('nation_2021-10-28.csv', 'r') as file:
        covid_data_reader = csv.reader(file)
        for row in covid_data_reader:
            print(row)

from uk_covid19 import Cov19API

def covid_API_request():
    """ this function uses the covid-19 api to display filtered news headlines
    surrounding the Exeter area
    """
    from requests import get
    from json import dumps


    ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
    location_type = "ltla"
    location = "Exeter"

    filters = [
        f"areaType={ AREA_TYPE }",
        f"areaName={ AREA_NAME }"
    ]

    structure = {
        "date": "date",
        "name": "areaName",
        "code": "areaCode",
        "dailyCases": "newCasesByPublishDate",
        "cumulativeCases": "cumCasesByPublishDate",
        "dailyDeaths": "newDeaths28DaysByPublishDate",
        "cumulativeDeaths": "cumDeaths28DaysByPublishDate"
    }

    api_params = {
        "filters": str.join(";", filters),
        "structure": dumps(structure, separators=(",", ":"))
    }


    response = get(ENDPOINT, params=api_params, timeout=10)

    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')

    print(response.url)
    print(response.json())

