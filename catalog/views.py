from django.shortcuts import render
from catalog.models import Product #, Category
from django.views.generic import ListView, DetailView


# def home(request):
#     category_list = Category.objects.all()
#     context = {
#         'object_list': category_list,
#         'title': 'Главная'
#     }
#     return render(request, 'catalog/home.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def contacts(request):
    context = {
        'title': 'Контакты',
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Name: {name}\n Phone: {phone}\n Message: {message}')
    return render(request, 'catalog/contacts.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
