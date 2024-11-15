
from Mago import Mago
from Ranger import Ranger
from Mascota import Mascota
from Mision import Mision
from Guerrero import Guerrero

class Gremio:
    def __init__(self):
        self.aventureros = []
        self.misiones = []

    def registrar_aventurero(self):
        print("Elija la clase del aventurero:")
        print("1. Guerrero")
        print("2. Mago")
        print("3. Ranger")
        clase = input("Ingrese su opción (1-3): ")

        if clase not in ['1', '2', '3']:
            print("Error: Opción inválida. Regresando al menú principal.")
            return

        nombre = input("Ingrese el nombre del aventurero: ")

        while True:
            try:
                id = int(input("Ingrese el ID del aventurero (número único): "))
                if any(aventurero.id == id for aventurero in self.aventureros):
                    print("Error: Ya existe un aventurero con ese ID. Ingrese un ID único.")
                else:
                    break
            except ValueError:
                print("Error: El ID debe ser un número entero.")

        while True:
            try:
                puntos_habilidad = int(input("Ingrese los puntos de habilidad (1-100): "))
                if 1 <= puntos_habilidad <= 100:
                    break
                else:
                    print("Error: Los puntos de habilidad deben estar entre 1 y 100.")
            except ValueError:
                print("Error: Los puntos de habilidad deben ser un número entero.")

        while True:
            try:
                experiencia = int(input("Ingrese la experiencia acumulada: "))
                break
            except ValueError:
                print("Error: La experiencia debe ser un número entero.")

        while True:
            try:
                dinero = float(input("Ingrese la cantidad de dinero: "))
                if dinero >= 0:
                    break
                else:
                    print("Error: El dinero no puede ser negativo.")
            except ValueError:
                print("Error: El dinero debe ser un número decimal.")

        if clase == '1':
            while True:
                try:
                    fuerza = int(input("Ingrese la fuerza (1-100): "))
                    if 1 <= fuerza <= 100:
                        nuevo_aventurero = Guerrero(nombre, id, puntos_habilidad, experiencia, dinero, fuerza)
                        break
                    else:
                        print("Error: La fuerza debe estar entre 1 y 100.")
                except ValueError:
                    print("Error: La fuerza debe ser un número entero.")
        elif clase == '2':
            while True:
                try:
                    mana = int(input("Ingrese el mana (1-1000): "))
                    if 1 <= mana <= 1000:
                        nuevo_aventurero = Mago(nombre, id, puntos_habilidad, experiencia, dinero, mana)
                        break
                    else:
                        print("Error: El mana debe estar entre 1 y 1000.")
                except ValueError:
                    print("Error: El mana debe ser un número entero.")
        elif clase == '3':
            tiene_mascota = input("¿Tiene una mascota? (S/N): ").strip().upper()
            if tiene_mascota == 'S':
                nombre_mascota = input("Ingrese el nombre de la mascota: ")
                while True:
                    try:
                        puntos_habilidad_mascota = int(input("Ingrese los puntos de habilidad de la mascota (1-50): "))
                        if 1 <= puntos_habilidad_mascota <= 50:
                            mascota = Mascota(nombre_mascota, puntos_habilidad_mascota)
                            nuevo_aventurero = Ranger(nombre, id, puntos_habilidad, experiencia, dinero, mascota)
                            break
                        else:
                            print("Error: Los puntos de habilidad de la mascota deben estar entre 1 y 50.")
                    except ValueError:
                        print("Error: Los puntos de habilidad de la mascota deben ser un número entero.")
            else:
                nuevo_aventurero = Ranger(nombre, id, puntos_habilidad, experiencia, dinero)

        self.aventureros.append(nuevo_aventurero)
        print("Aventurero registrado exitosamente.")

    def registrar_mision(self):
        nombre = input("Ingrese el nombre de la misión: ")

        while True:
            try:
                rango = int(input("Ingrese el rango de la misión (1-5): "))
                if 1 <= rango <= 5:
                    break
                else:
                    print("Error: El rango de la misión debe estar entre 1 y 5.")
            except ValueError:
                print("Error: El rango de la misión debe ser un número entero.")

        while True:
            try:
                recompensa = float(input("Ingrese la recompensa de la misión: "))
                if recompensa > 0:
                    break
                else:
                    print("Error: La recompensa debe ser un valor positivo.")
            except ValueError:
                print("Error: La recompensa debe ser un número decimal positivo.")

        tipo_mision = input("¿Es misión grupal? (S/N): ").strip().upper()
        cantidad_minima_miembros = 1
        if tipo_mision == 'S':
            while True:
                try:
                    cantidad_minima_miembros = int(input("Ingrese la cantidad mínima de miembros: "))
                    if cantidad_minima_miembros > 0:
                        break
                    else:
                        print("Error: La cantidad mínima de miembros debe ser un número positivo.")
                except ValueError:
                    print("Error: La cantidad mínima de miembros debe ser un número entero positivo.")

        nueva_mision = Mision(nombre, rango, recompensa, tipo_mision, minimo_de_miembros=cantidad_minima_miembros)
        self.misiones.append(nueva_mision)
        print("Misión registrada exitosamente.")

    def realizar_mision(self):
        nombre_mision = input("Ingrese el nombre de la misión que desea realizar: ")
        mision_encontrada = next((mision for mision in self.misiones if mision.nombre == nombre_mision), None)

        if not mision_encontrada:
            print("Error: Misión no encontrada. Regresando al menú principal.")
            return

        ids_aventureros = []
        while True:
            try:
                id_aventurero = int(input("Ingrese el ID del aventurero que desea registrarse: "))
                aventurero_encontrado = next((a for a in self.aventureros if a.id == id_aventurero), None)

                if aventurero_encontrado:
                    aventurero_encontrado.calcular_habilidad()
                    if self.validar_rango(aventurero_encontrado, mision_encontrada):
                        ids_aventureros.append(aventurero_encontrado)
                        print(f"{aventurero_encontrado.nombre} se ha registrado para la misión.")
                    else:
                        print(f"Error: {aventurero_encontrado.nombre} no cumple con el rango requerido para esta misión.")
                else:
                    print("Error: Aventurero no encontrado.")

                registrar_otro = input("¿Registrar otro aventurero? (S/N): ").strip().upper()
                if registrar_otro != 'S':
                    break
            except ValueError:
                print("Error: El ID debe ser un número entero.")

        if len(ids_aventureros) >= mision_encontrada.cantidad_minima_miembros:
            mision_encontrada.completado = True
            recompensa_por_aventurero = mision_encontrada.recompensa / len(ids_aventureros)

            for aventurero in ids_aventureros:
                aventurero.dinero += recompensa_por_aventurero
                experiencia_ganada = self.calcular_experiencia(mision_encontrada.rango)
                aventurero.experiencia += experiencia_ganada
                aventurero.agregar_mision_completada()

            print("Misión completada exitosamente.")
        else:
            print("Error: No se cumplió con la cantidad mínima de miembros para la misión.")

    def validar_rango(self, aventurero, mision):
        habilidad_total = aventurero.calcular_habilidad()
        if mision.rango == 1 and habilidad_total >= 1 and habilidad_total <= 20:
            return True
        elif mision.rango == 2 and habilidad_total >= 21 and habilidad_total <= 40:
            return True
        elif mision.rango == 3 and habilidad_total >= 41 and habilidad_total <= 60:
            return True
        elif mision.rango == 4 and habilidad_total >= 61 and habilidad_total <= 80:
            return True
        elif mision.rango == 5 and habilidad_total > 80:
            return True
        return False

    def calcular_experiencia(self, rango):
        if rango == 1:
            return 5
        elif rango == 2:
            return 10
        elif rango == 3:
            return 20
        elif rango == 4:
            return 50
        elif rango == 5:
            return 100
        return 0

    def mostrar_top_aventureros_misiones(self):
        aventureros_ordenados = sorted(self.aventureros, key=lambda x: (-x._misiones_completadas, x.nombre))
        print("Top 10 Aventureros con Más Misiones Completadas:")
        for i, aventurero in enumerate(aventureros_ordenados[:10]):
            print(f"{i + 1}. {aventurero.nombre} - {aventurero._misiones_completadas} misiones")

    def mostrar_top_aventureros_habilidad(self):
        aventureros_ordenados = sorted(self.aventureros, key=lambda x: (-x.calcular_habilidad(), x.nombre))
        print("Top 10 Aventureros con Mayor Habilidad:")
        for i, aventurero in enumerate(aventureros_ordenados[:10]):
            print(f"{i + 1}. {aventurero.nombre} - {aventurero.calcular_habilidad()} habilidad")

    def mostrar_top_misiones_recompensa(self):
        misiones_ordenadas = sorted(self.misiones, key=lambda x: (-x.recompensa, x.nombre))
        print("Top 5 Misiones con Mayor Recompensa:")
        for i, mision in enumerate(misiones_ordenadas[:5]):
            print(f"{i + 1}. {mision.nombre} - {mision.recompensa} recompensa")

    def menu_principal(self):
        while True:
            print("\nBienvenido al Simulador de Gremio de Aventureros!")
            print("Seleccione una opción:")
            print("1. Registrar Aventurero")
            print("2. Registrar Misión")
            print("3. Realizar Misión")
            print("4. Otras Consultas")
            print("5. Salir")

            opcion = input("Ingrese su opción (1-5): ")

            if opcion == '1':
                self.registrar_aventurero()
            elif opcion == '2':
                self.registrar_mision()
            elif opcion == '3':
                self.realizar_mision()
            elif opcion == '4':
                self.submenu_consultas()
            elif opcion == '5':
                print("¡Gracias por usar el simulador!")
                break
            else:
                print("Opción inválida, intente de nuevo.")

    def submenu_consultas(self):
        while True:
            print("\n--- Submenú de Consultas ---")
            print("1. Top 10 Aventureros con Más Misiones Completadas")
            print("2. Top 10 Aventureros con Mayor Habilidad")
            print("3. Top 5 Misiones con Mayor Recompensa")
            print("4. Mostrar Aventureros por Clase")

            opcion = input("Ingrese su opción (1-4): ")

            if opcion == '1':
                self.mostrar_top_aventureros_misiones()
            elif opcion == '2':
                self.mostrar_top_aventureros_habilidad()
            elif opcion == '3':
                self.mostrar_top_misiones_recompensa()
            elif opcion == '4':
                break
            else:
                print("Opción inválida, intente de nuevo.")
if __name__=="__main__":
    gremio = Gremio()
    gremio.menu_principal()
  
