# Módulo: Arena de combate

**Equipo:** E3  
**Versión:** 1.0 inicial

## 1. Contexto y alcance

Permitir que dos personajes se enfrenten en un combate 1 contra 1 por turnos. Durante el combate, cada participante podrá realizar acciones de ataque o defensa (esquiva), recibir daño, perder puntos de vida y contribuir a determinar el ganador. El sistema registrará y mostrará el resultado final.

El módulo permite seleccionar dos personajes diferentes, verificar que tienen puntos de vida superiores a 0, iniciar un combate 1 contra 1, alternar turnos, ejecutar ataque o defensa (esquiva), calcular y aplicar daño, actualizar la vida, determinar el ganador y registrar y mostrar un único resultado por combate finalizado.

Quedan fuera de alcance la administración de personajes y sus clases, el inventario, el equipamiento, las misiones, la progresión de niveles, el ranking, las cuentas de usuario, los combates grupales, las habilidades especiales y las recompensas por victoria. Se utilizan los datos mínimos de los personajes, sin administrar otros módulos.

## 2. Actores

- **Jugador**: usuario que selecciona a los dos personajes, solicita el inicio del combate y selecciona la acción disponible para el personaje que tiene el turno.

## 3. Requerimientos funcionales

- **RF-01** Seleccionar participantes: El sistema permitirá seleccionar dos personajes diferentes para realizar un combate.
  - Criterio de aceptación: Dado que existen personajes disponibles, cuando el jugador selecciona dos personajes diferentes, el sistema deberá aceptar la selección.

- **RF-02** Iniciar combate: El sistema permitirá iniciar un combate entre los dos personajes seleccionados, siempre que sean válidos.
  - Criterio de aceptación: Dado que hay dos participantes válidos, cuando se solicita iniciar el combate, el sistema deberá crear el enfrentamiento.

- **RF-03** Validar participantes: Antes de iniciar el combate, el sistema comprobará que ambos personajes tengan puntos de vida superiores a cero. Si alguno tiene 0 puntos de vida, rechazará el inicio.
  - Criterio de aceptación: Dado que uno de los personajes tiene 0 puntos de vida, cuando se intenta iniciar el combate, el sistema deberá rechazarlo.

- **RF-04** Establecer turno inicial: El sistema asignará el primer turno al personaje que inició el enfrentamiento.
  - Criterio de aceptación: Dado que el combate ha iniciado, el sistema deberá asignar el primer turno al personaje que inició el enfrentamiento.

- **RF-05** Gestionar turnos: El sistema alternará los turnos entre los dos personajes después de cada acción válida, mientras el combate continúe.
  - Criterio de aceptación: Dado que un personaje termina su acción válida, el sistema deberá asignar el siguiente turno al oponente, si el combate continúa.

- **RF-06** Seleccionar acción: Durante su turno, el participante podrá seleccionar una de las acciones disponibles: ataque o defensa (esquiva).
  - Criterio de aceptación: Dado que un personaje tiene el turno, cuando selecciona ataque o defensa, el sistema deberá procesar la acción seleccionada.

- **RF-07** Ejecutar ataque: El sistema ejecutará el ataque del personaje que tenga el turno correspondiente contra su oponente.
  - Criterio de aceptación: Dado que un personaje tiene el turno, cuando selecciona atacar, el sistema deberá ejecutar el ataque contra su oponente.

- **RF-08** Ejecutar defensa: El sistema permitirá activar una acción defensiva para esquivar el siguiente ataque del oponente durante el siguiente turno de este.
  - Criterio de aceptación: Dado que un personaje selecciona defensa, el sistema deberá activar la protección para el siguiente ataque del oponente durante el siguiente turno de este.

- **RF-09** Calcular daño: El sistema calculará el daño de un ataque usando el atributo de ataque del personaje atacante y respetando un daño mínimo de 1 punto.
  - Criterio de aceptación: Dado que se ejecuta un ataque, el sistema deberá calcular un daño igual al atributo de ataque, respetando el mínimo de 1 punto.

- **RF-10** Aplicar daño: El sistema descontará los puntos de daño de la vida del personaje afectado, excepto cuando el ataque haya sido esquivado.
  - Criterio de aceptación: Dado que un personaje recibe un ataque que no ha esquivado, el sistema deberá descontar el daño correspondiente de sus puntos de vida.

- **RF-11** Actualizar puntos de vida: Después de aplicar daño, el sistema actualizará los puntos de vida del personaje afectado y reflejará el nuevo valor.
  - Criterio de aceptación: Dado que un personaje recibe daño, el sistema deberá actualizar sus puntos de vida y reflejar el nuevo valor.

- **RF-12** Verificar estado del combate: Después de cada acción, el sistema comprobará si alguno de los personajes ha llegado a 0 puntos de vida.
  - Criterio de aceptación: Dado que se ejecuta una acción, el sistema deberá comprobar si alguno de los participantes tiene 0 puntos de vida.

