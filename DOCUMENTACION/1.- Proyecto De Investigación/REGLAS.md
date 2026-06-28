# REGLAS

Para Referencias:
- El formato de referencias es IEEE.
- Para las referencias usaremos un sistema aleatorio: **Código de 4 caracteres alfanuméricos aleatorios con numeración asociada:** [X7K2][1], [Q9P1][2], [H8R3][4]. Totalmente neutro, no se parece a numeración secuencial, y con 4 caracteres alfanuméricos tienes más de un millón de combinaciones posibles, así que la probabilidad de repetir es prácticamente nula incluso sin mucho control (ESTO CON EL FIN DE NO EQUIVOCARNOS POR NUMERACIÓN Y DE QUE CADA REFERENCIA TENGA UN CÓDIGO ÚNICO E IRREPETIBLE).
- Cuando una referencia ya tenga un código asignado, ese código no debe cambiar durante toda la redacción.
- Además del código único, cada referencia debe llevar una **numeración estable** asociada según el orden actual de la lista de referencias.
- El formato oficial de cita y referencia será siempre **[CODIGO][NUMERO]**.
- En las citas dentro del texto, el código debe ir primero y el número después, por ejemplo: [X7K2][1].
- En la lista de referencias, cada entrada también debe iniciar con el mismo formato **[CODIGO][NUMERO]** para mantener sincronía entre cita, identificador único y numeración.
- Si se agrega una nueva referencia, se le asigna un nuevo código único y una nueva numeración según su posición final en la lista de referencias.
- Si una referencia cambia de posición dentro de la lista final, se actualiza su numeración, pero se conserva su mismo código.
- Si una referencia presenta mojibake o caracteres dañados, la solución será **reescribir la referencia completa en UTF-8 limpio**, conservando su mismo código y su misma numeración asociada y verificando que autores, título, revista, año y enlace queden correctos.
- Si al limpiar una referencia aparecen enlaces duplicados, símbolos extraños o comillas dañadas, se debe dejar la entrada en formato simple y legible, con un solo enlace final válido.
- Las referencias de tipo **página web**, **portal institucional**, **noticia**, **sitio informativo** o fuente equivalente que no sea artículo científico no requieren PDF local para considerarse válidas como cita y referencia.
- Las referencias web sí cuentan como citas y deben conservar su código dentro del documento, pero **no deben incluirse en la lista de faltantes de PDF**.
- La lista de faltantes de PDF debe considerar solo artículos, papers, proceedings, capítulos, preprints o documentos académicos para los cuales sí tendría sentido conservar un PDF local.

Para Codificación de Archivos:
- El formato de codificación para crear y editar archivos `.md` será **UTF-8**.
- Cada vez que se cree o reescriba un archivo, debe guardarse explícitamente en **UTF-8**, para evitar problemas de caracteres como tildes, eñes, comillas especiales o símbolos.
- Al editar desde terminal o scripts, se debe usar guardado en **UTF-8** y evitar mezclar codificaciones como ANSI, Windows-1252 o UTF-8 interpretado incorrectamente.
- Si un archivo se visualiza con texto dañado tipo **mojibake** (`CÃƒÂ³digo`, `IntroducciÃƒÂ³n`, `informaciÃƒÂ³n`), se asume que hubo un problema de interpretación o guardado de codificación.
- Si ocurre mojibake, la solución será: **reescribir o guardar nuevamente el archivo completo en UTF-8 limpio**, verificando que el contenido correcto quede restaurado antes de continuar editando.
- Si el editor visualiza correctamente el archivo, pero la terminal lo muestra dañado, no se asumirá de inmediato que el archivo está mal; primero se considerará que el problema puede ser solo de visualización de consola.

