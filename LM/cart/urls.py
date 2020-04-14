from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('', views.viewcart, name="viewcart"),
    path('update/<int:pk>', views.updatecart, name="updatecart"),
]


















