from rest_framework import routers
from django.urls import path

from .views import PictureViewSet

app_name = "plants"


router = routers.SimpleRouter()
router.register("images", PictureViewSet)
urlpatterns = router.urls
