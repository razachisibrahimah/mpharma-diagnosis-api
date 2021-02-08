from rest_framework import routers
from .api import DxcodeViewSet

router = routers.DefaultRouter()

router.register('api/dxcodes', DxcodeViewSet, 'dxcodes')

urlpatterns = router.urls