- **RF-13** Finalizar combate: El sistema finalizará inmediatamente el combate cuando uno de los personajes llegue a 0 puntos de vida.
  - Criterio de aceptación: Dado que uno de los personajes llega a 0 puntos de vida, el sistema deberá finalizar inmediatamente el combate.

- **RF-14** Determinar ganador: El sistema identificará como ganador al personaje que conserve puntos de vida superiores a 0 cuando su oponente llegue a 0.
  - Criterio de aceptación: Dado que un personaje llega a 0 puntos de vida, el sistema deberá identificar al otro personaje como ganador.

- **RF-15** Registrar resultado: El sistema almacenará un único resultado por combate finalizado, incluyendo el combate, sus participantes y el ganador.
  - Criterio de aceptación: Dado que un combate ha finalizado, el sistema deberá almacenar un único registro con sus participantes y ganador.

- **RF-16** Mostrar resultado: El sistema presentará el resultado final del combate y los datos de los personajes participantes.
  - Criterio de aceptación: Dado que el combate ha finalizado, el sistema deberá mostrar el resultado y el ganador del enfrentamiento.

## 4. Requerimientos no funcionales

- **RNF-01** Rendimiento: El sistema deberá procesar cada acción del combate en un máximo de 2 segundos en condiciones normales.

- **RNF-02** Integridad de datos: En una batería de 100 acciones de prueba, los puntos de vida, el turno actual y el estado del combate deberán coincidir con los valores esperados en el 100 % de los casos.

- **RNF-03** Confiabilidad: El sistema deberá finalizar correctamente el 100 % de los combates en los que un personaje alcance 0 puntos de vida.

- **RNF-04** Usabilidad: En una batería de 20 escenarios de interacción, el sistema deberá mostrar correctamente las acciones disponibles durante el combate y el resultado al finalizarlo en el 100 % de los escenarios aplicables.

- **RNF-05** Validación: El sistema deberá rechazar el 100 % de las acciones realizadas fuera del turno correspondiente o después de que el combate haya finalizado.

- **RNF-06** Mantenibilidad: Las operaciones de ataque, defensa, cálculo de daño y finalización del combate deberán estar separadas en al menos 4 métodos independientes, uno por operación.

- **RNF-07** Consistencia: En una batería de 100 combates finalizados de prueba, el resultado registrado deberá coincidir con los participantes y el estado final en el 100 % de los casos.

## 5. Reglas de negocio

- **RN-01** Orden de turnos: Los personajes deberán participar siguiendo un orden de turnos establecido y alternado.

- **RN-02** Daño mínimo: Todo ataque que produzca daño deberá respetar un valor mínimo de 1 punto.

- **RN-03** Vida en cero: Un personaje con 0 puntos de vida no podrá iniciar ni participar en un combate.

- **RN-04** Combate individual: Cada enfrentamiento deberá contar exactamente con dos personajes diferentes.

- **RN-05** Primer turno: El personaje que inicia el enfrentamiento tendrá el primer turno.

- **RN-06** Acción por turno: Cada personaje podrá ejecutar solamente una acción por turno.

- **RN-07** Funcionamiento del ataque: El daño de un ataque será igual al atributo de ataque del personaje atacante, con un mínimo de 1 punto.

- **RN-08** Funcionamiento de la defensa: La acción de defensa permitirá esquivar el siguiente ataque del oponente durante el siguiente turno de este.

- **RN-09** Ataque esquivado: Cuando un ataque sea esquivado, no se descontarán puntos de vida al personaje defensor.

- **RN-10** Finalización inmediata: Cuando un personaje alcance 0 puntos de vida, el combate finalizará y no se permitirán nuevas acciones.

- **RN-11** Registro único: Cada combate finalizado deberá generar un único registro de resultado.

La protección de la defensa dura solo durante el siguiente turno del oponente. Si el oponente no ataca en ese turno, la protección desaparece.

## 6. Supuestos y glosario

**Supuestos**

- Los personajes ya existen y el módulo puede consultar sus datos necesarios.
- Cada personaje dispone de un valor de puntos de vida y un atributo de ataque.
- Los valores de vida y ataque se encuentran disponibles al iniciar el combate.
- El módulo recibe la identificación del personaje que inicia el enfrentamiento.
- El registro de resultados puede almacenar los participantes y el ganador.

**Glosario**

- **Combate:** enfrentamiento entre dos personajes.
- **Participante:** personaje que forma parte del combate.
- **Turno:** oportunidad de un participante para ejecutar una acción.
- **Ataque:** acción que intenta reducir los puntos de vida del oponente.
- **Defensa / esquiva:** acción que evita el siguiente ataque del oponente durante el turno indicado.
- **Puntos de vida:** valor que representa la vida restante de un personaje.
- **Daño:** cantidad de puntos de vida que se descuentan por un ataque no esquivado.
- **Ganador:** participante que conserva más de 0 puntos de vida cuando el oponente llega a 0.
- **Resultado:** información final registrada y mostrada al terminar el combate.
