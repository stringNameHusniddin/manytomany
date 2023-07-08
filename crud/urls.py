from django.urls import path
from .views import *

urlpatterns = [
    path("product/", product_list),
    path("product/<int:id>", product_detail)
]