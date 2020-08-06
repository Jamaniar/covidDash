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

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)