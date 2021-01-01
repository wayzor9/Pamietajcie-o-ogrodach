import base64

from rest_framework import serializers

from django.conf import settings

from plantID.utils import PlantIdClient
from plants.models import Picture, Description, Plant, CommonName
from trefle_api.schemas import FinalSchema
from trefle_api.utils import ClientTrefleApi


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ("image",)

    def create(self, validated_data):
        user = validated_data.pop('user')
        plantid_client = PlantIdClient()
        trefle_client = ClientTrefleApi()
        schema = FinalSchema()

        searched_plant_name = "Rhododendron"
        get_plant_data = trefle_client.get_detail_info(searched_plant_name)
        deserialized_data = schema.load(get_plant_data)
        description = "TODO"
        duration = deserialized_data['data']['main_species']['duration']
        
        #growth
        atmospheric_humidity = deserialized_data['data']['main_species']['growth']['atmospheric_humidity']
        bloom_months = deserialized_data['data']['main_species']['growth']['bloom_months']
        fruit_months = deserialized_data['data']['main_species']['growth']['fruit_months']
        growth_months = deserialized_data['data']['main_species']['growth']['growth_months']
        light = deserialized_data['data']['main_species']['growth']['light']
        maximum_precipitation = deserialized_data['data']['main_species']['growth']['maximum_precipitation']['mm']
        minimum_precipitation = deserialized_data['data']['main_species']['growth']['minimum_precipitation']['mm']
        minimum_temperature = deserialized_data['data']['main_species']['growth']['minimum_temperature']['deg_c']
        ph_maximum = deserialized_data['data']['main_species']['growth']['ph_maximum']
        ph_minimum = deserialized_data['data']['main_species']['growth']['ph_minimum']
        soil_humidity = deserialized_data['data']['main_species']['growth']['soil_humidity']
        soil_nutriments = deserialized_data['data']['main_species']['growth']['soil_nutriments']
        soil_salinity = deserialized_data['data']['main_species']['growth']['soil_salinity']
        soil_texture = deserialized_data['data']['main_species']['growth']['soil_texture']
        sowing = deserialized_data['data']['main_species']['growth']['sowing']
        # #specifications
        average_height = deserialized_data['data']['main_species']['specifications']['average_height']['cm']
        growth_habit = deserialized_data['data']['main_species']['specifications']['growth_habit']
        growth_rate = deserialized_data['data']['main_species']['specifications']['growth_rate']
        maximum_height = deserialized_data['data']['main_species']['specifications']['maximum_height']['cm']
        toxicity = deserialized_data['data']['main_species']['specifications']['toxicity']
        #create objects
        picture_obj = super().create(validated_data)
        plant_obj = Plant.objects.create(name=searched_plant_name)
        plant_obj.plant.add(user)
        picture_obj.plant = plant_obj
        picture_obj.save()
        common_name_obj = CommonName(name=searched_plant_name, plant=plant_obj)
        description_data = dict(
            plant=plant_obj,
            description=description,
            duration=duration,
            atmospheric_humidity=atmospheric_humidity,
            bloom_months=bloom_months,  
            growth_months=growth_months, 
            fruit_months=fruit_months,
            light=light,
            maximum_precipitation=maximum_precipitation,
            minimum_precipitation=minimum_precipitation,
            minimum_temperature=minimum_temperature,
            ph_maximum=ph_maximum,
            soil_humidity=soil_humidity,
            ph_minimum=ph_minimum,
            soil_nutriments=soil_nutriments,
            soil_salinity=soil_salinity,
            soil_texture=soil_texture,
            sowing=sowing,
            average_height=average_height,
            growth_habit=growth_habit,
            growth_rate=growth_rate,
            maximum_height=maximum_height,
            toxicity=toxicity)

        description_obj_kwargs = {}

        for k, v in description_data.items():
            if v is not None:
                description_obj_kwargs[k] = v
            
        description_obj = Description.objects.create(**description_obj_kwargs)
        return picture_obj
