import pytest
import requests
import os
import json
from lib.const import BASE_URL
from http import HTTPStatus
import logging


logger = logging.getLogger()


class TestShipDetailsByNameAPI:
    TEST_DATA_DIR = "test_data"
    DEVASTATOR_DATA_FILE = "devastator_data.json"
    logger.setLevel(logging.DEBUG)

    def test_ship_filtering_by_name_positive(self):
        """
        Verifying happy path test when a query results in an expected response
        """
        payload = {
            """ 
            Whatever the query should look like.
            Format was not specified in the documentation.
            """
            "name": "Devastator"
        }

        with open(os.path.join(self.TEST_DATA_DIR, self.DEVASTATOR_DATA_FILE), 'r') as f:
            test_data = json.load(f.read())

        response = requests.get(url=BASE_URL, params=payload)
        logger.log(msg="HTTP CODE: {}".format(response.status_code))
        logger.log(msg="RESPONSE JSON: {}".format(response.json()))

        assert response.status_code == HTTPStatus.OK, \
            "Expected status code is {}, recieved {}".format(HTTPStatus.OK, response.status_code)

        assert test_data == response.json(), "Unexpected data: {}".format(response.json())

    def test_ship_filtering_by_name_empty_set(self):
        """
        Verifying happy path test when a query results in an empty set
        """
        payload = {
            """ 
            Whatever the query should look like.
            Format was not specified in the documentation.
            """
            "name": "Some not existing ship name"
        }

        response = requests.get(url=BASE_URL, params=payload)
        logger.log(msg="HTTP CODE: {}".format(response.status_code))
        logger.log(msg="RESPONSE JSON: {}".format(response.json()))

        # Presumably it will return HTTP 200, but depends on the spec code could be changed.
        assert response.status_code == HTTPStatus.OK, \
            "Expected status code is {}, recieved {}".format(HTTPStatus.OK, response.status_code)

        # Should return an empty spec
        assert [] == response.json(), "Unexpected data: {}".format(response.json())

    def test_ship_filtering_by_name_incorrect_input(self):
        """
        Verifying happy path test when a query results in an empty set
        """
        payload = {
            """ 
            Whatever the query should look like.
            Format was not specified in the documentation.
            """
            "name": "'bla' or 1=1;–"
        }

        response = requests.get(url=BASE_URL, params=payload)
        logger.log(msg="HTTP CODE: {}".format(response.status_code))
        logger.log(msg="RESPONSE JSON: {}".format(response.json()))

        # Presumably it will return HTTP 400, but depends on the spec code could be changed.
        assert response.status_code == HTTPStatus.BAD_REQUEST, \
            "Expected status code is {}, recieved {}".format(HTTPStatus.BAD_REQUEST, response.status_code)

        # Should return an empty spec
        assert not response.json(), "Unexpected data: {}".format(response.json())


