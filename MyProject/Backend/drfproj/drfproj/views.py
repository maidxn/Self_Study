# import imp
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drfapp.serializers import HeroSerializer
from drfapp.models import Hero

class TesView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Hero.objects.all()
        hero = qs.first()
        serializer = HeroSerializer(hero)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)