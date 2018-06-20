from django.db import models
from django.shortcuts import reverse

class Xposed_models(models.Model):
    fullname = models.CharField(max_length=225)
    date_of_birth = models.DateField()
    address = models.CharField(max_length = 225)
    sex = models.CharField(max_length = 10)
    phone_number = models.CharField(max_length = 14)
    email = models.EmailField()
    instagram_profile = models.CharField(max_length = 225)
    height = models.SmallIntegerField()
    bust = models.SmallIntegerField()
    waist = models.SmallIntegerField()
    hips = models.SmallIntegerField()
    weight = models.SmallIntegerField(blank=True, null=True)
    shoes_size = models.SmallIntegerField()
    hair_color = models.CharField(max_length = 10)
    eyes_color = models.CharField(max_length = 10)
    portrait_photo = models.ImageField()
    profile_photo  = models.ImageField()
    full_figure_photo = models.ImageField()
    is_model = models.BooleanField(default = False)

    def __str__(self):
        return self.fullname.split(' ')[0]

    def get_absolute_url(self):
        return reverse('xposed:index', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Xposed_model'
        verbose_name_plural = 'Xposed_models'



class Pictures(models.Model):
    model = models.ForeignKey(Xposed_models, on_delete = models.CASCADE)
    pictures = models.ImageField()
    

    def __str__(self):
        return self.model.fullname.split(' ')[0]

class Gallery(models.Model):
    photo = models.ImageField()
    date = models.DateTimeField(auto_now=True, auto_now_add=False)


    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'

        
    def __str__(self):
        name = 'photo'
        return name