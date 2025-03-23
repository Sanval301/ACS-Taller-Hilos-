import threading
import logging
from abc import ABC, abstractmethod

# Configuración del logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
)

class AreaCalculationStrategy(ABC):
    """Interfaz para la estrategia de cálculo de área (Patrón Strategy)."""
    
    @abstractmethod
    def execute(self, figure):
        """Ejecuta el cálculo de área con la estrategia específica."""
        pass

class SimpleAreaCalculationStrategy(AreaCalculationStrategy):
    """Estrategia simple para calcular el área de una figura."""
    
    def execute(self, figure):
        """Calcula el área de la figura usando su método calcular_area()."""
        return figure.calcular_area()

class ThreadedAreaCalculator:
    """Clase para calcular áreas usando hilos."""
    
    def __init__(self, strategy):
        """
        Inicializa el calculador con una estrategia específica.
        
        Args:
            strategy (AreaCalculationStrategy): Estrategia de cálculo de área
        """
        self.strategy = strategy
        self.total_area = 0
        self.lock = threading.Lock()
        
    def calculate_area(self, figure, figure_name):
        """
        Calcula el área de una figura y actualiza el área total.
        
        Args:
            figure (Figure): Figura geométrica
            figure_name (str): Nombre descriptivo de la figura
        """
        area = self.strategy.execute(figure)
        
        with self.lock:
            self.total_area += area
            
        logging.info(f"Área de {figure_name}: {area} m²")
        
    def get_total_area(self):
        """Retorna el área total calculada."""
        return self.total_area
