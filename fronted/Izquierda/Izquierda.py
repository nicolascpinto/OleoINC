from dash import html, dcc
import dash_bootstrap_components as dbc

# Crear un componente de espaciado
espaciado = html.Div(style={'margin': '20px'})

# Crear un componente de espaciado estilo 2
espaciado2 = html.Div(style={'margin': '10px'})

# Crear un componente de almacenamiento para la pendiente
store_pendiente = dcc.Store(id='store-pendiente', data=None)

# Crear el modal para ingresar la pendiente
modal_pendiente = dbc.Modal(
    [
        dbc.ModalHeader("Ingrese l a pendiente"),
        dbc.ModalBody(
            [
                dbc.Label("Pendiente:"),
                dcc.Input(id='input-pendiente', type='number'),
            ]
        ),
        dbc.ModalFooter(
            [
                dbc.Button("Cancelar", id='cancelar-pendiente', className='mr-auto'),
                dbc.Button("Guardar", id='guardar-pendiente', className='ml-auto'),
            ]
        ),
    ],
    id='modal-pendiente',
    size='md'
)

# Actualizar el contenido de Izquierda para incluir el modal y el componente de almacenamiento
Izquierda = dbc.Container(
    [
        html.Div(
            [
                html.Label('Selecciona un color para tu oleducto:'),
                espaciado,
                dbc.Button('Rojo', color='danger', id='boton-rojo', className='mr-1'),
                dbc.Button('Azul', color='primary', id='boton-azul', className='mr-1'),
                dbc.Button('Verde', color='success', id='boton-verde', className='mr-1'),
                dbc.Button('Naranja', color='warning', id='boton-naranja', className='mr-1'),
            ]
        ),
        
        html.Hr(),
        
        html.Div(
            [
                html.Label('Por favor de click en el botón e ingrese la pendiente'),
                espaciado,
                dbc.Button('Ingresar pendiente', id='abrir-modal', className='ml-3'),
                store_pendiente,  # Agregar el componente de almacenamiento aquí
                modal_pendiente  # Agregar el modal aquí
            ]
        ),
        
        html.Hr(),
        
        html.Div(
            [
                html.Label('¿Cuantos oleoductos quiere trazar? (solo son posibles 3)'),
                espaciado,
                dbc.Button('1', className='mr-1'),
                espaciado2,
                dbc.Button('2', className='mr-1'),
                espaciado2,
                dbc.Button('3', className='mr-1'),
            ]
        ),
        
        html.Hr(),
        
        html.Div(
            [
                dbc.Label('Tagea tus oleoductos:'),
                dbc.Input(id='input_oleoducto', type='number', placeholder='Ingresa el tag')
            ]
        )
    ]
)