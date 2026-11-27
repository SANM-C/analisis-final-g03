# Reporte de la corrida

- Fecha: 2026-11-26 21:20
- Spec: `specs\spec_v1.md`
- Origen del modelo: LLM ollama / qwen2.5:7b
- Intentos al LLM: 2
- Duración de la extracción: 59.7 s

## Revisión de la spec (sin LLM)

- Sin observaciones.

## Validación del modelo generado

Intento 1 fallido:
  - CU-02 usa el actor 'Personaje1', que no está en 'actores'.
  - CU-02 usa el actor 'Personaje2', que no está en 'actores'.
  - CU-03 usa el actor 'Personaje1', que no está en 'actores'.
  - CU-03 usa el actor 'Personaje2', que no está en 'actores'.
  - CU-04 usa el actor 'Personaje1', que no está en 'actores'.
  - CU-04 usa el actor 'Personaje2', que no está en 'actores'.
  - CU-05 usa el actor 'Personaje1', que no está en 'actores'.
  - CU-05 usa el actor 'Personaje2', que no está en 'actores'.
  - CU-06 usa el actor 'Personaje1', que no está en 'actores'.
  - CU-06 usa el actor 'Personaje2', que no está en 'actores'.
  - CU-07 usa el actor 'Personaje1', que no está en 'actores'.
  - CU-07 usa el actor 'Personaje2', que no está en 'actores'.
  - CU-08 usa el actor 'Personaje1', que no está en 'actores'.
  - CU-08 usa el actor 'Personaje2', que no está en 'actores'.
  - Entidad Combate no indica req_ids (trazabilidad).
  - Entidad Resultado no indica req_ids (trazabilidad).
  - Entidad Personaje no indica req_ids (trazabilidad).
- ⚠️ Secuencia CU-01: 'Sistema' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-01: 'Sistema' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-02: 'Sistema' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-02: 'Sistema' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-03: 'Sistema' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-03: 'Sistema' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-04: 'Sistema' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-04: 'Sistema' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-05: 'Sistema' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-05: 'Sistema' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-06: 'Sistema' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-06: 'Personaje2' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-06: 'Personaje2' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-06: 'Sistema' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-06: 'Sistema' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-07: 'Sistema' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-07: 'Sistema' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-08: 'Sistema' no es actor ni entidad del modelo.
- ⚠️ Secuencia CU-08: 'Sistema' no es actor ni entidad del modelo.

## Cobertura declarada por el modelo

- Requerimientos con elementos asociados: 27 de 34
- Todos los RF y RN tienen algún elemento asociado.

> Que el modelo *declare* cubrir un requerimiento no significa que lo cubra bien.
> Verifica cada fila de `trazabilidad_generada.csv` contra la spec y los diagramas.
