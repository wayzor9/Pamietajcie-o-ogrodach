from django.contrib import admin

from .models import Plant, ProfilePlant, CommonName, PlantPicture, Description

# Register your models here.


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ("name", "plantId_id")
    search_fields = ("name",)


@admin.register(ProfilePlant)
class ProfilePlantAdmin(admin.ModelAdmin):
    list_display = ("plant", "user")
    ordering = ("plant",)


@admin.register(PlantPicture)
class PlantPictureAdmin(admin.ModelAdmin):
    list_display = ("plant", "profile_plant")
    search_fields = ("plant",)


admin.site.register(CommonName)
admin.site.register(Description)
