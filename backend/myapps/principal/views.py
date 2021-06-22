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