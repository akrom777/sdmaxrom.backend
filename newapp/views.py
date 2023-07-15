from django.shortcuts import render
from .models import Category1, Category2, Comment, Team, Information, Partner, Product1, Product2, Statistika, Connection
from .serializers import Category1Serializers, Category2Serializers, InformationSerializers,  CommentSerializers, TeamSerializers, PartnerSerializers, Product1Serializers, Product2Serializers, StatistikaSerializers, ConnectionSerializers 
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
# Create your views here.

class Category1Viewset(viewsets.ModelViewSet):
    queryset = Category1.objects.all()
    serializer_class = Category1Serializers
    permission_classes = [AllowAny]
    
class Category2Viewset(viewsets.ModelViewSet):
    queryset = Category2.objects.all()
    serializer_class = Category2Serializers
    permission_classes = [AllowAny]
    
class InformationViewset(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializers
    permission_classes = [AllowAny]
     
class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [AllowAny]
    
class TeamViewset(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializers
    permission_classes = [AllowAny]
    
class PartnerViewset(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializers
    permission_classes = [AllowAny]

class Product1Viewset(viewsets.ModelViewSet):
    queryset = Product1.objects.all()
    serializer_class = Product1Serializers
    permission_classes = [AllowAny]

class Product2Viewset(viewsets.ModelViewSet):
    queryset = Product2.objects.all()
    serializer_class = Product2Serializers
    permission_classes = [AllowAny]

class StatistikaViewset(viewsets.ModelViewSet):
    queryset = Statistika.objects.all()
    serializer_class = StatistikaSerializers 
    permission_classes = [AllowAny]

class ConnectioViewset(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializers
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'branch_trottle'

    permission_classes = [AllowAny]
    # lookup_field = 'slug'

    """ CRUD functions """

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
        except:
            return Response({'error': "Ma'lumotni olishda xatolik yuzaga keldi !!!"})

        try:
            new_connection = Connection.objects.create(
                full_name=data['full_name'],
                text=data['text'],
                number=data['number'],
            )
            new_connection.save()
            serializer = ConnectionSerializers(new_connection)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Ma'lumotni saqlashda xatolik yuzaga keldi !!!"},
                            status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = self.get_object()
        request_data = request.data

        try:
            data.full_name = request_data['full_name'] if 'full_name' in request_data else data.full_name
            data.text = request_data['text'] if 'text' in request_data else data.text
            data.status = request_data['number'] if 'number' in request_data else data.number
            data.save()
            serializer = Connection(data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Ma'lumot saqlashda hatolik yuzaga keldi !!!"})

    def destroy(self, request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response({'mesage': "Ma'lumot muvaffaqiyatli o'chirildi"}, status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        data = self.get_object()
        new_data = {}

        new_data['id'] = data.id
        new_data['full_name'] = data.full_name
        new_data['text'] = data.text
        serializer = ConnectionSerializers(new_data)
        return Response(serializer.data)