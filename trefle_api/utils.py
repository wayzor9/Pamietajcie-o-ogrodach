import requests
import urllib.parse

from django.conf import settings

import pprint

pp = pprint.PrettyPrinter(indent=4)

name = "Fraxinus Pennsylvanica"


class ClientTrefleApi:
    def __init__(self):
        self.api_key = settings.TREFLE_API_KEY
        self.base_search_url = "https://trefle.io/api/v1/plants/search?q="
        self.name = name

    def parsed_name(self, name):
        return urllib.parse.quote(name)

    def get_resource(self):
        plant_name = self.name
        parse_name = self.parsed_name(plant_name)
        search_endpoint = f"{self.base_search_url}{parse_name}&token={self.api_key}"
        r = requests.get(search_endpoint).json()
        return r

    def get_detail_info(self):
        '''
        Get detail info link stored in get_resource response and request the data
        link: '/api/v1/plants/fraxinus-pensylvannica'
        '''
        resource = self.get_resource()
        detail_link = resource["data"][0]["links"]["plant"]
        detail_info_endpoint = f"https://trefle.io{detail_link}?token={self.api_key}"
        r = requests.get(detail_info_endpoint).json()
        # pp.pprint(r)
        return r

    def get_field_info(self, key=None, field_name=None, field_key=None):
        """
        :param key: growth or specifications
        :param field_name: all plant.description model fields
        :param field_key: e.g. 'minimum_temperature': {'deg_f': -47, 'deg_c': -43},
        """
        response_dict = self.get_detail_info()
        field_value = response_dict["data"]["main_species"][f"{key}"][f"{field_name}"]
        return field_value

    def get_sowing_value(self):
        """
        get value of specified field
        """
        return self.get_field_info(key="growth", field_name="sowing")
