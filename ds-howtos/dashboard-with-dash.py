# WARNING
#
# this code won't work from a notebook server
# you need to kick it off locally using
#
# python dashboard-with-dash.py

import plotly.express as px

from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Load Data
df = px.data.tips()

# Build App
app = JupyterDash(__name__)

# create html content
app.layout = html.Div([
    html.H1("JupyterDash Demo"),
    # the graph
    dcc.Graph(id='graph'),
    # the colorscale picker (dropdown)
    html.Label([
        "colorscale",
        dcc.Dropdown(
            id='colorscale-dropdown', clearable=False,
            value='plasma', options=[
                {'label': c, 'value': c}
                for c in px.colors.named_colorscales()
            ])
    ]),
])

# flask-friendly
# Define callback to update graph
@app.callback(
    Output('graph', 'figure'),
    [Input("colorscale-dropdown", "value")]
)

def update_figure(colorscale):
    return px.scatter(
        df, x="total_bill", y="tip", color="size",
        color_continuous_scale=colorscale,
        render_mode="webgl", title="Tips"
    )

# Run app and display result inline in the notebook
# here the notebook is the http server !

app.run_server(mode='external')
