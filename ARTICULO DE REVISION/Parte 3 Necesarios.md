# Parte 3 — Datos cuantitativos necesarios

## Categoría: Problema (interoperabilidad, silos, integración, tiempo real, plataformas)

---

### [Q9P1][1] Industry 4.0/IIoT Platforms for manufacturing systems — A systematic review

- **Dato 1:** Solo **17%** de las plataformas científicas procesan datos en tiempo real; **50%** ofrecen soporte AI/ML.
  - Página: 11
  - Texto base: "6 platforms (17%) that the processing is being executed in real-time... 50% of the platforms... AI tasks include decision making (3), predictive maintenance (3)"
  - Uso en Parte 3: evidencia directa de que la mayoría de plataformas IIoT aún no soportan procesamiento en tiempo real ni integración con IA, reforzando el problema de interoperabilidad.

- **Dato 2:** Solo **53%** de las plataformas permiten compartir o usar datos externos.
  - Página: 12
  - Texto base: "53% of the platforms..."
  - Uso en Parte 3: demuestra que la integración de datos entre sistemas sigue siendo limitada incluso a nivel de plataforma.

- **Dato 3:** Se identificaron **21 plataformas IIoT industriales**; **90% son comerciales**, 38% de USA.
  - Página: 3, 14
  - Texto base: "21 industrial IIoT platforms... 90% of platforms are commercial"
  - Uso en Parte 3: muestra la fragmentación del mercado y el dominio comercial frente a soluciones académicas interoperables.

---

### [X7K2][2] Data Integration for Digital Twins in Industrial Automation: A Systematic Literature Review

- **Dato 1:** Se proyectan **280 Zettabytes (ZB)** de datos globales para 2025; los dispositivos IoT generarían **~41% (79 ZB de 181 ZB)**.
  - Página: 2
  - Texto base: "280 Zettabytes (ZB) [12] with IoT-based devices presumably generating approximately 41% of this data in 2025 (79 ZB of 181 ZB)"
  - Uso en Parte 3: dimensiona el volumen masivo de datos industriales que necesitan integración, justificando la urgencia del problema.

- **Dato 2:** Los sistemas heterogéneos y diversos en una red de producción interconectada son el principal desafío para la integración de datos.
  - Página: 2
  - Texto base: "the heterogeneous and diverse systems in an interconnected production network"
  - Uso en Parte 3: respalda que la heterogeneidad es el núcleo del problema de interoperabilidad.

---

### [T5W9][8] Manufacturing Integration Framework: A SOA Perspective on Manufacturing

- **Dato 1:** El costo de soporte de sistemas heredados puede crecer **exponencialmente** debido a HW/SW propietarios en arquitecturas punto a punto.
  - Página: 4
  - Texto base: "Support cost associated with these aging systems can grow exponentially"
  - Uso en Parte 3: evidencia que las arquitecturas de integración tradicionales (punto a punto) generan costos crecientes e insostenibles.

- **Dato 2:** Las soluciones actuales **no pueden soportar cambios ni mejoras** en los procesos, ni proveer la accesibilidad a datos requerida.
  - Página: 4
  - Texto base: "cannot support process changes/improvements or provide required data accessibility"
  - Uso en Parte 3: refuerza la rigidez e inflexibilidad de los sistemas de integración tradicionales como problema central.

*(Nota: este paper es conceptual/arquitectónico, no contiene cifras porcentuales. Los datos cualitativos sobre costos exponenciales y falta de flexibilidad son útiles para contextualizar el problema.)*

---

### [J9F5][9] Strategic Integration of ERP and Manufacturing Information Systems

- **Dato 1:** Las implementaciones de ERP típicamente toman entre **12 y 36 meses**, con costos de mantenimiento post-implementación que representan **más del 50%** del gasto total.
  - Página: 4 (838), 9 (843)
  - Texto base: "ERP implementations typically take between 12 to 36 months... more than half of ERP-related expenses arise from post-implementation maintenance"
  - Uso en Parte 3: muestra que la integración ERP-manufactura es lenta, costosa y con costos ocultos elevados.

- **Dato 2:** Las disrupciones en integración pueden generar pérdidas financieras por **millones de dólares** si no se mitigan proactivamente.
  - Página: 6 (840)
  - Texto base: "Mitigating these disruptions proactively can prevent significant financial losses, often totaling millions of dollars"
  - Uso en Parte 3: cuantifica el impacto económico de los fallos de integración.

- **Dato 3:** La implementación completa de ERP puede tomar de **3 a 5 años**, con declives temporales de productividad durante el proceso.
  - Página: 7 (841)
  - Texto base: "Implementing an ERP system typically spans approximately three to five years, during which organizations may experience temporary declines in productivity"
  - Uso en Parte 3: evidencia que los proyectos de integración son largos y afectan negativamente la productividad durante la transición.

