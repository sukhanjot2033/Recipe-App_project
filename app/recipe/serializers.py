"""
Serializer for the recipe api..
"""

from rest_framework import serializers
from core.models import (
    Recipe,
    Tag,
    Ingredient,
)
class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag"""
    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'name']
        read_only_field = ['id']

class RecipeSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True, required=False)
    ingredient = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_mintue', 'price', 'link', 'tags', 'ingredient','image']
        read_only_fields = ['id']

    def _get_or_create_tags(self, tags, recipe):
        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(
                user=auth_user,
                **tag,
            )
            recipe.tags.add(tag_obj)

    def _get_or_create_ingredient(self, ingredients, recipe):
        auth_user = self.context['request'].user
        for ingredient in ingredients:
            ingredient_obj, created = Ingredient.objects.get_or_create(
                user = auth_user,
                **ingredient,
            )
            recipe.ingredient.add(ingredient_obj)


    def create(self, validated_data):
        """Crete a recipe. """
        tags = validated_data.pop('tags', [])
        ingredients = validated_data.pop('ingredient', [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_tags(tags, recipe)
        self._get_or_create_ingredient(ingredients, recipe)
        return recipe

    def update(self, instance, validated_data):
        """ update recipe. """
        tags = validated_data.pop('tags', None)
        ingredient = validated_data.pop('ingredient', None)
        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)

        if ingredient is not None:
            instance.ingredient.clear()
            self._get_or_create_ingredient(ingredient, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class RecipeDetailSerializer(RecipeSerializer):

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']


class RecipeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'image']
        read_only_field = ['id']
        extra_kwargs = {'image':{'required':'True'}}