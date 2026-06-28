## **2.1 Tipo y Diseño de Investigación**

La presente investigación adopta un enfoque cuantitativo, dado que evalúa de manera objetiva el desempeño de agentes de inteligencia artificial a través de métricas que permiten medir mejoras en la integración y automatización de datos industriales. De acuerdo con [B5H1][31], este enfoque es pertinente cuando se busca contrastar hipótesis mediante datos numéricos y procedimientos estadísticos.

El tipo de investigación es aplicada y tecnológica, puesto que se orienta a resolver un problema real asociado a la fragmentación y baja eficiencia en la gestión de datos industriales, y desarrolla una solución concreta basada en agentes de IA usando Model Context Protocol (MCP).La investigación tecnológica se centra en diseñar, implementar y validar artefactos computacionales que aportan mejoras funcionales en contextos específicos, lo cual se ajusta al propósito de este estudio [T2R6][28].

El diseño de investigación es experimental de carácter tecnológico, ya que se manipula deliberadamente la variable independiente a implementación de agentes MCP y se mide su efecto sobre la variable dependiente, correspondiente al nivel de integración y automatización de datos. De acuerdo [D7E5][29] los diseños experimentales permiten establecer relaciones causales mediante el control de condiciones. En este estudio, la experimentación se realizará en un entorno computacional controlado que permitirá evaluar el desempeño de los agentes mediante métricas operativas.

En síntesis, la investigación es cuantitativa, aplicada, tecnológica y con diseño experimental, garantizando coherencia metodológica con el problema, los objetivos y la hipótesis planteada, y permitiendo validar rigurosamente el impacto de los agentes MCP en la mejora de los procesos de integración y automatización de datos industriales.

## **2.2 Variables, Operacionalización**

Tabla 1. Operacionalización de la variable dependiente

<div style="overflow-x:auto; width:100%;">
<table>
  <thead>
    <tr>
      <th>Variable de estudio</th>
      <th>Definición conceptual</th>
      <th>Definición operacional</th>
      <th>Dimensiones</th>
      <th>Indicadores</th>
      <th>Fórmula / Medición</th>
      <th>Instrumentos de recolección de datos</th>
      <th>Valores finales</th>
      <th>Tipo de variable</th>
      <th>Escala de medición</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">Implementación de una arquitectura multiagente basada en IA utilizando MCP</td>
      <td rowspan="7">Conjunto de agentes de inteligencia artificial que interactúan de manera coordinada mediante Model Context Protocol (MCP) para ejecutar tareas, intercambiar información y colaborar en procesos de integración de datos.</td>
      <td rowspan="7">Se expresa mediante la configuración, coordinación y desempeño de los agentes que conforman la arquitectura multiagente basada en MCP, considerando conexiones activas, intercambio de información, tiempos de respuesta y ejecución de tareas automatizadas.</td>
      <td rowspan="3">1. Configuración de la arquitectura</td>
      <td>N.º de agentes configurados</td>
      <td>Conteo directo</td>
      <td>Archivo <code>config.yaml</code> / <code>tools.json</code></td>
      <td>Entero</td>
      <td>Numérica discreta</td>
      <td>Razón</td>
    </tr>
    <tr>
      <td>N.º de herramientas MCP configuradas</td>
      <td>Conteo directo</td>
      <td>Registros del sistema</td>
      <td>Entero</td>
      <td>Numérica discreta</td>
      <td>Razón</td>
    </tr>
    <tr>
      <td>N.º de fuentes de datos conectadas</td>
      <td>Conteo directo</td>
      <td>Registros del sistema</td>
      <td>Entero</td>
      <td>Numérica discreta</td>
      <td>Razón</td>
    </tr>
    <tr>
      <td rowspan="2">2. Rendimiento operativo</td>
      <td>Tiempo promedio de respuesta</td>
      <td>T = Σtᵢ / n</td>
      <td>Logs de ejecución del sistema</td>
      <td>Milisegundos</td>
      <td>Numérica continua</td>
      <td>Razón</td>
    </tr>
    <tr>
      <td>N.º de consultas procesadas correctamente</td>
      <td>Conteo</td>
      <td>Logs y reportes del sistema</td>
      <td>Entero</td>
      <td>Numérica discreta</td>
      <td>Razón</td>
    </tr>
    <tr>
      <td rowspan="2">3. Nivel de automatización</td>
      <td>N.º de tareas automatizadas</td>
      <td>Conteo</td>
      <td>Bitácora del sistema</td>
      <td>Entero</td>
      <td>Numérica discreta</td>
      <td>Razón</td>
    </tr>
    <tr>
      <td>Tasa de éxito de tareas</td>
      <td>(Tareas exitosas / Total de tareas) × 100</td>
      <td>Registros del sistema</td>
      <td>Porcentaje</td>
      <td>Numérica continua</td>
      <td>Razón</td>
    </tr>
  </tbody>
