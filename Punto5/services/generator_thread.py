import threading
import random
import time
from ..models.shared_list import SharedList
from ..utils.logger import Logger

class GeneratorThread(threading.Thread):
    """
    Hilo encargado de generar números aleatorios y añadirlos 
    a la lista compartida.
    """
    
    def __init__(self, name="GeneratorThread", interval=0.1):
        """
        Inicializa el hilo generador.
        
        Args:
            name (str): Nombre del hilo
            interval (float): Intervalo entre generaciones en segundos
        """
        super(GeneratorThread, self).__init__(name=name)
        self.shared_list = SharedList()
        self.logger = Logger()
        self.interval = interval
        self.running = True
        # Registrar este hilo como observador
        self.shared_list.register_observer(self)
    
    def run(self):
        """Ejecuta el hilo, generando números aleatorios continuamente."""
        self.logger.info(f"{self.name} iniciado")
        
        try:
            while self.running and self.shared_list.should_continue():
                # Generar un número aleatorio entre 1 y 100
                number = random.randint(1, 100)
                # Añadir a la lista compartida
                self.shared_list.add_value(number)
                
                total_sum = self.shared_list.get_sum()
                list_length = self.shared_list.get_length()
                
                self.logger.info(f"Generado: {number}, Total elementos: {list_length}, Suma: {total_sum}")
                
                # Esperar un intervalo antes de la siguiente generación
                time.sleep(self.interval)
        except Exception as e:
            self.logger.error(f"Error en {self.name}: {str(e)}")
        
        self.logger.info(f"{self.name} finalizado")
    
    def stop(self):
        """Detiene la ejecución del hilo."""
        self.running = False
        self.logger.info(f"{self.name} recibió señal de parada")