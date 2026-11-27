# Módulo: Arena de combate

**Equipo:** E3\
**Versión:** 2.0 --- revisión posterior a la segunda corrida\
**Base:** `specs/spec_v1.md`\
**Propósito de esta versión:** precisar reglas y criterios de aceptación
que puedan interpretarse de forma ambigua durante la generación del
ModeloAnalisis. Se conservan los identificadores RF, RN y RNF de la
versión 1.

## 1. Contexto y alcance

El módulo permite que dos personajes diferentes se enfrenten en un
combate individual 1 contra 1 por turnos. Durante el combate, cada
participante ejecuta una acción de ataque o defensa (esquiva), puede
recibir daño y perder puntos de vida. El sistema controla los turnos, el
estado del combate, determina el ganador y registra y muestra un único
resultado al finalizar.

El módulo permite: - seleccionar dos personajes diferentes; - validar
que ambos tengan puntos de vida mayores que cero; - iniciar el combate e
identificar cuál de los dos personajes inicia; - asignar el turno
inicial al personaje iniciador; - alternar turnos después de cada acción
válida mientras el combate permanezca activo; - ejecutar ataque o
defensa (esquiva); - calcular y aplicar daño, actualizar puntos de vida
y comprobar el fin del combate; - determinar y registrar al ganador; -
mostrar el resultado final.

Quedan fuera de alcance: administración de personajes y clases,
inventario, equipamiento, misiones, progresión de niveles, ranking,
cuentas de usuario, combates grupales, habilidades especiales y
recompensas por victoria. El módulo consulta los datos mínimos de los
personajes y no administra otros módulos.

## 2. Actor externo

-   **Jugador:** persona que selecciona los dos personajes, indica cuál
    de ellos inicia el combate, solicita iniciar el enfrentamiento y
    elige la acción del personaje que tiene el turno.

**Regla de modelado:** `Jugador` es el único actor externo declarado en
esta especificación. `Personaje`, `Combate` y `Resultado` son conceptos
del dominio, no actores. `Sistema`, `Interfaz` y `Controlador` son
términos de implementación y no deben declararse como actores externos.

## 3. Entidades y conceptos del dominio

Estos conceptos se incluyen para representar el estado y las reglas del
combate. No son actores.

### 3.1 Personaje

Representa a un personaje existente cuyos datos consulta el módulo.

Datos mínimos usados: - identificador del personaje; - nombre o dato
necesario para mostrarlo; - puntos de vida actuales; - atributo de
ataque.

El módulo no administra la creación ni la edición de personajes.

### 3.2 Combate

Representa un enfrentamiento individual entre exactamente dos personajes
distintos.

Debe permitir representar, como mínimo: - identificador del combate; -
los dos participantes y sus roles dentro de ese combate; - personaje
iniciador; - personaje cuyo turno está activo; - estado del combate
(activo o finalizado); - estado de defensa pendiente de cada
participante, cuando exista.

Los dos participantes son roles o referencias dentro de un combate. No
se establece una relación permanente de enfrentamiento entre personajes
fuera del combate.

### 3.3 Resultado

Representa el resultado único de un combate finalizado.

Debe incluir: - referencia al combate; - sus dos participantes; -
ganador; - datos finales necesarios para mostrar el resultado.

Un combate finalizado genera como máximo un resultado registrado.

## 4. Requerimientos funcionales

### RF-01 --- Seleccionar participantes

El sistema permitirá al Jugador seleccionar dos personajes diferentes
para realizar un combate.

**Criterio de aceptación:** dado que existen personajes disponibles,
cuando el Jugador selecciona dos identificadores distintos, el sistema
acepta la selección. Si selecciona el mismo personaje dos veces, la
selección se rechaza.

### RF-02 --- Iniciar combate

El sistema permitirá al Jugador iniciar un combate con los dos
personajes seleccionados, siempre que la selección y ambos participantes
sean válidos.

**Criterio de aceptación:** dado que hay dos participantes distintos y
válidos, cuando el Jugador solicita iniciar el combate, el sistema crea
un Combate en estado activo.

### RF-03 --- Validar participantes

