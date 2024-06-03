from django.urls import path
from catalog.views import MainPageView, ProductPageView, InProgress, SearchPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('product/<slug:slug>', ProductPageView.as_view(), name='product_view'),
    path('search/', SearchPageView.as_view(), name='search'),
    path('in_progress/', InProgress.as_view(), name='in_progress')
]
