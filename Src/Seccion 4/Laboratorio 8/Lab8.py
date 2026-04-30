print("--- DESARROLLADOR DE MECÁNICAS DE JUEGO ---")

# LAB - Ejercicios de Algoritmos

# 1. Puntaje total de un jugador
n1 = int(input("Nivel 1: "))
n2 = int(input("Nivel 2: "))
n3 = int(input("Nivel 3: "))
print("Puntaje total:", n1 + n2 + n3)


# 2. Tiempo total en segundos
h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))
total_segundos = (h * 3600) + (m * 60) + s
print("Tiempo total en segundos:", total_segundos)


# 3. Daño total
d1 = int(input("Daño 1: "))
d2 = int(input("Daño 2: "))
d3 = int(input("Daño 3: "))
print("Daño total:", d1 + d2 + d3)


# 4. Experiencia total
e1 = int(input("Experiencia misión 1: "))
e2 = int(input("Experiencia misión 2: "))
e3 = int(input("Experiencia misión 3: "))
print("Experiencia total:", e1 + e2 + e3)


# 5. Porcentaje de vida restante
vida_max = int(input("Vida máxima: "))
vida_actual = int(input("Vida actual: "))
porcentaje = (vida_actual / vida_max) * 100
print("Vida restante:", porcentaje, "%")


# 6. Oro total
o1 = int(input("Oro misión 1: "))
o2 = int(input("Oro misión 2: "))
o3 = int(input("Oro misión 3: "))
print("Oro total:", o1 + o2 + o3)


# 7. Velocidad promedio
distancia = float(input("Distancia recorrida: "))
tiempo = float(input("Tiempo: "))
velocidad = distancia / tiempo
print("Velocidad promedio:", velocidad)


# 8. Costo total de mejoras
c1 = int(input("Costo mejora 1: "))
c2 = int(input("Costo mejora 2: "))
c3 = int(input("Costo mejora 3: "))
print("Costo total:", c1 + c2 + c3)


# 9. Tiempo restante
tiempo_total = int(input("Tiempo total misión: "))
tiempo_usado = int(input("Tiempo transcurrido: "))
print("Tiempo restante:", tiempo_total - tiempo_usado)


# 10. Nivel promedio
l1 = int(input("Nivel jugador 1: "))
l2 = int(input("Nivel jugador 2: "))
l3 = int(input("Nivel jugador 3: "))
promedio = (l1 + l2 + l3) / 3
print("Nivel promedio:", promedio)


# 11. Daño crítico
danio_base = int(input("Daño base: "))
multiplicador = float(input("Multiplicador crítico: "))
print("Daño crítico:", danio_base * multiplicador)


# 12. Convertir minutos a horas y minutos
min_total = int(input("Minutos totales: "))
horas = min_total // 60
minutos = min_total % 60
print("Horas:", horas, "Minutos:", minutos)


# 13. Porcentaje de misiones completadas
total_misiones = int(input("Total misiones: "))
completadas = int(input("Misiones completadas: "))
porcentaje = (completadas / total_misiones) * 100
print("Porcentaje completado:", porcentaje, "%")


# 14. Costo total de objetos
obj1 = int(input("Objeto 1: "))
obj2 = int(input("Objeto 2: "))
obj3 = int(input("Objeto 3: "))
print("Costo total:", obj1 + obj2 + obj3)


# 15. Tiempo promedio de partidas
t1 = int(input("Tiempo partida 1: "))
t2 = int(input("Tiempo partida 2: "))
t3 = int(input("Tiempo partida 3: "))
print("Promedio:", (t1 + t2 + t3) / 3)


# 16. Porcentaje de enemigos derrotados
total_enemigos = int(input("Total enemigos: "))
derrotados = int(input("Enemigos derrotados: "))
porcentaje = (derrotados / total_enemigos) * 100
print("Porcentaje derrotados:", porcentaje, "%")