</table>
</div>

Tabla 2. Operacionalización de la variable independiente

<div style="overflow-x:auto; width:100%;">
<table>
  <thead>
    <tr>
      <th>Variable de estudio</th>
      <th>Definición conceptual</th>
      <th>Definición operacional</th>
      <th>Dimensiones</th>
      <th>Indicadores</th>
      <th>Fórmula / Medición</th>
      <th>Instrumentos de recolección de datos</th>
      <th>Valores finales</th>
      <th>Tipo de variable</th>
      <th>Escala de medición</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">Orquestación e integración de datos industriales.</td>
      <td rowspan="7">Proceso mediante el cual los datos provenientes de sistemas industriales se unifican, sincronizan y gestionan de forma coordinada para facilitar el intercambio de información y la automatización de procesos.</td>
      <td rowspan="7">Se mide mediante métricas de eficiencia de integración, automatización, trazabilidad y coordinación de procesos de intercambio de datos industriales.</td>
      <td rowspan="2">1. Eficiencia de integración</td>
      <td>% de fuentes de datos integradas</td>
      <td>(Fi / Ft) × 100</td>
      <td>Registros SCADA / MES</td>
      <td>Porcentaje</td>
      <td>Numérica continua</td>
      <td>Razón</td>
    </tr>
    <tr>
      <td>N.º de conexiones activas</td>
      <td>Conteo</td>
      <td>Logs de sistema</td>
      <td>Entero</td>
      <td>Numérica discreta</td>
      <td>Razón</td>
    </tr>
    <tr>
      <td rowspan="3">2. Automatización y orquestación de procesos</td>
      <td>Tiempo promedio de procesamiento de datos</td>
      <td>T = Σtᵢ / n</td>
      <td>Logs del sistema</td>
      <td>Segundos</td>
      <td>Numérica continua</td>
      <td>Razón</td>
    </tr>
    <tr>
      <td>Reducción de tareas manuales (%)</td>
      <td>Comparación pre/post</td>
      <td>Hoja de validación / Bitácora</td>
      <td>Porcentaje</td>
      <td>Numérica continua</td>
      <td>Razón</td>
    </tr>
    <tr>
      <td>N.º de flujos de trabajo orquestados automáticamente</td>
      <td>Conteo</td>
      <td>Registros del sistema</td>
      <td>Entero</td>
      <td>Numérica discreta</td>
      <td>Razón</td>
    </tr>
    <tr>
      <td rowspan="2">3. Calidad y trazabilidad</td>
      <td>N.º de errores de consistencia</td>
      <td>Conteo</td>
      <td>Auditoría del sistema</td>
      <td>Entero</td>
      <td>Numérica discreta</td>
      <td>Razón</td>
    </tr>
    <tr>
      <td>Índice de trazabilidad</td>
      <td>Fórmula propia del sistema</td>
      <td>Reportes de auditoría</td>
      <td>Porcentaje</td>
      <td>Numérica continua</td>
      <td>Razón</td>
    </tr>
  </tbody>
</table>
</div>

## **2.3 Población de estudio, muestra, muestreo y criterios de selección**

### **2.3.1. Población de estudio**

La población de estudio estará constituida por el conjunto de registros de datos industriales generados por sensores instalados en una planta de fabricación de pulpa y papel, correspondiente al dataset público *Rare Event Classification in Multivariate Time Series* [R1C6][56]. Este dataset reúne lecturas continuas de sensores ubicados en distintos puntos de la línea de producción, las cuales registran variables de proceso tales como cantidad de fibra de pulpa, dosificación de químicos, tipo de cuchilla, vacío de la prensa (*couch vacuum*) y velocidad del rotor, entre otras 61 variables predictoras (x1-x61), además de una variable de respuesta binaria (y) que indica la ocurrencia de una rotura de hoja de papel.

