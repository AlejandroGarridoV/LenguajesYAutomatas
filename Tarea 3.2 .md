# Caso de uso real de un autómata finito 
## Semáforos de tránsito

### Aplicación:
El control de semáforos de tráfico es un ejemplo aplicación de autómatas finitos. Los semáforos regulan el flujo de vehículos y peatones en intersecciones viales para prevenir accidentes y optimizar el tráfico. Un autómata finito se puede utilizar para modelar el comportamiento del semáforo y determinar cuándo cambiar las luces en función de las condiciones del tráfico y las señales recibidas.

### Implementación:

1. **Definición de estados y transiciones:**
   - Estado 1: **Verde para los vehículos**
     - Transición: Después de cierto tiempo, cambia a estado de "Amarillo para los vehículos".
   - Estado 2: **Amarillo para los vehículos**
     - Transición: Después de un breve tiempo, cambia a estado de "Rojo para los vehículos".
   - Estado 3: **Rojo para los vehículos**
     - Transición: Después de cierto tiempo, cambia a estado de "Verde para los peatones".
   - Estado 4: **Verde para los peatones**
     - Transición: Después de cierto tiempo, cambia a estado de "Rojo para los peatones".
   - Estado 5: **Rojo para los peatones**
     - Transición: Después de cierto tiempo, vuelve a estado de "Verde para los vehículos".

2. **Implementación del autómata:**
   - Se pueden utilizar lenguajes de programación como Python para implementar el autómata finito. Aquí hay un ejemplo simplificado:

   ```python
   class Semáforo:
       def __init__(self):
           self.estado = "verde_vehículos"

       def cambiar_estado(self):
           if self.estado == "verde_vehículos":
               self.estado = "amarillo_vehículos"
           elif self.estado == "amarillo_vehículos":
               self.estado = "rojo_vehículos"
           elif self.estado == "rojo_vehículos":
               self.estado = "verde_peatones"
           elif self.estado == "verde_peatones":
               self.estado = "rojo_peatones"
           elif self.estado == "rojo_peatones":
               self.estado = "verde_vehículos"

   # Uso del autómata
   semaforo = Semáforo()
   print("Estado actual:", semaforo.estado)
   semaforo.cambiar_estado()
   print("Nuevo estado:", semaforo.estado)
