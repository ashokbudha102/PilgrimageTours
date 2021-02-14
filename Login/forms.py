from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()

class Login_Form(forms.ModelForm):

    username=forms.CharField(max_length=16,widget=forms.TextInput(attrs={
        "class":"form-control",
        "id":"email1",
        "placeholder":"Username...",

    }))
    password=forms.CharField(max_length=16,widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "id":"password1",
        "placeholder":"Your password...",
    }))
    class Meta:
        model=User
        fields=['username','password']
