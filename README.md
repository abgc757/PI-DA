# Análisis de Datos de Homicidios en la Ciudad de Buenos Aires


## Exploración y Limpieza de Datos

### DataFrame `hechos`
1. **Consistencia de Datos**:
   Los valores para las variables `N_VICTIMAS`, `FECHA`, `AAAA`, `MM`, `DD`, `HH`, `pos x` y `pos y` son coherentes y se encuentran dentro de los parámetros esperados. Esto sugiere que los datos son válidos y consistentes.

2. **Variable "Altura"**:
   La variable "Altura" presenta dificultades para su validación debido a que indica el número aproximado del lugar del hecho según la numeración de los inmuebles dentro de la vialidad donde ocurrieron los eventos. Dado que no disponemos de información suficiente para validarla, se recomienda descartarla. En su lugar, consideraremos únicamente la ubicación del hecho basada en las coordenadas de latitud (`pos y`) y longitud (`pos x`).

3. **Variable "COMUNA"**:
   La variable "COMUNA" contiene dos registros que indican que el lugar de los hechos se encuentra en la comuna `0`. Sin embargo, en la Ciudad Autónoma de Buenos Aires no existe una una comuna con ese número. Además, no se proporciona una geoposición precisa para estos registros. Por lo tanto, se sugiere excluirlos de los análisis. Es importante destacar que diferentes variables para estos dos únicos registros no se dispone de información relevante para su inclusión en la base de datos.

   Se observa un valor atipico en la variable `COMUNA`, ya que los valores admitidos para comunas en CABA es del 1 al 15, por ello se identifican 2 registros `2016-0151` y `2016-0174` los cuales presentan como comuna el identificador `0`, al revisar la los datos notamo que es imposible imputar la comuna correcta ya que no se posee información que permita localizarlo de forma correcta, ademas de que no posee información completa para fines estadisticos (`VICTIMA`, `PARTICIPANTES`, `ACUSADO`, etc), por lo que se considera que estos registros deberan ser eliminados del los dataframes `hechos` y `victimas`

   Se identifican datos incorrectos en la columna `XY (CABA)`. La preservación de datos relevantes es crucial en el análisis de datos geoespaciales. En el caso de los 12 registros con datos erróneos en la columna `XY (CABA)`, es importante implementar métodos de limpieza que no comprometan la integridad de la información valiosa.
   
   Se propone utilizar los datos de geoposición de las columnas `pos y` (latitud) y `pos x` (longitud) con las cuales se pretende crear mapas que contengan información relevante a los incidentes estudiados.

El gráfico de barras representa la "Distribución de accidentes por año" desde 2016 hasta 2021, evidenciando una disminución notable en la frecuencia de accidentes en los últimos años.

![Distribución de accidentes por año](/images/distribución_accidentes_año.png)

En el año 2020 hubo una reducción significativa durante la mayor parte del año, pero de forma abrupta hubo  un incremento notable de accidentes en diciembre del mismo año, en el cual se presentan un total de 20 accidentes, mientras que el mes julio registro el menor número de accidentes en el historico comprendido entre 2016 y 2021.

Es interesante mencionar que el año 2020 represento un record en la disminución de accidentes viales durante pero para el año 2021 se incremento el número de accidentes en un 24.36%, lo cual podria deberse a una relajación de las medidas tomadas en años anteriores, serie conveniente realizar un analisis mas profundo al respecto.

La evolución del número de víctimas por medio de transporte desde el año 2016 hasta el 2021 muestra que el segmento de la población más afectada son en primera instancia los `peatones` y `motociclistas` registrandose número de incidentes similares, mientras que en segunda instancia los `automovilistas` representan un buena proporción de los accidentes viales. El gráfico muestra la evolución de acccidentes a travez del tiempo.

![Victimas por medio de transporte](/images/victimasxtransporte.png)


La Autopista ``GRAL PAZ`` muestra una distribución de accidentes no uniforme (consulte el mapa), en el tramo entre la intersección con ``Ricardo Gutiérrez`` y la intersección con ``Av. Juan Bautista Justo``, no se registra ningún accidente, lo cual es anormal en un periodo de 6 años de registros, mientras que en el resto de la vialidad, los accidentes están distribuidos de manera más uniforme. Para comprender mejor la ausencia de accidentes en esa sección específica, se requiere un análisis más profundo de los factores que podrían estar influyendo.

![Av Gral Paz](/images/avGralPaz.png)
El mayor numero de victimas para la vialidad `GRAL PAZ` son en primera instancia motociclistas  con 36 defunciones, seguido por automovilistas con 15 y 11 peatones afectados.

La evolución de victimas de accidentes viales en la autopista `Gral. Paz.` muestran un mayor número de victimas del segmento `motociclistas` mostrando una buena evolución. Por otro lado notamos que no hay registros de accidentes para el año 2021 para esta vialidad por lo que podemos deducir que durante ese año  las seguridad vial fue excelente en esta importante arteria de CABA.


### Dashboard Streamlit

- **Título del Dashboard**: "Siniestros Viales en CAPA"
- **Tema**: Interfaz con tema oscuro que facilita la visualización y reduce la fatiga visual durante el análisis de datos.
- **Barra Lateral**:
  - **Selección de Año**: Permite filtrar los datos por año específico.
  - **Selección de Semestre**: Ofrece la opción de filtrar los datos por semestre.
- **Contenido Principal**:
  - **Indicadores Clave**: Presenta porcentajes de "Tasa de Homicidios" y "Accidentes en Moto", proporcionando un resumen rápido de las métricas importantes.
  - **Gráfico de Líneas**: Muestra el "Número de Víctimas por Año (MOTO)" desde 2016 hasta 2021, lo que permite identificar tendencias y patrones en los datos de siniestros viales relacionados con motocicletas.
- **Interactividad**: Los usuarios pueden interactuar con los filtros para personalizar las visualizaciones y obtener insights específicos.
