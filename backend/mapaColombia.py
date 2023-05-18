from dash import Dash, html, dcc, Input, Output
import geopandas as gpd
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

# Cargar datos de los departamentos
departamentos = gpd.read_file("data/Departamentos.zip")
departamentos_4326 = departamentos.to_crs(epsg=4326)

# Crear figura del mapa
fig = px.choropleth_mapbox(
    departamentos_4326,
    geojson=departamentos_4326.geometry,
    locations=departamentos_4326.index,
)

# Actualizar el diseño del mapa
fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=4,
    mapbox_center={"lat": 4.5709, "lon": -74.2973},
)

# Crear la aplicación Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(
    children=[
        html.H1("Mapa con puntos y línea"),
        dcc.Graph(id="mapa", figure=fig, clickData={"points": []}),
        html.Button("Limpiar", id="limpiar-btn", n_clicks=0)
    ]
)

# Definir el callback para manejar los clics en el mapa
@app.callback(
    Output("mapa", "figure"),
    Output("limpiar-btn", "n_clicks"),
    Input("mapa", "clickData"),
    Input("limpiar-btn", "n_clicks"),
    prevent_initial_call=True
)
def dibujar_linea(clickData, n_clicks):
    if n_clicks % 2 != 0:
        return fig, n_clicks

    if len(clickData["points"]) < 2:
        return fig, n_clicks

    punto1 = clickData["points"][0]
    punto2 = clickData["points"][1]

    linea = go.Scattermapbox(
        lat=[punto1["lat"], punto2["lat"]],
        lon=[punto1["lon"], punto2["lon"]],
        mode="lines",
        line=dict(width=2, color="black")
    )

    fig.add_trace(linea)

    return fig, n_clicks

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)