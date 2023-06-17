from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Seller, Store, Product, ProductCategory
from .serializers import StoreSerializer, ProductSerializer, ProductCategorySerializer, SellerSerializer

@api_view(['POST'])
def seller_signup(request):
    mobile_number = request.data.get('mobile_number')
    otp = request.data.get('otp')

    # Create seller account
    seller = Seller.objects.create(mobile_number=mobile_number)

    serializer = SellerSerializer(seller)
    return Response(serializer.data)

@api_view(['POST'])
def create_store(request):
    serializer = StoreSerializer(data=request.data)
    if serializer.is_valid():
        # Assign the current authenticated user as the seller of the store
        serializer.validated_data['seller'] = request.user
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def upload_product(request):
    product_name = request.data.get('product_name')
    description = request.data.get('description')
    mrp = request.data.get('mrp')
    sale_price = request.data.get('sale_price')
    image = request.FILES.get('image')
    category_name = request.data.get('category')

    # Create or get the category
    category, _ = ProductCategory.objects.get_or_create(name=category_name)

    # Create product
    product = Product.objects.create(name=product_name, description=description, mrp=mrp, sale_price=sale_price,
                                     image=image, category=category)

    serializer = ProductSerializer(product)
    return Response(serializer.data)
