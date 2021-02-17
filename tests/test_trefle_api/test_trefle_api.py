import pytest
import requests
import urllib.parse

from unittest.mock import patch, Mock, MagicMock

from trefle_api.utils import ClientTrefleApi


class GetResponseMock():
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


class GetDetailInfoMock():
    def __init__(self, data):
        self.data = data

    def json(self):
        return self.data


def test_terfle_client_init(trefle_client):
    assert trefle_client

def test_parse_plant_name(trefle_client, plant_name):
    parse_name = urllib.parse.quote(plant_name)
    assert parse_name == trefle_client.parsed_name(plant_name)

@patch.object(ClientTrefleApi, "parsed_name", return_value="fraxinus-test")
@patch.object(requests, "get")
def test_get_resource(get_mock, parse_mock, trefle_client, plant_name, get_resource_backend_resp):
    get_mock.return_value = GetResponseMock(get_resource_backend_resp)
    assert trefle_client.get_resource(plant_name)["data"][0]["links"]["plant"] == '/api/v1/plants/fraxinus-pennsylvanica'
    assert trefle_client.get_resource(plant_name)["data"][0]["image_url"] == 'https://bs.floristic.org/image/o/92e034dda311bcc34a497da70e2bc2fb2e554f17'


@patch.object(ClientTrefleApi, "get_resource", return_value={
    'data': [
        {'links': {
            'plant': '/api/v1/plants/fraxinus-pennsylvanica'
            }}
        ]
    })
@patch.object(requests, "get")
def test_get_detail_info(get_mock2, resource_mock, trefle_client, plant_name, get_detail_info_backend_response):
    get_mock2.return_value = GetDetailInfoMock(get_detail_info_backend_response)
    assert trefle_client.get_detail_info(plant_name)["data"]["main_species"]["growth"]["light"] == 10
    # breakpoint()
    assert trefle_client.get_detail_info(plant_name)["data"]["main_species"]["specifications"]['average_height']['cm'] == 1500

