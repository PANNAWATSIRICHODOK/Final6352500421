# -*- coding: utf-8 -*-
"""sort_object.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ro68sZxdG39rkTg7Sf0FxkgqMYYAA1yw
"""

obj_detected = {'bottle': [110, 30], 'glass': [60, 35], 'book': [310, 23], 'phone': [90, 33], 'dice': [155, 38], 'mouse':
[200, 45], 'keyboard': [298, 65], 'fan': [300, 36]}

obj_detected

dict(sorted(obj_detected.items(), key=lambda item: item[1]))