Para Ordenar el Índice:
- El índice del proyecto debe reflejar **toda la estructura real del documento**, incluyendo capítulos, subcapítulos y apartados específicos existentes en los archivos fuente.
- En Obsidian, el índice se redactará **sin números de página**, ya que esos valores pertenecen a la versión final en Word o PDF.
- Cada entrada del índice debe enlazar al encabezado correspondiente mediante enlaces internos de Obsidian, manteniendo coincidencia exacta entre el texto visible y el título o subtítulo enlazado.
- Las jerarquías del índice deben respetarse visualmente mediante sangría: un apartado hijo debe ir más adentro que su apartado padre.
- Para distinguir claramente la jerarquía visual, los subniveles del índice deben usar **tabulación real** y no solo uno o dos espacios simples.
- Los capítulos principales como `I. INTRODUCCIÓN`, `II. MATERIAL Y MÉTODO`, `III. ASPECTOS ADMINISTRATIVOS` y `REFERENCIAS` van al nivel base del índice.
- Los apartados como `1.1`, `1.2`, `1.3`, `2.1`, `2.2`, `3.1`, `3.2` y similares van en el primer nivel de viñeta bajo su capítulo principal.
- Los subapartados como `1.3.1`, `2.3.1`, `2.4.1`, `3.1.1` y equivalentes deben ir un nivel más adentro, con una tabulación adicional respecto al apartado padre.
- La jerarquía visual del índice debe mantenerse uniforme en todo el documento; no se permite mezclar subniveles con distintas sangrías.
- Si un apartado tiene subapartados, estos nunca deben quedar alineados al mismo nivel visual que su apartado padre.
- Si se agrega, elimina o renombra una sección del documento, el índice debe actualizarse de inmediato para conservar coherencia estructural.
- El apartado `ANEXOS` puede figurar al final del índice como texto simple mientras no exista aún un archivo o encabezado definitivo para enlazarlo.

