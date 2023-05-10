from dash import html
import dash_bootstrap_components as dbc

Inferior = dbc.Container(
    [
        html.H5('© Copyright 2023', className='text-center'),
        html.Div(
            [
            html.H6('Esta página web es realizada con fines educativos, derechos de programación al estudiante y al ingeniero Carlos Arturo quien aporta su ayuda para cumplir los parámetros.', className='text-center, small'),
            ]
        )
    ]
)