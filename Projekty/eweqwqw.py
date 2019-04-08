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
image_directory = '/Users/Jurand/Desktop/'
list_of_images = ['image.png']
static_image_route = '/static/'
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_excel(r'C:\Users\Jurand\Desktop\kon.xlsx')
app.layout = html.Div([
html.Div([

    html.Div([
html.H1(children='FizQuiz')]),

        ]
        ,
            style = {
                 'vertical-align': 'middle',
                'background-color': 'lightblue',



  'text-align': 'center',

            }),
    html.Hr(),

    html.Div([
    dash_table.DataTable(
        editable=True,
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("rows"),

        style_cell={
            'whiteSpace': 'no-wrap',
            'overflow': 'hidden',
            'maxWidth': 0,
        }

    )],style={'background-color': 'lightblue'}),
    html.Div(
        id='tak',
        style={'textAlign':'center','font-size':'3.0rem'},

    ),
html.Div([
    dcc.Graph(id='table-editing-simple-output',style={'width': '80%', 'display': 'block',
  'margin-left': 'auto',
  'margin-right': 'auto'
})] ),

],style={'background-color': 'lightblue'})


@app.callback(
    Output('table-editing-simple-output', 'figure'),
    [Input('table', 'data'),
     Input('table', 'columns')])
def display_output(rows, columns):
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    y = df['nazwa drużyny'].tolist()
    df.set_index("nazwa drużyny", inplace=True)
    df = df.transpose()
    sum = []
    df.astype(np.int64)

    for i in df.columns:
        sum.append(df[i].astype(np.int64).sum())

    t = pd.DataFrame(data={'dr': y, 'punkty': sum})
    t.sort_values(by=['punkty'], inplace=True)

    figure = {
        'data': [go.Bar(
            x=t['punkty'].tolist(),
            y=t['dr'].tolist(),
            orientation='h',
            text=t['punkty'].tolist(),
            textposition='auto',
            marker=dict(
                    color=['rgb(6,20,255)', 'rgb(6,20,255)','rgb(6,20,255)', 'rgb(6,20,255)',
                            'rgb(6,20,255)', 'rgb(6,20,255)',
                            'rgb(6,20,255)', 'rgb(150,75,0)',
                            'rgb(192, 192, 192)', 'rgb(255,215,4)'
                   ]),
        )]

    }
    return figure

@app.callback  (
    Output('tak', 'children'),
    [Input('table', 'data'),
     Input('table', 'columns')])
def display_output(rows, columns):
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    y = df['nazwa drużyny'].tolist()
    df.set_index("nazwa drużyny", inplace=True)
    df = df.transpose()
    sum = []
    df.astype(np.int64)

    for i in df.columns:
        sum.append(df[i].astype(np.int64).sum())

    t = pd.DataFrame(data={'dr': y, 'punkty': sum})
    t.sort_values(by=['punkty'],ascending=False,inplace=True)

    k=t.iloc[0].tolist()[0]

    return 'Obecnie wygrywa drużyna  "{}"'.format(k)



if __name__ == '__main__':
    app.run_server(debug=True)
