from rest_framework.serializers import ModelSerializer
from .models import *

class CategoriesS(ModelSerializer):    
    class Meta:
        model = Category
        fields = "__all__"

class ProductS(ModelSerializer):    
    category = CategoriesS(many =True, read_only=True)
    class Meta:
        model = Product
        fields = "__all__"