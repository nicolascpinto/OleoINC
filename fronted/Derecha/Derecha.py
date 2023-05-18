from dash import Dash, html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc


#Importamos el Backend
from backend.mapaColombia import fig

Derecha = dbc.Container(
    [
        html.H1("Mapa de Colombia", className='text-center'),
        dcc.Graph(
            figure=fig,
            style={
                'width': '100%',
                'height':'1000px'
            }
        ),
    ]   
),