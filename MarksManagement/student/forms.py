from django import forms
from .models import students

class studentsform(forms.ModelForm):
  
    def clean_pin_number(self):
        """
        ensure that email is always lower case.
        """
        return self.cleaned_data['pin_number'].upper()

    def clean_branch(self):
         return self.cleaned_data['branch'].upper()

  