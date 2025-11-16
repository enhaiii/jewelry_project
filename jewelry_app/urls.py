from jewelry_app import views
from django.urls import path

urlpatterns = [
    path('', views.online),
    path('product_card/<int:name_id>', views.cards),
]
