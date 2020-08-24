import base64
import requests

from django.conf import settings

PLANTID_API_KEY = getattr(settings, "PLANTID_API_KEY", None)


class PlantIdClient:
    def __init__(self):
        self.api_key = PLANTID_API_KEY
        self.identification_url = "api.plant.id/v2/identify"
        self.usage_info_url = "https://api.plant.id/v2/usage_info"

    def check_usage_info(self):
        endpoint = self.usage_info_url
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            endpoint, headers=headers, auth=("client", self.api_key)
        )
        return response.json()

    def encode_files(self, file_names):
        files_encoded = []
        for file_name in file_names:
            with open(file_name, "rb") as file:
                files_encoded.append(base64.b64encode(file.read()).decode("ascii"))
        return files_encoded

    def identify_plant(self, file_names):
        images = self.encode_files(file_names)

        params = {
            "api_key": self.api_key,
            "images": images,
            "modifiers": ["crops_fast", "similar_images"],
            "plant_language": "en",
            "plant_details": [
                "common_names",
                "url",
                "name_authority",
                "wiki_description",
                "taxonomy",
                "synonyms",
            ],
        }

        headers = {"Content-Type": "application/json"}

        response = requests.post(self.identification_url, json=params, headers=headers)

        return response.json()
