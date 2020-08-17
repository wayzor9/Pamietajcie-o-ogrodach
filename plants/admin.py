from django.contrib import admin

from .models import CommonName, Description, Picture, Plant, ProfilePlant, Service


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ProfilePlant)
class ProfilePlantAdmin(admin.ModelAdmin):
    list_display = ("plant", "user")
    ordering = ("plant",)


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ("plant", "profile_plant")
    search_fields = ("plant",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "internal_id", "external_id")
    search_fields = ("plant",)


admin.site.register(CommonName)
admin.site.register(Description)
