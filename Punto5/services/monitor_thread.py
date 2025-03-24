import threading
import time
from ..models.shared_list import SharedList
from ..utils.logger import Logger

class MonitorThread(threading.Thread):
    """
    Hilo encargado de monitorear la suma total de los elementos
    y detener los otros hilos cuando la suma supere 20000.
    """
    
    def __init__(self, name="MonitorThread", interval=0.5, threshold=20000):
        """
        Inicializa el hilo monitor.
        
        Args:
            name (str): Nombre del hilo
            interval (float): Intervalo entre verificaciones en segundos
            threshold (int): Umbral de suma para detener el programa
        """
        super(MonitorThread, self).__init__(name=name)
        self.shared_list = SharedList()
        self.logger = Logger()
        self.interval = interval
        self.threshold = threshold
        self.running = True
        # Registrar este hilo como observador
        self.shared_list.register_observer(self)
    
    def run(self):
        """Ejecuta el hilo, monitoreando la suma total."""
        self.logger.info(f"{self.name} iniciado")
        
        try:
            while self.running and self.shared_list.should_continue():
                # Obtener la suma actual
                total_sum = self.shared_list.get_sum()
                
                # Verificar si la suma supera el umbral
                if total_sum > self.threshold:
                    self.logger.info(f"Suma total ({total_sum}) supera el umbral ({self.threshold})")
                    # Notificar a todos los hilos que deben detenerse
                    self.shared_list.notify_stop()
                    break
                
                # Esperar un intervalo antes de la siguiente verificación
                time.sleep(self.interval)
        except Exception as e:
            self.logger.error(f"Error en {self.name}: {str(e)}")
        
        self.logger.info(f"{self.name} finalizado")
    
    def stop(self):
        """Detiene la ejecución del hilo."""
        self.running = False
        self.logger.info(f"{self.name} recibió señal de parada")
