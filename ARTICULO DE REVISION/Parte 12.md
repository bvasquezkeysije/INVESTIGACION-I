# 2.3 Fuentes de información

La identificación de los estudios primarios se realizó mediante una búsqueda sistemática en las bases de datos <mark style="background-color:#fff59d">**Scopus**, **Web of Science (WoS)** e **IEEE Xplore**</mark>, seleccionadas por su amplia cobertura multidisciplinaria, rigurosidad en los procesos de indexación y reconocimiento internacional como fuentes de información científica de alta calidad. Estas plataformas reúnen publicaciones revisadas por pares en áreas como Ciencias de la Computación, Inteligencia Artificial, Ingeniería, Automatización, Sistemas de Información, Informática Industrial e Industria 4.0, disciplinas que convergen directamente con el estudio de <mark style="background-color:#8be9fd">arquitecturas multiagente, Model Context Protocol (MCP) y orquestación e integración de datos industriales</mark>.

La selección de estas bases de datos respondió a tres criterios fundamentales. En primer lugar, ofrecen una cobertura amplia y complementaria de revistas científicas y actas de congresos de alto impacto, reduciendo el riesgo de omitir estudios relevantes. En segundo lugar, disponen de herramientas avanzadas de búsqueda que permiten combinar operadores booleanos, operadores de proximidad y filtros por campos específicos, facilitando la construcción de estrategias de búsqueda precisas, exhaustivas y reproducibles. Finalmente, permiten exportar la información bibliográfica en formatos estandarizados compatibles con herramientas especializadas para la gestión de revisiones sistemáticas [P8S2][16], [K7H4][17].

La **Tabla 5** resume las principales características de las fuentes de información empleadas durante el proceso de búsqueda.

## Tabla 5. Bases de datos utilizadas en la revisión sistemática

| Base de datos | Cobertura temática | Campo de búsqueda utilizado | Formatos de exportación |
|---|---|---|---|
| **Scopus** | Ciencias de la Computación, Inteligencia Artificial, Ingeniería, Automatización, Sistemas de Información e Industria 4.0 | `TITLE-ABS-KEY` (título, resumen y palabras clave) | RIS, CSV |
| **Web of Science (Core Collection)** | Ciencias de la Computación, Ingeniería, Inteligencia Artificial, Informática Industrial y áreas tecnológicas afines | `TS` (Topic: título, resumen, author keywords y keywords plus) | RIS, TXT |
| **IEEE Xplore** | Ingeniería, Ciencias de la Computación, Inteligencia Artificial, Sistemas Industriales, Automatización, Robótica e Informática Industrial | Título, resumen, términos de índice y metadatos | RIS, CSV |

La búsqueda bibliográfica se ejecutó entre el <mark style="background-color:#fff59d">**5 de mayo y el 30 de junio de 2026**</mark>, periodo durante el cual se realizaron búsquedas iterativas hasta obtener una estrategia estable y reproducible. Con el propósito de garantizar la actualidad de la evidencia científica, únicamente se consideraron publicaciones indexadas hasta la fecha de realización de la búsqueda. No se establecieron restricciones geográficas respecto al país de procedencia de los estudios; sin embargo, los resultados se limitaron a publicaciones en <mark style="background-color:#fff59d">**idioma inglés y español**</mark>, debido a que estos idiomas concentran la mayor parte de la producción científica pertinente para el dominio analizado.

Las cadenas de búsqueda específicas formuladas para cada base de datos fueron las siguientes:

Para **Scopus**:

```text
TITLE-ABS-KEY(
  ("multi-agent system*" OR "multiagent system*" OR "AI agent*" OR "LLM agent*" OR "large language model agent*" OR "agentic AI")
  AND
  ("Model Context Protocol" OR MCP OR "tool orchestration" OR "agent orchestration" OR "workflow orchestration")
  AND
  ("industrial data" OR "data integration" OR "industrial integration" OR interoperability OR "heterogeneous data" OR "manufacturing data")
  AND
  ("Industry 4.0" OR manufacturing OR "industrial automation" OR "smart factory" OR IIoT OR "industrial internet of things")
)
```

Para **Web of Science (WoS)**:

```text
TS=(
  ("multi-agent system*" OR "multiagent system*" OR "AI agent*" OR "LLM agent*" OR "large language model agent*" OR "agentic AI")
  AND
  ("Model Context Protocol" OR MCP OR "tool orchestration" OR "agent orchestration" OR "workflow orchestration")
  AND
  ("industrial data" OR "data integration" OR "industrial integration" OR interoperability OR "heterogeneous data" OR "manufacturing data")
  AND
  ("Industry 4.0" OR manufacturing OR "industrial automation" OR "smart factory" OR IIoT OR "industrial internet of things")
)
```

Para **IEEE Xplore**:

```text
("multi-agent system" OR "multiagent system" OR "AI agent" OR "LLM agent" OR "large language model agent" OR "agentic AI")
AND
("Model Context Protocol" OR MCP OR "tool orchestration" OR "agent orchestration" OR "workflow orchestration")
AND
("industrial data" OR "data integration" OR "industrial integration" OR interoperability OR "heterogeneous data" OR "manufacturing data")
AND
("Industry 4.0" OR manufacturing OR "industrial automation" OR "smart factory" OR IIoT OR "industrial internet of things")
```

Todos los registros recuperados fueron exportados desde las bases de datos en formatos compatibles <mark style="background-color:#fff59d">**RIS, CSV y TXT**</mark>, preservando la información bibliográfica necesaria para las etapas posteriores de la revisión. Posteriormente, los registros fueron incorporados a **Parsifal**, plataforma especializada para la gestión de revisiones sistemáticas, con el fin de centralizar la información recuperada, identificar y eliminar registros duplicados, documentar las decisiones adoptadas durante el proceso de selección y mantener la trazabilidad completa de cada estudio desde su identificación inicial hasta su inclusión definitiva [P2A6][18]. Para el análisis descriptivo y la visualización exploratoria de tendencias bibliográficas se contempló el uso complementario de **VOSviewer**, software orientado a la construcción y representación de redes bibliométricas [V9S4][19].

La utilización conjunta de <mark style="background-color:#c8e6c9">Scopus, Web of Science, IEEE Xplore, Parsifal y VOSviewer</mark> proporcionó un entorno metodológico robusto para la administración de la evidencia científica, garantizando transparencia, reproducibilidad y consistencia durante el proceso de revisión, en concordancia con las recomendaciones establecidas por la declaración **PRISMA 2020** [P8S2][16].

Una vez definidas las fuentes de información, se procedió al diseño de la estrategia de búsqueda documental. Para ello, se identificaron los conceptos principales derivados del marco **PICOC** y de las preguntas de investigación, se establecieron los términos de búsqueda y sus sinónimos, y posteriormente se construyeron las cadenas de búsqueda específicas para cada base de datos, tal como se describe en la siguiente subsección.

## 2.4.1 Validación y refinamiento de la estrategia de búsqueda

Con el propósito de garantizar la sensibilidad, exhaustividad y reproducibilidad de la estrategia de búsqueda, se incorporó un proceso de validación iterativo basado en un **Golden Set**, metodología ampliamente utilizada en revisiones sistemáticas de Ciencias de la Computación para verificar la capacidad de una cadena de búsqueda de recuperar los estudios más representativos del dominio de investigación [K7H4][17].

El **Golden Set** estuvo conformado por un conjunto preliminar de artículos considerados relevantes para el tema de estudio. La selección se realizó a partir de publicaciones ampliamente relacionadas con arquitecturas multiagente, agentes LLM, **MCP**, integración de datos industriales e interoperabilidad en entornos de automatización. Inicialmente se construyó una primera versión de la cadena de búsqueda utilizando los conceptos definidos en el marco **PICOC**. Posteriormente, dicha cadena fue ejecutada de manera independiente en **Scopus**, **Web of Science** e **IEEE Xplore**, verificando la recuperación de cada uno de los artículos pertenecientes al **Golden Set**.

Cuando algún estudio de referencia no era recuperado, se analizaban detalladamente su título, resumen y palabras clave con el propósito de identificar nuevos términos, sinónimos o expresiones equivalentes que pudieran incorporarse a la estrategia de búsqueda. Después de cada modificación, la cadena era nuevamente ejecutada y evaluada, repitiéndose este procedimiento hasta obtener un nivel de recuperación considerado satisfactorio.

La sensibilidad de la estrategia fue estimada mediante la siguiente expresión:

$$
\text{Sensibilidad (\%)} =
\frac{\text{Número de artículos del Golden Set recuperados}}
{\text{Número total de artículos del Golden Set}}
\times 100
$$

