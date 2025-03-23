# main.py
import time
from .utils.logging_util import setup_logger
from .utils.observer import Observer
from .services.factory import BasicSequenceFactory
from .services.thread_service import SequenceCalculator
from .models.sequence import Sequence

class SequenceResultObserver(Observer):
    """Observador para recibir resultados de la secuencia."""
    
    def __init__(self, logger):
        """
        Inicializa el observador con un logger.
        
        Args:
            logger: Logger para registrar información
        """
        self.logger = logger
        self.result = None
    
    def update(self, subject):
        """
        Recibe la actualización del sujeto.
        
        Args:
            subject: Sujeto que notifica el cambio
        """
        self.result = subject.sequence
        self.logger.info(f"Secuencia compartida recibida: {self.result}")

def main():
    """Función principal del programa."""
    # Configurar logger
    logger = setup_logger()
    logger.info("Iniciando programa de cálculo de secuencia compartida")
    
    # Solicitar los números
    try:
        n1 = int(input("Ingrese el primer número (n1): "))
        n2 = int(input("Ingrese el segundo número (n2): "))
        
        if n1 >= n2:
            logger.error("Error: n1 debe ser menor que n2")
            return
    except ValueError:
        logger.error("Error: Debe ingresar números enteros válidos")
        return
    
    # Crear secuencia para calcular la diferencia en el hilo principal
    try:
        sequence = Sequence(n1, n2)
        difference = sequence.calculate_difference()
    except ValueError as e:
        logger.error(f"Error: {e}")
        return
    
    # Configurar el observador
    observer = SequenceResultObserver(logger)
    
    # Crear el servicio de cálculo
    factory = BasicSequenceFactory()
    calculator = SequenceCalculator(factory)
    calculator.register_observer(observer)
    
    # Iniciar el cálculo en un hilo separado
    logger.info(f"Iniciando cálculo de secuencia entre {n1} y {n2}")
    thread = calculator.calculate_sequence_threaded(n1, n2)
    
    # Mientras el hilo secundario calcula, el hilo principal muestra la diferencia
    logger.info(f"Diferencia (n2 - n1): {difference}")
    
    # Esperar a que el hilo secundario termine
    thread.join()
    
    # Verificar si tenemos un resultado
    if observer.result:
        logger.info("Programa finalizado con éxito")
    else:
        logger.warning("No se recibió ningún resultado del hilo secundario")

if __name__ == "__main__":
    main()