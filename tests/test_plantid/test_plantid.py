import base64
import pytest
import requests

from unittest.mock import patch, Mock, MagicMock

from plantID.utils import PlantIdClient


class CheckUsageRequestMock():
    def json(self):
        return {"requestes_available": 99}


class IdentifyPlantRequestMock():
    def __init__(self, json_data):
        self.json_data = json_data
    
    def json(self):
        return self.json_data


@patch.object(requests, "post")
def test_usage_info(post_mock, plant_client):
    post_mock.return_value = CheckUsageRequestMock()
    assert plant_client.check_usage_info() == {"requestes_available": 99}


def test_plantid_client_initialization(plant_client):
    assert plant_client

def test_image_encoding(plant_client, image_file):
    a = PlantIdClient.encode_files(image_file)
    with open(image_file, "rb") as file:
            file64 = base64.b64encode(file.read()).decode("ascii")
    assert a == file64

@patch.object(PlantIdClient, "encode_files", return_value="test")
@patch.object(requests, "post")
def test_identify_plant(requests_mock, encode_mock, plant_client, backend_response):
    requests_mock.return_value = IdentifyPlantRequestMock(backend_response)
    assert plant_client.identify_plant(encode_mock, encode64=True) == [
                                                                        'Camellia japonica', 
                                                                        'Rosa',
                                                                        'Paeonia',
                                                                        'Rosa chinensis',
                                                                        'Paeonia officinalis',
                                                                        'Hibiscus syriacus', 
                                                                        'Hibiscus rosa-sinensis',
                                                                        'Paeonia lactiflora',
                                                                        'Alcea rosea'
                                                                        ]

    requests_mock.assert_called()

@patch.object(requests, "post")
def test_identify_plant_encode_false(requests_mock, image_file, plant_client, backend_response):
    requests_mock.return_value = IdentifyPlantRequestMock(backend_response)
    assert plant_client.identify_plant(image_file, encode64=False) == [
                                                                        'Camellia japonica', 
                                                                        'Rosa',
                                                                        'Paeonia',
                                                                        'Rosa chinensis',
                                                                        'Paeonia officinalis',
                                                                        'Hibiscus syriacus', 
                                                                        'Hibiscus rosa-sinensis',
                                                                        'Paeonia lactiflora',
                                                                        'Alcea rosea'
                                                                        ]
