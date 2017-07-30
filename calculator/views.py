# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from calculator.forms import MyForm

# Create your views here.

def index(request, valid = True):
    op = ""
    num1 = ""
    num2 = ""
    if request.method == 'POST':
        form = MyForm(request.POST or Nome)
        if form.is_valid():
            op = form.cleaned_data['op']
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            if op=="+":
                rs = float(num1)+float(num2)
            elif op == "-":
                rs = float(num1)-float(num2)
            elif op == "x":
                rs = float(num1)*float(num2)
            elif op == "/":
                rs = float(num1)/float(num2)
            else :
                rs = "operação não reconhecida"
            return render(request,"base.html",vars())


    form = MyForm()
    return render(request, 'base.html', vars())
