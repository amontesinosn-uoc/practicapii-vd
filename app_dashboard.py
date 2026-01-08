import dash
from dash import html, dcc
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# ======================
# DATOS FICTICIOS
# ======================

np.random.seed(42)

n_no_cai = 7850
n_cai = 250

df = pd.DataFrame({
    "Has_CAI": [0]*n_no_cai + [1]*n_cai,
    "SVI": np.concatenate([
        np.random.normal(0.2, 0.5, n_no_cai),
        np.random.normal(-0.1, 0.4, n_cai)
    ]),
    "Income_level": np.concatenate([
        np.random.choice(["Low", "Medium", "High"], n_no_cai, p=[0.4, 0.4, 0.2]),
        np.random.choice(["Low", "Medium", "High"], n_cai, p=[0.2, 0.4, 0.4])
    ]),
    "Renewable_profile": np.concatenate([
        np.random.choice(["Solar", "Wind", "Hydro"], n_no_cai),
        np.random.choice(["Solar", "Wind", "Hydro"], n_cai, p=[0.5, 0.3, 0.2])
    ]),
    "Area_type": np.concatenate([
        np.random.choice(["Urban", "Rural"], n_no_cai, p=[0.6, 0.4]),
        np.random.choice(["Urban", "Rural"], n_cai, p=[0.7, 0.3])
    ])
})

# ======================
# FIGURAS
# ======================

# 1. Municipios con vs sin CAI
fig1 = go.Figure(
    data=[
        go.Bar(
            x=["Sin CAI", "Con CAI"],
            y=[n_no_cai, n_cai]
        )
    ]
)
fig1.update_layout(title="Municipios con y sin CAIs")

# 2. Boxplot SVI (CAI vs no CAI)
fig2 = go.Figure()
fig2.add_trace(go.Box(
    y=df[df["Has_CAI"] == 0]["SVI"],
    name="Sin CAI"
))
fig2.add_trace(go.Box(
    y=df[df["Has_CAI"] == 1]["SVI"],
    name="Con CAI"
))
fig2.update_layout(title="Vulnerabilidad social (SVI)")

# 3. Proporción de CAIs por nivel de ingresos
income_cai = (
    df.groupby(["Income_level", "Has_CAI"])
    .size()
    .reset_index(name="count")
)

income_pivot = income_cai.pivot(
    index="Income_level",
    columns="Has_CAI",
    values="count"
).fillna(0)

fig3 = go.Figure()
fig3.add_trace(go.Bar(
    x=income_pivot.index,
    y=income_pivot[1] / (income_pivot[0] + income_pivot[1]) * 100,
))
fig3.update_layout(
    title="Porcentaje de municipios con CAI por nivel de ingresos",
    yaxis_title="% municipios con CAI"
)

# 4. Perfil energético dominante
energy_dist = (
    df.groupby(["Renewable_profile", "Has_CAI"])
    .size()
    .reset_index(name="count")
)

fig4 = go.Figure()
for has_cai, label in zip([0, 1], ["Sin CAI", "Con CAI"]):
    subset = energy_dist[energy_dist["Has_CAI"] == has_cai]
    fig4.add_trace(go.Bar(
        x=subset["Renewable_profile"],
        y=subset["count"],
        name=label
    ))

fig4.update_layout(
    title="Perfil energético dominante",
    barmode="group"
)

# 5. Urbano vs rural
area_dist = (
    df.groupby(["Area_type", "Has_CAI"])
    .size()
    .reset_index(name="count")
)

fig5 = go.Figure()
for has_cai, label in zip([0, 1], ["Sin CAI", "Con CAI"]):
    subset = area_dist[area_dist["Has_CAI"] == has_cai]
    fig5.add_trace(go.Bar(
        x=subset["Area_type"],
        y=subset["count"],
        name=label
    ))

fig5.update_layout(
    title="Distribución urbano / rural",
    barmode="group"
)

# ======================
# DASHBOARD
# ======================

app = dash.Dash(__name__)
app.title = "Energy Communities & Vulnerability Dashboard"

app.layout = html.Div(
    style={
        "height": "100vh",
        "width": "100vw",
        "display": "grid",
        "gridTemplateRows": "80px 1fr",
        "overflow": "hidden",
        "fontFamily": "Arial"
    },
    children=[

        # HEADER
        html.Div(
            style={
                "backgroundColor": "#f5f5f5",
                "padding": "10px 20px",
                "borderBottom": "1px solid #ddd"
            },
            children=[
                html.H2(
                    "Spatial Analysis of Energy Communities and Vulnerability in Spain",
                    style={"margin": "0"}
                ),
                html.Span(
                    "Dashboard demostrativo con datos simulados",
                    style={"color": "gray"}
                )
            ]
        ),

        # MAIN GRID
        html.Div(
            style={
                "display": "grid",
                "gridTemplateColumns": "1fr 1fr 1fr",
                "gridTemplateRows": "1fr 1fr",
                "gap": "10px",
                "padding": "10px"
            },
            children=[

                html.Div(
                    style={"gridColumn": "1 / 3"},
                    children=[dcc.Graph(figure=fig1)]
                ),

                dcc.Graph(figure=fig2),
                dcc.Graph(figure=fig3),
                dcc.Graph(figure=fig4),
                dcc.Graph(figure=fig5),
            ]
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
