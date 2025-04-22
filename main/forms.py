from django import forms
from django.forms import ModelForm
from product.models import Product
class LoginForm(forms.Form):
    login = forms.CharField(
        max_length=30,
        label="Login",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Password"
    )

class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ["user", "created_at", "updated_at"]
