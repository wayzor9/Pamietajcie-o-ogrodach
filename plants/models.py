from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel


class Plant(TimeStampedModel):
    name = models.CharField(max_length=200)
    plant = models.ManyToManyField(settings.AUTH_USER_MODEL, through="ProfilePlant")

    def __str__(self):
        return self.name


class ProfilePlant(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_plant_profile",
    )
    plant = models.ForeignKey(
        Plant, on_delete=models.CASCADE, related_name="plant_profile"
    )

    def __str__(self):
        return f"Profile plant: {self.user}, {self.plant}"


class CommonName(TimeStampedModel):
    name = models.CharField(max_length=200)
    plant = models.ForeignKey(
        Plant, on_delete=models.CASCADE, related_name="common_name"
    )

    def __str__(self):
        return self.name


class Picture(TimeStampedModel):
    image = models.ImageField()
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    profile_plant = models.ForeignKey(ProfilePlant, on_delete=models.CASCADE)


class Description(TimeStampedModel):
    ANNUAL = "AL"
    BIENNIAL = "BL"
    PERENNIAL = "PL"
    DURATION_CHOICES = [
        (ANNUAL, "Annual"),
        (BIENNIAL, "Biennial"),
        (PERENNIAL, "Perennial"),
    ]

    NONE = "NO"
    LOW = "LO"
    MEDIUM = "MD"
    HIGH = "HI"

    TOXICITY_CHOICES = [
        (NONE, "Annual"),
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),
    ]

    plant = models.OneToOneField(Plant, on_delete=models.CASCADE)
    description = models.TextField()

    # specifications
    duration = models.CharField(max_length=2, choices=DURATION_CHOICES, blank=True)
    growth_habit = models.CharField(max_length=250, blank=True)
    growth_rate = models.CharField(max_length=250, blank=True)
    average_height = models.CharField(max_length=250, blank=True)
    maximum_height = models.CharField(max_length=250, blank=True)
    toxicity = models.CharField(
        max_length=2, choices=TOXICITY_CHOICES, blank=True, default=NONE
    )

    # growth
    sowing = models.CharField(max_length=250, blank=True, null=True)
    ph_maximum = models.DecimalField(
        max_digits=3, decimal_places=2, blank=True, null=True
    )
    ph_minimum = models.DecimalField(
        max_digits=3, decimal_places=2, blank=True, null=True
    )
    light = models.IntegerField(blank=True, null=True)  # 0 > 10
    atmospheric_humidity = models.IntegerField(blank=True)
    growth_months = models.CharField(max_length=200, blank=True)
    bloom_months = models.CharField(max_length=200, blank=True)
    fruit_months = models.CharField(max_length=200, blank=True)
    minimum_precipitation = models.CharField(max_length=250, blank=True)
    maximum_precipitation = models.CharField(max_length=250, blank=True)
    minimum_temperature = models.CharField(max_length=250, blank=True)
    soil_nutriments = models.IntegerField(blank=True, null=True)  # 0 > 10
    soil_salinity = models.IntegerField(blank=True, null=True)  # 0 > 10
    soil_texture = models.IntegerField(blank=True, null=True)  # 0 > 10
    soil_humidity = models.IntegerField(blank=True, null=True)  # 0 > 10

    def __str__(self):
        return f"{self.plant.name}"


class Service(TimeStampedModel):
    name = models.CharField(max_length=200)
    internal_id = models.IntegerField()
    external_id = models.IntegerField()
