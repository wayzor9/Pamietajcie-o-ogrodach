import requests
import urllib.parse

from django.conf import settings

import pprint

pp = pprint.PrettyPrinter(indent=4)


class ClientTrefleApi:
    def __init__(self):
        self.api_key = settings.TREFLE_API_KEY
        self.base_search_url = "https://trefle.io/api/v1/plants/search?q="


    def parsed_name(self, name):
        return urllib.parse.quote(name)

    def get_resource(self, plant_name):
        parse_name = self.parsed_name(plant_name)
        search_endpoint = f"{self.base_search_url}{parse_name}&token={self.api_key}"
        r = requests.get(search_endpoint).json()
        return r

    def get_detail_info(self, plant_name):
        '''
        Get detail info link stored in get_resource response and request the data
        link: '/api/v1/plants/fraxinus-pensylvannica'
        '''
        resource = self.get_resource(plant_name)
        detail_link = resource["data"][0]["links"]["plant"]
        detail_info_endpoint = f"https://trefle.io{detail_link}?token={self.api_key}"
        r = requests.get(detail_info_endpoint).json()
        # pp.pprint(r)
        return r
