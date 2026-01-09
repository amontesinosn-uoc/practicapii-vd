# Spatial Analysis of Energy Communities and Vulnerability in Spain

Dashboard interactivo realizado en Python usando las librerías Dash y Plotly realizado para la parte II de la práctica **Visualización de Datos** perteneciente al **Máster en Ciencia de Datos** de la **UOC**.

Este repositorio contiene el código fuente de un **dashboard interactivo** que permite analizar la relación entre la presencia de **Comunidades Energéticas (CAI)**, la **vulnerabilidad social** y diversas **variables socioeconómicas y territoriales** de los municipios en España.

El dashboard acompaña el trabajo académico:

Spatial Analysis of Energy Communities and Vulnerability in Spain  
Universidad de Deusto (2025)

---

## Objetivo del dashboard

El objetivo principal del dashboard es **analizar si el despliegue de Comunidades Energéticas en España está alineado con criterios de equidad social y transición energética justa**, explorando patrones espaciales, económicos y sociales a escala municipal y autonómica.

---

## Preguntas de investigación

El dashboard está diseñado para responder de forma visual e interactiva a las siguientes preguntas:

1. ¿Cuál es la distribución territorial de las Comunidades Energéticas en España?

2. ¿Qué porcentaje de municipios cuenta con al menos una Comunidad Energética?

3. ¿Existen diferencias socioeconómicas entre municipios con y sin CAI?

4. ¿Qué relación existe entre vulnerabilidad social y presencia de CAI?

5. ¿Qué perfiles de energías renovables dominan en los municipios con CAI?

6. ¿El despliegue actual de Comunidades Energéticas contribuye a una transición energética justa?

---

## Contenido del dashboard

El dashboard incluye los siguientes elementos visuales:

- Mapa coroplético del número de CAI por Comunidad Autónoma.
- Gráfico de cajas (boxplot) comparando la renta media de hogares en municipios con y sin CAI.
- Indicadores clave sobre el número y porcentaje de municipios con y sin CAI.
- Gráfico de dispersión que relaciona vulnerabilidad social y densidad poblacional.
- Gráfico de barras sobre la distribución de perfiles renovables dominantes.

---

## Tecnologías utilizadas

- Dash
- Plotly

---

## Estructura del proyecto

├── src/
│ ├── app_dashboard.py
│ ├── export_dashboard.py
│ ├── index.html
│ ├── LICENSE
│ ├── README.md
│ └── requirements.txt

---

## Fuente de datos

Los datos utilizados proceden de:

Spatial Analysis of Energy Communities and Vulnerability in Spain  
Mendeley Data, V5  
https://data.mendeley.com/datasets/v8cv52frdh/5

---

## Licencia

Este proyecto se distribuye bajo la licencia **MIT License**.

Se permite el uso, copia, modificación, fusión, publicación, distribución, sublicencia y/o venta del software, siempre que se incluya el aviso de copyright y la licencia original.

Consulta el archivo LICENSE para más detalles.
