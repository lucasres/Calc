from django import forms

class MyForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    num1 = forms.CharField(max_length=20)
    num2 = forms.CharField(max_length=20)
    op = forms.CharField(max_length=20)