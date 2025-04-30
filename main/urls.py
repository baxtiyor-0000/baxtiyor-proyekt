from django.urls import path
from .views import *

urlpatterns = [
    path('banners/', BannerListView.as_view(), name='banner-list'),
    path('brands/', BrandListView.as_view(), name='brand-list'),
    path('catalogs/', CatalogListView.as_view(), name='catalog-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/search/', CategorySearchView.as_view(), name='category-search'),
    path('contact/', ContactListView.as_view(), name='contact-post'),
    path('desktops/', DesktopListView.as_view(), name='desktop-list'),
    path('desktop/<int:id>/', DesktopDetailView.as_view(), name='desktop-detail'),
    path('discounts/', DiscountListView.as_view(), name='discount-list'),
    path('discount/<str:slug>/', DiscountDetailView.as_view(), name='discount-detail'),
    path('games/', GameListView.as_view(), name='game-list'),
    path('news/', NewsListView.as_view(), name='news-list'),
    path('news/<int:id>/', NewsDetailView.as_view(), name='news-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('payment-types/', PaymentTypeListView.as_view(), name='payment-type-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('product/<str:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('search/', SearchView.as_view(), name='product-search'),
    path('combined/', CombinedCatalogView.as_view(), name='combined-catalog-products'),
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('service/<int:id>/', ServiceDetailView.as_view(), name='desktop-detail'),
    path('testimonials/', TestimonialListAPIView.as_view(), name='testimonial-list'),
]