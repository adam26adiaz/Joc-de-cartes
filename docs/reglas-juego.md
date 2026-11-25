# Reglas del juego

## 1. Objetivo de la partida

El objetivo de la partida es reducir los puntos de vida del rival hasta llegar a 0.
Cada jugador utiliza un mazo de cartas y juega por turnos.

---

## 2. Cartas

Cada carta tendrá las siguientes características:

- **Nombre**
- **Rareza**
- **Puntos de vida (PV)**
- **Ataque**
- **Defensa**
- **Habilidad**

Ejemplo:

**Dragón de Fuego**
- Rareza: Rara
- PV: 100
- Ataque: 30
- Defensa: 10
- Habilidad: pendiente de definir

Durante el desarrollo inicial se utilizará un número reducido de cartas para facilitar las pruebas.

---

## 3. Mazo

Cada jugador tendrá un **mazo de 10 cartas**.

El mazo se seleccionará antes de comenzar la partida.

Las cartas se gestionan en diferentes estados: **mazo, cartas disponibles y cartas en juego**.

Cuando el jugador obtiene una carta del mazo, esta pasa a estar entre sus **cartas disponibles**.

El número reducido de cartas permite realizar las primeras pruebas del juego de forma sencilla.

---

## 4. Preparación de la partida

Al comenzar una partida:

1. Cada jugador selecciona su mazo de 10 cartas.
2. El mazo se baraja.
3. Cada jugador recibe **4 cartas iniciales disponibles**.
4. Después de recibir las 4 cartas iniciales, quedan **6 cartas en el mazo**.
5. Cada jugador comienza con **100 puntos de vida**.
6. Se determina qué jugador empieza.
7. Comienza el primer turno.

Las 4 cartas iniciales están disponibles para que el jugador pueda decidir cuáles jugar.

---

## 5. Turnos

Los jugadores se alternan los turnos.

Al comenzar el turno:

1. El jugador obtiene **1 carta** del mazo.
2. Puede jugar cartas de sus cartas disponibles.
3. Las cartas jugadas pasan a estar **en juego**.
4. Puede realizar acciones con las cartas que tenga en juego.
5. Puede realizar un ataque.
6. Finaliza su turno.

Después comienza el turno del jugador rival.

El flujo básico de las cartas es:

**Mazo → Cartas disponibles → Cartas en juego → Combate**

---

## 6. Combate

Durante su turno, un jugador puede utilizar una carta que esté en juego para atacar.

Una carta puede atacar a una carta del rival que esté en juego.

Si el rival no tiene ninguna carta en juego, el jugador puede atacar directamente los puntos de vida del rival.

El daño contra una carta se calcula de la siguiente forma:

**Daño recibido = Ataque - Defensa**

El daño mínimo que puede recibir una carta es **1 punto**.

Cuando los puntos de vida de una carta llegan a **0**, la carta queda fuera de combate.

---

## 7. Puntos de vida de los jugadores

Cada jugador comienza la partida con:

**100 puntos de vida.**

Los puntos de vida del jugador disminuyen cuando recibe daño durante la partida.

---

## 8. Victoria y derrota

Un jugador gana la partida cuando los puntos de vida del jugador rival llegan a **0**.

Por tanto:

- **Victoria:** los PV del rival llegan a 0.
- **Derrota:** los propios PV llegan a 0.
- La partida termina cuando se cumple una de estas condiciones.

El resultado de la partida deberá quedar registrado para poder consultarlo posteriormente.

---