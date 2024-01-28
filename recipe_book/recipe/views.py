from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes

from .models import IngredientsAmount, Recipe, Ingredient

@api_view(('GET',))
def add_product_to_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    recipe = get_object_or_404(Recipe, id=recipe_id)
    product_id = request.GET.get('product_id')
    ingredient = get_object_or_404(Ingredient, id=product_id)
    weight = request.GET.get('weight')
    product, created = IngredientsAmount.objects.update_or_create(
        recipe=recipe,
        ingredient=ingredient,
        defaults={'weight': weight}
    )
    if created:
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_200_OK)

@api_view(('GET',))
def cook_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = recipe.ingredients_amount_in_recipe.all()
    for ingredient in ingredients:
        count = ingredient.ingredient.use_count
        ingredient.ingredient.use_count = count + 1
        ingredient.ingredient.save()
    return Response(status=status.HTTP_200_OK)




def show_recipes_without_product(request):
    product_id = request.GET.get('product_id')
    ingredient = get_object_or_404(Ingredient, id=product_id)
    ingredients_without = []
    ingredients_in = ingredient.ingredients_amount.all()
    for ingredient_in in ingredients_in:
        if ingredient_in.weight <= 10:
            ingredients_without.append(ingredient.recipe)
    recipes = Recipe.objects.exclude(
        ingredients_amount_in_recipe__ingredient__id=product_id
    )
    for recipe in recipes:
        ingredients_without.append(recipe)
    context = {
        'recipes': ingredients_without,
        'ingredient': ingredient
    }
    return render(request, 'recipe_without.html', context)
