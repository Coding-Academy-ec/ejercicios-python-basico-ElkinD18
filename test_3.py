from programa import imprimir_datos_personales
from io import StringIO
import sys

def test_imprimir_datos_personales(capsys):
    nombre = "Elkin Chulca"
    edad = 20
    estatura = 1.6
    imprimir_datos_personales(nombre, edad, estatura)
    captured = capsys.readouterr()
    assert captured.out == "Nombre: Elkin Chulca\nEdad: 20\nEstatura: 1.6\n"
