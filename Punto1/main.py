import threading
import logging
import time
from .services.figure_factory import FigureFactory
from .services.area_calculator import (
    SimpleAreaCalculationStrategy,
    ThreadedAreaCalculator
)

def main():
    """Función principal del programa."""
    # Configuración del logging
    logging.info("Iniciando cálculo del área de la figura geométrica")
    
    # Crear la estrategia de cálculo
    strategy = SimpleAreaCalculationStrategy()
    
    # Crear el calculador de área con hilos
    calculator = ThreadedAreaCalculator(strategy)
    
    # Crear las figuras usando el Factory Method
    factory = FigureFactory()
    
    # Dimensiones de las figuras según la imagen
    rect1 = factory.create_figure('rectangle', 10, 12)  # Rectángulo izquierdo
    rect2 = factory.create_figure('rectangle', 8, 6)    # Rectángulo derecho
    triangle = factory.create_figure('triangle', 5, 6)  # Triángulo superior derecho
    
    # Crear hilos para calcular el área de cada figura
    thread1 = threading.Thread(
        target=calculator.calculate_area,
        args=(rect1, "Rectángulo Izquierdo (10m × 12m)"),
        name="Thread-Rect1"
    )
    
    thread2 = threading.Thread(
        target=calculator.calculate_area,
        args=(rect2, "Rectángulo Derecho (8m × 6m)"),
        name="Thread-Rect2"
    )
    
    thread3 = threading.Thread(
        target=calculator.calculate_area,
        args=(triangle, "Triángulo Superior Derecho (5m × 6m)"),
        name="Thread-Triangle"
    )
    
    # Iniciar los hilos
    start_time = time.time()
    
    thread1.start()
    thread2.start()
    thread3.start()
    
    # Esperar a que todos los hilos terminen
    thread1.join()
    thread2.join()
    thread3.join()
    
    end_time = time.time()
    
    # Mostrar el resultado final
    logging.info(f"Área total de la figura: {calculator.get_total_area()} m²")
    logging.info(f"Tiempo de ejecución: {end_time - start_time:.4f} segundos")

if __name__ == "__main__":
    main()
