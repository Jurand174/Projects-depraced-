import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import flask
import glob
import os


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Graph()
    ])



if __name__ == '__main__':
    app.run_server(debug=True)