Para Antecedentes (Trabajos Previos):
- Cada antecedente se redacta como un solo párrafo corrido, sin subtítulos ni numeración visible (las preguntas guía no se marcan como "1, 2, 3...", quedan disueltas dentro del texto).
- El título, los autores y el código de referencia no se listan arriba del párrafo; la identificación del antecedente queda integrada dentro de la redacción del mismo párrafo.
- El párrafo debe iniciar de forma narrativa y académica, integrando autor(es) y código desde la primera oración. Fórmulas recomendadas: **"El estudio de Autor et al. [CÓDIGO][NUMERO]..."**, **"La investigación desarrollada por Autor et al. [CÓDIGO][NUMERO]..."**, **"Autor et al. [CÓDIGO][NUMERO] propusieron..."**.
- La estructura base recomendada para la primera oración es: **"El estudio de Autor(es) [CÓDIGO][NUMERO] tuvo como objetivo..."**; desde esa oración ya debe quedar explícito qué hicieron los autores.
- El párrafo debe cubrir en orden, sin etiquetarlas: qué se hizo (objetivo del estudio), cómo se hizo (datos usados, preprocesamiento, variables o características seleccionadas, algoritmos o métodos empleados, división de datos si aplica), qué resultados obtuvieron (cifras exactas con su indicador: "94.1% de Accuracy", "AUC de 0.957", nunca aproximaciones como "buenos resultados"), a qué conclusión llegaron los autores, y cómo esa investigación aporta al trabajo propio (esto último puede ir en frase final o por separado, según se indique).
- Todo antecedente debe responder obligatoriamente, dentro del mismo párrafo y en este orden lógico, a estas cinco preguntas guía: **¿Qué se hizo?**, **¿Cómo se hizo?**, **¿Qué resultados obtuvieron?**, **¿A qué conclusión llegaron los autores?** y **¿Cómo aporta esta investigación al trabajo propio?**
- La primera parte del párrafo responde **qué se hizo** y debe quedar explícita desde la oración inicial con autor(es) + código + objetivo del estudio.
- La segunda parte responde **cómo se hizo** y debe describir la metodología con detalle técnico suficiente: datos, arquitectura, agentes, herramientas, variables, algoritmos, validación, casos de estudio o entorno experimental, según corresponda.
- La tercera parte responde **qué resultados obtuvieron** y debe incluir resultados **cuantitativos exactos** siempre que existan: accuracy, F1, RMSE, AUC, latencia, costo, reducción porcentual, tiempos, etc.
- La cuarta parte responde **a qué conclusión llegaron los autores** y debe expresar el hallazgo principal validado por el estudio.
- La quinta parte responde **cómo aporta a mi investigación** y debe cerrar el antecedente con un aporte específico al trabajo propio, evitando cierres genéricos.
- Se debe usar resaltado de color para diferenciar visualmente cada parte: amarillo = objetivo, celeste = metodología, verde = resultados, rosa/morado = conclusión o hallazgo destacado.
- Los términos técnicos clave (nombres de algoritmos, métricas, variables, porcentajes) van en negrita dentro del texto.
- La metodología se describe con nivel de detalle técnico: nombrar uno por uno los datos, variables o algoritmos usados, no generalizar ("varios algoritmos" está prohibido si se puede nombrar cada uno).
- Solo se trabaja con artículos científicos originales (no de revisión), provenientes de bases de datos académicas (Scopus, ScienceDirect, IEEE Xplore, PubMed, ISI, etc.).
- No se copian frases textuales del artículo original; todo se redacta con palabras propias para evitar plagio.
- El antecedente cierra con una frase que conecta el hallazgo con una aplicación práctica o proyección futura, no con un cierre genérico tipo "los autores concluyeron que...".
- Para que un antecedente sea considerado **fuerte metodológicamente**, debe incluir **resultados cuantitativos reales** tomados del artículo fuente: porcentajes, accuracy, F1, AUC, RMSE, tiempos, latencia, reducción porcentual, número de casos, tamaño de muestra u otra métrica objetiva equivalente.
- Los resultados cuantitativos del antecedente deben ser **reales y verificables** en el PDF o fuente primaria; no se permite inferir, redondear arbitrariamente ni inventar métricas que el artículo no reporta.
- Si el artículo no presenta resultados numéricos explícitos, el antecedente puede conservarse solo como apoyo conceptual, arquitectónico o demostrativo, pero debe marcarse internamente como **antecedente débil en evidencia cuantitativa**.
- Cuando un artículo no reporte métricas numéricas, en la redacción del antecedente se debe dejar claro que validó la propuesta mediante prototipo, demostrador, caso de estudio o evidencia cualitativa, sin atribuirle precisión, mejora porcentual o desempeño cuantitativo no reportado.
- Como criterio de calidad para esta investigación, se buscará reunir **al menos 20 antecedentes** que sí presenten resultados cuantitativos reales y explícitos.
- Si un antecedente no alcanza ese estándar cuantitativo y existe otro artículo más cercano al tema con métricas reales, se debe priorizar el reemplazo del antecedente débil por el antecedente fuerte.

