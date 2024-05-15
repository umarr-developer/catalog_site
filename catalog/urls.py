from django.urls import path
from catalog.views import MainPageView, ProductPageView, InProgress

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('product/<slug:slug>', ProductPageView.as_view(), name='product_view'),
    path('in_progress/', InProgress.as_view(), name='in_progress')
]
