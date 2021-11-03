from django.contrib import admin
from .models import Tag

# Register your models here.
from .models import Produit
admin.site.register(Produit)
admin.site.register(Tag)
