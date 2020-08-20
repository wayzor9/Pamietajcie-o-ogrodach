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