Antes de iniciar el combate, el sistema comprobará que los puntos de
vida actuales de ambos personajes sean mayores que cero. Si alguno tiene
0 puntos de vida, rechazará el inicio.

**Criterio de aceptación:** si al menos uno de los participantes tiene 0
puntos de vida, al solicitar el inicio el sistema no crea un combate
activo y comunica el rechazo.

### RF-04 --- Establecer turno inicial

Al iniciar el combate, el Jugador identifica cuál de los dos personajes
seleccionados es el personaje iniciador. El sistema asigna el primer
turno a ese personaje.

**Criterio de aceptación:** dado un combate válido y un personaje
iniciador que pertenece a sus participantes, al iniciar el combate el
turno activo queda asignado a ese personaje. El término "personaje
iniciador" no se refiere al actor Jugador.

### RF-05 --- Gestionar turnos

El sistema alternará el turno entre los dos participantes después de
cada acción válida, únicamente si el combate continúa activo.

**Criterio de aceptación:** después de una acción válida que no finaliza
el combate, el turno activo cambia al otro participante. Si la acción
finaliza el combate, no se asigna otro turno.

### RF-06 --- Seleccionar acción

Durante su turno, el Jugador podrá seleccionar una de estas acciones
para el personaje que tiene el turno: ataque o defensa (esquiva).

**Criterio de aceptación:** si el combate está activo y el personaje
seleccionado tiene el turno, el sistema procesa la acción elegida. No se
procesa una acción de un participante que no tenga el turno.

### RF-07 --- Ejecutar ataque

El sistema ejecutará el ataque del personaje cuyo turno está activo
contra el otro participante del mismo combate.

**Criterio de aceptación:** cuando el Jugador selecciona ataque durante
un turno válido, el sistema identifica al atacante como el participante
con el turno y al objetivo como el otro participante.

### RF-08 --- Ejecutar defensa

El sistema permitirá que el participante cuyo turno está activo
seleccione defensa para esquivar el siguiente ataque del oponente
durante el turno inmediatamente siguiente de ese oponente.

La defensa es temporal: - se activa al ejecutar una acción de defensa
válida; - protege contra el siguiente ataque del oponente durante el
turno inmediatamente siguiente de este; - si el oponente ataca en ese
turno, el ataque se esquiva y la protección se consume; - si el oponente
no ataca durante ese turno, la protección expira al terminar dicho
turno; - la protección no se acumula ni permanece para turnos
posteriores.

**Criterio de aceptación:** después de una defensa válida, si el
oponente ataca en su siguiente turno, el sistema marca el ataque como
esquivado y consume la protección. Si el oponente realiza otra acción,
la protección expira al finalizar ese turno.

### RF-09 --- Calcular daño

El sistema calculará el daño de un ataque usando el atributo de ataque
del atacante. El daño aplicado será el atributo de ataque si es mayor
que 1; en caso contrario, será 1.

**Criterio de aceptación:** para un ataque no esquivado, el daño
calculado equivale a `max(1, atributo_ataque)`.

### RF-10 --- Aplicar daño

El sistema descontará el daño calculado de los puntos de vida del
objetivo, excepto cuando el ataque haya sido esquivado.

**Criterio de aceptación:** si el ataque no fue esquivado, el sistema
reduce los puntos de vida del objetivo por el daño calculado. Si fue
esquivado, no reduce sus puntos de vida.

### RF-11 --- Actualizar puntos de vida

Después de aplicar daño, el sistema actualizará y reflejará los puntos
de vida actuales del personaje afectado.

**Criterio de aceptación:** después de un ataque no esquivado, los
puntos de vida reflejados corresponden a los puntos de vida anteriores
menos el daño aplicado, sin quedar por debajo de 0.

### RF-12 --- Verificar estado del combate

Después de cada acción válida, el sistema comprobará si alguno de los
participantes tiene 0 puntos de vida.

**Criterio de aceptación:** tras procesar la acción, el sistema verifica
los puntos de vida de ambos participantes antes de decidir si cambia el
turno.

### RF-13 --- Finalizar combate

