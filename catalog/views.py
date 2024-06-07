from django.db.models import Q
from django.shortcuts import render
from django.views import generic

from catalog.models import Product


class MainPageView(generic.TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_products'] = Product.objects.all().order_by('create_on')[:4:]
        return context


class ProductPageView(generic.DetailView):
    model = Product
    template_name = 'product.html'


class SearchPageView(generic.ListView):
    template_name = 'search.html'
    model = Product

    def get(self, request, *args, **kwargs):
        context = {}
        query_value = request.GET.get('value')
        search_result = Product.objects.filter(
            Q(name__icontains=query_value) |
            Q(description__icontains=query_value)
        )

        context['search_products'] = search_result

        return render(request, self.template_name, context)


class ProductLaptopPage(generic.ListView):
    template_name = 'ptype.html'
    model = Product
    type = 'laptops'
    queryset = Product.objects.filter(ptype__slug=type)
    context_object_name = 'products_list'
    extra_context = {'page': 'Ноутбуки 0'}



class SmartPhonePageView(ProductLaptopPage):
    type = 'smartphones'
    extra_context = {'page': 'Смартфоны'}
    template_name = 'ptype.html'
    model = Product
    queryset = Product.objects.filter(ptype__slug=type)
    context_object_name = 'products_list'




class AccessoriesPageView(ProductLaptopPage):
    type = 'accessories'
    extra_context = {'page': 'Акксессуары'}
    template_name = 'ptype.html'
    model = Product
    queryset = Product.objects.filter(ptype__slug=type)
    context_object_name = 'products_list'

class InProgress(generic.TemplateView):
    template_name = 'in_progress.html'
