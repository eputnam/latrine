from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Place, Resource
from .serializers import PlaceSerializer


class AllPlaces(APIView):
    """
    Listing all places.
    """
    def get(self, request, format=None):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)


class ResourceList(APIView):
    """
    Filtering places against resource types passed in the URL.
    """
    def get_resources(self, resource_type):
        allowed = ["showers", "restrooms"]
        try:
            resource_list = resource_type.split('+')
            for r in resource_list:
                if r not in allowed:
                    raise Http404
            requested_recources = Resource.objects.filter(facility_type__in=resource_list)
            return set(Place.objects.filter(resources__in=requested_recources))  # set() shows distinct results
        except Resource.DoesNotExist:
            raise Http404

    def get(self, request, resource_type, format=None):
        selected_places = self.get_resources(resource_type)
        serializer = PlaceSerializer(selected_places, many=True)
        return Response(serializer.data)
