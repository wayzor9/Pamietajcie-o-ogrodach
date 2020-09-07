from django.core.management.base import BaseCommand

from plants.models import Picture
from plantID.utils import PlantIdClient


class Command(BaseCommand):
    help = "Send last uploaded plant image to PlantId backend"

    def handle(self, *args, **kwargs):

        picture_obj = Picture.objects.latest("created")
        picture_path = picture_obj.image.path

        client = PlantIdClient()
        client.identify_plant(picture_path)
