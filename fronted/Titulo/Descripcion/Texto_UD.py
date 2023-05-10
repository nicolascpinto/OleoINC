from dash import html
import dash_bootstrap_components as dbc

Texto_UD = dbc.Container(
    [
        html.H5('Universidad Distrital Francisco José De Caldas.', className='text-center'),
        html.Div(
            [
                html.H5('Facultad Tecnológica', className='text-center'),
                html.H5('Ingeniería Civil (ciclos)', className='text-center'),
                html.H5('Programación II', className='text-center'),
                html.H5('2023', className='text-center')
            ]
        )
    ]
)
