from datetime import datetime

class Paciente:
    def __init__(self, nombre, fecha_nacimiento, genero):
        self.nombre = nombre
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
        self.genero = genero
        self.historial = []
        self.citas = []

    def calcular_edad(self):
        hoy = datetime.today()
        edad = hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return edad

    def agregar_cita(self, fecha, hora):
        self.citas.append({'fecha': fecha, 'hora': hora})

    def mostrar_info(self):
        print(f'Introduce el nombre del paciente: {self.nombre}')
        print(f'Edad del paciente: {self.calcular_edad()}')
        print(f'Género del paciente: {self.genero}')
        print("Historial médico")
        for registro in self.historial:
            print(registro)
        print("Cita programada")
        for cita in self.citas:
            print(f'{cita["fecha"]} a las {cita["hora"]}')

def registrar_paciente():
    nombre = input("¿Cuál es el nombre del paciente? ")
    fecha_nacimiento = input("¿Cuál es la fecha de nacimiento del paciente? (DD/MM/AAAA): ")
    genero = input("Género del paciente: ")
    return Paciente(nombre, fecha_nacimiento, genero)

def actualizar_paciente(paciente):
    print("Actualizando la información del paciente: ")
    paciente.nombre = input("Nombre del paciente: ")
    fecha_nacimiento = input("Fecha de nacimiento (DD/MM/AAAA): ")
    paciente.fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
    paciente.genero = input("Género: ")

def programar_cita(paciente):
    fecha = input("Fecha de la cita (DD/MM/AAAA): ")
    hora = input("Hora de la cita (HH:MM): ")
    paciente.agregar_cita(fecha, hora)

def mostrar_pacientes(pacientes):
    if not pacientes:
        print("No hay registro de pacientes")
        return None
    else:
        for i, paciente in enumerate(pacientes):
            print(f'{i + 1}. {paciente.nombre}')
        return pacientes

def main():
    pacientes = []
    while True:
        print("\nMenú Principal")
        print("1. Registrar Paciente")
        print("2. Actualizar Información del Paciente")
        print("3. Programar Cita")
        print("4. Consultar Información del Paciente")
        print("5. Salir")
        opción = input("Seleccione una opción: ")

        if opción == "1":
            paciente = registrar_paciente()
            pacientes.append(paciente)
        elif opción == "2":
            if mostrar_pacientes(pacientes) is not None:
                index = int(input("Seleccione el número del paciente a actualizar: ")) - 1
                if 0 <= index < len(pacientes):
                    actualizar_paciente(pacientes[index])
                else:
                    print("Selección inválida.")
        elif opción == "3":
            if mostrar_pacientes(pacientes) is not None:
                index = int(input("Seleccione el número del paciente: ")) - 1
                if 0 <= index < len(pacientes):
                    programar_cita(pacientes[index])
                else:
                    print("Selección inválida.")
        elif opción == "4":
            if mostrar_pacientes(pacientes) is not None:
                index = int(input("Seleccione el número del paciente: ")) - 1
                if 0 <= index < len(pacientes):
                    pacientes[index].mostrar_info()
                else:
                    print("Selección inválida.")
        elif opción == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    main()
