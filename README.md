# Presentamos nuestro Gremio de Aventureros!

Este proyecto se trata de un gremio de aventureros al estilo de Dungeons & Dragons, en el mismo aplicamos lo aprendido sobre Programación Orientada a Objetos (POO), representando el entregable final de la asignatura Programación 1 (Universidad de Montevideo). Nuestro proyecto permite gestionar un gremio de aventureros, consultar información sobre el mismo, así como registrar y completar misiones. Fue creado por Augusto Calastretti y Lucas Gómez.


## Uso de la Aplicación
                 
- [Manejo de la aplicación](#manejo-de-la-aplicación) 
- [Modelado (UML)](https://github.com/lucasgomez13/entregable_programacion1/raw/master/ModeladoUML.jpg)
- [Características y Funcionalidades](#características-y-funcionalidades)
- [Instalación](#instalación)


### Manejo de la Aplicación

El manejo de la aplicación permite realizar diversas acciones para gestionar los aventureros y misiones del gremio. Las principales funcionalidades incluyen la creación de aventureros, registro de misiones y asignación de estas a los aventureros.


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

