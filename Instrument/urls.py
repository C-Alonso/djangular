from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Instrument import views


router = DefaultRouter()
router.register('sections', views.SectionViewset)
router.register('instruments', views.InstrumentViewset)


app_name = 'instrument'

urlpatterns = [
    path('', include(router.urls))
]
