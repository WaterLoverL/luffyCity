from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Banner
from .serializers import BannerModelSerializer,NavModelSerializer
from luffyapi.settings import constants

class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True,is_deleted=False).order_by('-orders','-id')[:constants.banner_length]
    serializer_class = BannerModelSerializer


from .models import Nav
class HeaderNavListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, is_deleted=False,position=1).order_by('-orders', '-id')[:constants.head_nav_length]
    serializer_class = NavModelSerializer


class FooterNavListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, is_deleted=False,position=2).order_by('-orders', '-id')[:constants.foot_nav_length]
    serializer_class = NavModelSerializer