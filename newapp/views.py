from django.shortcuts import render
from .models import Category1, Category2, Comment, Team, Information, Partner, Product1, Product2, Statistika, Connection
from .serializers import Category1Serializers, Category2Serializers, InformationSerializers, \
    CommentSerializers, TeamSerializers, PartnerSerializers, Product1Serializers, Product2Serializers,\
    StatistikaSerializers, ConnectionSerializers , Category1AdminSerializers, Category2AdminSerializers, CommentAdminSerializers, TeamAdminSerializers,\
    InformationsAdminSerializers, PartnerAdminSerializers, Product1AdminSerializers, Product2AdminSerializers, StatistikaAdminSerializers
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
    
class Category1AdminViewset(viewsets.ModelViewSet):
    queryset = Category1.objects.all()
    serializer_class = Category1AdminSerializers
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
            new_connection = Category1.objects.create(
                name=data['name'],
            )
            new_connection.save()
            serializer = Category1AdminSerializers(new_connection)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Ma'lumotni saqlashda xatolik yuzaga keldi !!!"},
                            status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = self.get_object()
        request_data = request.data

        try:
            data.name = request_data['name'] if 'name' in request_data else data.name
            data.save()
            serializer = Category1(data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Ma'lumot saqlashda hatolik yuzaga keldi !!!"})

    def destroy(self, request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response({'mesage': "Ma'lumot muvaffaqiyatli o'chirildi"}, status.HTTP_204_NO_CONTENT)
    
class Category2AdminViewset(viewsets.ModelViewSet):
    queryset = Category2.objects.all()
    serializer_class = Category2AdminSerializers
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
            new_connection = Category2.objects.create(
                name=data['name'],
            )
            new_connection.save()
            serializer = Category2AdminSerializers(new_connection)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Ma'lumotni saqlashda xatolik yuzaga keldi !!!"},
                            status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = self.get_object()
        request_data = request.data

        try:
            data.name = request_data['name'] if 'name' in request_data else data.name
            data.save()
            serializer = Category2(data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Ma'lumot saqlashda hatolik yuzaga keldi !!!"})

    def destroy(self, request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response({'mesage': "Ma'lumot muvaffaqiyatli o'chirildi"}, status.HTTP_204_NO_CONTENT)
    
class StatistikaAdminViewset(viewsets.ModelViewSet):
    queryset = Statistika.objects.all()
    serializer_class = StatistikaAdminSerializers
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
            new_connection = Statistika.objects.create(
                name=data['name'],
                number=data['number'],
            )
            new_connection.save()
            serializer = StatistikaAdminSerializers(new_connection)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Ma'lumotni saqlashda xatolik yuzaga keldi !!!"},
                            status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = self.get_object()
        request_data = request.data

        try:
            data.name = request_data['name'] if 'name' in request_data else data.name
            data.number = request_data['number'] if 'number' in request_data else data.number
            data.save()
            serializer = Statistika(data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Ma'lumot saqlashda hatolik yuzaga keldi !!!"})

    def destroy(self, request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response({'mesage': "Ma'lumot muvaffaqiyatli o'chirildi"}, status.HTTP_204_NO_CONTENT)


class Product1AdmminViewset(viewsets.ModelViewSet):
    queryset = Product1.objects.all()
    serializer_class = Product1AdminSerializers
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
            new_connection = Product1.objects.create(\
                category1=data['category1'],
                name=data['name'],
                body=data['body'],
                photo=data['photo'],
            )
            new_connection.save()
            serializer = Product1AdminSerializers(new_connection)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Ma'lumotni saqlashda xatolik yuzaga keldi !!!"},
                            status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = self.get_object()
        request_data = request.data

        try:
            data.category1 = request_data['category1'] if 'category1' in request_data else data.category1
            data.name = request_data['name'] if 'name' in request_data else data.name
            data.body = request_data['body'] if 'body' in request_data else data.body
            data.photo = request_data['photo'] if 'photo' in request_data else data.photo
            data.save()
            serializer = Product1(data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Ma'lumot saqlashda hatolik yuzaga keldi !!!"})

    def destroy(self, request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response({'mesage': "Ma'lumot muvaffaqiyatli o'chirildi"}, status.HTTP_204_NO_CONTENT)

class Product2AdmminViewset(viewsets.ModelViewSet):
    queryset = Product2.objects.all()
    serializer_class = Product2AdminSerializers
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
            new_connection = Product1.objects.create(
                category2=data['category2'],
                name=data['name'],
                body=data['body'],
                photo=data['photo'],
            )
            new_connection.save()
            serializer = Product2AdminSerializers(new_connection)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Ma'lumotni saqlashda xatolik yuzaga keldi !!!"},
                            status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = self.get_object()
        request_data = request.data

        try:
            data.category1 = request_data['category1'] if 'category1' in request_data else data.category1
            data.name = request_data['name'] if 'name' in request_data else data.name
            data.body = request_data['body'] if 'body' in request_data else data.body
            data.photo = request_data['photo'] if 'photo' in request_data else data.photo
            data.save()
            serializer = Product2(data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Ma'lumot saqlashda hatolik yuzaga keldi !!!"})

    def destroy(self, request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response({'mesage': "Ma'lumot muvaffaqiyatli o'chirildi"}, status.HTTP_204_NO_CONTENT)


class PartnerAdmminViewset(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerAdminSerializers
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
            new_connection = Product1.objects.create(
                email=data['email'],
                name=data['name'],
                body=data['body'],
            )
            new_connection.save()
            serializer = PartnerAdminSerializers(new_connection)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Ma'lumotni saqlashda xatolik yuzaga keldi !!!"},
                            status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = self.get_object()
        request_data = request.data

        try:
            data.name = request_data['name'] if 'name' in request_data else data.name
            data.body = request_data['body'] if 'body' in request_data else data.body
            data.email = request_data['email'] if 'email' in request_data else data.email
            data.save()
            serializer = Partner(data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Ma'lumot saqlashda hatolik yuzaga keldi !!!"})

    def destroy(self, request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response({'mesage': "Ma'lumot muvaffaqiyatli o'chirildi"}, status.HTTP_204_NO_CONTENT)

class TeamAdmminViewset(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamAdminSerializers
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
            new_connection = Team.objects.create(
                name=data['name'],
                number=data['number'],
                photo=data['photo'],
            )
            new_connection.save()
            serializer = TeamAdminSerializers(new_connection)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Ma'lumotni saqlashda xatolik yuzaga keldi !!!"},
                            status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = self.get_object()
        request_data = request.data

        try:
            data.name = request_data['name'] if 'name' in request_data else data.name
            data.number = request_data['number'] if 'number' in request_data else data.number
            data.photo = request_data['photo'] if 'photo' in request_data else data.photo
            data.save()
            serializer = Team(data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Ma'lumot saqlashda hatolik yuzaga keldi !!!"})

    def destroy(self, request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response({'mesage': "Ma'lumot muvaffaqiyatli o'chirildi"}, status.HTTP_204_NO_CONTENT)

class CommentAdmminViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentAdminSerializers
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
            new_connection = Comment.objects.create(
                full_name=data['full_name'],
                text=data['text'],

            )
            new_connection.save()
            serializer = Product2AdminSerializers(new_connection)
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
            data.save()
            serializer = Comment(data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Ma'lumot saqlashda hatolik yuzaga keldi !!!"})

    def destroy(self, request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response({'mesage': "Ma'lumot muvaffaqiyatli o'chirildi"}, status.HTTP_204_NO_CONTENT)


