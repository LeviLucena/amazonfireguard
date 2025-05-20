import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import requests

app = dash.Dash(__name__)

def load_data():
    response = requests.get("http://localhost:5000/api/fires")
    data = response.json()
    return pd.DataFrame(data)

df = load_data()
fig = px.scatter_mapbox(
    df,
    lat="latitude",
    lon="longitude",
    color="brightness",
    hover_data=["acq_date", "satellite"],
    zoom=4,
    height=600
)
fig.update_layout(mapbox_style="open-street-map")

app.layout = html.Div([
    html.H1("Monitoramento de Queimadas - AmazonFireGuard"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
