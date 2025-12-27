import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load processed data
df = pd.read_csv("data/pink_morsels_sales.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsels Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Total Sales"
    }
)

# Initialize Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div(
    children=[
        html.H1("Soul Foods Pink Morsels Sales Visualiser"),
        dcc.Graph(figure=fig)
    ]
)

# Run server
if __name__ == "__main__":
    app.run(debug=True)
