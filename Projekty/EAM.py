import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

c=pd.read_csv(r'C:\Users\Jurand\Desktop\EAM projekt\Kasia\S4_0004.txt')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([



    dcc.Graph(
        figure={
'data':[go.Scatter3d(
            x=c['MagX'].tolist(),
            y=c['MagY'].tolist(),
            z=c['MagZ'].tolist()

)]}

    )
    ],style={'height':'200%'})



if __name__ == '__main__':
    app.run_server(debug=True)