# Herencia y polimorfismo
# Empleado y Supervisor

class Persona():

    def __init__(self, nombre_completo, dni, ciudad):
        self.nombre_completo = nombre_completo
        self.dni = dni
        self.ciudad = ciudad

    def mostrar_nombre(self):
        print(f"Mi nombre completo es: {self.nombre_completo}")

class Empleado(Persona):

    def __init__(self, nombre_completo, dni, ciudad, legajo, sector):
        super().__init__(nombre_completo, dni, ciudad)
        self.legajo = legajo
        self.sector = sector

    def mostrar_nombre(self):
        print(f"Soy {self.nombre_completo} y tengo legajo {self.legajo}")

class Supervisor(Empleado):

    def __init__(self, nombre_completo, dni, ciudad, legajo, sector, cant_empleados_a_cargo):
        super().__init__(nombre_completo, dni, ciudad, legajo, sector)
        self.empleados_a_cargo = cant_empleados_a_cargo

    def mostrar_nombre(self):
        print("Soy supervisor y no te doy mi nombre...")

persona_1 = Persona("Maria Garcia", "1234567", "La Paz")
persona_1.mostrar_nombre()
empleado_1 = Empleado("Javier Garcia", "35555555", "Resistencia", "2555", "Administrativo")   
empleado_1.mostrar_nombre()     
supervisor_1 = Supervisor("Cruela devil", "55555000", "Montreal", "25555", "Maestranza", 55)
supervisor_1.mostrar_nombre()   


lista_personas = [persona_1, empleado_1, supervisor_1]

for persona in lista_personas:
    persona.mostrar_nombre()