Como criterio metodológico, se estableció que la estrategia de búsqueda sería considerada adecuada cuando recuperara al menos el <mark style="background-color:#fff59d">**90 %**</mark> de los artículos pertenecientes al **Golden Set**. Este umbral fue definido con el propósito de asegurar una cobertura suficientemente amplia de la literatura científica relevante y reducir el riesgo de excluir estudios potencialmente significativos.

La **Tabla 8** presenta la estructura utilizada para documentar el conjunto de artículos empleados durante la validación.

## Tabla 8. Golden Set utilizado para validar la estrategia de búsqueda (borrador metodológico)

| ID | Autor | Año | Título del artículo | Base de datos | Recuperado |
|---|---|---|---|---|---|
| GS01 | Xia et al. | 2025 | *Control Industrial Automation System with Large Language Model Agents* | Scopus / WoS / IEEE Xplore | Sí / No |
| GS02 | Krishnan | 2025 | *Advancing Multi-Agent Systems Through Model Context Protocol: Architecture, Implementation, and Applications* | Scopus / WoS / IEEE Xplore | Sí / No |
| GS03 | da Silva et al. | 2025 | *Beyond Formal Semantics for Capabilities and Skills: Model Context Protocol in Manufacturing* | Scopus / WoS / IEEE Xplore | Sí / No |
| GS04 | Hu et al. | 2026 | *Applying Model Context Protocol for Offline Small Language Models in Industrial Data Management* | Scopus / WoS / IEEE Xplore | Sí / No |
| GS05 | Vyas y Mercangöz | 2024 | *Autonomous Industrial Control using an Agentic Framework with Large Language Models* | Scopus / WoS / IEEE Xplore | Sí / No |
| GS06 | Hoffmann et al. | 2016 | *Semantic Integration of Multi-Agent Systems using an OPC UA Information Modeling Approach* | Scopus / WoS / IEEE Xplore | Sí / No |
| GS07 | Wen et al. | 2026 | *MICA: Multi-Agent Industrial Coordination Assistant* | Scopus / WoS / IEEE Xplore | Sí / No |
| GS08 | Saleh et al. | 2026 | *Self-Evolving Multi-Agent Network for Industrial IoT Predictive Maintenance* | Scopus / WoS / IEEE Xplore | Sí / No |
| GS09 | Tokal et al. | 2025 | *AgentX: Towards Orchestrating Robust Agentic Workflow Patterns with FaaS-hosted MCP Services* | Scopus / WoS / IEEE Xplore | Sí / No |
| GS10 | Kulkarni et al. | 2026 | *Optimizing FaaS Platforms for MCP-enabled Agentic Workflows* | Scopus / WoS / IEEE Xplore | Sí / No |

El refinamiento de la estrategia fue documentado de manera sistemática para garantizar la trazabilidad de las modificaciones realizadas durante el proceso de validación. La **Tabla 9** registra las principales iteraciones efectuadas antes de obtener la versión definitiva de la cadena de búsqueda.

## Tabla 9. Historial de refinamiento de la estrategia de búsqueda (borrador metodológico)

| Versión | Modificación realizada | Justificación | Artículos recuperados | Sensibilidad (%) |
|---|---|---|---|---|
| V1 | Cadena inicial basada en PICOC | Primera formulación | Pendiente | Pendiente |
| V2 | Incorporación de nuevos sinónimos para integración y orquestación de datos | Recuperar estudios no identificados | Pendiente | Pendiente |
| V3 | Incorporación de términos relacionados con agentes LLM y MCP | Incrementar cobertura temática | Pendiente | Pendiente |
| V4 | Optimización de operadores booleanos, truncamientos y combinaciones por campo | Reducir falsos negativos y mejorar precisión | Pendiente | Pendiente |
| V5 | Cadena definitiva validada | Estrategia final reproducible | Pendiente | Pendiente |

Una vez validada la estrategia de búsqueda, la versión definitiva fue aplicada en las bases de datos **Scopus**, **Web of Science** e **IEEE Xplore** para recuperar los estudios primarios considerados en la presente revisión sistemática. Los registros obtenidos fueron posteriormente exportados e incorporados a **Parsifal** para iniciar el proceso de identificación, deduplicación y selección de estudios conforme al flujo metodológico propuesto por **PRISMA 2020** [P2A6][18], [P8S2][16].
