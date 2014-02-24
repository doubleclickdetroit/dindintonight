# class IngredientResource(ModelResource):
#     class Meta:
#         queryset = Ingredient.objects.all()
#         resource_name = "ingredients"

# TastyPie
from tastypie import fields
from tastypie.resources import ModelResource

# Local Apps
from meals.models import Meal
# from vendors.api.resources import VendorLocationResource

class MealResource(ModelResource):
    # vendor_location = fields.ToOneField(VendorLocationResource, 'vendor_location')

    class Meta:
        resource_name = 'meals'
        queryset = Meal.objects.all()
        allowed_methods = ['get']
