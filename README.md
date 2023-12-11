# nieto_marta_estrella
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
# A continuación procederemos a usar el comando turtle.forward que se encargará de mover hacia adelante en la dirrección actual por la cantidad específica de píxeles que indica "longitud_puntas". Estas líneas además serán dibujadas hacia fuera desde el centro de la estrella.
        turtle.forward(longitud_puntas)
# El comando que utilizaremos ahora va a girar a la tortuga hacia la derecha en un ángulo específico, lo que enmarcamos en el parántesis es el cálculo del ángulo necesario para formar una punta de la estrella. Divide 180 (la mitad del ángulo completo) entre el número de puntas, así obtendremos el ángulo necesario para cada punta.
        turtle.right(180 - (180 / num_puntas))
# Esta línea hace que la ventana gráfica se cierre en cuanto la pulsemos
    turtle.exitonclick()
# Ejemplifico con la función dibujar_estrella cogiendo los valores 9 para el número de puntas y 100 para la longitud en unidades de la misma.
dibujar_estrella(9, 100)