---

### [E6M1][10] Implementing Manufacturing Execution Systems (MES) for Industry 4.0

- **Dato 1:** En un caso de estudio, el comprador reportó haber aprovechado solo **~10%** de las capacidades del MES implementado.
  - Página: 8
  - Texto base: "we were only able to leverage about 10% of its capabilities. We ended up using just a production display"
  - Uso en Parte 3: evidencia contundente de que la integración MES real es deficiente, con enorme potencial desaprovechado.

- **Dato 2:** Un contrato MES fue **terminado después de un año** por problemas de integración entre comprador y proveedor.
  - Página: 7
  - Texto base: "after a year of grappling with these challenges, FurnitureCo opted to terminate the contract"
  - Uso en Parte 3: muestra fracaso de integración MES por asimetrías de información y falta de interoperabilidad.

- **Dato 3:** Estudio basado en **56 expertos de 33 empresas**; **45% grandes**, **39% medianas**, **15% pequeñas**; sectores: servicios (30%), automotriz (15%), muebles (12%), bebidas (9%).
  - Página: 4
  - Texto base: "56 key experts from 33 companies... Services 30%, Automotive 15%..."
  - Uso en Parte 3: respalda la validez del estudio y muestra que los problemas de integración MES afectan a todos los tamaños y sectores.

- **Dato 4:** Se identificaron **3 configuraciones** de MES 4.0: (1) visibilidad local, (2) integración unidireccional, (3) integración bidireccional (con IA + Digital Twins).
  - Página: 6
  - Texto base: "Local visibility, One-way integration, Two-way integration"
  - Uso en Parte 3: muestra que la integración plena (bidireccional con IA) es aún la excepción, no la norma.

---

### [U3K7][11] Secured cloud SCADA system implementation for industrial applications

- **Dato 1:** El sistema SCADA propuesto es **5 veces más barato** que Arduino+WiFi y **13 veces más barato** que Raspberry-Pi.
  - Página: 1, 5
  - Texto base: "lower than Arduino + WIFI method by five times and 13 times lower than Raspberry-PI method"
  - Uso en Parte 3: demuestra que hay brecha de costos en implementaciones SCADA, relevante para PyMEs.

- **Dato 2:** Polling de nodos cada **500 ms** para datos en tiempo real; latencia depende solo de la velocidad de internet.
  - Página: 5, 7
  - Texto base: "Node sends frequent requests to server each 500 msec... Latency depends only on the speed of the internet access"
  - Uso en Parte 3: evidencia que SCADA en la nube puede lograr tiempos de respuesta cercanos a tiempo real.

- **Dato 3:** El sistema soporta **número ilimitado de nodos RTU** con **4 niveles de seguridad** (autenticación, autorización, RSA, CBC).
  - Página: 1, 4
  - Texto base: "unlimited number of added Remote Terminal Units (RTU) nodes... four (4) security levels"
  - Uso en Parte 3: muestra que SCADA cloud puede ser escalable y seguro, pero sigue siendo un sistema supervisado, no autónomo.

---

### [U2M5][13] Semantic Integration of Multi-Agent Systems using an OPC UA Information Modeling Approach

- **Dato 1:** El estándar OPC fue integrado en entornos de automatización desde los **años 1990**; OPC UA permite modelado de información semántica.
  - Página: 2
  - Texto base: "1990s when OPC standard was embedded in automation environments"
  - Uso en Parte 3: OPC UA es un estándar maduro pero su integración con sistemas multiagente sigue siendo un área emergente sin métricas cuantitativas publicadas.

- **Dato 2:** Se demostró integración semántica MAS+OPC UA en un **caso demostrador de producción de yogur** con 4 pasos de producción (secuenciales y paralelos) y mecanismo de pricing aleatorio.
  - Página: 4
  - Texto base: "Yogurt Production → Yogurt Refinement → Cap Engraving → Filling... randomly picks one of the machines"
  - Uso en Parte 3: sirve como ejemplo conceptual de integración semántica, pero no hay datos cuantitativos de rendimiento.

*(Nota: paper arquitectónico/conceptual — sin evaluación cuantitativa. Útil para enfoque cualitativo sobre integración semántica.)*

---

### [F6I1][14] Smart Factory of Industry 4.0: Key Technologies, Application Case, and Challenges

