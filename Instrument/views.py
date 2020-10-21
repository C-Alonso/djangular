from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status

from Instrument.models import Instrument, Section
from Instrument.serializers import InstrumentSerializer, \
                                   SectionSerializer
                                   


# The following decorator allows other domains (front-end)
# into our API methods.
@method_decorator(csrf_exempt, name='dispatch')
class SectionViewset(viewsets.ModelViewSet):    

    queryset = Section.objects.all()

    #api_root = reverse_lazy('api-root', request=request)

    serializer_class = SectionSerializer



@method_decorator(csrf_exempt, name='dispatch')
class InstrumentViewset(viewsets.ModelViewSet):

    queryset = Instrument.objects.all()

    serializer_class = InstrumentSerializer
