from rest_framework import serializers
from .models import *

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'title_uz', 'title_ru', 'description_uz', 'description_ru', 'image']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']

class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'name_uz', 'name_ru', 'image']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name_uz', 'name_ru', 'description_uz', 'description_ru', 'type']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone_number']

class DesktopSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    catalog = CatalogSerializer()
    brand = BrandSerializer()

    class Meta:
        model = Desktop
        fields = ['id', 'category', 'catalog', 'brand', 'name_uz', 'name_ru', 'description_uz', 'description_ru', 'processor', 'videocard', 'cooler', 'memory', 'price_uzs', 'price_usd', 'image', 'monitor', 'resolution', 'fps']

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'name_uz', 'name_ru', 'description_uz', 'description_ru', 'price_uzs', 'price_usd', 'image', 'slug']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'image']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title_uz', 'title_ru', 'description_uz', 'description_ru', 'image', 'created_time']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'name', 'phone_number', 'address', 'comment', 'items']

class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ['id', 'type', 'logo', 'uzs_3month', 'uzs_6month', 'usd_3month', 'usd_6month']

class ProductSerializer(serializers.ModelSerializer):
    catalog = CatalogSerializer()

    class Meta:
        model = Product
        fields = ['id', 'catalog', 'name_uz', 'name_ru', 'description_uz', 'description_ru', 'price_uzs', 'price_usd', 'image', 'slug']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name_uz', 'name_ru', 'min_description_uz', 'min_description_ru', 'description_uz', 'description_ru', 'image']

class TestimonialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'profession_uz', 'profession_ru', 'review_uz', 'review_ru', 'image', 'youtube_url']