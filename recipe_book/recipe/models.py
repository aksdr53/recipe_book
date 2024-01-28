from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from recipe_book.settings import RECIPES_NAME_MAX_LENGTH

class Ingredient(models.Model):
    name = models.CharField(verbose_name='Имя', blank=False,
                            max_length=RECIPES_NAME_MAX_LENGTH)
    use_count = models.IntegerField(verbose_name='Количество использований',default=0)


    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        constraints = [
            models.UniqueConstraint(fields=['name',],
                                    name='ingredient_unique')
        ]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(blank=False, max_length=RECIPES_NAME_MAX_LENGTH,
                            verbose_name='Имя',)
    ingredients = models.ManyToManyField(Ingredient,
                                         through='IngredientsAmount',
                                         through_fields=('recipe',
                                                         'ingredient'),
                                         related_name='recipe',
                                         verbose_name='Ингридиенты',
                                         blank=False)


class IngredientsAmount(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='ingredients_amount_in_recipe',
                               verbose_name='Рецепт')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,
                                   related_name='ingredients_amount',
                                   verbose_name='Ингридиент')
    weight = models.PositiveIntegerField(verbose_name='Количество',
                                         validators=[MinValueValidator(1),
                                                     MaxValueValidator(10000)])
    
    class Meta:
        verbose_name = 'Ингредиенты в рецепте'
        verbose_name_plural = 'Ингредиенты в рецепте'

    def __str__(self):
        return f'{self.ingredient} в {self.recipe}'