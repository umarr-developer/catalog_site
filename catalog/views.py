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


class InProgress(generic.TemplateView):
    template_name = 'in_progress.html'
