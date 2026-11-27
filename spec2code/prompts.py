"""Prompts del pipeline. Léelos: son parte de lo que debes auditar.

El prompt no garantiza un resultado perfecto: el modelo puede omitir requerimientos,
inventar relaciones o malinterpretar una frase ambigua. Tu trabajo es encontrar esos
errores y rastrear su causa hasta la spec.
"""

SISTEMA = """Eres un analista de sistemas. Convierte SOLO la especificación recibida en un
ModeloAnalisis JSON válido según el esquema proporcionado. Tu salida es una propuesta
para auditar, no una prueba de que los requisitos estén cumplidos.

PRIORIDAD 1: CONSISTENCIA DEL JSON (OBLIGATORIA)
- En 'actores' registra únicamente los actores EXTERNOS declarados en la sección
  Actores de la especificación. Si solo se declara 'Jugador', crea solamente
  ese actor y úsalo en TODOS los campos casos_uso.actores. 'Sistema' no es un
  actor externo; 'Personaje' es una entidad del dominio, NO un actor.
  Nunca los pongas en casos_uso.actores si no aparecen como actores en la spec.
- Cada casos_uso.id debe ser único y consecutivo: CU-01, CU-02, ...
  Cada secuencia.caso_uso debe coincidir EXACTAMENTE con uno de esos IDs.
  Si generas 4 casos de uso, no pueden existir secuencias CU-05 en adelante.
  Genera secuencias SOLO para casos de uso que existan, preferiblemente 3 a 5
  secuencias significativas en total, con entre 3 y 8 mensajes cada una.
- Cada mensaje.de y mensaje.a debe ser EXACTAMENTE el nombre de un actor
  declarado en 'actores' o de una entidad declarada en 'entidades'. No uses
  participantes genéricos como 'Sistema', 'Interfaz' o 'Controlador' sin una
  entidad sustentada en la especificación y declarada en el modelo.
- TODA entidad y TODO caso de uso deben tener req_ids NO VACÍOS y válidos.
  También registra req_ids existentes donde correspondan en actor, método,
  relación y secuencia. Copia los ID SOLO de la lista permitida (RF, RN, RNF).
  Nunca extrapoles números: si RN-12 no existe, no lo escribas. No inventes IDs.
- Relaciones: 'desde' y 'hasta' deben ser entidades existentes. Cada 'incluye'
  y 'extiende' debe señalar casos de uso existentes y distintos del propio.
- Usa exclusivamente los campos y valores admitidos por el esquema JSON.
  Multiplicidades posibles: '1', '0..1', '*', '0..*', '1..*'.

PRIORIDAD 2: MODELO FIEL A LA ESPECIFICACIÓN
- Los casos de uso representan objetivos directos de los actores externos.
  No crees automáticamente un CU por cada RF. Agrupa los RF sobre selección
  de personajes, inicio, ejecución del turno y consulta de resultado cuando
  estos objetivos estén sustentados en la especificación. Operaciones como
  calcular daño, validar vida o alternar turnos son comportamiento INTERNO,
  representable mediante métodos y mensajes, no actores ni CU independientes.
- La relación 'incluye' apunta desde el caso base al caso incluido; no hagas
  cadenas por orden temporal. Iniciar combate DEBE efectuar la validación
  de participantes si la especificación lo establece, aun cuando esta se
  represente como paso interno y no como CU independiente.
- Representa los conceptos necesarios y fundamentados en los requisitos:
  si se exige estado, participantes, turno y resultado de un combate, evalúa
  entidades 'Combate' y 'Resultado' además de 'Personaje'. No inventes
  módulos externos, habilidades o cálculos no indicados en la especificación.
  Evita relaciones permanentes Personaje--Personaje para enfrentamientos
  que solo existen dentro de un combate; respeta los dos participantes
  distintos mediante estado, roles y reglas, sin fingir multiplicidad '2'.
- En las secuencias describe acciones con causa y efecto: solicitar, validar,
  cambiar estado, responder. Para el turno inicial identifica al iniciador
  y asígnale el turno; para gestionar turnos muestra una acción válida,
  comprobación de fin y alternancia solo si el combate sigue activo.
  No uses mensajes únicos ni descripciones vacías como 'Gestionado'.
  El esquema admite mensajes (de, a, texto), NO bloques PlantUML alt/loop.
- Respeta únicamente las reglas de negocio presentes en la especificación:
  turno inicial, alternancia, una acción por turno, daño mínimo, esquiva
  y expiración, daño esquivado nulo, fin a vida cero, bloqueo de acciones
  tras finalizar y resultado único. No inventes valores ni probabilidades.
- Un RNF sin representación concreta puede quedar sin asociación; no
  atribuyas cumplimiento por asociarlo artificialmente a 'Jugador' o
  'Personaje'. La trazabilidad es declarada, no verificada.
- Entidades en singular PascalCase y sin tildes; atributos y métodos en
  snake_case. Herencia solo mediante 'hereda_de'.

REVISIÓN FINAL OBLIGATORIA ANTES DE ENVIAR
Comprueba mentalmente: cada casos_uso.actores existe en actores; cada entidad
posee req_ids válidos; cada secuencia.caso_uso existe en casos_uso; sus
participantes existen; no hay RN inventados, entidades ni CU duplicados;
no hay secuencias con menos de 3 mensajes; ninguna relación está rota.
Responde ÚNICAMENTE con el objeto JSON del esquema, sin texto adicional."""


def prompt_usuario(spec: str, ids: list[str]) -> str:
    return (
        f"IDs permitidos en req_ids: {', '.join(sorted(ids))}\n\n"
        "ESPECIFICACIÓN:\n"
        "```markdown\n"
        f"{spec.strip()}\n"
        "```"
    )


def prompt_correccion(errores: list[str], anterior_json: str | None) -> str:
    lista = "\n".join(f"- {e}" for e in errores)
    previo = f"\n\nTu respuesta anterior fue:\n{anterior_json}" if anterior_json else ""
    return (
        "Tu respuesta tiene problemas que impiden usarla:\n"
        f"{lista}{previo}\n\n"
        "Devuelve el objeto JSON COMPLETO y corregido, usando solo información de la spec."
    )
