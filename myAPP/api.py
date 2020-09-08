from rest_framework import routers

from plants.views import PictureViewSet


router = routers.DefaultRouter()
router.register("images", PictureViewSet)
urlpatterns = router.urls
