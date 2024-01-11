from django.shortcuts import render, get_object_or_404
from . import models
from django.views import generic


class ProductList(generic.ListView):
    model = models.Product
    template_name = 'product/product_list.html'

    def get_queryset(self):
        # return self.model.objects.filter().order_by('-id')
        return self.model.objects.filter().order_by('-id')


class ManClothView(generic.ListView):
    template_name = 'product/cloth_man_list.html'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tags__name='мужское')


class WomenClothView(generic.ListView):
    template_name = 'product/cloth_women_list.html'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tags__name='женское')


class ChildClothView(generic.ListView):
    template_name = 'product/cloth_child_list.html'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tags__name='детское')


class OldClothView(generic.ListView):
    template_name = 'product/cloth_old_list.html'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tags__name='для пожилых')
