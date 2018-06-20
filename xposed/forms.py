from django import forms
from .models import Xposed_models

class RegistratonForm(forms.ModelForm):
    
    date_of_birth = forms.DateField(
                attr= {
                    'class':
                }
            )
        )
      
    class Meta:
        model = Xposed_models
        exclude = [
            'is_model'
        ]

       