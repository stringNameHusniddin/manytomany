from rest_framework import serializers
from .models import *

class CategoriesS(serializers.ModelSerializer):    
    class Meta:
        model = Category
        fields = "__all__"

class ProductS(serializers.ModelSerializer):    
    category = CategoriesS(many =True, read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Category.objects.all()
    )
    class Meta:
        model = Product
        fields = "__all__"
    
    def create(self, validated_data):

        category = validated_data.pop("category_id", None)
        product = Product.objects.create(**validated_data)
        if category:
            product.category.set(category)
        return product     

    def update(self, instance, validated_data):
        category = validated_data.pop("category_id", None)

        instance.name = validated_data.get("name", instance.name)
        instance.price = validated_data.get("price", instance.price)
        instance.created_at = validated_data.get("created_at", instance.created_at)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        instance.description = validated_data.get("description", instance.description)
        instance.save()

        if category:
            instance.category.clear()
            for cat in category:
                instance.category.add(cat)
        return instance 

class ReporterS(serializers.ModelSerializer):    
    class Meta:
        model = Reporter
        fields = "__all__"

class ArticleS(serializers.ModelSerializer):  
    reporter = ReporterS(read_only=True)  
    class Meta:
        model = Article
        fields = "__all__"