# Spatial Analysis of Energy Communities and Vulnerability in Spain

Dashboard interactivo realizado en Python (3.13) usando las librerías Dash y Plotly realizado para la parte II de la práctica **Visualización de Datos** perteneciente al **Máster en Ciencia de Datos** de la **UOC**.

El dashboard está alojada en esta URL de GitHub pages: https://amontesinosn-uoc.github.io/practicapii-vd/

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

## Decisiones de diseño a comentar

Se ha utilizado Dash y Plotly ya que son el tándem perfecto para crear visualizaciones de datos web en Python. Dash permite crear aplicaciones web dinámicas, las cuales contienen elementos de visualizaciónes de datos (como son las gráficas de Plotly). El resultado es un dashboard que pese a mostrar miles de elementos en las gráficas de manera simultánea, es bastante ágil y fluido, manteniendo al mismo tiempo la interactividad de los gráficos que Plotly proporciona en otros medios como podría ser un notebook de Jupyter.

Dado que el dashboard se concibió para ser publicado en GitHub pages y éste utiliza un único fichero HTML, el script de la aplicación contiene todos los datos necesarios embebidos, lo cual resalta la idoneidad de las tecnologías escogidas al ser la navegación tan rápida.

---

## Estructura del proyecto

    src/
        app_dashboard.py (Script Python con el dashboard)
        export_dashboard.py (Script Python para generar el html compatible con GitHub Pages)
        index.html (HTML que muestra GitHub Pages)
        LICENSE 
        README.md
        requirements.txt

---

## Ejecución en servidor local

Para la ejecución en un servidor local basta con clonar el repositorio, descargar las librerías necesarias del fichero requirements.txt y ejecutar el siguiente comando desde una terminal situada en la carpeta del proyecto: python app_dashboard.py. Para ver la app acceder a http://127.0.0.1:8050/.

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
