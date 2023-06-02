from django.shortcuts import render
from .models import Book
import random

def main(request):
    recipes = Book.objects.order_by('?')
    return render(request, 'main.html', {'recipes': recipes})

def recipe_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = category.categories.all()
    return render(request, 'category_detail.html', {'category': category, 'recipes': recipes})