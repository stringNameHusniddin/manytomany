from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

@api_view(["GET", "POST"])
def product_list(req):
    if req.method == "GET":
        products = Product.objects.all()
        ser = ProductS(products, many=True)

        return Response(ser.data)
    
    elif req.method == "POST":
        ser = ProductS(data=req.data)

        if ser.is_valid():
            ser.save()
        for cat in req.data["category"]:
            Product.objects.get(id=ser.data["id"]).category.add(cat["id"])

        return Response(ser.data)
    
@api_view(["GET", "PUT", "DELETE"])
def product_detail(req, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return Response("This item is not exist")
    
    if req.method == "GET":
        ser = ProductS(product)
        return Response(ser.data)
    
    if req.method == "PUT":
        ser = ProductS(instance=product, data=req.data)

        if ser.is_valid():
            ser.save()
        product.category.clear()
        for cat in req.data["category"]:
            product.category.add(cat["id"])
        
        return Response(ser.data)

    elif req.method == "DELETE":
        product.delete()
        return Response('This item has deleted')