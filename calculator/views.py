# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from calculator.forms import FormCalc

# Create your views here.

def index(request, valid = True):
    if request.method == 'POST':
        form = FormCalc(request.POST)
        if form.is_valid():
            return redirect('%s/%d/%d/', form.op.bound_data, form.n1.bound_data,
                            form.n2.bound_data)
        return redirect('/', valid = False)

    form = FormCalc()
    return render(request, 'base.html', vars())

def operation(request, op, n1, n2):
    n1 = float(n1)
    n2 = float(n2)

    if op == 'soma':
        op = '+'
        result = n1 + n2
    elif op == 'sub':
        op = '-'
        result = n1 - n2
    elif op == 'mul':
        op = '*'
        result = n1 * n2
    elif op == 'div':
        op = '/'
        try:
            result = n1 / n2
        except ZeroDivisionError:
            return redirect('/', valid = False)

    return render(request, 'operation.html', vars())
