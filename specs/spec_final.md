# Módulo: Arena de combate

**Equipo:** E3  
**Versión:** Especificación final para la corrida obligatoria  
**Base:** `spec_v1.md` y aclaraciones derivadas de la auditoría de la primera corrida.

## 1. Contexto y alcance

El módulo Arena de combate permite ejecutar un enfrentamiento individual (1 contra 1) entre dos personajes diferentes por turnos. El jugador selecciona a los participantes, solicita el inicio y selecciona una acción válida para el personaje que tiene el turno. El módulo valida los participantes, asigna y alterna turnos, resuelve ataques y defensas, actualiza la vida, finaliza el combate y registra y muestra un único resultado.

El módulo utiliza personajes existentes, con identificador, puntos de vida y atributo de ataque; no crea, edita ni administra personajes o sus clases. Tampoco gestiona inventario, equipamiento, misiones, progresión, ranking, cuentas, combates grupales, habilidades especiales, efectos adicionales ni recompensas.

**Responsabilidades internas:** El *Sistema de Arena* valida solicitudes y administra las acciones, el turno actual y el estado del combate; no es un actor externo. El concepto de *Combate* reúne exactamente dos participantes distintos, identifica al iniciador y al personaje con turno, conserva su estado (`EN_CURSO` o `FINALIZADO`) y se vincula con su resultado único al finalizar. *Personaje* representa a los participantes existentes y *Resultado* registra el combate, los participantes y el ganador. Una relación entre participantes se establece a través del combate específico; no implica una relación permanente entre dos personajes.

## 2. Actores

- **Jugador**: usuario externo que selecciona los dos personajes, solicita iniciar el combate, indica qué acción ejecuta el personaje con turno y consulta el resultado.

## 3. Requerimientos funcionales

- **RF-01** Seleccionar participantes: El sistema permitirá seleccionar exactamente dos personajes diferentes para realizar un combate.
  - Criterio de aceptación: dado que hay personajes disponibles, cuando el jugador selecciona dos identificadores distintos, entonces el sistema acepta la selección; si selecciona el mismo personaje dos veces, la rechaza.

- **RF-02** Iniciar combate: El sistema permitirá iniciar un combate entre los dos personajes seleccionados, siempre que sean válidos.
  - Criterio de aceptación: dado que la selección contiene dos participantes válidos, cuando el jugador confirma el inicio, entonces el sistema crea un combate con estado `EN_CURSO`.

- **RF-03** Validar participantes: Antes de iniciar el combate, el sistema comprobará que ambos personajes existan y tengan puntos de vida superiores a cero. Si alguno no existe, está repetido o tiene 0 puntos de vida, rechazará el inicio.
  - Criterio de aceptación: dado que al menos una condición de validez falla, cuando se solicita iniciar el combate, entonces no se crea el combate y se informa el rechazo.

- **RF-04** Establecer turno inicial: El sistema asignará el primer turno al personaje que inició el enfrentamiento. La identificación del personaje iniciador se recibe al iniciar el combate y se conserva durante el enfrentamiento.
  - Criterio de aceptación: dado que el combate válido va a comenzar, cuando se establece el estado inicial, entonces el turno actual corresponde al personaje que inició el enfrentamiento.

- **RF-05** Gestionar turnos: El sistema alternará los turnos entre los dos personajes después de cada acción válida, mientras el combate continúe. Una acción rechazada no consume el turno; si el combate finaliza tras la acción válida, no se asigna un turno posterior.
  - Criterio de aceptación: dado que una acción válida fue resuelta y ambos personajes tienen vida mayor que cero, cuando se habilita la siguiente acción, entonces el turno pasa al oponente.

- **RF-06** Seleccionar acción: Durante su turno, el participante podrá seleccionar una de las acciones disponibles: ataque o defensa (esquiva).
  - Criterio de aceptación: dado que el combate está `EN_CURSO` y el personaje tiene el turno, cuando selecciona ataque o defensa, entonces el sistema procesa esa acción; una acción distinta se rechaza.

- **RF-07** Ejecutar ataque: El sistema ejecutará el ataque del personaje que tenga el turno correspondiente contra su oponente.
  - Criterio de aceptación: dado que el personaje atacante tiene el turno y el combate está `EN_CURSO`, cuando solicita atacar, entonces el sistema resuelve el ataque contra el otro participante.

