import random
import requests
import time
from bs4 import BeautifulSoup
from platform import system
from subprocess import call

os = system()

if os == "Windows":
	call("cls", shell=True)
else:
	call("clear", shell=True)

lista_exito = []

cantidad_enlaces = int(input("Cantidad de enlaces a generar: "))
print("\n")

letra = ""

alpha = "AaBbCcDdEeFfGgHhIiJjKkMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890"

contador_pos = 0

tiempo_ini = time.time()

for k in range(cantidad_enlaces):

	for i in range(0, 22):
		letra += random.choice(alpha)

	letra = "https://chat.whatsapp.com/" + letra

	pagina = requests.get(letra)
	soup = BeautifulSoup(pagina.text, "html.parser")

	objetos_h3 = soup.find_all("h3")
	h3 = objetos_h3[1]
	h3 = str(h3)

	if len(h3) == 52:
		print("[FALLO]")
		print(letra + "\n")
		letra = ""

	else:
		print("[EXITO]")
		contador_pos += 1

		lista_exito.append(letra)

		print(letra + "\n")
		letra = ""

tiempo_fin = time.time()

tiempo_total = tiempo_fin - tiempo_ini

tiempo_total = round(tiempo_total, 2)
print("=========================================")
print(f"Tiempo de ejecucion en segundos: {tiempo_total}")
print(f"Cantidad de enlaces validos: {contador_pos}")
print("Enlaces:")
for j in lista_exito:
	print(j)
print("=========================================")

input("Precione ENTER para salir.")
