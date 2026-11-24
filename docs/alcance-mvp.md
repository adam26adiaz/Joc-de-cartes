# Alcance del MVP y ampliaciones

## Descripción del proyecto

Juego de cartas coleccionables digital, inspirado en juegos como Pokémon TCG. Los jugadores crean una cuenta, consiguen cartas con sobres, construyen mazos y juegan partidas por turnos contra otros jugadores. El servidor controla las reglas, valida las acciones y guarda el estado de las partidas.

## Tecnologías

| Parte | Tecnología |
|---|---|
| Servidor y API REST | Python + FastAPI |
| Base de datos | MySQL |
| Cliente del juego | Python + Pygame |
| Panel de administración | FastAPI + Jinja2 |
| Control de versiones | Git + GitHub |
| Gestión del proyecto | Jira |

## Alcance del MVP

El MVP (Sprints 0 a 5) incluye:

- **Cuentas:** registro, inicio de sesión, perfil, nivel y monedas.
- **Colecciones y álbum:** cartas organizadas por colección, con las no conseguidas en silueta y contador de progreso.
- **Sobres y tienda:** un tipo de sobre por colección, comprados con monedas y abiertos con probabilidades por rareza.
- **Mazos:** crear, editar y validar mazos, y elegir un mazo activo.
- **Partidas por turnos asíncronas:** un jugador crea la partida y otro se une o es retado. Cada uno juega su turno cuando puede y el servidor guarda el estado en MySQL. El cliente consulta el estado cada pocos segundos.
- **Buffs:** al inicio de cada ronda aparecen 3 buffs y el jugador elige 1 antes de actuar.
- **Reglas en el juego:** pantalla "Reglas" que muestra el documento `docs/reglas.md`.

## Completan el proyecto (Sprints 6 y 7)

- **Recompensas de partida:** monedas y XP al terminar, subida de nivel.
- **Historial y estadísticas del jugador.**
- **Panel web de administración:**
  - Alta de cartas y colecciones.
  - Equilibrado de estadísticas de las cartas.
  - Gestión de buffs y de sobres.
  - Métricas de usuarios.
- **Calidad y documentación:** pruebas, revisión de seguridad, documentación de la API y memoria.

## Ampliaciones (fuera del alcance actual)

Quedan en el backlog, sin sprint asignado:

- Matchmaking y partidas en tiempo real (WebSockets).
- Ranking de jugadores.
- Juego contra IA.
- Intercambio de cartas entre jugadores.
- Notificaciones (por ejemplo, aviso de "es tu turno").
- Misiones diarias para conseguir más monedas.
- Más colecciones, cartas y buffs.
- Modo de realidad virtual (solo investigación).

## Decisiones de alcance

- Las **reglas del juego se pueden consultar dentro del propio juego**: se escriben una sola vez en `docs/reglas.md`, el servidor las sirve con `GET /rules` y el cliente las muestra en la pantalla "Reglas" (desde el menú principal) y con el botón "?" del tablero durante la partida. Por eso se redactan en texto plano o Markdown sencillo, con secciones cortas.
- Las partidas son **asíncronas**: no se usan WebSockets en el MVP.
- No hay matchmaking automático: se juega creando una partida, uniéndose a una abierta o retando a un jugador por su nombre de usuario.
- Si hay poco tiempo, se recortan primero las métricas del panel de administración y las estadísticas del jugador. Lo último que se toca son los sobres, las monedas, el álbum, los buffs y las partidas por turnos.