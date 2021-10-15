from difflib import context_diff

from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Product, Category


# Create your views here.
class IndexView(TemplateView):
    model = Product
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Productos'
        context['productList'] = Product.objects.all()
        return context