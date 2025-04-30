from django.contrib import admin
from .models import (
    Testimonial,
    Service,
    Product,
    PaymentType,
    Contact,
    Desktop,
    Discount,
    Game,
    News,
    Order,
    Category,
    Catalog,
)

admin.site.register(Testimonial)
admin.site.register(Service)
admin.site.register(Product)
admin.site.register(PaymentType)
admin.site.register(Contact)
admin.site.register(Desktop)
admin.site.register(Discount)
admin.site.register(Game)
admin.site.register(News)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Catalog)