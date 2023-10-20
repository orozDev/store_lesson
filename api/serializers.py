from rest_framework import serializers

from core.models import Category, Product, Tag, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'created_at')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    tags = TagSerializer(many=True)
    user = serializers.CharField(source='user.email')
    user_id = serializers.IntegerField(source='user.id')
    # image = serializers.ReadOnlyField(source='image.url')
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_image(self, item):
        req = self.context['request']
        if item.image:
            return req.build_absolute_uri(item.image.url)
        return None


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ('image',)


class CreateUpdateProductSerializer(serializers.ModelSerializer):

    image = serializers.ImageField()

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        validated_data.pop('image', None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('image', None)
        return super().update(instance, validated_data)