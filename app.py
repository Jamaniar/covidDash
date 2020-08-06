#Switching to a tab set up - Junaid 06/26/2020
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Plotly express and GO. -- Patrick 6/18/2020
import plotly.graph_objects as go
import plotly.express as px

# Data pulls. -- Patrick 6/18/2020
import requests
import json
from urllib.request import urlopen

# Essential tools. -- Patrick 6/18/2020
import pandas as pd 
import numpy as np
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

pd.options.mode.chained_assignment = None

import figures as figures

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)


colors = {
    'background': '#2D3D7B',
    'text': '#FFFFFF'
}


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    [
        # Adding tabs for the 4 main pages currently 3 will finish monday -- Junaid 06/26/2020
        dcc.Tabs(
            [
                # Home page tab. -- Patrick 6/29/2020
                dcc.Tab(
                    label="Home",
                    children=[
                        # Labels for Home. -- Patrick 6/29/2020
                        html.Br(),
                        html.H1(
                            "COVID-19 Tracker Homepage",
                            style={
                                "textAlign": "center",
                                "color": "#FFFFFF",
                                "backgroundColor": colors["background"],
                            },
                        ),
                        html.H2(
                            children="An interactive tool for tracking important COVID-19-related information",
                            style={
                                "textAlign": "center",
                                "color": colors["text"],
                                "backgroundColor": colors["background"],
                            },
                        ),
                    ],
                ),
                dcc.Tab(
                    label="By State",
                    children=[
                        # Labels for State. -- Patrick 6/29/2020
                        html.Br(),
                        html.H1(
                            "COVID-19 Tracking by State",
                            style={
                                "textAlign": "center",
                                "color": colors["text"],
                                "backgroundColor": colors["background"],
                            },
                        ),
                        html.Div(
                            children="An interactive tool for tracking important COVID-19 related information",
                            style={
                                "textAlign": "center",
                                "color": colors["text"],
                                "backgroundColor": colors["background"],
                            },
                        ),
                        html.Div(
                            dcc.Graph(
                                id="Map-with-CurrentInfo", figure=figures.country_fig,
                            ),
                            style={"display": "inline-block"},
                        ),
                        html.Div(
                            dcc.Graph(
                                id="Multi-state-plot", figure=figures.states_line_fig,
                            ),
                            style={"display": "inline-block"},
                        ),
                    ],
                ),
                # the county set of figures on page 2 --Junaid 06/26/2020
                dcc.Tab(
                    label="By County",
                    children=[
                        # Labels for county. -- Patrick 6/29/2020
                        html.Br(),
                        html.H1(
                            "COVID-19 Tracking by County",
                            style={
                                "textAlign": "center",
                                "color": colors["text"],
                                "backgroundColor": colors["background"],
                            },
                        ),
                        html.Div(
                            children="An interactive tool for tracking important COVID-19-related information at a state-level view",
                            style={
                                "textAlign": "center",
                                "color": colors["text"],
                                "backgroundColor": colors["background"],
                            },
                        ),
                        html.Div(
                            dcc.Graph(
                                id="County-Map-1-NC-Default", figure=figures.county_fig,
                            ),
                            style={"display": "inline-block"},
                        ),
                        html.Div(
                            dcc.Graph(
                                id="County-Map-2-NY-Default", figure=figures.county_fig,
                            ),
                            style={"display": "inline-block"},
                        ),
                        html.Div(
                            dcc.Dropdown(
                                id="page-2-dropdown",
                                options=figures.county_options,
                                searchable=True,
                                value="North Carolina",
                                style={
                                    "height": "30px",
                                    "width": "45%",
                                    "textAlign": "center",
                                    "display": "inline-block",
                                    "float": "left",
                                },
                            )
                        ),
                        html.Div(
                            dcc.Dropdown(
                                id="county-dropdown-2",
                                options=figures.county_options,
                                searchable=True,
                                value="New York",
                                style={
                                    "height": "30px",
                                    "width": "45%",
                                    "textAlign": "center",
                                    "display": "inline-block",
                                    "float": "right",
                                },
                            )
                        ),
                    ],
                ),
                # Timeseries plot and the respective dropdowns
                dcc.Tab(
                    label="Timeseries",
                    children=[
                        # Labels for Timeseries. -- Patrick 6/29/2020
                        html.Br(),
                        html.H1(
                            "COVID-19 Timeseries Tool",
                            style={
                                "textAlign": "center",
                                "color": colors["text"],
                                "backgroundColor": colors["background"],
                            },
                        ),
                        html.Div(
                            children="An interactive timeseries for tracking important COVID-19-related information",
                            style={
                                "textAlign": "center",
                                "color": colors["text"],
                                "backgroundColor": colors["background"],
                            },
                        ),
                        html.Div(
                            dcc.Graph(
                                id="Single-state-plot", figure=figures.states_line_fig,
                            ),
                            style={"display": "inline-block"},
                        ),
                        # creating the second single state plot -Junaid 06/22/2020
                        html.Div(
                            dcc.Graph(
                                id="Single-state-plot2", figure=figures.states_line_fig,
                            ),
                            style={"display": "inline-block"},
                        ),
                        html.Div(
                            dcc.Dropdown(
                                id="page-3-dropdown",
                                options=figures.options,
                                searchable=True,
                                value="ny",
                            ),
                            style={
                                "height": "30px",
                                "width": "30%",
                                "display": "inline-block",
                                "textAlign": "left",
                                "float": "left",
                            },
                        ),
                        # The drop down for the second single state plot -Junaid 06/22/2020
                        html.Div(
                            dcc.Dropdown(
                                id="page-3-dropdown2",
                                options=figures.options,
                                searchable=True,
                                value="nc",
                            ),
                            style={
                                "height": "30px",
                                "width": "30%",
                                "display": "inline-block",
                                "textAlign": "right",
                                "float": "right",
                            },
                        ),
                    ],
                ),
                # 4th tab for the worldwide view
                dcc.Tab(
                    label="World View",
                    children=[
                        # Labels for Worldview. -- Patrick 6/29/2020
                        html.Br(),
                        html.H1(
                            "World View",
                            style={
                                "textAlign": "center",
                                "color": colors["text"],
                                "backgroundColor": colors["background"],
                            },
                        ),
                        html.Div(
                            dcc.Graph(id="World-plot", figure=figures.world_fig,),
                            style={"display": "inline-block", "textAlign": "center"},
                        ),
                    ],
                ),
            ]
        )
    ]
)
# implemented the app callbacks for the 2nd page will add the rest on monday --Junaid 06/26/2020
@app.callback(
    Output("County-Map-1-NC-Default", "figure"), [Input("page-2-dropdown", "value")]
)