- **Dato 1:** En un caso de estudio de 6 meses en una línea prototipo de empaquetado de caramelos, el OEE (Efectividad General del Equipo) mejoró de **0.42 a 0.82** (~95% de mejora) usando un sistema de manufactura asistido por nube con scheduling auto-organizado.
  - Página: 9-10
  - Texto base: "the Overall Equipment Effectiveness (OEE) of tested equipment is improved from 0.42 to 0.82 using the cloud-aided manufacturing system"
  - Uso en Parte 3: evidencia cuantitativa de que la integración cloud y scheduling auto-organizado puede casi duplicar la efectividad.

- **Dato 2:** Las métricas del caso mostraron mejora sostenida mes a mes: Availability Ratio **0.78→0.92**, Performance Ratio **0.59→0.96**, Qualified Ratio **0.92→0.93**.
  - Página: 9
  - Texto base: "Availability: 0.78→0.92, Performance: 0.59→0.96, Qualified: 0.92→0.93"
  - Uso en Parte 3: desglose de cómo la integración mejora cada componente del OEE, especialmente rendimiento (+63%).

- **Dato 3:** Se identificaron tecnologías clave: IWSNs (Wireless HART, WIA-AP, ISA100.11a), OPC UA, SDN (OpenFlow), Edge Computing, y Ontologías (OWL2.0, SWRL).
  - Página: 4-6
  - Texto base: "Physical Resource Layer... Network Layer... Data Application Layer"
  - Uso en Parte 3: muestra el ecosistema tecnológico disponible para smart factory, pero también la complejidad de integrar todas estas capas.

---

## Categoría: Impacto (productividad, costos, eficiencia, errores, retrasos, competitividad)

---

### [F6I1][14] + [Q9P1][1] — Impacto en productividad y eficiencia

- **Dato combinado:** El OEE puede mejorar **~95%** (0.42→0.82) con integración cloud + scheduling auto-organizado [F6I1][14], pero solo **17%** de las plataformas IIoT procesan en tiempo real [Q9P1][1].
  - Uso en Parte 3: el contraste muestra el enorme potencial de mejora versus la baja adopción real.

---

### [J9F5][9] — Impacto económico

- **Dato 1:** Las disrupciones en integración pueden causar pérdidas por **millones de dólares** si no se mitigan.
  - Página: 6
  - Uso en Parte 3: impacto económico directo de la falta de integración efectiva.

- **Dato 2:** **Más del 50%** de los costos totales de ERP ocurren después de la implementación, durante el mantenimiento.
  - Página: 9
  - Uso en Parte 3: los costos ocultos de integración superan a los de implementación inicial, afectando el ROI.

---

### [E6M1][10] — Impacto en adopción y aprovechamiento

- **Dato 1:** Solo **~10%** de las capacidades del MES fueron realmente aprovechadas en un caso real, usando solo una pantalla de producción.
  - Página: 8
  - Uso en Parte 3: el bajo aprovechamiento de MES implica desperdicio de inversión y brecha entre capacidades técnicas y uso real.

- **Dato 2:** Contrato MES **terminado tras 1 año** por problemas de integración, indicando que los fracasos en integración llevan a abandono de la solución.
  - Página: 7
  - Uso en Parte 3: los problemas de interoperabilidad no solo reducen eficiencia, sino que pueden llevar al fracaso total del proyecto.

---

### [T5W9][8] — Impacto en costos operativos

- **Dato 1:** Costos de soporte de sistemas heredados crecen **exponencialmente** en arquitecturas punto a punto con HW/SW propietarios.
  - Página: 4
  - Uso en Parte 3: la falta de estandarización en integración genera costos operativos crecientes, no lineales.

---

### [U3K7][11] — Impacto en accesibilidad económica

- **Dato 1:** Solución SCADA cloud es **5× más barata** que Arduino+WiFi y **13× más barata** que Raspberry-Pi (135 LE vs 450 LE vs 1350 LE).
  - Página: 1, 5
  - Uso en Parte 3: las soluciones basadas en cloud pueden reducir barreras económicas de entrada, especialmente para PyMEs.

---

## Categoría: Solución (MCP, multiagentes, IA, MES, SCADA, OPC UA)

---

### [M6P3][6] Advancing Multi-Agent Systems Through Model Context Protocol

- **Dato 1:** Asignación de tareas: sistemas MCP lograron **12% del óptimo computado** frente a **27%** de enfoques baseline (mejora del ~55%).
  - Página: 82
  - Uso en Parte 3: MCP mejora significativamente la optimalidad en asignación de tareas entre agentes.

- **Dato 2:** Resolución de conflictos **3.2 veces más rápida** en sistemas MCP, con **94%** resueltos sin escalar a decisión centralizada.
  - Página: 82
  - Uso en Parte 3: MCP permite coordinación descentralizada eficiente, clave para entornos industriales dinámicos.

