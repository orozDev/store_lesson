from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.filters import ProductFilter
from api.mixins import UltraModelViewSet
from api.paginations import SimpleResultPagination
from api.permissions import IsOwner, IsSuperAdmin, IsOwnerForProduct
from api.serializers import CategorySerializer, ReadProductSerializer, CreateProductSerializer, \
    TagSerializer, ProductAttributeSerializer, ProductImageSerializer, ProductSerializer
from core.models import Category, Product, Tag, ProductAttribute, ProductImage


class CategoryViewSet(UltraModelViewSet):
    queryset = Category.objects.all()
    pagination_class = SimpleResultPagination
    serializer_class = CategorySerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']
    permission_classes_by_action = {
        'list': (AllowAny,),
        'retrieve': (AllowAny,),
        'create': (IsAuthenticated, IsSuperAdmin,),
        'update': (IsAuthenticated, IsSuperAdmin,),
        'destroy': (IsAuthenticated, IsSuperAdmin,),
    }


class ProductViewSet(UltraModelViewSet):
    queryset = Product.objects.all()
    serializer_classes = {
        'list': ReadProductSerializer,
        'update': CreateProductSerializer,
        'create': ProductSerializer,
        'retrieve': ReadProductSerializer,
    }
    pagination_class = SimpleResultPagination
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['rating', 'is_published', 'price']
    search_fields = ['name', 'description', 'content']
    filterset_class = ProductFilter
    permission_classes_by_action = {
        'list': (AllowAny,),
        'retrieve': (AllowAny,),
        'create': (IsAuthenticated,),
        'update': (IsAuthenticated, IsOwner,),
        'destroy': (IsAuthenticated, IsOwner,),
    }


class TagViewSet(UltraModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = SimpleResultPagination
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']
    permission_classes_by_action = {
        'list': (AllowAny,),
        'retrieve': (AllowAny,),
        'create': (IsAuthenticated, IsSuperAdmin,),
        'update': (IsAuthenticated, IsSuperAdmin,),
        'destroy': (IsAuthenticated, IsSuperAdmin,),
    }


class ProductAttributeViewSet(UltraModelViewSet):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer
    pagination_class = SimpleResultPagination
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'value']
    filterset_fields = ['product']
    permission_classes_by_action = {
        'list': (AllowAny,),
        'retrieve': (AllowAny,),
        'create': (IsAuthenticated,),
        'update': (IsAuthenticated, IsOwnerForProduct,),
        'destroy': (IsAuthenticated, IsOwnerForProduct,),
    }


class ProductImageViewSet(UltraModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    pagination_class = SimpleResultPagination
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['product']
    permission_classes_by_action = {
        'list': (AllowAny,),
        'retrieve': (AllowAny,),
        'create': (IsAuthenticated,),
        'update': (IsAuthenticated, IsOwnerForProduct,),
        'destroy': (IsAuthenticated, IsOwnerForProduct,),
    }
