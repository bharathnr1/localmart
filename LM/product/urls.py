from django.urls import path
from product import views as product_view

app_name = 'product'

urlpatterns = [
    path('list/', product_view.productlist, name="productlist"),
    path('create/', product_view.createproduct, name="createproduct"),
    path('delete/<int:pk>', product_view.deleteview, name="deleteview")
]
