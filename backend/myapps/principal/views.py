import json
import stripe

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapps.principal.models import Product
from myapps.principal.serializers import ProductSerializer, OrderSerializer
from django.conf import settings

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

@api_view(['POST'])
def create_order(request):
    
    if request.method == 'POST':
        order_serializer = OrderSerializer(data = request.data)
        
        # validation
        if order_serializer.is_valid():
            order_serializer.save()            
            return Response({'message':'Order created successfully!'},status = status.HTTP_201_CREATED)
        
        return Response(order_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_stripe_pub_key(request):
    pub_key = settings.STRIPE_PUB_KEY

    return Response({'pub_key': pub_key})

@api_view(['POST'])
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data = json.loads(request.body)
    product = data['product']

    price_id = settings.STRIPE_PRICE_ID_PRODUCT_TEST
    
    team = Team.objects.filter(members__in=[request.user]).first() 

    try:
        checkout_session = stripe.checkout.Session.create(
            client_reference_id = team.id,
            success_url = '%s?session_id={CHECKOUT_SESSION_ID}' % settings.FRONTEND_WEBSITE_SUCCESS_URL,
            cancel_url = '%s' % settings.FRONTEND_WEBSITE_CANCEL_URL,
            payment_method_types = ['card'],
            mode = 'subscription',
            line_items = [
                {
                    'price': price_id,
                    'quantity': 1
                }
            ]
        )
        return Response({'sessionId': checkout_session['id']})
    except Exception as e:
        return Response({'error': str(e)})