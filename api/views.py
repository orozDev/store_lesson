from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from api.paginations import SimpleResultPagination
from api.permissions import IsOwner, IsSuperAdmin
from api.serializers import CategorySerializer, ProductSerializer, CreateUpdateProductSerializer, ProductImageSerializer
from core.models import Category, Product


class CategoriesAPIView(
    # ListAPIView, CreateAPIView
    ListCreateAPIView,
):
    queryset = Category.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    pagination_class = SimpleResultPagination


class DetailCategoryRetrieveAPIView(
    # RetrieveAPIView, DestroyAPIView, UpdateAPIView
    RetrieveUpdateDestroyAPIView

):
    queryset = Category.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    lookup_field = 'id'


@api_view()
@permission_classes((AllowAny,))
def list_categories(request):
    categories = Category.objects.all()
    count = categories.count()
    limit = request.GET.get('limit', 2)
    offset = request.GET.get('offset', 1)
    paginator = Paginator(categories, limit)
    categories = paginator.get_page(offset)
    serializer = CategorySerializer(instance=categories, many=True)
    response = {
        'count': count,
        'limit': int(limit),
        'offset': int(offset),
        'page_count': paginator.num_pages,
        'data': serializer.data
    }
    return Response(response)


@api_view()
def detail_categories(request, id):
    category = get_object_or_404(Category, id=id)
    serializer = CategorySerializer(instance=category, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated, IsSuperAdmin))
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes((IsAuthenticated, IsSuperAdmin))
def update_category(request, id):
    category = get_object_or_404(Category, id=id)
    serializer = CategorySerializer(instance=category, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view()
def list_products(request):
    products = Product.objects.all()
    count = products.count()
    limit = request.GET.get('limit', 2)
    offset = request.GET.get('offset', 1)
    paginator = Paginator(products, limit)
    products = paginator.get_page(offset)
    serializer = ProductSerializer(instance=products, many=True, context={'request': request})
    response = {
        'count': count,
        'limit': int(limit),
        'offset': int(offset),
        'page_count': paginator.num_pages,
        'data': serializer.data
    }
    return Response(response)


@api_view()
def detail_products(request, id):
    product = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(instance=product, many=False, context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_product(request):
    create_serializer = CreateUpdateProductSerializer(data=request.data)
    create_serializer.is_valid(raise_exception=True)
    product = create_serializer.save()
    image_serializer = ProductImageSerializer(data={'image': request.data['image']})
    image_serializer.is_valid(raise_exception=True)
    image_serializer.save(product=product)
    serializer = ProductSerializer(instance=product, context={'request': request})
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PATCH'])
@permission_classes((IsAuthenticated, IsOwner))
def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    serializer = CreateUpdateProductSerializer(instance=product, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    product = serializer.save()
    if request.data.get('image', False):
        image_serializer = ProductImageSerializer(data={'image': request.data['image']})
        image_serializer.is_valid(raise_exception=True)
        image_serializer.save(product=product)
    response_serializer = ProductSerializer(instance=product, context={'request': request})
    return Response(response_serializer.data)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated, IsOwner))
# @permission_classes((IsAuthenticated | IsOwner))
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return Response({'is_deleted': True}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated, IsSuperAdmin))
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return Response({'is_deleted': True}, status=status.HTTP_204_NO_CONTENT)
