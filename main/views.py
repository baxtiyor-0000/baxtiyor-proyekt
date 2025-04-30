from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class BannerListView(APIView):
    def get(self, request):
        banners = Banner.objects.all()
        serializer = BannerSerializer(banners, many=True)
        return Response(serializer.data)
    
class BrandListView(APIView):
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)
    
class CatalogListView(APIView):
    def get(self, request):
        catalogs = Catalog.objects.all()
        serializer = CatalogSerializer(catalogs, many=True)
        return Response(serializer.data)
    
class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategorySearchView(APIView):
    def get(self, request):
        query = request.query_params.get('query', None)
        
        if query is None or query == '':
            return Response({"message": "Query is required"}, status=400)
            
        categories = Category.objects.filter(type__icontains=query)
        if not categories.exists():
            return Response({"message": "Not Found"}, status=404)
        
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
class ContactListView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DesktopListView(APIView):
    def get(self, request):
        desktops = Desktop.objects.all()
        serializer = DesktopSerializer(desktops, many=True)
        return Response(serializer.data)

class DesktopDetailView(APIView):
    def get(self, request, id):
        try:
            desktop = Desktop.objects.get(id=id)
            serializer = DesktopSerializer(desktop)
            return Response(serializer.data)
        except Desktop.DoesNotExist:
            return Response({"error": "Desktop not found"}, status=404)
        
class DiscountListView(APIView):
    def get(self, request):
        products = Discount.objects.all()
        serializer = DiscountSerializer(products, many=True)
        return Response(serializer.data)

class DiscountDetailView(APIView):
    def get(self, request, slug):
        try:
            product = Discount.objects.get(slug=slug)
            serializer = DiscountSerializer(product)
            return Response(serializer.data)
        except Discount.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)
        
class GameListView(APIView):
    def get(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
class NewsListView(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

class NewsDetailView(APIView):
    def get(self, request, id):
        try:
            news = News.objects.get(id=id)
            serializer = NewsSerializer(news)
            return Response(serializer.data)
        except News.DoesNotExist:
            return Response({"error": "News not found"}, status=404)
        
class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentTypeListView(APIView):
    def get(self, request):
        payment_types = PaymentType.objects.all()
        serializer = PaymentTypeSerializer(payment_types, many=True)
        return Response(serializer.data)
    
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetailView(APIView):
    def get(self, request, slug):
        try:
            product = Product.objects.get(slug=slug)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)
        
class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get('query', None)

        if query is None or query == '':
            return Response({"message": "Query is required"}, status=400)
        
        desktops = Desktop.objects.filter(name_uz__icontains=query) | Desktop.objects.filter(name_ru__icontains=query) | \
                   Desktop.objects.filter(description_uz__icontains=query) | Desktop.objects.filter(description_ru__icontains=query)
        desktop_data = [{'type': 'desktop', **data} for data in DesktopSerializer(desktops, many=True).data]
        
        discounts = Discount.objects.filter(name_uz__icontains=query) | Discount.objects.filter(name_ru__icontains=query) | \
                    Discount.objects.filter(description_uz__icontains=query) | Discount.objects.filter(description_ru__icontains=query)
        discount_data = [{'type': 'discount', **data} for data in DiscountSerializer(discounts, many=True).data]
        
        products = Product.objects.filter(name_uz__icontains=query) | Product.objects.filter(name_ru__icontains=query) | \
                   Product.objects.filter(description_uz__icontains=query) | Product.objects.filter(description_ru__icontains=query)
        product_data = [{'type': 'product', **data} for data in ProductSerializer(products, many=True).data]

        services = Service.objects.filter(name_uz__icontains=query) | Service.objects.filter(name_ru__icontains=query) | \
                   Service.objects.filter(description_uz__icontains=query) | Service.objects.filter(description_ru__icontains=query)
        service_data = [{'type': 'service', **data} for data in ServiceSerializer(services, many=True).data]
        
        combined_results = desktop_data + discount_data + product_data + service_data
        
        return Response(combined_results)

class CombinedCatalogView(APIView):
    def get(self, request):
        catalog_param = request.query_params.get('catalog_id', None)

        if catalog_param is None:
            return Response({"error": "The 'catalog_id' parameter is required!"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            catalog_id = int(catalog_param)
        except ValueError:
            return Response({"error": "The 'catalog_id' parameter must be an integer!"}, status=status.HTTP_400_BAD_REQUEST)

        products = Product.objects.filter(catalog_id=catalog_id)
        desktops = Desktop.objects.filter(catalog_id=catalog_id)

        products_data = ProductSerializer(products, many=True).data
        desktops_data = DesktopSerializer(desktops, many=True).data

        return Response({
            "products": products_data,
            "desktops": desktops_data
        }, status=status.HTTP_200_OK)
    
class ServiceListView(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

class ServiceDetailView(APIView):
    def get(self, request, id):
        try:
            service = Service.objects.get(id=id)
            serializer = ServiceSerializer(service)
            return Response(serializer.data)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=404)
        
class TestimonialListAPIView(APIView):
    def get(self, request):
        testimonials = Testimonial.objects.all()
        serializer = TestimonialSerializer(testimonials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)