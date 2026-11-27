# Comparación de corridas — E3 Arena de combate

> Documento de auditoría comparativa. Se conservan los datos observados y se separan los hallazgos confirmados de los puntos que deben cotejarse con los archivos originales.

## 1. Objetivo

Comparar la primera y la segunda generación del módulo **Arena de combate**, revisar si el prompt corregido mejoró la calidad de los artefactos y registrar los defectos que aún requieren corrección.

La comparación se basa en los reportes y fragmentos compartidos por el equipo. No se considera que una corrida sea correcta únicamente porque el pipeline la haya validado.

## 2. Identificación de las corridas

| Dato | Primera corrida | Segunda corrida |
|---|---|---|
| Módulo | Arena de combate | Arena de combate |
| Modelo | Ollama `qwen2.5:7b` | Qwen2.5 7B |
| Fecha / duración reportada | 26/11/2026, 20:10; 63,7 s | Generada posteriormente con prompt corregido |
| Prompt | Prompt anterior | Prompt corregido |
| Ubicación reportada | `salida/primera_corrida/` | `salida/segunda_corrida/` |
| Rama | No indicada en el reporte compartido | `bonus-pipeline` |
| Diagramas generados | 19 | 11 |
| Archivos de código generados | 2 | 4 |
| Estado general del pipeline | El reporte compartido muestra advertencias de validación | Pipeline validó la generación, pero permanecen errores en diagramas y advertencias de trazabilidad |

**Diferencia de volumen:** la segunda corrida produjo 8 diagramas menos y 2 archivos de código más que la primera. Esto describe la cantidad de artefactos, no demuestra por sí solo una mejora o regresión de calidad.

## 3. Primera corrida: evidencia y hallazgos

### Datos del reporte

- Especificación: `specs\\spec_v1.md`
- Origen: LLM Ollama / `qwen2.5:7b`
- Intentos al LLM: 1
- Duración de extracción: 63,7 segundos
- Revisión de la spec sin LLM: sin observaciones
- Requerimientos con elementos asociados: 27 de 34
- El reporte indica que todos los RF y RN tienen algún elemento asociado.

### Advertencias de validación

El reporte presenta advertencias de secuencia para **CU-01 a CU-16** porque el participante `Sistema` no está declarado como actor ni como entidad del modelo.

Además:

- La secuencia de CU-04 tiene menos de 2 mensajes.
- La secuencia de CU-05 tiene menos de 2 mensajes.

Estas advertencias indican que las secuencias generadas no cumplen correctamente con el modelo de participantes y que CU-04 y CU-05 tienen una interacción incompleta.

### Cobertura y trazabilidad

El reporte declara cobertura asociada para 27 de 34 requerimientos. Los 27 RF y RN aparecen asociados a elementos; sin embargo, los 7 RNF-01 a RNF-07 aparecen sin elementos, con la nota de que los RNF suelen no verse en diagramas y deben revisarse manualmente.

Por tanto, la cobertura declarada no equivale a cobertura verificada. La matriz debe revisarse requisito por requisito y marcarse como verificada solo cuando el artefacto realmente representa el comportamiento requerido.

### Observaciones del modelo JSON compartido

- Se declara un único actor, `Jugador`, y se le asignan los RF y RN completos, además de RN-01 a RN-11. Esto sobreasocia al actor con operaciones internas del sistema.
- En los casos de uso CU-03 a CU-16, las acciones que realiza internamente el sistema aparecen asociadas al actor `Jugador`.
- Los casos de uso están encadenados mediante `include` de forma lineal (por ejemplo, CU-02 incluye CU-01, CU-03 incluye CU-02, etc.). Debe revisarse si esas relaciones representan comportamiento reutilizado obligatorio o si se usaron solo para expresar orden del flujo.
- En las secuencias CU-01 a CU-16 se utiliza `Sistema`, pero no se declara como participante permitido por el modelo/validador.
- CU-04 y CU-05 tienen una sola interacción cada una.
- La entidad `Personaje` contiene solo `puntos_vida` y `atributo_ataque`; no se observa una entidad explícita para el combate ni para el resultado registrado.
- Los métodos de `Personaje` agrupan muchas responsabilidades: `iniciar_combate` reúne RF-02 a RF-05 y `realizar_accion` reúne RF-06 a RF-16. Esto dificulta representar separadamente las operaciones de ataque, defensa, daño y finalización.
- La relación de `Personaje` consigo mismo tiene multiplicidad 1 a 1. Debe comprobarse que el modelo represente exactamente dos personajes distintos por combate y no una asociación general insuficiente.

## 4. Segunda corrida: evidencia y hallazgos disponibles

La segunda corrida se generó con el **prompt corregido** y el modelo **Qwen2.5 7B**, en `salida/segunda_corrida/`, rama `bonus-pipeline`.

El pipeline validó la generación. No obstante, se reportó que todavía existen errores en los diagramas y advertencias de trazabilidad.

### Hallazgos observados en los artefactos compartidos

- CU-03 aparece tratado como un objetivo independiente, aunque la validación de participantes forma parte de la preparación/inicio del combate.
- CU-08 presenta relaciones `include` con CU-06 y CU-07 que fueron señaladas como incorrectas.
- Las clases/entidades `Combate`, `Resultado` y `Personaje` aparecen vacías en el material revisado.
- Hay secuencias con menos de 3 mensajes.
- No se encontró una secuencia de defensa en el material revisado.

