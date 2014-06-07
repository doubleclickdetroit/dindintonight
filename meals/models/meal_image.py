from django.db import models
from django.db.models.signals import post_save
from core.models import BaseModel


class MealImage(BaseModel):
    id = models.AutoField(primary_key=True)
    meal = models.ForeignKey('meals.Meal', related_name='images')
    name = models.CharField(max_length=125, blank=True)
    description = models.CharField(max_length=1024, blank=True)
    location = models.CharField(max_length=2048, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'meals'
        db_table = 'meal_images'
        verbose_name = 'Meal Image'
        verbose_name_plural = 'Meal Images'

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.pk, self.meal.name, self.name)


def meal_image_post_save_handler(sender, instance, **kwargs):
    pass

post_save.connect(meal_image_post_save_handler, sender=MealImage)
