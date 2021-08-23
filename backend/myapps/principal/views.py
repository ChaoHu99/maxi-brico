import json
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
        if request.method == 'GET': 
            product_serializer = ProductSerializer(product)
            return Response(product_serializer.data,status = status.HTTP_200_OK)
    
    return Response({'message':'No se ha encontrado un usuario con estos datos'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_product(request,pk=None):

    product = Product.objects.filter(barcode = pk).first()
    if product:
        if request.method == 'POST': 
            product_serializer = ProductSerializer(product, data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status = status.HTTP_200_OK)
            return Response(product_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    return Response({'message':'No se ha encontrado un usuario con estos datos'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_order(request):
    
    if request.method == 'POST':
        order_serializer = OrderSerializer(data = request.data)
        
        # validation
        if order_serializer.is_valid():
            order_serializer.save()
            return Response({'message':'Order created successfully!', 'order': order_serializer.data},status = status.HTTP_201_CREATED)
        
        return Response(order_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_stripe_pub_key(request):
    pub_key = settings.STRIPE_PUB_KEY

    return Response({'pub_key': pub_key})

@api_view(['POST'])
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data = json.loads(request.body)
    order = data['order']

    try:
        checkout_session = stripe.checkout.Session.create(
            success_url = "http://localhost:8080/payment-success",
            cancel_url = "http://localhost:8080/payment-failed",
            payment_method_types = ["card"],
            mode = "payment",
            line_items = [
                {   
                    'name': 'Pedido de Maxi Brico',
                    'currency': 'EUR',
                    'amount': order['price'],
                    'quantity': 1
                }
            ],
            
        )
        return Response({'sessionId': checkout_session['id']})
    except Exception as e:
        return Response({'error': str(e)})

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    webhook_key = settings.STRIPE_WEBHOOK_KEY
    payload = request.body
    sign_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    print('payload', payload)

    try:
        event = stripe.Webhook.construct_event(
            payload, sign_header, webhook_key
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignaturVerificationError as e:
        return HttpResponse(status=400)
    
    if event['type'] == 'checkout.session.completed':
        payment_intent = event['data']['object']

    return HttpResponse(status=200)