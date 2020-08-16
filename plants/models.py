from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Plant(models.Model):
    plantId_id = models.IntegerField()
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, plantId: {self.plantId_id}"


class ProfilePlant(models.Model):
    user = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True, null=True, blank=True)
    # location

    def __str__(self):
        return f"Profile plant: {self.user}, {self.plant}"


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plant = models.ManyToManyField(Plant, through=ProfilePlant)

    # weather = models.ForeignKey(User, on_delete=models.CASCADE)
    # location

    def __str__(self):
        return f"Profile owner: {self.user}"


class CommonName(models.Model):
    name = models.CharField(max_length=200)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PlantPicture(models.Model):
    image = models.ImageField()
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    profile_plant = models.ForeignKey(ProfilePlant, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True, null=True, blank=True)


DURATION = (("Annual", "Annual"), ("Biennial", "Biennial"), ("Perennial", "Perennial"))

TOXICITY = (("None", "None"), ("Low", "Low"), ("Medium", "Medium"), ("High", "High"))


class Description(models.Model):
    plant = models.OneToOneField(Plant, on_delete=models.CASCADE)
    description = models.TextField()

    # specifications
    duration = models.CharField(max_length=9, choices=DURATION, blank=True, null=True)
    growth_habit = models.CharField(max_length=250, blank=True, null=True)
    growth_rate = models.CharField(max_length=250, blank=True, null=True)
    average_height = models.CharField(max_length=250, blank=True, null=True)
    maximum_height = models.CharField(max_length=250, blank=True, null=True)
    toxicity = models.CharField(max_length=6, choices=TOXICITY, blank=True, null=True)

    # growth
    sowing = models.CharField(max_length=250, blank=True, null=True)
    ph_maximum = models.DecimalField(
        max_digits=3, decimal_places=2, blank=True, null=True
    )
    ph_minimum = models.DecimalField(
        max_digits=3, decimal_places=2, blank=True, null=True
    )
    light = models.IntegerField(blank=True, null=True)  # 0 > 10
    atmospheric_humidity = models.IntegerField(blank=True, null=True)
    growth_months = models.CharField(max_length=200, blank=True, null=True)
    bloom_months = models.CharField(max_length=200, blank=True, null=True)
    fruit_months = models.CharField(max_length=200, blank=True, null=True)
    minimum_precipitation = models.CharField(max_length=250, blank=True, null=True)
    maximum_precipitation = models.CharField(max_length=250, blank=True, null=True)
    minimum_temperature = models.CharField(max_length=250, blank=True, null=True)
    soil_nutriments = models.IntegerField(blank=True, null=True)  # 0 > 10
    soil_salinity = models.IntegerField(blank=True, null=True)  # 0 > 10
    soil_texture = models.IntegerField(blank=True, null=True)  # 0 > 10
    soil_humidity = models.IntegerField(blank=True, null=True)  # 0 > 10

    def __str__(self):
        return f"{self.plant.name}"