Para Objetivos:
- Los objetivos específicos deben seguir una secuencia lógica de ejecución del proyecto.
- El primer objetivo específico debe orientarse a la **revisión de la literatura científica** directamente relacionada con el tema de investigación.
- Cuando el estudio trate sobre agentes de IA, MCP e integración de datos industriales, el objetivo inicial debe formularse con una estructura semejante a: **"Realizar una revisión de la literatura científica sobre arquitecturas multiagente basadas en inteligencia artificial y Model Context Protocol (MCP) aplicadas a la integración y orquestación de datos industriales."**
- Después del objetivo de revisión de literatura, los siguientes objetivos deben avanzar en orden hacia análisis del problema, construcción y preparación del dataset, diseño, desarrollo, implementación y evaluación.
Para Evitar Mojibake:
- Antes de editar un archivo `.md`, se debe asumir como regla base que el archivo debe leerse y escribirse únicamente en **UTF-8**.
- No se debe usar edición que mezcle codificaciones como ANSI, Windows-1252, Latin-1 o UTF-8 mal interpretado.
- Si se edita desde scripts o terminal, se debe preferir lectura y escritura explícita con codificación UTF-8 y evitar operaciones que reinterpreten bytes sin control.
- Después de cada edición importante, se debe hacer una verificación visual inmediata buscando patrones típicos de mojibake como: `Ã`, `Â`, `�`, `CÃ³`, `aciÃ³n`, `investigaciÃ³n`, `diseÃ±o`.
- Si aparece cualquiera de esos patrones, se debe detener la edición y corregir el archivo antes de seguir avanzando.
- No se debe continuar agregando contenido sobre un archivo que ya muestre mojibake sin antes limpiarlo.
- Cuando se reescriba un bloque completo para corregir codificación, se debe reemplazar el texto dañado por el texto correcto completo, no hacer correcciones parciales letra por letra.
- Si una operación en terminal produce texto con mojibake, se debe considerar esa operación como riesgosa y no reutilizarla para futuras ediciones del documento.
- Para cambios sensibles, primero se debe identificar el bloque exacto a modificar y luego escribirlo completo en UTF-8 limpio.
- Si existe duda entre problema de archivo y problema de consola, se debe validar el resultado final en Obsidian antes de seguir editando otras secciones.
Para Evitar Signos de Interrogación en Tildes:
- Después de cada edición de un archivo `.md`, se debe verificar que no aparezcan signos `?` dentro de palabras que deberían llevar tildes, eñes o caracteres especiales.
- Se consideran señales de error formas como: `revisi?n`, `integraci?n`, `gesti?n`, `dise?ar`, `librer?as`, `desempe?o`, `t?rminos`, `reducci?n`.
- Si aparece un signo `?` reemplazando una vocal acentuada o una `ñ`, no se debe continuar editando el archivo hasta corregir ese bloque.
- Antes de dar por finalizada una modificación, se debe hacer una búsqueda rápida de caracteres sospechosos como `?`, `Ã`, `Â` y `�` dentro del archivo editado.
- Si el signo `?` aparece dentro de una palabra académica o técnica, se debe asumir que hubo pérdida de codificación y se debe reescribir la línea completa en UTF-8 limpio.
- No se debe corregir solo el carácter aislado cuando el bloque completo pueda estar comprometido; se debe preferir reemplazar la oración o lista completa correctamente escrita.
- En secciones sensibles como títulos, objetivos, hipótesis, variables, tablas y referencias, la revisión de estos caracteres es obligatoria después de cada edición.
Para Diferenciar 1.3 y 2.2:
- El apartado **1.3 Teorías relacionadas al tema** debe fortalecer la **base teórica general** del estudio.
- En `1.3` se deben definir y sustentar conceptualmente las métricas, indicadores, fórmulas y dimensiones desde fuentes académicas generales, libros, artículos y estándares.
- El contenido de `1.3` debe responder qué significa cada métrica o indicador, por qué existe y cómo se entiende en la literatura científica, sin depender todavía del experimento concreto del proyecto.
- El apartado **2.2 Variables, Operacionalización** debe fortalecer la **validez metodológica aplicada al proyecto**.
- En `2.2` cada variable, dimensión, indicador, fórmula e instrumento debe quedar orientado directamente a la investigación en curso.
- El contenido de `2.2` debe explicar cómo se aplicará cada métrica dentro del proyecto, con qué instrumento se medirá, en qué unidad se expresará y por qué ese indicador es pertinente para evaluar la propuesta.
- En términos prácticos: `1.3` es más **general y teórico**, mientras que `2.2` es más **específico y metodológico**.
- Si una fórmula aparece en ambos apartados, en `1.3` se justifica teóricamente y en `2.2` se operacionaliza para el caso concreto del proyecto.

