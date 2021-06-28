from django import forms
from userlogin.models import login
from django.core import validators
from django.core.exceptions import ValidationError
import re
def firstname(value):
    for i in value:
        if '0'<=i<='9':
            raise ValidationError("plz give only alphabets")
        if i in '''`~!@#$%^&*()__+={[]}|\';:?/.>,<"''':
            raise ValidationError("plz give only for alphabets either uppercase or lowercase")
    return value

def lastname(value):
    for i in value:
        if '0'<=i<='9':
            raise ValidationError("plz give only alphabets")
        if i in '''`~!@#$%^&*()__+={[]}|\';:?/.>,<"''':
            raise ValidationError("plz give only for alphabets either uppercase or lowercase")
    return value

def phone(value):
    print(value)
    if len(str(value))!=10:
        raise ValidationError("plz give Ten Digit Phone Number")
    return value  

password = 0
def password(value):
    if len(value)>=8:
        if 'A'<=value[0]<='Z':
            if not re.findall('[0-9]', value):
                raise ValidationError("Your password atleast one numeric value ")
        else:
            raise ValidationError("Your password first character should  uppercase alphabet")
    else:    
        raise ValidationError("Your password must contain at least 8 characters.")
    global password
    password=value
    return value

def repassword(value):
    if len(value)>=8:
        if 'A'<=value[0]<='Z':
            if not re.findall('[0-9]', value):
                raise ValidationError("Your password atleast one numeric value ")
        else:
            raise ValidationError("Your password first character should  uppercase alphabet")
    else:    
        raise ValidationError("Your password must contain at least 8 characters.")
    if password!=value:
        raise ValidationError("Your password is not match plz renter the password ")
    return value

def loginpassword(value):
    if len(value)>=8:
        if 'A'<=value[0]<='Z':
            if not re.findall('[0-9]', value):
                raise ValidationError("Your password atleast one numeric value ")
        else:
            raise ValidationError("Your password first character should  uppercase alphabet")
    else:    
        raise ValidationError("Your password must contain at least 8 characters.")
    global password
    password=value
    return value
class Reg(forms.ModelForm):
    firstname= forms.CharField(label="FIRSTNAME",validators=[firstname], widget=forms.TextInput(attrs={'class':'form-control','id':"floatingInput", 'placeholder':"FIRSTNAME"}))
    lastname= forms.CharField(label="LASTNAME",validators=[lastname], widget=forms.TextInput(attrs={'class':'form-control','id':"floatingInput", 'placeholder':"LASTNAME"}))
    email= forms.EmailField(label="EMAIL", widget=forms.TextInput(attrs={'class':'form-control','id':"floatingInput", 'placeholder':"name@example.com"}))
    phone= forms.IntegerField(validators=[phone], widget=forms.TextInput(attrs={'class':'form-control','id':"floatingInput", 'placeholder':"MOBILE NUMBER"}), label="PHONE")
    password= forms.CharField(validators=[password], widget=forms.PasswordInput(attrs={'class':'form-control','id':"floatingInput", 'placeholder':"PASSWORD"}), label="PASSWORD")
    repassword= forms.CharField(validators=[repassword], widget=forms.PasswordInput(attrs={'class':'form-control','id':"floatingInput", 'placeholder':"REPASSWORD"}), label="REPASSWORD")
    class Meta:
        model = login
        fields= '__all__'
        #fields=('email','phone')
        #exclude=("password","repassword")

class Login(forms.Form):
    usermail= forms.EmailField(label="USER-EMAIL",widget=forms.EmailInput(attrs={'class':'form-control','id':"floatingInput", 'placeholder':"name@example.com"}))
    password= forms.CharField(label="PASSWORD", validators=[loginpassword],widget=forms.TextInput(attrs={'class':'form-control','id':"floatingInput", 'placeholder':"strong password",'for':"floatingInput"}))