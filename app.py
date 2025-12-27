import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("data/pink_morsels_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Initialize app
app = Dash(__name__)

# Layout
app.layout = html.Div(
    className="container",
    children=[
        html.H1("Soul Foods  Pink Morsels Sales Visualiser"),

        html.Div(
            className="radio-group",
            children=[
                dcc.RadioItems(
                    id="region-selector",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True
                )
            ]
        ),

        html.Div(
            className="graph-container",
            children=[
                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)

# Callback
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        labels={
            "Date": "Date",
            "Sales": "Total Sales"
        },
        title="Pink Morsels Sales Over Time"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
