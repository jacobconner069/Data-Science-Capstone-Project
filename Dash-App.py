import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load data
import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"

r = requests.get(url)
open("spacex_launch_dash.csv", "wb").write(r.content)
spacex_df = pd.read_csv('spacex_launch_dash.csv')

max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

app = dash.Dash(__name__)

# Layout
app.layout = html.Div(children=[

    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center'}),

    dcc.Dropdown(
        id='site-dropdown',
        options=[{'label': 'All Sites', 'value': 'ALL'}] +
                [{'label': i, 'value': i} for i in spacex_df['Launch Site'].unique()],
        value='ALL',
        searchable=True
    ),

    html.Br(),

    dcc.Graph(id='success-pie-chart'),

    html.Br(),

    html.P("Payload range (Kg):"),

    dcc.RangeSlider(
        id='payload-slider',
        min=min_payload,
        max=max_payload,
        step=1000,
        value=[min_payload, max_payload],
        marks={int(i): str(int(i)) for i in range(0, 10001, 1000)}
    ),

    html.Br(),

    dcc.Graph(id='success-payload-scatter-chart')
])

# PIE CHART
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie(site):

    if site == 'ALL':
        df = spacex_df[spacex_df['class'] == 1]
        fig = px.pie(df, names='Launch Site', title='Total Successful Launches by Site')
        return fig

    df = spacex_df[spacex_df['Launch Site'] == site]
    fig = px.pie(df, names='class', title=f'Success vs Failure for {site}')
    return fig


# SCATTER PLOT
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_scatter(site, payload):

    low, high = payload

    df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= low) &
        (spacex_df['Payload Mass (kg)'] <= high)
    ]

    if site != 'ALL':
        df = df[df['Launch Site'] == site]

    fig = px.scatter(
        df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        title='Payload vs Outcome'
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)