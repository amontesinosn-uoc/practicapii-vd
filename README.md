# Spatial Analysis of Energy Communities and Vulnerability in Spain

Interactive dashboard exploring the relationship between **energy communities (CAIs)**,
**socioeconomic vulnerability**, **energy profiles** and **territorial characteristics**
across Spanish municipalities.

This project has been developed as part of the course **Visualización de Datos** and
focuses on understanding **in which socioeconomic and territorial contexts CAIs emerge**,
considering that they are a **rare phenomenon** (present in only a small fraction of municipalities).

---

## 🔍 Project goals

The main objective of this project is to answer the following questions:

- In which socioeconomic contexts do energy communities (CAIs) appear?
- Is the presence of CAIs associated with specific renewable energy profiles?
- Does inequality or income level influence the emergence of CAIs?
- Are there differences between urban and rural territories?
- Are there demographic or gender-related patterns linked to vulnerable contexts?

The visualizations have been designed to **compare contexts** rather than absolute values,
given the strong imbalance in the dataset.

---

## 📊 Dashboard

The dashboard consists of **five coordinated visualizations**, arranged in a
full-screen layout inspired by tools such as Power BI or Tableau:

1. Distribution of municipalities with and without CAIs  
2. Social Vulnerability Index (SVI): CAI vs non-CAI municipalities  
3. Percentage of municipalities with CAIs by income level  
4. Dominant renewable energy profile and CAI presence  
5. Urban vs rural differences in the emergence of CAIs  

The dashboard has been exported to **static HTML** to ensure public access without
authentication.

🔗 **Live version (GitHub Pages):**  
👉 https://USUARIO.github.io/NOMBRE_DEL_REPOSITORIO/

---

## 🗂 Data

The original dataset is:

**Spatial Analysis of Energy Communities and Vulnerability in Spain**  
Authors: Oleksandr Husiev, Marta Enciso-Santocildes, Olatz Ukar Arrien  
Source: Mendeley Data  
License: CC BY 4.0  

> Note: The version published in this repository uses **simulated data**
for demonstration purposes. The final academic submission uses the original dataset.

---

## 🛠 Technologies used

- Python 3
- Plotly
- Dash (development and layout prototyping)
- Pandas & NumPy
- GitHub Pages (static publication)

---

## 🚀 How to run locally

1. Create a virtual environment (optional but recommended)
2. Install dependencies:

```bash
pip install -r requirements.txt
