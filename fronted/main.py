from dash import html, dcc
import dash_bootstrap_components as dbc

#import fronted
from fronted.Titulo.Titulo import Titulo
from fronted.Izquierda.Izquierda import Izquierda
from fronted.Derecha.Derecha import Derecha
from fronted.Inferior.Inferior import Inferior

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(Titulo, md=12, style={'background-color':'red'}),
                dbc.Col(Izquierda, md=4,style={'background-color':'green'}),
                dbc.Col(Derecha, md=8, style={'background-color':'orange'}),
                dbc.Col(Inferior, md=12, style={'background-color':'blue'}),
            ]
        )
    ]
)
