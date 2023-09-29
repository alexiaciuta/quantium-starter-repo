from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

colours = {
   "background" : '#FFF1F7',
   "text" : '#661F4B',
   "graph_text" : '#B02179',
   "graph" : '#EBA8DB'
}

df = pd.read_csv("daily_sales_data.csv")

app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY])
load_figure_template("MINTY")

app.layout = html.Div(
    children=
        [
        html.H1(children = "Sales of Pink Morsels", 
                style = {'text-align' : 'center', 'color': colours['text']}
                ),
        html.P(children = "Please select the region you want  to see the graph of:", style = {'marginLeft': '80px'}),

        dcc.RadioItems(
            options = {
                "All": "All regions",
                "north": "North",
                "south": "South",
                "east": "East",
                "west": "West"
                },
            value = "All",
            id = "Region",
            style = {'marginLeft': '80px'}),

        dcc.Graph(id = "sales_graph",
                  style = {'width': '100vw', 'height': "70vh"})
        ],
    style = {"color": colours['text']})

@callback(
    Output('sales_graph', 'figure'),
    Input('Region', 'value'))

def ChooseGraph(Region):
    if Region == "All":
        fig = px.line(df, x="date", y= "sales")
    else:
        dff = df[df["region"] == Region]
        fig = px.line(dff, x="date", y="sales")
    fig.update_layout(
    font_color = colours["graph_text"],
    plot_bgcolor = colours["background"])
    fig.update_traces(line_color = colours["graph"])
    return fig


if __name__ =='__main__':
   app.run_server(debug=True)
