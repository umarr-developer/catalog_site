from django.urls import path

from catalog.views import MainPageView, ProductPageView, InProgress, SearchPageView, ProductLaptopPage, \
    SmartPhonePageView, AccessoriesPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('product/<slug:slug>', ProductPageView.as_view(), name='product_view'),
    path('search/', SearchPageView.as_view(), name='search'),
    path('laptops/', ProductLaptopPage.as_view(), name='laptops'),
    path('smartphones/', SmartPhonePageView.as_view(), name='smartphones'),
    path('accessories/', AccessoriesPageView.as_view(), name='accessories'),
    path('in_progress/', InProgress.as_view(), name='in_progress')
]
