# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from calculator.utils import validateData

# Create your views here.

def operation(request, op, n1, n2):
    n1 = float(n1)
    n2 = float(n2)
    valid = True

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
            valid = False

    return render(request, 'operation.html', vars())
