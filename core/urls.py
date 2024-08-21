from rest_framework.routers import DefaultRouter

from core.views import WellViewset


router = DefaultRouter()
router.register('data', WellViewset)

urlpatterns = [
    
] + router.urls
