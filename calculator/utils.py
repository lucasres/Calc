# -*- coding: utf-8 -*-

def validateData(n1, n2):
    try:
        n1 = int(n1)
        n2 = int(n2)
    except ValueError:
        return n1, n2, False
    return n1, n2, True
