# Note Log until BitBucket --
# Changed spacing on = to be consistent
# Import statements, revise to remove unused - Patrick 6/10/2020
# Created multichart, need to make functional checklist. -- Patrick 6/11/2020
# Added Styling to the dropdown to make it closer to the figure it interacts with - Junaid 6/11/2020
# Added colors(in other version) to the display to make it look more appealing -Junaid 6/11/2020
# Swapped the base version to a page based version - Junaid 6/11/2020
# Added page 2, created figures for county level -- Patrick 6/16/2020
# These import are gross, fixing later..  -- Patrick 6/16/2020
# Changed all color schemes/moved dropdowns. -- Patrick 6/17-18/2020
# Added hyperlinks to pg1, 2 for ease of access. -- Patrick 6/18/2020
# NOTES FOR NANA --
#   These figure sizes do NOT upgrade to screen size. These are set at our laptop's resolution atm. -- Patrick 6/17/2020
#   Additionally -- Our screen resolution is 1920x1080 by default, but the zoom is set incorrectly. I am setting these figures to display
#                   properly at 1920x1080p. -- Patrick 6/17/2020
#   There may be SOME duplicate/unnecessary code scattered about. I am working on finding it and removing it. -- Patrick 6/17/2020

# Dash core. -- Patrick 6/18/2020
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

pd.options.mode.chained_assignment = None

# Page references. -- Patrick 6/18/2020
import Covid19_page1 as pg1
import Covid19_page2 as pg2
import Covid19_page3 as pg3
import Covid19_page4 as pg4
import Covid19_figures as figures
import Covid19_about as about


# Import county data. -- Patrick 6/14/2020
with urlopen(
    "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
) as response:
    counties = json.load(response)
# Dash declaration :). -- Patrick 6/12/2020
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Colors for html elements, declared early. -- Patrick 6/12/2020
colors = {"background": "#2D3D7B", "text": "#FFFFFF"}

# App layout page, may need to be used for full background. -- Patrick 6/17/2020
app.layout = html.Div(
    style={"backgroundcolor": colors["background"], "height": 962},
    children=[dcc.Location(id="url", refresh=False), html.Div(id="page-content")],
)

# Main homepage layout. Made significant edits, fully formatting page.. -- Patrick 6/18/2020
index_page = (
    html.Div(
        style={},
        children=[
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
            html.Br(),
            # This block contains the first sub-headers. -- Patrick 6/18/2020
            html.Div(
                style={},
                children=[
                    html.H2(
                        "COVID-19 by State",
                        style={
                            "textAlign": "center",
                            "color": "#FFFFFF",
                            "backgroundColor": colors["background"],
                        },
                    ),
                    html.H3(
                        dcc.Link("By State", href="/page-1"),
                        style={"textAlign": "center"},
                    ),
                    html.H2(
                        "COVID-19 by County",
                        style={
                            "textAlign": "center",
                            "color": "#FFFFFF",
                            "backgroundColor": colors["background"],
                        },
                    ),
                    html.H3(
                        dcc.Link("By County", href="/page-2"),
                        style={"textAlign": "center",},
                    ),
                    html.H2(
                        "COVID-19 Timeseries",
                        style={
                            "textAlign": "center",
                            "color": "#FFFFFF",
                            "backgroundColor": colors["background"],
                        },
                    ),
                    html.H3(
                        dcc.Link("Timeseries", href="/page-3"),
                        style={"textAlign": "center"},
                    ),
                    html.H2(
                        "COVID-19 World View",
                        style={
                            "textAlign": "center",
                            "color": "#FFFFFF",
                            "backgroundColor": colors["background"],
                        },
                    ),
                    html.H3(
                        dcc.Link("World View", href="/page-4"),
                        style={"textAlign": "center"},
                    ),
                ],
            ),
        ],
    ),
)

# Start of page 1 layout. -- Patrick 6/17/2020
page_1_layout = html.Div(
    style={},
    children=[
        # Title formatting... -- Patrick 6/17/2020
        html.H1(
            "COVID-19 Tracker by State",
            style={
                "textAlign": "center",
                "color": colors["text"],
                "backgroundColor": colors["background"],
            },
        ),
        html.Div(
            children="An interactive tool for tracking important COVID-19-related information",
            style={
                "textAlign": "center",
                "color": colors["text"],
                "backgroundColor": colors["background"],
            },
        ),
        html.Div(id="page-1-content"),
        # End of Title, start of figure plots -- Patrick 6/17/2020
        html.Div(
            dcc.Graph(id="Map-with-CurrentInfo", figure=figures.country_fig,),
            style={"display": "inline-block"},
        ),
        html.Div(
            dcc.Graph(id="Multi-state-plot", figure=figures.states_line_fig,),
            style={"display": "inline-block"},
        ),
        html.Div(id="page-1-content"),
        html.Br(),
        html.Br(),
        # Hyperlinks at bottom of page... working on adding to second page. -- Patick 6/18/2020
        html.H2(
            "-- Useful Links -- ",
            style={
                "textAlign": "center",
                "color": "#FFFFFF",
                "backgroundColor": colors["background"],
            },
        ),
        html.H3(
            dcc.Link("Home Page", href="/"),
            style={"textAlign": "left", "float": "left", "display": "inline-block"},
        ),
        html.H3(
            dcc.Link("County View", href="/page-2"),
            style={"textAlign": "left", "float": "right", "display": "inline-block"},
        ),
    ],
)

