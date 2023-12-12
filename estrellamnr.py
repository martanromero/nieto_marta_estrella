# El comando import importa el módulo "turtle" que lo que hará será proporcionar herramientas para dibujar grádicos en una nueva ventana
import turtle
# Definimos una función llamada "dibujar_estrella", esta función toma dos parámetros, el primero "num_puntas", que hace referencia al número de puntas de la estrella y "longitud_puntas" que hace referencia a cuantos pixeles de pantalla ocupa cada punta
def dibujar_estrella(num_puntas, longitud_puntas):
# A continuación vamos a establecer el título de la ventana gráfica
    turtle.title("Dibujar Estrella")
# Estableceremos también la velocidad de reproducción
    turtle.speed(2)
# El bucle for lo utilizaremos para repetir las puntas el número que num_puntas establezca
    for _ in range(num_puntas):
        turtle.forward(longitud_puntas)
        turtle.right(180 - (180 / num_puntas))

    turtle.exitonclick()

dibujar_estrella(9, 100)