# Changes fig to the selected state. -- Patrick 6/18/2020
def update_county_state(selected_county_state):
    county_state = figures.county_df_us[
        figures.county_df_us.state == selected_county_state
    ]
    county_state["fips"] = county_state["countyId"].str.split(":").str[1]
    dtype = {"fips": str}
    county_coords = pd.read_csv("datasets/county_coords.csv")
    selected_coords = county_coords[county_coords.state == selected_county_state]

    # Removing highest value for county cases, there is a row that sums all cases. -- Patrick 6/16/2020
    county_state = county_state.drop(county_state["cases"].idxmax())

    # For some reason these need to be printed before they're functional... -- Patrick 6/16/2020
    # These values allow the figure to scale based on selected state. -- Patrick 6/17/2020
    max_color = county_state["cases"].max()
    min_color = county_state["cases"].min()

    # Main figure plot. Plotly express choro. -- Patrick 6/15/2020
    fig_county = px.choropleth_mapbox(
        county_state,
        geojson=counties,
        locations="fips",
        color="cases",
        color_continuous_scale="YlGnBu",
        range_color=(min_color, max_color),
        mapbox_style="carto-positron",
        zoom=5.5,
        center={
            "lat": selected_coords["lat"].iloc[0].astype(float),
            "lon": selected_coords["lon"].iloc[0].astype(float),
        },
        opacity=0.5,
        labels={"cases": "Cases"},
        hover_name="county",
    )
    fig_county.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0}, width=935, height=758
    )
    return fig_county


# Callback for 2nd county dropdown. -- Patrick 6/18/2020
@app.callback(
    Output("County-Map-2-NY-Default", "figure"), [Input("county-dropdown-2", "value")]
)

# Changes fig to selected state. -- Patrick 6/18/2020
def update_county_state2(selected_county_state):
    county_state = figures.county_df_us[
        figures.county_df_us.state == selected_county_state
    ]
    county_state["fips"] = county_state["countyId"].str.split(":").str[1]
    dtype = {"fips": str}
    county_coords = pd.read_csv("datasets/county_coords.csv")
    selected_coords = county_coords[county_coords.state == selected_county_state]

    # Same as before, dropping sum row. -- Patrick 6/17/2020
    county_state = county_state.drop(county_state["cases"].idxmax())

    max_color2 = county_state["cases"].max()
    min_color2 = county_state["cases"].min()

    # Implementing above feature to scale graphs. -- Patrick 6/17/2020
    fig_county = px.choropleth_mapbox(
        county_state,
        geojson=counties,
        locations="fips",
        color="cases",
        color_continuous_scale="YlGnBu",
        range_color=(min_color2, max_color2),
        mapbox_style="carto-positron",
        zoom=5.5,
        center={
            "lat": selected_coords["lat"].iloc[0].astype(float),
            "lon": selected_coords["lon"].iloc[0].astype(float),
        },
        opacity=0.5,
        labels={"cases": "Cases"},
        hover_name="county",
    )
    fig_county.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0}, width=935, height=758
    )
    return fig_county


# Appcallbacks for page3
@app.callback(
    Output("Single-state-plot", "figure"), [Input("page-3-dropdown", "value")]
)

# Updates the single state plot -- Junaid 06/29/2020
def update_state(selected_state):
    state_id = selected_state
    api_key = "/daily.json"
    url = "http://covidtracking.com/api/v1/states/%s%s" % (state_id, api_key)
    r2 = requests.get(url)
    new_df = pd.DataFrame(data=r2.json())
    new_df["date"] = pd.to_datetime(new_df["date"], format="%Y%m%d")
    fig = px.line(
        new_df,
        x="date",
        y="positive",
        title="COVID-19 Timeseries by State (Use dropdown)",
    )
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(
        height=758,
        width=920,
        # Transparency. -- Patrick 6/29/2020
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig


# app call back for the second single state graph -Junaid 06/22/2020
@app.callback(
    Output("Single-state-plot2", "figure"), [Input("page-3-dropdown2", "value")]
)
# updates the second single state graph -Junaid 06/22/2020
def update_state2(selected_state):
    state_id = selected_state
    api_key = "/daily.json"
    url = "http://covidtracking.com/api/v1/states/%s%s" % (state_id, api_key)
    r2 = requests.get(url)
    new_df = pd.DataFrame(data=r2.json())
    new_df["date"] = pd.to_datetime(new_df["date"], format="%Y%m%d")
    fig = px.line(
        new_df,
        x="date",
        y="positive",
        title="COVID-19 Timeseries by State (Use dropdown)",
    )
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(
        height=758,
        width=920,
        # Transparency. -- Patrick 6/29/2020
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig
if __name__ == '__main__':
    app.run_server(debug=True)
    