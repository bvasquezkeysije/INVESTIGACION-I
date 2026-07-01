# 2.2 Criterios de elegibilidad

Con el propósito de garantizar la pertinencia, consistencia y calidad metodológica de los estudios incluidos, los criterios de elegibilidad fueron definidos utilizando el marco **PICOC** (*Population, Intervention, Comparison, Outcome and Context*). Este marco constituye una herramienta ampliamente utilizada en revisiones sistemáticas de Ciencias de la Computación e Ingeniería de Software, ya que facilita la delimitación del alcance de la investigación, la formulación de las preguntas de investigación, el diseño de las estrategias de búsqueda y la definición objetiva de los criterios de selección de los estudios primarios [K7H4][17].

En esta investigación, el marco **PICOC** fue adaptado al contexto de las arquitecturas multiagente basadas en inteligencia artificial y **Model Context Protocol (MCP)** aplicadas a la orquestación e integración de datos industriales. A diferencia de revisiones centradas en intervenciones clínicas o experimentos controlados tradicionales, la presente revisión se orienta al análisis de propuestas tecnológicas, modelos arquitectónicos, agentes inteligentes, protocolos de interoperabilidad, mecanismos de integración y resultados de validación reportados en estudios científicos del ámbito industrial. Por ello, el foco se concentra en las arquitecturas propuestas, las fuentes de datos industriales utilizadas, los mecanismos de comunicación e integración empleados, los entornos de validación y el desempeño alcanzado en términos de interoperabilidad, automatización, trazabilidad o eficiencia operativa.

La **Tabla 1** presenta la definición de cada uno de los componentes del marco **PICOC** utilizados para delimitar el alcance de esta revisión sistemática.

## Tabla 1. Marco PICOC utilizado en la revisión sistemática

| Componente | Descripción |
|---|---|
| **Population (P)** | Estudios científicos relacionados con arquitecturas multiagente, agentes LLM, sistemas inteligentes o propuestas de inteligencia artificial aplicadas a entornos industriales. |
| **Intervention (I)** | Uso de arquitecturas multiagente basadas en inteligencia artificial y/o **Model Context Protocol (MCP)** para la orquestación, interoperabilidad o integración de datos industriales. |
| **Comparison (C)** | Comparación entre arquitecturas, agentes, protocolos, mecanismos de integración, estrategias de orquestación o métricas de desempeño, cuando el estudio lo reporta. |
| **Outcome (O)** | Resultados asociados al desempeño de la solución propuesta, medidos mediante indicadores como latencia, interoperabilidad, precisión, F1-score, trazabilidad, task success, automatización, escalabilidad o eficiencia operativa. |
| **Context (C)** | Investigaciones desarrolladas en escenarios industriales o dominios cercanos a la industria, incluyendo manufactura, automatización, IIoT, digital twins, sistemas energéticos, mantenimiento predictivo o integración de sistemas industriales. |

El marco **PICOC** también permitió identificar los conceptos fundamentales sobre los cuales se construyó la estrategia de búsqueda bibliográfica. Cada uno de sus componentes fue asociado con un conjunto de palabras clave y sinónimos, los cuales posteriormente fueron combinados mediante operadores booleanos para formular las cadenas de búsqueda específicas en las bases de datos seleccionadas.

## Tabla 2. Relación entre el marco PICOC y los términos de búsqueda

| Componente PICOC | Concepto principal | Términos utilizados en la búsqueda |
|---|---|---|
| **Population** | Arquitecturas multiagente e IA industrial | "multi-agent system", "multi-agent architecture", "AI agent", "LLM agent", "industrial agent", "intelligent agent" |
| **Intervention** | MCP e integración/orquestación | "Model Context Protocol", "MCP", "data integration", "data orchestration", "industrial orchestration", "interoperability" |
| **Comparison** | Estrategias y enfoques tecnológicos | "architecture", "framework", "protocol", "workflow", "coordination", "tool integration" |
| **Outcome** | Desempeño y resultados | "latency", "F1-score", "accuracy", "task success", "traceability", "automation", "scalability", "efficiency" |
| **Context** | Entornos industriales | "Industry 4.0", "industrial data", "manufacturing", "IIoT", "digital twin", "SCADA", "MES", "industrial automation" |

