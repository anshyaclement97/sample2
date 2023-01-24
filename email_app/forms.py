from django import forms

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,
                              widget=forms.Textarea(attrs={'rows': 3,'cols': 30}))


class regform(forms.Form):
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    password=forms.CharField(max_length=20)
    cpass=forms.CharField(max_length=20)



















#how to convert a forms.py to an html document ?
class register(forms.Form):
    name=forms.CharField(max_length=20)
    phone=forms.IntegerField()
    image=forms.FileField()


