import base64
import requests
from io import BytesIO
from django.conf import settings

from .signals import plantid_backend_response


class PlantIdClient:

    identification_url = "https://api.plant.id/v2/identify"
    usage_info_url = "https://api.plant.id/v2/usage_info"

    def __init__(self, api_key=None, identification_url=None, usage_info_url=None):
        self.api_key = api_key or settings.PLANTID_API_KEY

    def check_usage_info(self):
        endpoint = self.usage_info_url
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            endpoint, headers=headers, auth=("client", self.api_key)
        )
        return response.json()

    @staticmethod
    def encode_files(file_name):
        with open(file_name, "rb") as file:
            file64 = base64.b64encode(file.read()).decode("ascii")
        return file64

    def identify_plant(self, file, encode64=False):
        if encode64:
            images = file
        else:
            images = encode_files(file)
            
        params = {
            "api_key": self.api_key,
            "images": [images],
            # "modifiers": ["similar_images"],
            "plant_details": [
                "common_names",
                "url",
                "name_authority",
                "taxonomy"
            ],
        }

        headers = {"Content-Type": "application/json"}
        response = requests.post(self.identification_url, json=params, headers=headers).json()
        # signal
        plantid_backend_response.send(
            sender=self.__class__
        )
        scientific_names = []
        for name in response["suggestions"]:
            a = name["plant_details"]["scientific_name"]
            scientific_names.append(a)
        return scientific_names