- **RF-08** Ejecutar defensa: El sistema permitirá activar una acción defensiva para esquivar el siguiente ataque del oponente durante el siguiente turno de este. La protección se consume si el oponente ataca durante ese turno y, si no ataca, expira al terminar dicho turno.
  - Criterio de aceptación: dado que el personaje elige defensa, cuando llega el siguiente turno del oponente, entonces el primer ataque de ese turno es esquivado; si no ataca en ese turno, la protección expira.

- **RF-09** Calcular daño: El sistema calculará el daño de un ataque usando el atributo de ataque del personaje atacante y respetando un daño mínimo de 1 punto.
  - Criterio de aceptación: dado que se ejecuta un ataque no esquivado, cuando se calcula el daño, entonces el valor aplicado es el atributo de ataque del atacante, pero nunca menor que 1.

- **RF-10** Aplicar daño: El sistema descontará los puntos de daño de la vida del personaje afectado, excepto cuando el ataque haya sido esquivado.
  - Criterio de aceptación: dado que un ataque no fue esquivado, cuando se aplica el daño, entonces la vida del objetivo disminuye en el daño calculado; si fue esquivado, no disminuye.

- **RF-11** Actualizar puntos de vida: Después de aplicar daño, el sistema actualizará los puntos de vida del personaje afectado y reflejará el nuevo valor. La vida no podrá quedar por debajo de cero.
  - Criterio de aceptación: dado que se aplica daño, cuando se actualiza la vida, entonces el valor nuevo es `máximo(0, vida anterior - daño)` y se refleja en el estado del combate.

- **RF-12** Verificar estado del combate: Después de resolver cada acción, el sistema comprobará si alguno de los personajes ha llegado a 0 puntos de vida.
  - Criterio de aceptación: dado que una acción terminó, cuando se verifica el estado, entonces el sistema detecta si algún participante tiene vida igual a cero.

- **RF-13** Finalizar combate: El sistema finalizará inmediatamente el combate cuando uno de los personajes llegue a 0 puntos de vida.
  - Criterio de aceptación: dado que un participante llega a 0 puntos de vida, cuando se verifica el estado, entonces el combate cambia a `FINALIZADO` y no acepta más acciones.

- **RF-14** Determinar ganador: El sistema identificará como ganador al personaje que conserve puntos de vida superiores a 0 cuando su oponente llegue a 0.
  - Criterio de aceptación: dado que un personaje llega a 0 puntos de vida, cuando se determina el resultado, entonces el otro participante con vida mayor que cero queda registrado como ganador.

- **RF-15** Registrar resultado: El sistema almacenará un único resultado por combate finalizado, incluyendo el identificador del combate, sus participantes y el ganador. Un intento repetido de registro del mismo combate no crea un segundo resultado.
  - Criterio de aceptación: dado que el combate finalizó, cuando se registra el resultado, entonces existe exactamente un registro asociado a ese combate con ambos participantes y el ganador.

- **RF-16** Mostrar resultado: El sistema presentará el resultado final del combate y los datos de los personajes participantes.
  - Criterio de aceptación: dado que el combate finalizó y el resultado fue registrado, cuando el jugador consulta el resultado, entonces se muestran los participantes y el ganador.

## 4. Requerimientos no funcionales

- **RNF-01** Rendimiento: Cada acción de combate deberá procesarse en un máximo de 2 segundos en condiciones normales. Métrica de verificación: medir el tiempo desde la solicitud de acción hasta la respuesta; el tiempo debe ser ≤ 2 s en una prueba de 100 acciones.

- **RNF-02** Integridad de datos: Después de cada acción, el sistema mantendrá coherentes los puntos de vida, el turno actual y el estado del combate. Métrica de verificación: ejecutar 100 acciones válidas e inválidas en pruebas y comprobar que el 100 % de los estados cumplen las reglas de vida ≥ 0, turnos válidos y estado consistente.

- **RNF-03** Confiabilidad: El sistema finalizará correctamente todos los combates en los que un personaje alcance 0 puntos de vida. Métrica de verificación: en 100 combates de prueba que terminen con un participante en 0 PV, el 100 % debe quedar `FINALIZADO` y con ganador correcto.

