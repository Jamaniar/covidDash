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

# PAGE 1 CONTENTS --
# country
# states_line
# PAGE 2 CONTENTS --
# county_map
#
# PAGE 3 CONTENTS --
#
#
# PAGE 4 CONCENTS --
#
#

country_r = requests.get(
    "https://covidtracking.com/api/v1/states/current.json"
)  # Changed to current.json, doesn't work with daily. -- Patrick 6/10/2020
country_df = pd.DataFrame(data=country_r.json())
country_df["date"] = pd.to_datetime(country_df["date"], format="%Y%m%d")

# Hover pop-up to display relevant information. FOR FIG1 -- Patrick 6/10/2020
country_df["text"] = (
    "State: "
    + country_df["state"]
    + "<br>"
    + "Date: "
    + country_df["date"].astype(str)
    + "<br>"
    + "Positive Cases: "
    + country_df["positive"].astype(str)
    + " --- Negative Cases: "
    + country_df["negative"].astype(str)
    + "<br>"
    + "Hospitalized Currently: "
    + country_df["hospitalizedCurrently"].astype(str)
    + " --- Total hospitalized: "
    + country_df["hospitalizedCumulative"].astype(str)
    + "<br>"
    + "Total Death: "
    + country_df["death"].astype(str)
    + " --- Total Recovered: "
    + country_df["recovered"].astype(str)
)

# country_fig declaration, displays map of USA with current cases and relevant information on hover. -- Patrick 6/10/2020
country_fig = go.Figure(
    data=go.Choropleth(
        locations=country_df["state"],
        z=country_df["positive"].astype(float),
        locationmode="USA-states",
        colorscale="YlGnBu",
        text=country_df["text"],
        marker_line_color="black",
        colorbar_title="Cases",
    )
)

country_fig.update_layout(
    title_text="Current COVID-19 Values by State (Hover for Info)",
    geo_scope="usa",
    geo_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    autosize=False,
    width=940,
    height=788,
)
# Modified figsize to fit tab view. -- Patrick 6/29/2020

states_line_r = requests.get("https://covidtracking.com/api/v1/states/daily.json")
states_line_df = pd.DataFrame(data=states_line_r.json())
states_line_df["date"] = pd.to_datetime(states_line_df["date"], format="%Y%m%d")

states_line_fig = px.line(
    states_line_df,
    x="date",
    y="positive",
    color="state",
    line_group="state",
    title="COVID-19 Timeseries for ALL States (Use Sidebar))",
    hover_name="state",
    hover_data=["positive", "negative", "hospitalizedCurrently", "death", "recovered"],
    width=920,
    height=788,
)

states_line_fig.update_xaxes(rangeslider_visible=True)
states_line_fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
)


county_df = pd.read_json(
    "https://coronadatascraper.com/data.json"
)  # Modify this with user state selection. -- Patrick 6/14/2020
county_df_us = county_df[county_df.country == "United States"]
county_df_state = county_df_us[county_df_us.state == "North Carolina"]
county_df_state["fips"] = county_df_state["countyId"].str.split(":").str[1]
dtype = {"fips": str}

with urlopen(
    "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
) as response:
    counties = json.load(response)
# Create initial figure which will display NC as default. -- Patrick 6/13/2020
county_fig = px.choropleth_mapbox(
    county_df_state,
    geojson=counties,
    locations="fips",
    color="cases",
    color_continuous_scale="YlGnBu",
    range_color=(0, 7000),
    mapbox_style="carto-positron",
    zoom=3,
    center={"lat": 37.0902, "lon": -95.7129},
    opacity=0.5,
    labels={"cases": "Cases"},
    hover_name="county",
)
county_fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, width=930, height=760)

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]


world_df = pd.read_json(
    "https://coronavirus-19-api.herokuapp.com/countries"
)  # Modify this with user state selection. -- Patrick 6/14/2020
# Created world view. Set max to USA... thx phase 2. -- Patrick 6/24/2020
world_df = world_df.drop(world_df["cases"].idxmax())
world_max_cases = world_df["cases"].max()

world_fig = px.choropleth(
    world_df,
    color_continuous_scale="YlGnBu",
    locationmode="country names",
    locations="country",
    color="cases",
    hover_name="country",
    range_color=[100000, world_max_cases],
    width=1900,
    height=812,
)

world_fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
)

