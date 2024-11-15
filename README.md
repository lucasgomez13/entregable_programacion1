# Presentamos nuestro Gremio de Aventureros!

Este proyecto se trata de un gremio de aventureros al estilo de Dungeons & Dragons, en el mismo aplicamos lo aprendido sobre Programación Orientada a Objetos (POO), representando el entregable final de la asignatura Programación 1 (Universidad de Montevideo). Nuestro proyecto permite gestionar un gremio de aventureros, consultar información sobre el mismo, así como registrar y completar misiones. Fue creado por Augusto Calastretti y Lucas Gómez.


## Uso de la Aplicación
                 
- [Manejo de la aplicación](#manejo-de-la-aplicación) 
- [Modelado (UML)](https://github.com/lucasgomez13/entregable_programacion1/raw/master/ModeladoUML.jpg)
- [Características y Funcionalidades](#características-y-funcionalidades)
- [Instalación](#instalación)


### Manejo de la Aplicación

El manejo de la aplicación permite realizar diversas acciones para gestionar los aventureros y misiones del gremio. Las principales funcionalidades incluyen la creación de aventureros, registro de misiones y asignación de estas a los aventureros.
### Detalle modelado UML

**Gremio**
  La creamos para representar la asociación con las otras clases. Dentro de ella creamos todos los metodos y el main

**Misión**
  Esta clase representa una misión que pueden realizar los aventureros del gremio.
  Atributos:
    -nombre: El nombre de la misión (tipo str).
    -rango: El nivel o rango de dificultad de la misión (tipo int).
    -recompensa: La recompensa monetaria por completar la misión (tipo double).
    -completado: Un booleano que indica si la misión ha sido completada (tipo bool).
    -tipo_de_mision: El tipo de misión (tipo str).
    -cantidad_minima_miembros: El número mínimo de aventureros que pueden participar en la misión (tipo int).


**Aventurero**(abstracta)
  Es una clase abstracta que representa a un aventurero genérico, de la cual heredan clases más específicas como Guerrero, Mago, y Ranger.
  -Atributos:
    -nombre: El nombre del aventurero (tipo str).
    -id: Un identificador único para el aventurero (tipo int).
    -puntos_habilidad: Los puntos de habilidad del aventurero (tipo int).
    -experiencia: Los puntos de experiencia del aventurero (tipo int).
    -dinero: La cantidad de dinero que posee el aventurero (tipo double).

**Clases hijas de Aventurero:**

  **Guerrero**

  Representa un tipo específico de aventurero, enfocado en la fuerza.
  -Atributo:
    -fuerza: Representa la fuerza del guerrero (tipo int).

**Mago**

  Representa otro tipo de aventurero, enfocado en el uso de magia.
  -Atributo:
    -mana: Representa los puntos de maná del mago, necesarios para realizar hechizos (tipo int).

**Ranger**

  Otro tipo de aventurero, quizás especializado en el uso de habilidades especiales o destrezas.
  -Atributos:
      -nombre: Parece ser redundante, ya que Aventurero ya tiene un atributo nombre.
      -puntosDeHabilidad: Este podría ser un atributo específico que indica puntos de habilidad en habilidades específicas de rango.

  **Asociación:**
  mascota: Una relación de composición con la clase Mascota, indicando que el Ranger puede tener una mascota.

**Clases Asociadas:**

**Mascota**
  Representa una mascota que puede pertenecer a un Ranger.
  -Atributos:
    -nombre: El nombre de la mascota (tipo str).
    -puntos_habilidad: Los puntos de habilidad de la mascota (tipo int).
    -Relaciones
    -Asociación entre Gremio y Misión / Aventurero: Indica que el gremio está relacionado con misiones y aventureros, aunque el tipo de relación no está completamente especificado (si es una relación uno a muchos, por ejemplo).
    -Herencia: Guerrero, Mago, y Ranger extienden de la clase abstracta Aventurero, por lo que heredan sus atributos y pueden tener comportamiento específico.
    -Composición entre Ranger y Mascota: Un Ranger puede tener una mascota, y esta relación es de composición, lo que indica que la existencia de la mascota depende del Ranger.
    -Este diagrama parece estar diseñado para un sistema en el que se gestionan misiones y personajes de un gremio, donde cada tipo de aventurero tiene atributos únicos que le dan habilidades especiales para cumplir las misiones.

### Características y Funcionalidades

- **Registrar Aventureros**: Crear aventureros de las clases Guerrero, Mago, o Ranger, cada uno con atributos específicos (fuerza para guerreros, mana para magos, y mascota opcional para rangers).
- **Registrar Misiones**: Definir misiones que pueden ser individuales o grupales, cada una con atributos como nombre, rango, recompensa, y estado de completado.
- **Asignar Misiones**: Los aventureros pueden realizar misiones, ganando experiencia y recompensas. Se valida el rango de la misión y el aventurero.
- **Consultas**:
  - Ver los top 10 aventureros con más misiones completadas o mayor habilidad.
  - Listar las misiones con las mayores recompensas.
  - Filtrar aventureros por tipo (Guerrero, Mago, o Ranger).


### Instalación
Requerimientos:

- Es necesario  contar con [Python](https://www.python.org/downloads/).
- Descargar [Git](https://gitforwindows.org/) o directamente el archivo ZIP desde esta plataforma y ejecutar el mismo accediendo a main.py.

En caso de ejecutarlo desde Bash:
```
git clone https://github.com/lucasgomez13/entregable_programacion1.git
cd Entregable
python main.py