- **RNF-04** Usabilidad: El sistema deberá mostrar mensajes que identifiquen las acciones disponibles, las causas de rechazo y el resultado final. Métrica de verificación: en 10 escenarios de prueba, el mensaje correspondiente deberá mostrarse en 10/10 casos y describir la acción o causa del rechazo.

- **RNF-05** Validación: El sistema rechazará todas las acciones realizadas fuera del turno correspondiente o después de que el combate haya finalizado. Métrica de verificación: probar al menos 20 acciones fuera de turno y 20 acciones posteriores al final; el 100 % debe rechazarse sin modificar el estado.

- **RNF-06** Mantenibilidad: Las operaciones de ataque, defensa, cálculo de daño y finalización del combate deberán estar separadas en métodos independientes. Métrica de verificación: inspección del esqueleto/código generado; deben identificarse al menos 4 operaciones separadas, una por responsabilidad.

- **RNF-07** Consistencia: Cada resultado registrado deberá coincidir con los participantes y el estado final del combate. Métrica de verificación: comparar 100 resultados registrados con el estado final correspondiente; coincidencia del 100 % en participantes y ganador.

## 5. Reglas de negocio

- **RN-01** Orden de turnos: los turnos se alternan entre los dos participantes después de cada acción válida, si el combate continúa.

- **RN-02** Daño mínimo: todo ataque no esquivado produce al menos 1 punto de daño.

- **RN-03** Vida en cero: un personaje con 0 puntos de vida no puede iniciar ni participar en un combate.

- **RN-04** Combate individual: cada combate tiene exactamente dos personajes diferentes.

- **RN-05** Primer turno: el personaje que inicia el enfrentamiento tiene el primer turno.

- **RN-06** Acción por turno: Cada personaje ejecuta como máximo una acción válida por turno; las acciones rechazadas no consumen el turno.

- **RN-07** Funcionamiento del ataque: el daño es igual al atributo de ataque del personaje atacante, con mínimo de 1.

- **RN-08** Funcionamiento de la defensa: La defensa esquiva el siguiente ataque del oponente si ocurre durante el siguiente turno de este. Si el oponente no ataca durante dicho turno, la protección expira al terminarlo.

- **RN-09** Ataque esquivado: un ataque esquivado no descuenta puntos de vida.

- **RN-10** Finalización inmediata: Al llegar un personaje a 0 puntos de vida, el combate pasa a `FINALIZADO` inmediatamente; no se asignan más turnos ni se permiten nuevas acciones.

- **RN-11** Registro único: cada combate finalizado genera un único registro de resultado.

## 6. Supuestos y glosario

**Supuestos**

- Los personajes ya existen y el módulo puede consultar sus datos necesarios.
- Cada personaje dispone de puntos de vida y atributo de ataque.
- Los valores de vida y ataque están disponibles al iniciar el combate.
- El módulo recibe la identificación del personaje que inicia el enfrentamiento.
- El resultado puede almacenar los participantes y el ganador.

**Glosario**

- **Combate:** enfrentamiento entre dos personajes.
- **Participante:** personaje que forma parte del combate.
- **Turno:** oportunidad de un participante para ejecutar una acción.
- **Ataque:** acción que intenta reducir los puntos de vida del oponente.
- **Defensa/esquiva:** acción que evita el siguiente ataque del oponente durante el turno indicado.
- **Puntos de vida (PV):** valor que representa la vida restante.
- **Daño:** cantidad de puntos de vida descontados por un ataque no esquivado.
- **Ganador:** participante que conserva más de 0 PV cuando el oponente llega a 0.
- **Resultado:** información final registrada y mostrada al terminar el combate.

- **Sistema de Arena**: conjunto de responsabilidades internas que valida, ejecuta y registra las operaciones del módulo; no constituye un actor externo.
- **Estado del combate**: `EN_CURSO` mientras admite acciones y `FINALIZADO` cuando se determina el ganador y se cierra el enfrentamiento.

**Decisiones ya acordadas para esta versión:** el primer turno corresponde al personaje iniciador; los turnos se alternan después de cada acción válida; el daño no esquivado es `max(1, atributo_ataque)`; una defensa solo protege durante el siguiente turno del oponente; la vida no desciende de cero y se conserva un único resultado por combate finalizado.