El sistema finalizará inmediatamente el combate cuando uno de los
personajes llegue a 0 puntos de vida.

**Criterio de aceptación:** cuando un participante llega a 0 puntos de
vida, el estado del combate cambia a finalizado y no se habilitan nuevas
acciones.

### RF-14 --- Determinar ganador

Cuando un participante llega a 0 puntos de vida, el sistema identificará
como ganador al otro participante, siempre que conserve puntos de vida
mayores que 0.

**Criterio de aceptación:** al finalizar el combate por vida en 0, el
ganador registrado es el participante que conserva puntos de vida
mayores que 0.

### RF-15 --- Registrar resultado

El sistema almacenará un único resultado por combate finalizado,
incluyendo la referencia al combate, sus dos participantes y el ganador.

**Criterio de aceptación:** al finalizar un combate se registra un
resultado. Una segunda solicitud de finalización o registro para el
mismo combate no crea un resultado duplicado.

### RF-16 --- Mostrar resultado

El sistema presentará el resultado final del combate y los datos de los
dos personajes participantes, incluido el ganador.

**Criterio de aceptación:** después de finalizar el combate, el Jugador
puede consultar el resultado registrado y los datos finales requeridos.

## 5. Requerimientos no funcionales

### RNF-01 --- Rendimiento

El sistema procesará cada acción del combate en un máximo de 2 segundos
en condiciones normales.

**Verificación:** medir el tiempo de procesamiento de las acciones en
condiciones normales de prueba.

### RNF-02 --- Integridad de datos

En una batería de 100 acciones de prueba, los puntos de vida, el turno
actual y el estado del combate deberán coincidir con los valores
esperados en el 100 % de los casos.

**Verificación:** comparar los valores obtenidos con los resultados
esperados de cada caso de prueba.

### RNF-03 --- Confiabilidad

El sistema finalizará correctamente el 100 % de los combates en los que
un personaje alcance 0 puntos de vida.

**Verificación:** ejecutar casos de combate que lleven a un participante
a 0 puntos de vida y comprobar el estado final.

### RNF-04 --- Usabilidad

En una batería de 20 escenarios de interacción, el sistema deberá
mostrar correctamente las acciones disponibles durante el combate y el
resultado al finalizarlo en el 100 % de los escenarios aplicables.

**Verificación:** comprobar las opciones mostradas durante turnos
válidos y la presentación del resultado al finalizar.

### RNF-05 --- Validación

El sistema rechazará el 100 % de las acciones realizadas fuera del turno
correspondiente o después de que el combate haya finalizado.

**Verificación:** probar acciones de participantes sin turno y acciones
posteriores a la finalización.

### RNF-06 --- Mantenibilidad

Las operaciones de ataque, defensa, cálculo de daño y finalización del
combate estarán separadas en al menos 4 métodos independientes, uno por
operación.

**Verificación:** revisar el diseño e identificar los cuatro métodos
independientes.

### RNF-07 --- Consistencia

En una batería de 100 combates finalizados de prueba, el resultado
registrado deberá coincidir con los participantes y el estado final en
el 100 % de los casos.

**Verificación:** comparar cada resultado registrado con los datos
finales del combate correspondiente.

## 6. Reglas de negocio

-   **RN-01 --- Orden de turnos:** los dos personajes participan
    siguiendo un orden de turnos alternado.
-   **RN-02 --- Daño mínimo:** todo ataque no esquivado que produzca
    daño aplica como mínimo 1 punto.
-   **RN-03 --- Vida en cero:** un personaje con 0 puntos de vida no
    puede iniciar ni participar en un combate.
-   **RN-04 --- Combate individual:** cada combate tiene exactamente dos
    personajes diferentes.
-   **RN-05 --- Primer turno:** el personaje iniciador recibe el primer
    turno.
-   **RN-06 --- Acción por turno:** cada personaje ejecuta como máximo
    una acción válida por turno.
-   **RN-07 --- Funcionamiento del ataque:** el daño es igual al
    atributo de ataque, con mínimo de 1 punto.
-   **RN-08 --- Funcionamiento de la defensa:** la defensa permite
    esquivar el siguiente ataque del oponente durante su turno
    inmediatamente siguiente.
