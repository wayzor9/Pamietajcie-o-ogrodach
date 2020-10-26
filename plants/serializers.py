from rest_framework import serializers

from plantID.utils import PlantIdClient
from plants.models import Picture, Description
from trefle_api.schemas import FinalSchema
from trefle_api.utils import ClientTrefleApi


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ("image",)

    def create(self, validated_data):
        plantid_client = PlantIdClient()
        trefle_client = ClientTrefleApi()
        img = validated_data['image']
        obj_img = img.file
        if not isinstance(obj_img, bytes):
            obj_img = plantid_client.encode_file(obj_img)
        plant_names = plantid_client.identify_plants(obj_img)
        plant_name_parsed = trefle_client.parsed_name(plant_names[0])
        get_trefleapi_endpoint = trefle_client.get_resource(plant_name_parsed)
        get_plant_data = trefle_client.get_detail_info(plant_name_parsed)
        deserialized_data = FinalSchema(get_plant_data)

        description = "tralala tralala"
        #create Description object
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
        #specifications
        average_height = deserialized_data['data']['main_species']['specifications']['average_height']['cm']
        growth_habit = deserialized_data['data']['main_species']['specifications']['growth_habit']
        growth_rate = deserialized_data['data']['main_species']['specifications']['growth_rate']
        maximum_height = deserialized_data['data']['main_species']['specifications']['maximum_height']['cm']
        toxicity = deserialized_data['data']['main_species'['specifications']['toxicity']

        description_obj = Description.objects.create(
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
            toxicity=toxicity
        )
        Picture.objects.create(image=obj_img, plant=description_obj)
        latest_obj = Picture.objects.latest('created')
        return latest_obj