# Start of page 2 layout. -- Patrick 6/16/2020
page_2_layout = html.Div(
    style={},
    children=[
        html.H1(
            "COVID-19 Tracker by County",
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
        html.Br(),
        html.Div(id="page-2-content"),
        # End of Title, start of figure plots -- Patrick 6/16/2020
        html.Div(
            dcc.Graph(id="County-Map-1-NC-Default", figure=figures.county_fig,),
            style={"display": "inline-block"},
        ),
        html.Div(
            dcc.Graph(id="County-Map-2-NY-Default", figure=figures.county_fig,),
            style={"display": "inline-block"},
        ),
        # FINALLY MOVED DROPDOWN. Html is a headache. -- Patrick 6/18/2020
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
        html.Br(),
        html.H2(
            "--Useful Links -- ",
            style={
                "textAlign": "center",
                "color": "#FFFFFF",
                "backgroundColor": colors["background"],
            },
        ),
        html.H3(
            dcc.Link("Home Page", href="/"),
            style={"textAlign": "left", "float": "left ", "display": "inline-block"},
        ),
        html.H3(
            dcc.Link("Timeseries", href="/page-3"),
            style={"textAlign": "left", "float": "right", "display": "inline-block"},
        ),
    ],
)

page_3_layout = html.Div(
    style={},
    children=[
        html.H1(
            "COVID-19 Timeseries Tool",
            style={
                "textAlign": "center",
                "color": colors["text"],
                "backgroundColor": colors["background"],
            },
        ),
        html.Div(
            dcc.Graph(id="Single-state-plot", figure=figures.states_line_fig,),
            style={"display": "inline-block"},
        ),
        # creating the second single state plot -Junaid 06/22/2020
        html.Div(
            dcc.Graph(id="Single-state-plot2", figure=figures.states_line_fig,),
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
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H2(
            "-- Useful Links -- ",
            style={
                "textAlign": "center",
                "color": "#FFFFFF",
                "backgroundColor": colors["background"],
            },
        ),
        html.H3(
            dcc.Link("Home Page", href="/"),
            style={"textAlign": "left", "float": "left", "display": "inline-block"},
        ),
        html.H3(
            dcc.Link("By State", href="/page-1"),
            style={"textAlign": "left", "float": "right", "display": "inline-block"},
        ),
    ],
)

page_4_layout = html.Div(
    style={},
    children=[
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
        html.H2(
            "-- Useful Links -- ",
            style={
                "textAlign": "center",
                "color": "#FFFFFF",
                "backgroundColor": colors["background"],
            },
        ),
        html.H3(
            dcc.Link("Home Page", href="/"),
            style={"textAlign": "left", "float": "left", "display": "inline-block"},
        ),
        html.H3(
            dcc.Link("By State", href="/page-1"),
            style={"textAlign": "left", "float": "right", "display": "inline-block"},
        ),
    ],
)


# Beginning of the About Page layout. -- Patrick 6/18/2020
about_page_layout = html.Div(
    style={},
    children=[
        html.H1(
            "About Us",
            style={
                "textAlign": "center",
                "color": colors["text"],
                "backgroundColor": colors["background"],
            },
        ),
    ],
)

# Callback for the initial page-1-dropdown. -- Patrick 6/17/2020
@app.callback(
    Output("Single-state-plot", "figure"), [Input("page-3-dropdown", "value")]
)

# Fig2 updates, needed. -- Patrick 6/15/2020
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
        height=600,
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
        height=600,
        width=920,
        # Transparency. -- Patrick 6/29/2020
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig


# Callback for page-1-dropdown. -- Patrick 6/18/2020
@app.callback(
    dash.dependencies.Output("page-3-content", "children"),
    [dash.dependencies.Input("page-3-dropdown", "value")],
)

# Sadly, need to display this under dropdown. Future work. **** -- Patrick 6/18/2020
def page_3_dropdown(value):
    return "{}".format(value)


# Callback for switch urls. -- Patrick 6/18/2020
@app.callback(
    dash.dependencies.Output("page-content", "children"),
    [dash.dependencies.Input("url", "pathname")],
)

# Page change formatting. -- Patrick 6/18/2020
def display_page(pathname):
    if pathname == "/page-1":
        return page_1_layout
    elif pathname == "/page-2":
        return page_2_layout
    elif pathname == "/page-3":
        return page_3_layout
    elif pathname == "/page-4":
        return page_4_layout
    elif pathname == "/about":
        return about_page_layout
    else:
        return index_page


# Callback for 1st county dropdown. -- Patrick 6/18/2020
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
        margin={"r": 0, "t": 0, "l": 0, "b": 0}, width=935, height=770
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
        margin={"r": 0, "t": 0, "l": 0, "b": 0}, width=935, height=770
    )
    return fig_county


# Server start. -- Patrick 6/18/2020
if __name__ == "__main__":
    app.run_server(debug=True)