-   **RN-09 --- Ataque esquivado:** un ataque esquivado no descuenta
    puntos de vida.
-   **RN-10 --- Finalización inmediata:** cuando un personaje alcanza 0
    puntos de vida, el combate finaliza y no se permiten nuevas
    acciones.
-   **RN-11 --- Registro único:** cada combate finalizado genera como
    máximo un registro de resultado.

## 7. Supuestos

-   Los personajes existen previamente y el módulo puede consultar sus
    datos.
-   Cada personaje dispone de puntos de vida actuales y atributo de
    ataque.
-   Los valores de vida y ataque están disponibles al iniciar el
    combate.
-   El módulo recibe la identificación del personaje iniciador, que debe
    ser uno de los dos participantes seleccionados.
-   El sistema puede almacenar la referencia al combate, sus
    participantes y el ganador en el resultado.
-   El Jugador es el único actor externo del módulo.
-   La defensa tiene una duración limitada al siguiente turno del
    oponente, según RF-08 y RN-08.

## 8. Glosario

-   **Combate:** enfrentamiento entre dos personajes diferentes.
-   **Participante:** personaje que forma parte de un combate.
-   **Personaje iniciador:** participante al que se asigna el primer
    turno.
-   **Turno:** oportunidad de un participante para ejecutar una acción.
-   **Ataque:** acción que intenta reducir los puntos de vida del
    oponente.
-   **Defensa / esquiva:** acción que evita el siguiente ataque del
    oponente durante el turno indicado.
-   **Puntos de vida:** valor que representa la vida restante de un
    personaje.
-   **Daño:** cantidad de puntos de vida descontados por un ataque no
    esquivado.
-   **Ganador:** participante que conserva más de 0 puntos de vida
    cuando el oponente llega a 0.
-   **Resultado:** información final registrada y mostrada al terminar
    el combate.

## 9. Guía de trazabilidad para el modelo

La asociación de requisitos con elementos del modelo es una declaración
del modelo y debe ser revisada por el equipo; no constituye por sí misma
una verificación de cumplimiento.

-   Actor externo permitido: `Jugador`.
-   Entidades de dominio esperadas: `Personaje`, `Combate`, `Resultado`.
-   `Personaje1` y `Personaje2` no son actores; son roles/referencias a
    dos instancias distintas de `Personaje` dentro de `Combate`.
-   `Sistema`, `Interfaz` y `Controlador` no deben aparecer como actores
    ni como participantes de secuencia, salvo que se incorporen
    expresamente como entidades al esquema y estén sustentados por la
    especificación. Para este módulo no se incorporan.
-   Las secuencias deben referenciar únicamente IDs de casos de uso que
    existan en el modelo.
-   Las entidades y casos de uso deben asociarse con IDs existentes de
    RF/RN/RNF que realmente los sustenten.
-   Los RNF se verifican principalmente mediante pruebas, mediciones o
    revisión de diseño; no se debe declarar cobertura de un RNF solo por
    asociarlo a `Jugador` o `Personaje`.
-   Los casos de uso representan objetivos del Jugador. Validar vida,
    calcular daño, alternar turnos, aplicar daño y finalizar el combate
    son pasos internos, no casos de uso independientes por defecto.

## 10. Cambios respecto a la versión 1

-   Se aclaró que el personaje iniciador es un participante del combate,
    no el actor Jugador.
-   Se explicitó que `Jugador` es el único actor externo.
-   Se precisó el estado y los datos mínimos que deben representarse en
    `Combate` y `Resultado`.
-   Se detalló la duración y expiración de la defensa para evitar
    interpretaciones distintas.
-   Se aclaró que la vida no debe quedar por debajo de 0 al aplicar
    daño.
-   Se reforzó la regla de resultado único para evitar registros
    duplicados.
-   Se añadieron criterios de aceptación más verificables para
    selección, inicio, turno inicial, defensa, daño, finalización y
    registro.
-   Se incorporó una guía de trazabilidad para distinguir cobertura
    declarada de cobertura verificada.
