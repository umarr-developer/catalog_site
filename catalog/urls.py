from django.urls import path
from catalog.views import MainPageView, ProductPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('product/<slug:slug>', ProductPageView.as_view(), name='product_view')
]