- **Dato 3:** Los sistemas MCP seleccionaron la modalidad de salida óptima con **78.9% accuracy** frente a **61.2%** de baseline (+28.9%).
  - Página: 83
  - Uso en Parte 3: MCP mejora la calidad de la comunicación contextual entre agentes y herramientas.

- **Dato 4:** MCP redujo el esfuerzo de implementación en **47%** frente a integraciones personalizadas, con **92% menor varianza** en rendimiento.
  - Página: 84-85
  - Uso en Parte 3: MCP estandariza la integración, reduciendo costo y aumentando consistencia.

---

### [E6M1][10] — Taxonomía de integración MES 4.0 como solución

- **Dato 1:** Las **3 configuraciones** de MES 4.0 (visibilidad local, unidireccional, bidireccional con IA) muestran una progresión de madurez en integración.
  - Página: 6
  - Uso en Parte 3: sirve como marco para entender los niveles de integración posibles, desde lo básico hasta IA + Digital Twins.

- **Dato 2:** La configuración **bidireccional** (two-way integration) integra IoT + cloud + big data analytics con AI + digital twins, representando el nivel más avanzado.
  - Página: 6
  - Uso en Parte 3: MES con IA y Digital Twins es el estado del arte en integración, pero requiere madurez organizacional y técnica.

---

### [U3K7][11] — SCADA cloud como solución de monitoreo

- **Dato 1:** SCADA cloud con **4 niveles de seguridad** (autenticación, autorización, RSA, CBC) y soporte para **número ilimitado de nodos** RTU.
  - Página: 1, 4
  - Uso en Parte 3: las soluciones SCADA modernas pueden ser seguras, escalables y accesibles desde cualquier plataforma.

- **Dato 2:** Polling **cada 500 ms** con latencia limitada solo por velocidad de internet.
  - Página: 5
  - Uso en Parte 3: SCADA cloud puede aproximarse a tiempo real, pero no es equivalente a sistemas deterministicos industriales.

---

### [F6I1][14] — Smart factory como solución integral

- **Dato 1:** El caso de estudio mostró que un sistema cloud-aided con scheduling auto-organizado puede mejorar OEE de **0.42 a 0.82** (+95%) en 6 meses.
  - Página: 9-10
  - Uso en Parte 3: la integración cloud + auto-organización es una solución viable y mensurable para smart factory.

- **Dato 2:** Tecnologías habilitadoras identificadas: IWSNs, OPC UA, SDN, Edge Computing, Ontologías OWL2.0/SWRL, Big Data.
  - Página: 4-6
  - Uso en Parte 3: el ecosistema tecnológico existe, pero su integración coordinada sigue siendo el desafío.

---

### [U2M5][13] — Integración semántica MAS + OPC UA

- **Dato 1:** OPC UA (desde los 90s) permite modelado de información semántica, y su integración con MAS se demostró en un caso de producción con **4 pasos** secuenciales y paralelos.
  - Página: 2, 4
  - Uso en Parte 3: OPC UA + MAS es un enfoque prometedor para integración semántica, aunque sin evaluación cuantitativa publicada.

---

## Resumen ejecutivo para Parte 3

| Categoría | Cifras clave | Fuentes |
|-----------|-------------|---------|
| **Problema** | 17% tiempo real, 50% AI/ML, 53% datos externos, 90% comercial | Q9P1 |
| **Problema** | 280 ZB datos 2025, 41% IoT, heterogeneidad como desafío principal | X7K2 |
| **Problema** | Costos de soporte exponenciales en arquitecturas punto a punto | T5W9 |
| **Problema** | 12-36 meses implementación, >50% costos post-implementación | J9F5 |
| **Problema** | ~10% de capacidades MES aprovechadas, contrato terminado a 1 año | E6M1 |
| **Impacto** | OEE mejora 0.42→0.82 (+95%) con integración cloud | F6I1 |
| **Impacto** | Pérdidas de millones de dólares por disrupciones | J9F5 |
| **Impacto** | 5×-13× diferencias de costo en implementaciones SCADA | U3K7 |
| **Impacto** | Contrato MES cancelado, 10% de capacidades usadas | E6M1 |
| **Solución** | MCP: 12% vs 27% asignación, 3.2× más rápido, 78.9% accuracy, -47% esfuerzo | M6P3 |
| **Solución** | MES 4.0 bidireccional con IA + DT como nivel más avanzado | E6M1 |
| **Solución** | SCADA cloud: 500ms polling, ilimitado nodos, 4 niveles seguridad | U3K7 |
| **Solución** | OEE +95% con cloud + scheduling auto-organizado | F6I1 |
| **Solución** | OPC UA + MAS para integración semántica (demostrado conceptualmente) | U2M5 |
