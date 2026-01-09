import plotly.io as pio
from app_dashboard import fig1, fig2, fig3, fig4, fig5, fig6

def fig_html(fig):
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
body {{
    margin: 0;
    padding: 30px;
    font-family: Arial, sans-serif;
    background-color: #ffffff;
}}

h1 {{
    margin-bottom: 5px;
}}

.subtitle {{
    color: #555;
    margin-bottom: 20px;
}}

a {{
    color: #1f77b4;
}}

.dashboard {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: auto auto auto;
    gap: 25px;
}}

.card {{
    border-radius: 10px;
    background: #fafafa;
    padding: 15px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
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
