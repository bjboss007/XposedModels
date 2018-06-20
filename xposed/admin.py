from django.contrib import admin
from .models import Xposed_models,Pictures,Gallery
from django.forms import formset_factory

GalleryFormset = formset_factory(Gallery, extra = 3)
PicturesFormset = formset_factory(Pictures, extra = 3)

class GalleryModel(admin.ModelAdmin):
    list_display = ["{}".format('photo'),"date"]

    class Meta:
        model = Gallery

class XposedModel(admin.ModelAdmin):
    list_display = [
        "fullname",
        "is_model"
    ]

    class Meta:
        model = Xposed_models

admin.site.register(Xposed_models, XposedModel)
admin.site.register(Pictures)
admin.site.register(Gallery,GalleryModel)