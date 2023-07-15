from django.urls import path, include

from rest_framework import routers

from .views import Category1Viewset, Category2Viewset, Product2Viewset, Product1Viewset, CommentViewset, TeamViewset, PartnerViewset, InformationViewset, StatistikaViewset, ConnectioViewset

router = routers.DefaultRouter()

router.register('category1', Category1Viewset, basename='categroy1')
router.register('category2', Category2Viewset, basename='categroy2')
router.register('product1', Product1Viewset, basename='product1')
router.register('product2', Product2Viewset, basename='product2')
router.register('comment', CommentViewset, basename='comment')
router.register('team', TeamViewset, basename='team')
router.register('partner', PartnerViewset, basename='partner')
router.register('information', InformationViewset, basename='information')
router.register('statistika', StatistikaViewset, basename='statistika')
router.register('connection', ConnectioViewset, basename='connection')

urlpatterns = [
    path('', include(router.urls))
]