Para Diferenciar 1.3, 2.2 y 2.5:
- El apartado **2.5 Procedimiento de análisis de datos** debe aplicar de manera **específica y operativa** los indicadores ya definidos en `2.2` y sustentados en `1.3`.
- En `2.5` se deben mencionar los indicadores por su **nombre exacto**, tal como aparecen en las tablas de operacionalización.
- En `2.5` cada fórmula debe escribirse nuevamente, pero ya explicando qué representa cada variable **dentro del proyecto** y de dónde saldrán esos datos.
- `2.5` debe indicar con claridad las **fuentes de datos operativas** de cada indicador: logs del sistema, archivos de configuración, bitácoras, reportes de auditoría, dataset, registros SCADA/MES u otros equivalentes.
- En términos prácticos: `1.3` define, `2.2` organiza y `2.5` ejecuta metodológicamente.
- Las tablas de operacionalización de `2.2` son un instrumento propio del investigador, por lo tanto **no deben llevar citas dentro de la tabla**.
- Si una métrica aparece en `1.3`, `2.2` y `2.5`, su tratamiento correcto será: en `1.3` se fundamenta, en `2.2` se operacionaliza y en `2.5` se explica cómo se calculará y analizará en el estudio.

Para Fórmulas Matemáticas en Obsidian:
- La documentación del proyecto se visualiza en **Obsidian**, por lo tanto las fórmulas matemáticas deben escribirse en el formato que Obsidian renderiza correctamente.
- Para fórmulas dentro de un párrafo se debe usar el formato **inline** con signos de dólar: $...$.
- Para fórmulas centradas o destacadas se debe usar el formato de bloque con doble signo de dólar: `$$ ... $$`.
- No se debe usar como formato principal \(...\) ni \[...\], porque en Obsidian pueden mostrarse como texto crudo según el modo de visualización.
- Si una fórmula aparece visible como texto literal en Obsidian, se debe convertir inmediatamente de `\(...\)` a `$...$` o de `\[...\]` a `$$...$$`.
- Para revisar correctamente las fórmulas en Obsidian se debe usar **Live Preview** o **Reading View**; no se debe evaluar su renderizado final en **Source mode**.
- Cuando una variable matemática aparezca dentro de una oración, debe escribirse también en formato inline, por ejemplo: $F_i$, $F_t$, $T_{ex}$, $M_{pre}$.
- Antes de dar por concluida una edición con fórmulas, se debe verificar visualmente en Obsidian que la expresión se renderice como fórmula y no como texto plano.
Para Proteger Archivos Críticos:
- Antes de reemplazar, reescribir o reconstruir un archivo crítico del proyecto (por ejemplo: I. INTRODUCCIÓN.md, II. MATERIAL Y MÉTODO.md, REFERENCIAS.md, REGLAS.md o cualquier archivo principal), se debe verificar primero si el archivo actual contiene contenido que no esté presente en la fuente de rescate o apoyo.
- Nunca se debe sobrescribir por completo un archivo crítico usando otro archivo auxiliar, respaldo parcial o borrador si ese archivo auxiliar no contiene la totalidad de las secciones vigentes.
- Si existe un archivo de apoyo como Rescatado.md, este debe usarse solo para extraer o restaurar bloques puntuales, no para reemplazar de forma completa el archivo principal, salvo verificación previa sección por sección.
- Antes de cualquier reemplazo masivo, se debe crear obligatoriamente una copia de seguridad inmediata del archivo original en la misma carpeta, con un nombre visible y fechable, por ejemplo: I. INTRODUCCIÓN - BACKUP ANTES DE REEMPLAZO.md.
- Antes de guardar un cambio que afecte gran parte de un archivo, se debe comprobar explícitamente que permanecerán intactas todas las secciones existentes relevantes (1.1, 1.2, 1.3, 1.4, etc., según corresponda).
- Si el objetivo es restaurar imágenes, figuras o párrafos perdidos, la regla es insertar únicamente esos elementos faltantes dentro del archivo principal; no reemplazar el documento completo.
- Si hay duda sobre si una acción puede borrar contenido previo, se debe detener la edición y optar por una restauración incremental por bloques.
- Después de cualquier restauración grande, se debe verificar de inmediato que el archivo final conserve tanto el contenido previo como el contenido restaurado, antes de eliminar archivos auxiliares o respaldos.

