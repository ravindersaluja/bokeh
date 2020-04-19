#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:21:29 2020

@author: ravindersaluja
"""

from bokeh.plotting import figure, output_file, show

x=[1,2,3,4,5]
y=[4,6,2,4,3]

output_file('index.html')
p=figure(title='hello')
p.line(x,y, legend='test', line_width=5)

show(p)

