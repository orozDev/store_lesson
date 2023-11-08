from rest_framework import serializers

from core.models import Category, Product, Tag, ProductImage, ProductAttribute


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'created_at')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ImageForProductCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image',)


class AttributeForProductCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = ('id', 'name', 'value',)


class CreateProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        product = Product.objects.create(**validated_data)
        image_serializer = ImageForProductCreationSerializer(data=image)
        image_serializer.is_valid(raise_exception=True)
        image_serializer.save(product=product)
        return product


class ReadProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    tags = TagSerializer(many=True)
    user = serializers.CharField(source='user.email')
    user_id = serializers.IntegerField(source='user.id')
    # image = serializers.ReadOnlyField(source='image.url')
    image = serializers.SerializerMethodField()
    images = ImageForProductCreationSerializer(many=True)
    attributes = AttributeForProductCreationSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def get_image(self, item):
        req = self.context['request']
        if item.image:
            return req.build_absolute_uri(item.image.url)
        return None


class ProductAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductAttribute
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'