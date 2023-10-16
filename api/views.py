from rest_framework.decorators import api_view
from django.core.paginator import Paginator
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.serializers import CategorySerializer, ProductSerializer
from core.models import Category, Product


@api_view()
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


@api_view()
def list_products(request):
    products = Product.objects.all()
    count = products.count()
    limit = request.GET.get('limit', 2)
    offset = request.GET.get('offset', 1)
    paginator = Paginator(products, limit)
    products = paginator.get_page(offset)
    serializer = ProductSerializer(instance=products, many=True)
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
    serializer = ProductSerializer(instance=product, many=False)
    return Response(serializer.data)