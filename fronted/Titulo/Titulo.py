from dash import html
import dash_bootstrap_components as dbc

#importar componentes del navegador
from .Descripcion.LogoUD import LogoUD
from .Descripcion.Texto_UD import Texto_UD
from .Descripcion.Simbolo import Simbolo


Titulo = dbc.Container(
    [
        html.H1('CÁLCULO DE OLEODUCTOS', style={'font-family': 'Montserrat', 'color': '#333', 'font-size': '48px', 'font-weight': 'bold', 'text-align': 'center'}),
        dbc.Row(
            [
                dbc.Col(LogoUD, md=3, style={'background-color':'white'}),
                dbc.Col(Texto_UD, md=6 , style={'background-color':'white'}),
                dbc.Col(Simbolo,md =3, style={'background-color':'white'}),
            ]
        )
    ]
)
