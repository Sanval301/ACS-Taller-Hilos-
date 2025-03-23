import threading
import time
'''
Se debe pensar en estas señales como elementos booleanos que pueden estar activos 
o inactivos, al tiempo que tenemos bloqueos o cerraduras que solo pueden pasar
si la señal está activa. 
'''
    
def genera_eventos():
    for x in range(5):
        time.sleep(2)
        ev.set()
    # Cuando termine todas las iteraciones, activamos la señal de terminación
    stop_event.set()
    print("Hilo genera_eventos ha terminado")
  
def escribe_algo():
    while not stop_event.is_set():  # Verificamos si debemos terminar
        ev.wait()  # Esperamos a que se active el evento
        if not stop_event.is_set():  # Verificamos nuevamente para evitar imprimir después de terminar
            print("hola")
            ev.clear()  # Reiniciamos el evento para la próxima iteración
    print("Hilo escribe_algo ha terminado")
    
# Creamos dos eventos: uno para controlar los mensajes y otro para la terminación
ev = threading.Event()
stop_event = threading.Event()

T1 = threading.Thread(target=genera_eventos)
T2 = threading.Thread(target=escribe_algo)

T1.start()
T2.start()

# Esperamos a que ambos hilos terminen antes de finalizar el programa
T1.join()
T2.join()

print("Programa terminado correctamente")