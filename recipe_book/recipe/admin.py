from django.contrib import admin

from .models import Ingredient, IngredientsAmount, Recipe



class IngredientAmountInline(admin.TabularInline):
    model = IngredientsAmount
    min_num = 1


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'use_count')
    list_filter = ('name', )


class IngredientsAmountAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient')


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name','id')
    list_filter = ( 'name', )
    inlines = [
        IngredientAmountInline,
    ]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientsAdmin)
admin.site.register(IngredientsAmount, IngredientsAmountAdmin)
