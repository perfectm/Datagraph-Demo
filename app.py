from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go

# create the application object
app = Dash(__name__)

# create the chart Figure based on the data
def stock_prices():
    df = px.data.stocks()
    
    fig = go.Figure(
        [
            go.Scatter(
                x=df["date"],
                y=df["AAPL"],
                line=dict(color="blue", width=4),
                name="Apple",
            )
        ]
    )

    fig.update_layout(
        title="Prices over time", xaxis_title="Dates", yaxis_title="Prices"
    )
    return fig

# create the application layout
app.layout = html.Div(
    children=[
        html.H1(
            children="Apple Stock price",
            style={"textAlign": "center", "marginTop": 40, "marginBottom": 40},
        ),
        dcc.Graph(id="line_plot", figure=stock_prices()),
    ]
)

# define the app server and start it
app_server = app.server

if __name__ == "__main__":
    app_server.run(debug=False)