A partir de este marco conceptual se definieron los criterios de inclusión y exclusión que orientaron el proceso de selección de los estudios primarios.

## 2.2.1 Criterios de inclusión

Se consideraron elegibles aquellos estudios que cumplieron simultáneamente con los criterios descritos en la **Tabla 3**.

## Tabla 3. Criterios de inclusión

| Código | Criterio |
|---|---|
| **IC1** | Artículos científicos originales publicados en revistas, congresos o repositorios académicos reconocidos. |
| **IC2** | Estudios publicados entre enero de 2020 y julio de 2026. |
| **IC3** | Publicaciones escritas en idioma inglés o español. |
| **IC4** | Investigaciones que propongan, desarrollen, implementen, validen o evalúen arquitecturas multiagente basadas en inteligencia artificial y/o **Model Context Protocol (MCP)** aplicadas a la orquestación o integración de datos industriales. |
| **IC5** | Estudios que describan claramente el entorno industrial, las fuentes de datos utilizadas o el dominio de aplicación considerado. |
| **IC6** | Investigaciones que expliquen de forma explícita la metodología empleada, la arquitectura propuesta o el enfoque técnico desarrollado. |
| **IC7** | Estudios que reporten al menos una métrica cuantitativa o un resultado verificable para evaluar el desempeño de la propuesta, tales como **accuracy**, **F1-score**, latencia, **task success**, interoperabilidad, trazabilidad, eficiencia o escalabilidad. |
| **IC8** | Publicaciones con acceso al texto completo para permitir la evaluación metodológica y la extracción de información. |

## 2.2.2 Criterios de exclusión

Se excluyeron aquellos estudios que presentaban alguna de las condiciones descritas en la **Tabla 4**.

## Tabla 4. Criterios de exclusión

| Código | Criterio |
|---|---|
| **EC1** | Revisiones sistemáticas, revisiones narrativas, metaanálisis, editoriales, capítulos de libro, tesis o resúmenes de congreso sin evidencia primaria suficiente. |
| **EC2** | Estudios cuyo objetivo principal no estuviera relacionado con arquitecturas multiagente, agentes inteligentes, **MCP** o integración/orquestación de datos en contextos industriales. |
| **EC3** | Investigaciones orientadas exclusivamente a dominios no industriales sin una relación metodológica clara con interoperabilidad, automatización o integración de datos industriales. |
| **EC4** | Estudios que no emplearan agentes, arquitecturas multiagente, inteligencia artificial aplicada o mecanismos explícitos de contexto/protocolo relevantes para la revisión. |
| **EC5** | Publicaciones duplicadas recuperadas desde diferentes bases de datos. |
| **EC6** | Artículos sin acceso al texto completo. |
| **EC7** | Estudios que no describieran adecuadamente la metodología empleada o que no reportaran información suficiente para evaluar la propuesta desarrollada. |

Los criterios de elegibilidad fueron aplicados de manera secuencial durante las etapas de identificación, cribado y evaluación de elegibilidad de los estudios recuperados. Inicialmente se revisaron los títulos y resúmenes para descartar las publicaciones claramente irrelevantes. Posteriormente, los artículos potencialmente elegibles fueron evaluados mediante la lectura completa del documento, verificando el cumplimiento de todos los criterios de inclusión y la ausencia de criterios de exclusión.

Con el fin de reducir posibles sesgos durante el proceso de selección, la evaluación de los estudios se realizó de forma sistemática, documentando las decisiones de inclusión o exclusión en cada etapa del proceso. Este procedimiento permitió fortalecer la objetividad, consistencia y reproducibilidad de la revisión, en concordancia con las recomendaciones metodológicas establecidas por la declaración **PRISMA 2020** [P8S2][16].

Una vez definidos los criterios de elegibilidad y delimitado el alcance de la revisión mediante el marco **PICOC**, se procedió al diseño de la estrategia de búsqueda bibliográfica, la cual permitió identificar de manera sistemática los estudios potencialmente relevantes en las bases de datos científicas seleccionadas.
