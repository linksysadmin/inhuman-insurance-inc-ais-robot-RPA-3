from typing import List

from robocorp import workitems
from robocorp.tasks import task
from RPA.HTTP import HTTP
from RPA.JSON import JSON
from RPA.Tables import Tables

http = HTTP()  # The RPA.HTTP library provides the download() function for downloading the JSON file.
json = JSON()
table = Tables()

TRAFFIC_JSON_FILE_PATH = "output/traffic.json"

# JSON data keys
COUNTRY_KEY = "SpatialDim"
YEAR_KEY = "TimeDim"
RATE_KEY = "NumericValue"
GENDER_KEY = "Dim1"


@task
def produce_traffic_data():
    """
    Inhuman Insurance, Inc. Artificial Intelligence System automation.
    Produces traffic data work items.
        - downloads raw traffic data.
        - converts raw data into business data format.
        - stores business data as work items that can be used later.
    """
    http.download(
        url="https://github.com/robocorp/inhuman-insurance-inc/raw/main/RS_198.json",
        target_file=TRAFFIC_JSON_FILE_PATH,
        overwrite=True,
    )
    traffic_data = load_traffic_data_as_table()
    filtered_data = filter_and_sort_traffic_data(traffic_data)
    filtered_data = get_latest_data_by_country(filtered_data)
    # table.write_table_to_csv(filtered_data, "output/test.csv")
    payloads = create_work_item_payloads(filtered_data)
    save_work_item_payloads(payloads)


def load_traffic_data_as_table():
    json_data = json.load_json_from_file(TRAFFIC_JSON_FILE_PATH)
    table_from_json = table.create_table(json_data["value"])
    return table_from_json


def filter_and_sort_traffic_data(data):
    max_rate = 5.0
    both_genders = "BTSX"
    table.filter_table_by_column(data, RATE_KEY, "<", max_rate)
    table.filter_table_by_column(data, GENDER_KEY, "==", both_genders)
    table.sort_table_by_column(data, YEAR_KEY, False)
    return data


def get_latest_data_by_country(data):
    data = table.group_table_by_column(data, COUNTRY_KEY)
    latest_data_by_country = []

    for group in data:
        first_row = table.pop_table_row(group)
        latest_data_by_country.append(first_row)

    return latest_data_by_country


def create_work_item_payloads(traffic_data) -> List:
    """
     Function loops the list of traffic data - essentially rows.
     For each row, you create a new dictionary (a data structure that supports named keys).
     You append the dictionaries to a list that you then return from the keyword.

    :param traffic_data:
    :return:
    """
    payloads = []
    for row in traffic_data:
        payload = dict(
            country=row[COUNTRY_KEY],
            year=row[YEAR_KEY],
            rate=row[RATE_KEY]
        )
        payloads.append(payload)
    return payloads


def save_work_item_payloads(payloads):
    """
    Takes the list of payloads as an argument and saves each payload as a work item
    :param payloads:
    :return:
    """
    for payload in payloads:
        variables = dict(traffic_data=payload)
        workitems.outputs.create(variables)  # creates a new output work item. We store our payload as a dictionary with the given variable name
