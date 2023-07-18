from django.urls import path, include

from rest_framework import routers

from .views import Category1Viewset, Category2Viewset, Product2Viewset, Product1Viewset, CommentViewset, TeamViewset, PartnerViewset, InformationViewset, StatistikaViewset, ConnectioViewset,\
Category1AdminViewset,Category2AdminViewset,CommentAdmminViewset,TeamAdmminViewset,Product1AdmminViewset,Product2AdmminViewset,PartnerAdmminViewset,\
    StatistikaAdminViewset

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
router.register('category1admin', Category1AdminViewset, basename='category1admin')
router.register('category2admin', Category2AdminViewset, basename='category2admin')
router.register('product1admin', Product1AdmminViewset, basename='product1admin')
router.register('product2admin', Product2AdmminViewset, basename='product2admin')
router.register('partneradmin', PartnerAdmminViewset, basename='partneradmin')
router.register('teamadmin', TeamAdmminViewset, basename='teamadmin')
router.register('statistikaadmin', StatistikaAdminViewset, basename='statistikaadmin')
router.register('commentadmin', CommentAdmminViewset, basename='commentadmin')
router.register('connectionsadmin', ConnectioViewset, basename='connectionsadmin')


urlpatterns = [
    path('', include(router.urls))
]