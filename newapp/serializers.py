from .models import Category1, Category2, Comment, Team, Information, Partner, Product1, Product2, Statistika, Connection
from rest_framework import serializers

class Product1Serializers(serializers.ModelSerializer):
    class Meta:
        model = Product1
        # fields = ('__all__')
        fields = ('category1', 'name', 'body', 'photo','status')

class Product2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Product2
        # fields = ('__all__')
        fields = ('category2', 'name', 'body', 'photo','status')

class Category1Serializers(serializers.ModelSerializer):
    product1_category = Product1Serializers(many=True, read_only=True)
    class Meta:
        model = Category1
        # fields = ('__all__')
        fields = ('name', 'status', 'product1_category')

class Category2Serializers(serializers.ModelSerializer):
    product2_category = Product2Serializers(many=True, read_only=True)

    class Meta:
        model = Category2
        # fields = ('__all__')
        fields = ('name', 'status', 'product2_category')

class InformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Information
        # fields = ('__all__')
        fields = ('title', 'body', 'photo', 'status')

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = ('__all__')
        fields = ('full_name', 'text', 'status')

class TeamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Team
        # fields = ('__all__')
        fields = ('name', 'photo', 'number', 'status')

class PartnerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Partner
        # fields = ('__all__')
        fields = ('name', 'photo', 'email', 'status')

class StatistikaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Statistika
        # fields = ('__all__')
        fields = ('name', 'number', 'status')

class ConnectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ('__all__')
        # fields = ('name', 'number', 'status')

class ConnectionAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ('__all__')

class StatistikaAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Statistika
        fields = ('__all__')

class PartnerAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ('__all__')

class TeamAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('__all__')

class CommentAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')

class InformationsAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ('__all__')

class Category1AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category1
        fields = ('__all__')

class Category2AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category2
        fields = ('__all__')

class Product1AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product1
        fields = ('__all__')

class Product2AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product2
        fields = ('__all__')