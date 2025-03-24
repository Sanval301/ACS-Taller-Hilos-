import time
from .services.generator_thread import GeneratorThread
from .services.modifier_thread import ModifierThread
from .services.monitor_thread import MonitorThread
from .models.shared_list import SharedList
from .utils.logger import Logger

def main():
    """Función principal que inicia y coordina los hilos."""
    logger = Logger()
    logger.info("Iniciando programa de procesamiento concurrente")
    
    # Iniciar los hilos
    generator = GeneratorThread(interval=0.05)  # Genera números más rápido
    modifier = ModifierThread(interval=0.1)
    monitor = MonitorThread(interval=0.2, threshold=20000)
    
    # Iniciar la ejecución de los hilos
    generator.start()
    modifier.start()
    monitor.start()
    
    # Esperar a que todos los hilos terminen
    generator.join()
    modifier.join()
    monitor.join()
    
    # Mostrar estadísticas finales
    shared_list = SharedList()
    final_sum = shared_list.get_sum()
    final_length = shared_list.get_length()
    
    logger.info(f"Programa finalizado")
    logger.info(f"Estadísticas finales:")
    logger.info(f"- Número total de elementos: {final_length}")
    logger.info(f"- Suma total: {final_sum}")

if __name__ == "__main__":
    main()