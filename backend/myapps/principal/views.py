from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapps.principal.models import Product
from myapps.principal.serializers import ProductSerializer

@api_view(['GET'])
def list_all_products(request):

    # list
    if request.method == 'GET':
        # queryset
        products = Product.objects.all()
        products_serializer = ProductSerializer(products,many = True)
        return Response(products_serializer.data,status = status.HTTP_200_OK)

    else:
        return Response({'message':'The request must be a GET'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def show_product(request,pk=None):

    product = Product.objects.filter(barcode = pk).first()
    if product:
        # retrievevc
        if request.method == 'GET': 
            product_serializer = ProductSerializer(product)
            return Response(product_serializer.data,status = status.HTTP_200_OK)
    
    return Response({'message':'No se ha encontrado un usuario con estos datos'},status = status.HTTP_400_BAD_REQUEST)