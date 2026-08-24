from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Customer

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="", max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(label="", max_length=254, required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(label="", max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(label='', help_text='<span class="form-text text-muted">Your password must be at least 8 characters long and contain both letters and numbers.</span>', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='', help_text='<span class="form-text text-muted">Please enter the same password as above.</span>', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(label="", max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(label="", max_length=254, required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    phone_number = forms.CharField(label="", max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    address = forms.CharField(label="", max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    city = forms.CharField(label="", max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))      
    zip_code = forms.CharField(label="", max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}))
    state = forms.CharField(label="", max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}))
    country = forms.CharField(label="", max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}))

    class Meta:
        model = Customer
        exclude = ('user',)