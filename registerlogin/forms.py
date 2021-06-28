from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUser(UserCreationForm):
    email =forms.EmailField()
    phone =forms.IntegerField(widget=forms.TextInput)
    class meta:
        model = User
        fields={"username","email","phone","password1","password2"}
        
    def save(self, commit=True):
        user = super(NewUser,self).save(commit=False)
        user.email=self.cleaned_data['email']
        user.phone=self.cleaned_data['phone']
        if commit:
            user.save()
        return user