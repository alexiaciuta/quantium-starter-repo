from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv("daily_sales_data.csv")

app = Dash(__name__)

fig = px.line(df, x="date", y="sales")

app.layout = html.Div(children=[
    html.H1(children = "Sales of Pink Morsels"),
    
    dcc.Graph(figure = fig)])


if __name__ =='__main__':
   app.run_server(debug=True)
