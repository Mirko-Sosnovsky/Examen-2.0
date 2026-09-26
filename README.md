# Examen práctico — Terminal de Expedición Espacial

Van a desarrollar un programa en Python que simule una terminal de navegación espacial.

El programa deberá comenzar pidiendo el nombre del piloto. La nave arranca con **100 unidades de combustible**.

Los destinos disponibles serán:

```text
1. Luna      - 20 unidades
2. Marte     - 35 unidades
3. Saturno   - 50 unidades
4. Consultar estado
5. Finalizar expedición
```

El programa se va a desarrollar por etapas. Cada vez que terminen una etapa y funcione correctamente, deberán realizar el **commit indicado y luego hacer push** antes de continuar.

## Importante

- El examen es individual.
- Pueden realizar consultas al profesor durante el examen.
- **Cada consulta realizada al profesor descuenta 1 punto del puntaje total.**
- Antes de preguntar, revisen el código, los mensajes de error y prueben distintas entradas.
- Se evaluará tanto el resultado final como el proceso de desarrollo y los commits realizados.

---

## Etapa 1 — Inicio

Crear las variables necesarias para guardar:

- Nombre del piloto.
- Combustible disponible.
- Cantidad total de viajes realizados.
- Cantidad de viajes realizados a la Luna.
- Cantidad de viajes realizados a Marte.
- Cantidad de viajes realizados a Saturno.

También deberán crear dos listas:

- Una lista con los nombres de los destinos.
- Una lista con el costo de combustible de cada destino.

Por ejemplo:

```text
Destinos: Luna, Marte, Saturno
Costos: 20, 35, 50
```

Pedir al usuario su nombre y mostrar un mensaje de bienvenida junto con el combustible inicial.

Por ejemplo:

```text
TERMINAL DE EXPLORACIÓN ESPACIAL

Nombre del piloto: Martina

Bienvenida, Martina.
Combustible disponible: 100 unidades.
```

Cuando esta etapa funcione correctamente:

**Commit:** `Etapa 1 - Inicio de la terminal`

Luego realizar el **push**.

---

## Etapa 2 — Navegación

Mostrar el menú y pedir al usuario que seleccione una opción.

Según el destino elegido, deberán obtener el nombre del destino y su costo utilizando las listas creadas en la etapa anterior.

Antes de realizar el viaje, verificar si hay suficiente combustible disponible.

Por ejemplo:

```text
Destino seleccionado: Marte
Combustible necesario: 35

Viaje realizado correctamente.
Combustible restante: 65
```

Si no alcanza:

```text
Combustible insuficiente para realizar este viaje.
```

El combustible **nunca puede quedar en negativo**.

También deberán contemplar qué pasa si el usuario ingresa una opción que no existe.

### Pista para probar esta etapa

No alcanza con probar solamente que un viaje correcto funcione.

Para comprobar que la condición de combustible insuficiente funciona, pueden **cambiar momentáneamente el costo de un viaje por un valor mayor a 100**, o **bajar momentáneamente el combustible inicial**.

Cuando terminen de probarlo, vuelvan a colocar los valores indicados en la consigna.

Cuando esta etapa funcione correctamente:

**Commit:** `Etapa 2 - Sistema de navegación`

Luego realizar el **push**.

---

## Etapa 3 — Mantener el programa funcionando

Hasta este punto el programa realiza una sola operación.

Ahora deberán modificarlo para que el menú vuelva a aparecer después de cada acción.

El programa deberá seguir funcionando hasta que el usuario elija:

```text
5. Finalizar expedición
```

Cada vez que un viaje se realice correctamente:

- Restar el combustible utilizado.
- Sumar uno a la cantidad total de viajes realizados.
- Sumar uno al contador correspondiente al destino visitado.

Por ejemplo, si se viaja a Marte, además de aumentar la cantidad total de viajes, deberá aumentar el contador de viajes a Marte.

Si un viaje no puede realizarse por falta de combustible, **no debe contarse como viaje realizado**.

Cuando esta etapa funcione correctamente:

**Commit:** `Etapa 3 - Ciclo principal`

Luego realizar el **push**.

---

## Etapa 4 — Estado de la nave

Cuando el usuario seleccione:

```text
4. Consultar estado
```

El programa deberá mostrar:

- Nombre del piloto.
- Combustible restante.
- Cantidad total de viajes realizados.
- Cantidad de viajes realizados a cada destino.

Por ejemplo:

```text
===== ESTADO DE LA NAVE =====

Piloto: Martina
Combustible: 10
Viajes realizados: 3

Luna: 1
Marte: 2
Saturno: 0
```

Además, deberán mostrar nuevamente los destinos disponibles y sus costos recorriendo las listas con un `for`.

Por ejemplo:

```text
Destinos disponibles:

Luna - 20 unidades
Marte - 35 unidades
Saturno - 50 unidades
```

Cuando el usuario seleccione la opción `5`, mostrar un último resumen y finalizar el programa.

Cuando todo el programa esté terminado:

**Commit:** `Etapa 4 - Programa finalizado`

Luego realizar el **push**.

---

## Condiciones

Para resolver el examen deberán utilizar únicamente los contenidos vistos en clase.

Entre otras cosas, van a necesitar:

- Variables.
- `input()` y `print()`.
- Conversión de datos.
- Operaciones matemáticas.
- `if`, `elif` y `else`.
- Comparaciones.
- `while`.
- Listas.
- Índices.
- `for`.
- `range()`.
- Formato de texto.

No hace falta utilizar funciones, clases ni librerías externas.

El programa final deberá poder ejecutarse de principio a fin sin errores.

También se va a evaluar el historial del repositorio, por lo que **los commits pedidos forman parte del examen**.