La población total está compuesta por 18 398 registros, generados durante 30 días continuos de operación, con una frecuencia de muestreo de 2 minutos entre cada lectura. Esta delimitación responde directamente a las características reales del proceso industrial registrado en el dataset y no a una estimación teórica, lo que garantiza que cada unidad de análisis corresponda efectivamente a una observación verificable del comportamiento de un sistema industrial real, coherente con el objetivo de evaluar la capacidad del agente MCP en procesos de integración, automatización y gestión de datos.
### **2.3.2. Muestra**

Dado que la población es de tamaño acotado y verificable (18 398 registros), se utilizará la totalidad del dataset como base experimental, dividiéndolo en dos subconjuntos según el esquema de validación 80/20 comúnmente empleado en estudios de inteligencia artificial y aprendizaje automático para garantizar la generalización del modelo y evitar sobreajuste [R1C6][56]:

- **Conjunto de entrenamiento:** 14 718 registros (80 %), empleados para que el agente MCP procese, integre y aprenda los patrones de comportamiento del sistema industrial.

- **Conjunto de prueba:** 3 680 registros (20 %), reservados para evaluar el desempeño del agente sobre datos no utilizados durante el procesamiento inicial.

Esta proporción se fundamenta en el carácter técnico de la evaluación, ya que el objetivo no es generalizar resultados a una población estadística externa, sino medir el desempeño operativo del agente MCP (exactitud de integración, tasa de error y tiempo de procesamiento) sobre un conjunto de datos real, completo y con trazabilidad comprobada, evitando así el sesgo que introduciría una reducción arbitraria del volumen de datos disponible.
### **2.3.3. Tipo de muestreo**

El muestreo aplicado para la división del dataset es de tipo aleatorio simple, técnica estándar en estudios de inteligencia artificial y aprendizaje automático para particionar los datos en conjuntos de entrenamiento y prueba, evitando sesgos relacionados con el orden temporal o la posición de los registros dentro del dataset original [R1C6][56].

Este enfoque es coherente con el carácter experimental de la investigación, dado que no se busca una representatividad estadística respecto a una población externa, sino garantizar que ambos subconjuntos (entrenamiento y prueba) conserven una distribución similar de las variables de proceso y del evento de interés (rotura de hoja), de modo que la evaluación del agente MCP refleje su desempeño real frente a datos no vistos previamente.
### **2.3.4. Criterios de selección**

#### **a. Criterios de inclusión**

Se incluirán registros que cumplan con las siguientes características:

-        Datos con formato estructurado (JSON, XML, CSV) o semiestructurado compatible con MCP.

-        Registros completos que contengan todas las variables operativas requeridas.

-        Logs de sensores y máquinas con marcas de tiempo correctas y sin interrupciones.

-        Datos provenientes de sistemas SCADA, PLC, MES o IoT con trazabilidad comprobada.

-        Registros representativos de diversas condiciones operativas del sistema industrial.

#### **b. Criterios de exclusión**

Serán excluidos los registros que presenten:

-        Valores incompletos, corruptos o con pérdida significativa de información

-        Formatos incompatibles con las herramientas MCP

