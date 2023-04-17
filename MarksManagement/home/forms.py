from django import forms

class loginform(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
    password = forms.CharField(error_messages= {'required':'Enter Username'})