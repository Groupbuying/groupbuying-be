import json

from ApiBackEnd.utils import Envelope
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from products.models import Product, GroupCart, GroupCartItem


@method_decorator(csrf_exempt, name='dispatch')
class ProductListView(View):

    @staticmethod
    def get(request):
        products = Product.objects.all()
        data = []
        for product in products:
            data.append({
                'id': product.id,
                'name': product.name,
                'price': int(product.price),
                'description': product.description,
            })
        return Envelope(200, data, None).to_res()

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        name = data['name']
        price = data['price']
        description = data['description']
        Product.objects.create(name=name, price=price, description=description)
        return Envelope(200, None, None).to_res()

    @staticmethod
    def put(request, product_id: int):
        data = json.loads(request.body)
        product = Product.objects.get(pk=product_id)
        if data['name']:
            product.name = data['name']
        if data['price']:
            product.price = data['price']
        if data['description']:
            product.description = data['description']
        product.save()
        return Envelope(200, None, None).to_res()

    @staticmethod
    def delete(request, product_id: int):
        product = Product.objects.get(pk=product_id)
        product.delete()
        return Envelope(200, None, None).to_res()


@csrf_exempt
@require_http_methods(['GET'])
def get_carts(request):
    carts = GroupCart.objects.all()
    result = []
    for cart in carts:
        result.append({
            'id': cart.id,
            'name': cart.name,
        })
    return Envelope(200, result, None).to_res()


@csrf_exempt
@require_http_methods(['GET'])
def select_one_cart(request, cart_id: int):
    cart_items = GroupCartItem.objects.filter(cart_id=cart_id)
    return Envelope(200, [{
        'id': itme.id,
        'cartId': item.cart_id,
    } for item in cart_items], None).to_res()


@csrf_exempt
@require_http_methods(['POST'])
def create_new_group_cart(request):
    data = json.loads(request.body)
    GroupCart.objects.create(name=data['name'])
    return Envelope(200, None, None).to_res()
