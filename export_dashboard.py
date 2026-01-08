import plotly.io as pio
from app_dashboard import fig1, fig2, fig3, fig4, fig5

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Energy Communities Dashboard</title>
    <style>
        body {{
            margin: 0;
            font-family: Arial, sans-serif;
            height: 100vh;
            display: grid;
            grid-template-rows: 80px 1fr;
        }}
        header {{
            background: #f5f5f5;
            padding: 10px 20px;
            border-bottom: 1px solid #ddd;
        }}
        main {{
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            grid-template-rows: 1fr 1fr;
            gap: 10px;
            padding: 10px;
        }}
    </style>
</head>
<body>

<header>
    <h2>Spatial Analysis of Energy Communities and Vulnerability in Spain</h2>
    <span style="color: gray;">Dashboard publicado en GitHub Pages</span>
</header>

<main>
    <div style="grid-column: 1 / 3;">{pio.to_html(fig1, include_plotlyjs='cdn', full_html=False)}</div>
    {pio.to_html(fig2, full_html=False)}
    {pio.to_html(fig3, full_html=False)}
    {pio.to_html(fig4, full_html=False)}
    {pio.to_html(fig5, full_html=False)}
</main>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html generado correctamente")
