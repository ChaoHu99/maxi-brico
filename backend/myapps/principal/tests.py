from django.test import TestCase
from myapps.principal.models import Product, Order
from rest_framework.test import APITestCase
from rest_framework import status

class ProductTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.product = Product(barcode=1, name="Product Test", price=2, stock=5)
        self.product.save()

    def tearDown(self):
        super().tearDown()
        self.product = None

    def test_store_product(self):
        self.assertEqual(Product.objects.count(), 1)

    def test_product_created(self):
        p = Product.objects.all()[0]
        self.assertEqual(p.barcode, 1)
        self.assertEqual(p.name, "Product Test")
        self.assertEqual(p.price, 2)
        self.assertEqual(p.stock, 5)

class TestProductView(APITestCase):

    def setUp(self):
        super().setUp()
        self.product = Product(barcode=1, name="Product Test", price=2, stock=5)
        self.product.save()

    def tearDown(self):
        super().tearDown()
        self.product = None

    def test_list_products(self):
        response = self.client.get("/list/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_show_product(self):
        barcode = Product.objects.all()[0].barcode
        response = self.client.get("/product/"+ str(barcode) +"/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OrderTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.order = Order(id = 5, price= 1541, delivery_status="Preparación", address="direccion")
        self.product = Product(id = 8, barcode=2, name="Product Test", price=2, stock=5)
        
        self.order.save()
        self.product.save()
        self.order.products.add(self.product)
        self.order.save()

    def tearDown(self):
        super().tearDown()
        self.order = None

    def test_store_product(self):
        self.assertEqual(Order.objects.count(), 1)

    def test_order_created(self):
        o = Order.objects.all()[0]
        self.assertEqual(o.price, 1541)
        self.assertEqual(o.delivery_status, "Preparación")
        self.assertEqual(o.address, "direccion")

 