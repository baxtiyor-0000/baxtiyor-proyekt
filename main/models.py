from django.db import models
from django.utils.text import slugify

class Banner(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    description_uz = models.TextField(max_length=500)
    description_ru = models.TextField(max_length=500)
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.title_uz
    

class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Catalog(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    image = models.ImageField(upload_to='catalogs/')

    def __str__(self):
        return self.name_uz
    

class Category(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    description_uz = models.TextField(blank=True, null=True)
    description_ru = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=15)

    def __str__(self):
        return self.name_uz
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    

class Desktop(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='desktops')
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='desktops', null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='desktops')
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    description_uz = models.TextField(max_length=500)
    description_ru = models.TextField(max_length=500)
    processor = models.CharField(max_length=255)
    videocard = models.CharField(max_length=255)
    cooler = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
    price_uzs = models.DecimalField(max_digits=10, decimal_places=2)
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='desktop_images/')
    monitor = models.IntegerField()
    resolution = models.CharField(max_length=255)
    fps = models.CharField(max_length=255)

    def __str__(self):
        return self.name_uz
    
class Discount(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    description_uz = models.TextField()
    description_ru = models.TextField()
    price_uzs = models.DecimalField(max_digits=10, decimal_places=2)
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='discounts/')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_uz)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_uz
    
class Game(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='games/')

    def __str__(self):
        return self.name
    
class News(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    description_uz = models.TextField()
    description_ru = models.TextField()
    image = models.ImageField(upload_to='news/')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_uz
    
class Order(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    comment = models.TextField(max_length=1500)
    items = models.JSONField()
    
    def __str__(self):
        return self.name
    
class PaymentType(models.Model):
    type = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='payment_types/')
    uzs_3month = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    uzs_6month = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    usd_3month = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    usd_6month = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.type

class Product(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    description_uz = models.TextField()
    description_ru = models.TextField()
    price_uzs = models.DecimalField(max_digits=10, decimal_places=2)
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_uz)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_uz
    
class Service(models.Model):
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    min_description_uz = models.TextField(max_length=255)
    min_description_ru = models.TextField(max_length=255)
    description_uz = models.TextField(max_length=500)
    description_ru = models.TextField(max_length=500)
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.name_uz
    
class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    profession_uz = models.CharField(max_length=255)
    profession_ru = models.CharField(max_length=255)
    review_uz = models.TextField()
    review_ru = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    youtube_url = models.URLField()

    def __str__(self):
        return self.name