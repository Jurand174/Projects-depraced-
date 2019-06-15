import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from scipy.optimize import curve_fit


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df=pd.read_excel(r'C:\Users\Jurand\Desktop\test.xlsx')
app.layout = html.Div([
    dcc.RadioItems(
        options=[
            {'label': 'a*x+b', 'value': 'NYC'},
            {'label': 'a*e^b', 'value': 'MTL'},
            {'label': 'a*x^2+b*x+c', 'value': 'SF'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'}
    ),
dcc.Graph(
        id='basic-interactions',
    figure={
        'data':[{
        'x': df['x'],
        'y': df['X']
}]
    }
)


])

if __name__ == '__main__':
    app.run_server(debug=True)



def fitting():
    f=2
    return f
