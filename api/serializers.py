from rest_framework import serializers

from core.models import Category, Product, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'created_at')


class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=False)
    tags = TagSerializer(many=True)
    user = serializers.CharField(source='user.email')
    user_id = serializers.IntegerField(source='user.id')

    class Meta:
        model = Product
        fields = '__all__'