-        Inconsistencias temporales (timestamps repetidos, fuera de rango o ausentes

-        Datos duplicados o provenientes de eventos externos no relevantes

-        Registros alterados por fallos de comunicación, ruido digital o errores del dispositivo.

## **2.4 Técnicas e instrumentos de recolección de datos, validez y confiabilidad**

### **2.4.1 Técnicas de recolección de datos**

La técnica empleada para la recolección de datos será la observación automatizada de registros digitales, realizada a través de agentes de inteligencia artificial basados en Model Context Protocol (MCP). Esta técnica permite capturar, integrar y procesar información proveniente de sistemas industriales tales como sensores, PLCs, sistemas SCADA, bases de datos operativas y plataformas IoT de manera continua y sin intervención humana. Su uso garantiza la obtención de datos objetivos, consistentes y trazables, alineándose con el objetivo del estudio, que consiste en evaluar el desempeño del agente MCP en la integración y automatización de datos industriales.

### **2.4.2 Instrumentos de recolección de datos**

Para la obtención de datos se utilizarán instrumentos automatizados generados por el propio sistema y el agente MCP, entre los cuales se incluyen:

-        Logs de integración del MCP, que registran solicitudes procesadas, tiempos de respuesta, errores, volumen de datos integrados y eventos del sistema.

-        Métricas automáticas de desempeño, generadas por el agente, tales como exactitud en la integración, tasa de error, tiempo promedio por registro y porcentaje de automatización lograda.

-        Registros del sistema industrial, obtenidos directamente de dispositivos y plataformas conectadas, incluyendo lecturas de sensores, variables de proceso, estados de equipos y reportes digitales.

-        Herramientas de monitoreo computacional (como _nvidia-smi_, _Task Manager_, Prometheus o Grafana), empleadas para medir el uso de CPU, GPU, memoria y latencia computacional.

Cada instrumento corresponde directamente a los indicadores de la operacionalización de variables, asegurando una adecuada trazabilidad entre los datos recolectados y los objetivos de la investigación.

### **2.4.3 Validez de los instrumentos**

La validez de los instrumentos será de tipo técnica y funcional, garantizando que las herramientas empleadas midan efectivamente los indicadores definidos.La validez se asegura mediante los siguientes mecanismos:

Uso de tecnologías estandarizadas y validadas internacionalmente, como MCP, JSON Schema, TensorFlow, PyTorch y herramientas de monitoreo reconocidas, lo que garantiza precisión y estabilidad en la obtención de métricas.

Correspondencia lógica entre instrumentos e indicadores, de modo que cada métrica generada refleje directamente los aspectos operacionales de la variable dependiente.

Pruebas experimentales controladas, en las que se evalúa el comportamiento del agente MCP en distintos escenarios de integración de datos, verificando que los instrumentos produzcan resultados consistentes con lo esperado según la literatura técnica.

Estos elementos aseguran que los datos obtenidos sean válidos y pertinentes para evaluar el desempeño del agente de IA en procesos de integración y automatización industrial.

### **2.4.4 Confiabilidad de los instrumentos**

La confiabilidad se garantizará mediante procedimientos de repetibilidad, consistencia técnica y trazabilidad, enmarcados en los principios de reproducibilidad utilizados en investigaciones en inteligencia artificial.

El agente MCP será ejecutado tres veces bajo las mismas condiciones experimentales, considerándose confiable si la variación en las métricas obtenidas es menor al 5 %. Se verificará la consistencia técnica, asegurando que los scripts, configuraciones e instrucciones del agente generen resultados idénticos ante datos equivalentes. Se mantendrá una trazabilidad completa mediante el almacenamiento sistemático de todos los logs, parámetros de ejecución y reportes generados por el agente y el sistema industrial. Este procedimiento permite garantizar estabilidad, replicabilidad y precisión en los datos recolectados, fortaleciendo la rigurosidad metodológica del estudio.

## **2.5 Procedimiento de análisis de datos**

El análisis de datos se desarrollará mediante un enfoque cuantitativo, experimental y computacional, tomando como base el dataset *Rare Event Classification in Multivariate Time Series* [R1C6][56], los archivos de configuración de la arquitectura multiagente, los registros de ejecución del sistema, las bitácoras del agente MCP y los reportes de auditoría generados durante las pruebas. En una primera etapa, los datos serán depurados, transformados y estandarizados en formatos estructurados compatibles con el flujo de trabajo del sistema, principalmente **CSV**, **JSON** y archivos de configuración. Posteriormente, el dataset será dividido en conjunto de entrenamiento y conjunto de prueba conforme al esquema 80/20 definido en la muestra, y se ejecutará la arquitectura bajo condiciones controladas para registrar de forma automática todas las métricas operativas relevantes.

El análisis se organizará según las dimensiones e indicadores establecidos en las tablas de operacionalización. Para la variable **Implementación de una arquitectura multiagente basada en IA utilizando MCP**, en la dimensión **Configuración de la arquitectura** se analizarán el **número de agentes configurados**, el **número de herramientas MCP configuradas** y el **número de fuentes de datos conectadas**, todos medidos mediante conteo directo a partir de archivos de configuración, inventario de herramientas y registros del sistema. En la dimensión **Rendimiento operativo** se calculará el **tiempo promedio de respuesta**, aplicando la fórmula $T = \frac{\sum_{i=1}^{n} t_i}{n}$, donde $t_i$ representa el tiempo registrado en cada ejecución y $n$ el número total de ejecuciones observadas [J4M2][57], [S8L5][58]. En esta misma dimensión también se medirá el **número de consultas procesadas correctamente**, obtenido a partir de los logs y reportes de ejecución. Finalmente, en la dimensión **Nivel de automatización** se evaluarán el **número de tareas automatizadas** y la **tasa de éxito de tareas**, esta última calculada mediante $\frac{T_{ex}}{T_{tot}} \times 100$, donde $T_{ex}$ es el total de tareas completadas correctamente y $T_{tot}$ el total de tareas ejecutadas por la arquitectura [R7N3][59].

Para la variable **Orquestación e integración de datos industriales**, en la dimensión **Eficiencia de integración** se calculará el **porcentaje de fuentes de datos integradas** mediante la fórmula $\frac{F_i}{F_t} \times 100$, donde $F_i$ representa las fuentes integradas satisfactoriamente y $F_t$ el total de fuentes de datos previstas para el experimento [L8Q1][62]. Además, se medirá el **número de conexiones activas** a partir de los logs del sistema. En la dimensión **Automatización y orquestación de procesos** se analizarán el **tiempo promedio de procesamiento de datos**, nuevamente con la fórmula $T = \frac{\sum_{i=1}^{n} t_i}{n}$, la **reducción de tareas manuales (%)**, calculada mediante $\frac{M_{pre} - M_{post}}{M_{pre}} \times 100$, donde $M_{pre}$ corresponde al número de tareas manuales antes de implementar la arquitectura y $M_{post}$ al número de tareas manuales después de su implementación [G6P4][61], y el **número de flujos de trabajo orquestados automáticamente**, obtenido mediante conteo de procesos ejecutados por el sistema sin intervención manual. En la dimensión **Calidad y trazabilidad** se evaluarán el **número de errores de consistencia**, identificado mediante auditoría del sistema, y el **índice de trazabilidad**, calculado con la fórmula $\frac{E_r}{E_t} \times 100$, donde $E_r$ es el número de eventos, transacciones o registros trazables y $E_t$ el total de eventos relevantes del proceso [T4C6][66].

El procesamiento estadístico de estas métricas se realizará mediante **Python**, utilizando principalmente **Pandas** y **NumPy** para limpieza, estructuración y cálculo; y **Matplotlib** para la representación de resultados en tablas y gráficos comparativos. Cuando se requiera evaluar desempeño de clasificación o respuesta del agente sobre tareas específicas, podrán emplearse métricas complementarias como **accuracy** y **F1-score**, siempre que la naturaleza del experimento lo exija [W6A4][64]. Finalmente, los resultados obtenidos en las tres ejecuciones experimentales serán comparados para verificar estabilidad y consistencia, considerando aceptable una variación menor al 5 % entre mediciones equivalentes. Este procedimiento permitirá determinar, con base en evidencia cuantitativa, si la arquitectura multiagente basada en IA utilizando MCP mejora la orquestación e integración de datos industriales.

## **2.6 Criterios éticos**

Todas las fases del presente proyecto se desarrollarán en estricto cumplimiento de los principios generales y específicos establecidos en los Artículos 5 y 6 del Código de Ética en Investigación de la Universidad Señor de Sipán S.A.C. La investigación se conducirá bajo los principios de integridad científica, transparencia, responsabilidad y respeto por la veracidad de los datos, asegurando que los resultados obtenidos reflejen fielmente el comportamiento de los agentes de inteligencia artificial sin alteraciones ni manipulaciones.

Dado que el estudio se basa en el procesamiento automatizado de datos industriales mediante agentes de IA implementados bajo el Model Context Protocol (MCP), y no involucra experimentación con seres humanos ni animales, no se generan riesgos éticos directos. Sin embargo, se garantizará la confidencialidad, seguridad y trazabilidad de los datos utilizados, resguardando la información sensible de los sistemas industriales y permitiendo el acceso únicamente a los investigadores responsables.

Asimismo, se promoverá la reproducibilidad y transparencia del proceso experimental, documentando adecuadamente los procedimientos, configuraciones y resultados generados por los agentes. Se respetarán los derechos de autor y la propiedad intelectual en el uso de librerías, frameworks y fuentes especializadas, citando correctamente a los desarrolladores y autores correspondientes.

Finalmente, el proyecto busca contribuir al avance del conocimiento en el ámbito de la automatización industrial, promoviendo el uso ético, responsable y seguro de tecnologías basadas en inteligencia artificial que favorezcan la eficiencia operativa y el desarrollo tecnológico del sector productivo.