options = [
    {"label": "Alabama", "value": "al"},
    {"label": "Alaska", "value": "ak"},
    {"label": "Arizona", "value": "az"},
    {"label": "Arkansas", "value": "ar"},
    {"label": "American Samoa", "value": "as"},
    {"label": "California", "value": "ca"},
    {"label": "Colorado", "value": "co"},
    {"label": "Connecticut", "value": "ct"},
    {"label": "District of Columbia", "value": "dc"},
    {"label": "Delaware", "value": "de"},
    {"label": "Florida", "value": "fl"},
    {"label": "Georgia", "value": "ga"},
    {"label": "Guam", "value": "gu"},
    {"label": "Hawaii", "value": "hi"},
    {"label": "Idaho", "value": "id"},
    {"label": "Illinois", "value": "il"},
    {"label": "Indiana", "value": "in"},
    {"label": "Iowa", "value": "ia"},
    {"label": "Kansas", "value": "ks"},
    {"label": "Kentucky", "value": "ky"},
    {"label": "Louisiana", "value": "la"},
    {"label": "Maine", "value": "me"},
    {"label": "Maryland", "value": "md"},
    {"label": "Massachusetts", "value": "ma"},
    {"label": "Michigan", "value": "mi"},
    {"label": "Minnesota", "value": "mn"},
    {"label": "Mississippi", "value": "ms"},
    {"label": "Missouri", "value": "mo"},
    {"label": "Montana", "value": "mt"},
    {"label": "Northern Mariana Islands", "value": "mp"},
    {"label": "Nebraska", "value": "ne"},
    {"label": "Nevada", "value": "nv"},
    {"label": "New Hampshire", "value": "nh"},
    {"label": "New Jersey", "value": "nj"},
    {"label": "New Mexico", "value": "nm"},
    {"label": "New York", "value": "ny"},
    {"label": "North Carolina", "value": "nc"},
    {"label": "North Dakota", "value": "nd"},
    {"label": "Ohio", "value": "oh"},
    {"label": "Oklahoma", "value": "ok"},
    {"label": "Oregon", "value": "or"},
    {"label": "Pennsylvania", "value": "pa"},
    {"label": "Puerto Rico", "value": "pr"},
    {"label": "Rhode Island", "value": "ri"},
    {"label": "South Carolina", "value": "sc"},
    {"label": "South Dakota", "value": "sd"},
    {"label": "Tennessee", "value": "tn"},
    {"label": "Texas", "value": "tx"},
    {"label": "Utah", "value": "ut"},
    {"label": "Vermont", "value": "vt"},
    {"label": "Virginia", "value": "va"},
    {"label": "Virgin Islands", "value": "vi"},
    {"label": "Washington", "value": "wa"},
    {"label": "West Virginia", "value": "wv"},
    {"label": "Wisconsin", "value": "wi"},
    {"label": "Wyoming", "value": "wy"},
]
county_options = [
    {"label": "Alabama", "value": "Alabama"},
    {"label": "Alaska", "value": "Alaska"},
    {"label": "Arizona", "value": "Arizona"},
    {"label": "Arkansas", "value": "Arkansas"},
    {"label": "American Samoa", "value": "American Samoa"},
    {"label": "California", "value": "California"},
    {"label": "Colorado", "value": "Colorado"},
    {"label": "Connecticut", "value": "Connecticut"},
    {"label": "District of Columbia", "value": "District of Columbia"},
    {"label": "Delaware", "value": "Delaware"},
    {"label": "Florida", "value": "Florida"},
    {"label": "Georgia", "value": "Georgia"},
    {"label": "Guam", "value": "Guam"},
    {"label": "Hawaii", "value": "Hawaii"},
    {"label": "Idaho", "value": "Idaho"},
    {"label": "Illinois", "value": "Illinois"},
    {"label": "Indiana", "value": "Indiana"},
    {"label": "Iowa", "value": "Iowa"},
    {"label": "Kansas", "value": "Kansas"},
    {"label": "Kentucky", "value": "Kentucky"},
    {"label": "Louisiana", "value": "Louisiana"},
    {"label": "Maine", "value": "Maine"},
    {"label": "Maryland", "value": "Maryland"},
    {"label": "Massachusetts", "value": "Massachusetts"},
    {"label": "Michigan", "value": "Michigan"},
    {"label": "Minnesota", "value": "Minnesota"},
    {"label": "Mississippi", "value": "Mississippi"},
    {"label": "Missouri", "value": "Missouri"},
    {"label": "Montana", "value": "Montana"},
    {"label": "Northern Mariana Islands", "value": "Northern Mariana Islands"},
    {"label": "Nebraska", "value": "Nebraska"},
    {"label": "Nevada", "value": "Nevada"},
    {"label": "New Hampshire", "value": "New Hampshire"},
    {"label": "New Jersey", "value": "New Jersey"},
    {"label": "New Mexico", "value": "New Mexico"},
    {"label": "New York", "value": "New York"},
    {"label": "North Carolina", "value": "North Carolina"},
    {"label": "North Dakota", "value": "North Dakota"},
    {"label": "Ohio", "value": "Ohio"},
    {"label": "Oklahoma", "value": "Oklahoma"},
    {"label": "Oregon", "value": "Oregon"},
    {"label": "Pennsylvania", "value": "Pennsylvania"},
    {"label": "Puerto Rico", "value": "Puerto Rico"},
    {"label": "Rhode Island", "value": "Rhode Island"},
    {"label": "South Carolina", "value": "South Carolina"},
    {"label": "South Dakota", "value": "South Dakota"},
    {"label": "Tennessee", "value": "Tennessee"},
    {"label": "Texas", "value": "Texas"},
    {"label": "Utah", "value": "Utah"},
    {"label": "Vermont", "value": "Vermont"},
    {"label": "Virginia", "value": "Virginia"},
    {"label": "Virgin Islands", "value": "Virgin Islands"},
    {"label": "Washington", "value": "Washington"},
    {"label": "West Virginia", "value": "West Virginia"},
    {"label": "Wisconsin", "value": "Wisconsin"},
    {"label": "Wyoming", "value": "Wyoming"},
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
