from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer, Order, OrderItem
from .serializers import CustomerSerializer, OrderSerializer
from seller_app.serializers import StoreSerializer, ProductSerializer

@api_view(['POST'])
def create_customer(request):
    mobile_number = request.data.get('mobile_number')
    address = request.data.get('address')

    # Create or retrieve the customer account
    customer, _ = Customer.objects.get_or_create(mobile_number=mobile_number)
    customer.address = address
    customer.save()

    serializer = CustomerSerializer(customer)
    return Response(serializer.data)

@api_view(['POST'])
def get_store_details(request):
    store_link = request.data.get('store_link')

    # Retrieve store details based on the store link
    store = Store.objects.get(link=store_link)

    serializer = StoreSerializer(store)
    return Response(serializer.data)

@api_view(['POST'])
def add_to_cart(request):
    customer_id = request.data.get('customer_id')
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity')

    # Retrieve customer and product
    customer = Customer.objects.get(id=customer_id)
    product = Product.objects.get(id=product_id)

    # Create or update the cart item
    cart_item, created = CartItem.objects.get_or_create(customer=customer, product=product)
    cart_item.quantity = quantity
    cart_item.save()

    return Response({'message': 'Item added to cart successfully.'})

@api_view(['POST'])
def place_order(request):
    customer_id = request.data.get('customer_id')
    store_id = request.data.get('store_id')
    cart_items = request.data.get('cart_items')

    # Retrieve customer and store
    customer = Customer.objects.get(id=customer_id)
    store = Store.objects.get(id=store_id)

    # Create the order
    order = Order.objects.create(customer=customer, store=store)

    # Create order items
    for item in cart_items:
        product = Product.objects.get(id=item['product_id'])
        quantity = item['quantity']
        OrderItem.objects.create(order=order, product=product, quantity=quantity)

    return Response({'message': 'Order placed successfully.', 'order_id': order.id})