import threading
import time
from ..models.shared_list import SharedList
from ..utils.logger import Logger

class ModifierThread(threading.Thread):
    """
    Hilo encargado de recorrer circularmente la lista compartida
    y sustituir los valores que terminen en 0 por -1.
    """
    
    def __init__(self, name="ModifierThread", interval=0.2):
        """
        Inicializa el hilo modificador.
        
        Args:
            name (str): Nombre del hilo
            interval (float): Intervalo entre modificaciones en segundos
        """
        super(ModifierThread, self).__init__(name=name)
        self.shared_list = SharedList()
        self.logger = Logger()
        self.interval = interval
        self.running = True
        self.current_index = 0
        # Registrar este hilo como observador
        self.shared_list.register_observer(self)
    
    def run(self):
        """Ejecuta el hilo, modificando valores que terminan en 0."""
        self.logger.info(f"{self.name} iniciado")
        
        try:
            while self.running and self.shared_list.should_continue():
                # Obtener la longitud actual de la lista
                list_length = self.shared_list.get_length()
                
                if list_length > 0:
                    # Calcular el índice de forma circular
                    self.current_index = self.current_index % list_length
                    
                    # Obtener el valor actual en ese índice
                    current_values = self.shared_list.get_values()
                    current_value = current_values[self.current_index]
                    
                    # Verificar si el valor termina en 0
                    if current_value % 10 == 0 and current_value != -1:
                        # Sustituir el valor por -1
                        self.shared_list.update_value(self.current_index, -1)
                        self.logger.info(f"Modificado: índice {self.current_index}, valor {current_value} -> -1")
                    
                    # Avanzar al siguiente índice
                    self.current_index += 1
                
                # Esperar un intervalo antes de la siguiente modificación
                time.sleep(self.interval)
        except Exception as e:
            self.logger.error(f"Error en {self.name}: {str(e)}")
        
        self.logger.info(f"{self.name} finalizado")
    
    def stop(self):
        """Detiene la ejecución del hilo."""
        self.running = False
        self.logger.info(f"{self.name} recibió señal de parada")
