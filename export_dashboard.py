import plotly.io as pio
from app_dashboard import fig1, fig2, fig3, fig4, fig5, fig6

def fig_html(fig):
    fig.update_layout(
        height=300,
        width=450,
        autosize=False,
        margin=dict(l=40, r=20, t=45, b=40)
    )
    return pio.to_html(
        fig,
        include_plotlyjs="cdn",
        full_html=False,
        config={"displaylogo": False}
    )

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Spatial Analysis of Energy Communities and Vulnerability in Spain</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
html, body {{
    height: 100%;
    margin: 0;
}}

body {{
    font-family: Arial, sans-serif;
    background-color: #ffffff;
    padding: 20px;
    box-sizing: border-box;
    overflow: hidden;
}}

h1 {{
    margin: 0 0 5px 0;
}}

.subtitle {{
    color: #555;
    margin-bottom: 10px;
    font-size: 14px;
}}

a {{
    color: #1f77b4;
}}

.dashboard {{
    height: calc(100vh - 150px);
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(2, 1fr);
    gap: 15px;
}}

.card {{
    background: #fafafa;
    border-radius: 10px;
    padding: 8px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    display: flex;
    align-items: center;
    justify-content: center;
}}
</style>
</head>

<body>

<h1>Spatial Analysis of Energy Communities and Vulnerability in Spain</h1>

<div class="subtitle">
    Husiyev, Oleksandr; Enciso-Santocildes, Marta; Ukar Arrien, Olatz (2025).
    “Spatial Analysis of Energy Communities and Vulnerability in Spain”,
    Mendeley Data, V5, doi: 10.17632/v8cv52frdh.5<br>
    <a href="https://data.mendeley.com/datasets/v8cv52frdh/5" target="_blank">
        https://data.mendeley.com/datasets/v8cv52frdh/5
    </a>
</div>

<div class="dashboard">
    <div class="card">{fig_html(fig1)}</div>
    <div class="card">{fig_html(fig2)}</div>
    <div class="card">{fig_html(fig3)}</div>
    <div class="card">{fig_html(fig4)}</div>
    <div class="card">{fig_html(fig5)}</div>
    <div class="card">{fig_html(fig6)}</div>
</div>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html generado correctamente")