Estos hallazgos son de la revisión del material compartido. Deben cotejarse con los archivos definitivos de `salida/segunda_corrida/` antes de marcarlos como defectos cerrados o corregidos.

### Cambios cuantitativos

- Diagramas: 19 → 11 (**8 menos**).
- Archivos de código: 2 → 4 (**2 más**).

La segunda corrida genera menos diagramas y más código. La reducción de diagramas no se debe interpretar automáticamente como mejor organización: debe verificarse que estén presentes todos los diagramas requeridos y que cada uno tenga contenido válido y trazable.

## 5. Comparación cualitativa

| Aspecto | Primera corrida | Segunda corrida |
|---|---|---|
| Participantes en secuencias | `Sistema` no reconocido en CU-01 a CU-16 | Persisten problemas de secuencias; revisar participantes y completitud en archivos finales |
| CU-04 / turno inicial | Menos de 2 mensajes | El prompt corregido pidió completar el turno inicial; la evidencia disponible no confirma que haya quedado correcto |
| CU-05 / alternancia | Menos de 2 mensajes | El prompt corregido pidió representar alternancia/ciclo; debe verificarse la secuencia final |
| Casos de uso | Actor Jugador asociado a operaciones internas; cadena lineal de `include` por revisar | CU-03 independiente; relaciones `include` de CU-08 señaladas como incorrectas |
| Modelo de clases/entidades | `Personaje` con pocos atributos y métodos demasiado agrupados; no se ven entidades explícitas de combate/resultado | `Combate`, `Resultado` y `Personaje` reportadas vacías en el material revisado |
| Defensa | CU-08 existe, pero la secuencia compartida es simplificada | Se reportó ausencia de secuencia de defensa |
| Trazabilidad | 27/34 con elementos asociados; RNF-01 a RNF-07 sin elementos | Se reportaron advertencias de trazabilidad; revisar matriz completa |
| Validación automática | Advertencias concretas del reporte | Pipeline validó, pero esa validación no eliminó defectos semánticos/diagramáticos |
| Cantidad de diagramas | 19 | 11 |
| Cantidad de código | 2 | 4 |

## 6. Qué mejoró y qué no puede afirmarse todavía

### Cambios observables

- Se modificó el prompt para pedir secuencias más completas, turno inicial y alternancia.
- El prompt corregido pidió clases relacionadas con combate y resultado, reglas de combate y trazabilidad RF/RN/RNF.
- La segunda corrida produjo más archivos de código y menos diagramas.
- La generación pasó la validación del pipeline, aunque todavía se detectaron problemas en la revisión de los artefactos.

### No se puede concluir todavía

- Que la segunda corrida sea globalmente mejor que la primera.
- Que todos los requerimientos estén correctamente cubiertos.
- Que la trazabilidad esté completa o verificada.
- Que las clases vacías o las relaciones de CU-08 estén corregidas.
- Que la ausencia de una secuencia de defensa sea aceptable.
- Que la reducción de 19 a 11 diagramas corresponda a eliminación de duplicados y no a pérdida de artefactos requeridos.

## 7. Verificaciones pendientes antes de cerrar la comparación

- [ ] Revisar el `reporte.md` completo de la segunda corrida y registrar advertencias exactas.
- [ ] Comparar `modelo.json` de ambas corridas.
- [ ] Comparar las matrices `trazabilidad_generada.csv` y verificar cada RF, RN y RNF contra la spec.
- [ ] Abrir los diagramas finales de casos de uso, clases/entidades, ER y secuencias.
- [ ] Confirmar que CU-03 está integrado correctamente con el inicio del combate.
- [ ] Corregir/verificar las relaciones `include` de CU-08.
- [ ] Verificar que `Personaje`, `Combate` y `Resultado` tengan atributos, operaciones y relaciones pertinentes.
- [ ] Confirmar una secuencia completa de ataque y una secuencia completa de defensa.
- [ ] Confirmar que CU-04 representa el turno inicial y CU-05 la alternancia hasta terminar el combate.
- [ ] Verificar que el combate tiene exactamente dos personajes distintos.
- [ ] Revisar que el daño mínimo, esquiva, vida en cero, finalización inmediata y registro único estén representados.
- [ ] Comprobar que la segunda corrida conserva todos los artefactos necesarios, aunque genere menos diagramas.
- [ ] Registrar en la matriz del equipo `sí`, `no` o `parcial`, con observaciones concretas.

## 8. Conclusión provisional

La segunda corrida representa una nueva generación con prompt corregido y un volumen distinto de artefactos: 11 diagramas y 4 archivos de código, frente a 19 diagramas y 2 archivos de código en la primera. Aunque el pipeline validó la segunda generación, la revisión encontró problemas semánticos y de trazabilidad que impiden considerarla finalizada.

La conclusión adecuada por ahora es **mejora del proceso de generación, pero calidad de los artefactos aún pendiente de verificación**. La comparación definitiva debe cerrarse después de revisar los archivos completos de ambas carpetas y actualizar la matriz de trazabilidad con evidencia.
