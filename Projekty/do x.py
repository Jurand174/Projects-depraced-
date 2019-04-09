import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

c=pd.read_excel(r'C:\Users\Jurand\Desktop\hkl.xlsx')
for i in c.index:
    print(1+((-1)**(c['h'][i]+c['k'][i]))+((-1)**(c['h'][i]+c['l'][i]))+((-1)**(c['l'][i]+c['k'][i])))