from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Banner
from .serializers import BannerModelSerializer
from luffyapi.settings import constants

class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True,is_deleted=False).order_by('-orders','-id')[:constants.banner_length]
    serializer_class = BannerModelSerializer

