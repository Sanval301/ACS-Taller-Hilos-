import abc

class Figure(abc.ABC):
    """Clase abstracta base para las figuras geométricas."""
    
    @abc.abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de la figura."""
        pass
