import base64
import requests

from django.conf import settings

from .signals import plantid_backend_response


class PlantIdClient:
    def __init__(self):
        self.api_key = settings.PLANTID_API_KEY
        self.identification_url = "https://api.plant.id/v2/identify"
        self.usage_info_url = "https://api.plant.id/v2/usage_info"

    def check_usage_info(self):
        endpoint = self.usage_info_url
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            endpoint, headers=headers, auth=("client", self.api_key)
        )
        return response.json()

    def encode_files(self, file_name):
        with open(file_name, "rb") as file:
            file64 = base64.b64encode(file.read()).decode("ascii")
        return file64

    def identify_plant(self, file_names):
        images = self.encode_files(file_names)

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
