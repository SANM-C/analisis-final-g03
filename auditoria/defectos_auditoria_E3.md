# Auditoría de defectos — E3 Arena de combate

**Corrida auditada:** 26/11/2026 20:10  
**Spec:** `specs/spec_v1.md` — versión 1.0 inicial  
**Proveedor/modelo:** Ollama / `qwen2.5:7b`  
**Intentos:** 1  
**Duración de extracción:** 63.7 s

## Alcance y criterio

Se comparó la especificación compartida por el equipo, el reporte de validación y los diagramas generados que se enviaron en la conversación: casos de uso, clases, entidad-relación y secuencias CU-01 a CU-16.

El reporte indica que el modelo asoció 27 de 34 requerimientos y que todos los RF y RN tienen algún elemento asociado. La asociación declarada no garantiza que el elemento represente correctamente el requisito. El CSV de trazabilidad generado aún debe revisarse fila por fila para confirmar exactamente cuáles son los 7 requisitos sin asociación.

## Defectos detectados

| ID | Tipo | Dónde | Qué establece la spec | Qué generó el modelo | Causa / corrección recomendada en la spec |
|---|---|---|---|---|---|
| D-01 | Omisión / validación | Secuencias CU-01 a CU-16 | El único actor declarado es `Jugador`; el sistema procesa las acciones. | Las secuencias usan `Sistema` como participante, pero el validador advierte repetidamente que no es actor ni entidad del modelo. | La sección Actores no declara explícitamente una lifeline de sistema/control. Añadir una aclaración: “En diagramas de secuencia, representar el límite/control del módulo como `Sistema de combate`; no considerarlo actor externo ni entidad de negocio”. |
| D-02 | Omisión / estructura | Secuencias CU-04 y CU-05 | RF-04 establece el turno inicial y RF-05 alterna turnos después de cada acción válida. | CU-04 y CU-05 tienen un solo mensaje; el validador informa que tienen menos de 2 mensajes. | La spec explica el comportamiento, pero no exige representar solicitud/resultado o interacción entre componentes. Aclarar que las secuencias deben mostrar al menos el actor o componente que inicia la operación y la respuesta/efecto observable. |
| D-03 | Interpretación incompleta | Secuencias CU-03, CU-07 a CU-14 | La spec incluye validación de vida, ataque, defensa, daño mínimo, daño esquivado, actualización de vida y finalización inmediata. | Las secuencias son mensajes genéricos como “Ejecutar ataque” → “Ataque ejecutado”, sin mostrar las condiciones ni los efectos definidos. | No es una contradicción de la spec: el modelo omitió reglas explícitas. Para reducir la repetición, añadir una instrucción de modelado: las secuencias deben representar condiciones, decisiones y efectos clave del RF/RN relacionado, no solo una solicitud y una respuesta genéricas. |
| D-04 | Interpretación incorrecta | Diagrama de casos de uso | El actor `Jugador` selecciona participantes, inicia el combate y selecciona la acción de su turno. | El actor está conectado directamente a procesos internos como calcular daño, aplicar daño, actualizar vida, verificar estado y determinar ganador. | La spec no distingue explícitamente objetivos del actor frente a pasos internos del sistema. Aclarar que el actor se conecta con objetivos que realiza directamente; los cálculos y verificaciones internas se modelan como pasos incluidos, no como objetivos independientes del jugador. |
| D-05 | Interpretación incorrecta | Diagrama de casos de uso | RF-01 a RF-16 describen funcionalidades y pasos del combate, no necesariamente 16 objetivos independientes del jugador. | Se creó un caso de uso por cada RF y una cadena extensa de `include` entre CU-01 y CU-16. | La spec enumera RF secuenciales, lo que puede inducir una conversión mecánica RF→CU. Añadir que los casos de uso deben agruparse por objetivo del actor y que `include` solo se usa cuando un caso de uso base incorpora obligatoriamente el comportamiento de otro. |
| D-06 | Omisión | Diagrama de clases | El combate tiene dos participantes, turno actual, acciones, estado, vida y resultado final registrado. | Solo aparece la clase `Personaje`, con vida, ataque y métodos `iniciar_combate()` y `realizar_accion()`. | La spec describe el concepto de combate y resultado, pero no enumera explícitamente las entidades del modelo conceptual. Aclarar como entidades candidatas `Combate` y `Resultado`, y que el combate debe mantener participantes, turno/estado y ganador. |
| D-07 | Interpretación incorrecta | Diagrama de clases y ER | RF-04/RN-05 indican quién inicia; RF-15/RN-04 establecen que cada combate tiene dos personajes diferentes. | Se modeló una asociación directa `Personaje 1 -- 1 Personaje` / `Personaje ||--|| Personaje` llamada `enfrentamiento_con`. | La relación entre dos personajes existe dentro de un combate, no como relación permanente entre las entidades Personaje. Aclarar que la asociación debe estar mediada por `Combate`, que contiene exactamente dos participantes distintos. |
| D-08 | Omisión | Diagrama ER | RF-15 exige almacenar un único resultado por combate, con combate, participantes y ganador. | El ER solo contiene `Personaje`; no representa `Combate` ni `Resultado`. | RF-15 sí es explícito; el modelo omitió información necesaria para persistencia. Añadir una guía de modelado: representar el registro único del resultado y su relación con el combate, participantes y ganador. |
| D-09 | Omisión de trazabilidad | `reporte.md` / `trazabilidad_generada.csv` | La spec contiene 16 RF, 7 RNF y 11 RN: 34 requisitos. | El reporte dice 27/34 asociados y que todos los RF y RN tienen asociación. | Por diferencia, los 7 RNF parecen ser los requisitos no asociados. Esto debe confirmarse con las filas del CSV. La spec ya contiene métricas verificables para RNF-01 a RNF-07; no hace falta inventar nuevos requisitos, pero sí exigir que cada RNF tenga una asociación de trazabilidad apropiada. |
| D-10 | Omisión de regla de negocio | Secuencias CU-08 a CU-10 | RF-08/RN-08: defensa esquiva el siguiente ataque del oponente en su siguiente turno; si no ataca en ese turno, la protección desaparece. RN-09: un ataque esquivado no descuenta vida. | Las secuencias muestran seleccionar defensa, calcular y aplicar daño de forma genérica; no representan la activación, consumo o expiración de la protección ni la rama de ataque esquivado. | La regla está descrita en la spec, pero está en RF/RN y en una nota final. Reunir la expiración en RN-08 y exigir que CU-08/CU-09/CU-10 reflejen la rama “esquivado/no esquivado” y el vencimiento de la protección. |

## Evidencia de validación del reporte

- El validador advierte que `Sistema` no es actor ni entidad del modelo en las secuencias CU-01 a CU-16.
- CU-04 y CU-05 tienen menos de 2 mensajes.
- La cobertura declarada es 27 de 34; el reporte afirma que todos los RF y RN tienen asociación.
- La spec, por su cuenta, pasó la revisión automática sin observaciones.

## Conclusión

La spec cubre el flujo funcional principal y sus reglas de negocio; la revisión automática no encontró observaciones. Los defectos más importantes están en la representación generada: secuencias demasiado genéricas, uso incorrecto de asociaciones en casos de uso, modelo de clases/ER incompleto y trazabilidad posiblemente ausente para los RNF.

**Pendiente para cerrar la auditoría:** revisar `trazabilidad_generada.csv` fila por fila y añadir evidencia exacta (RF/RNF/RN y elemento generado) a cada defecto. La inferencia de que los 7 RNF son los no asociados se debe confirmar con ese CSV.
