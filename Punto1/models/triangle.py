from .figure import Figure

class Triangle(Figure):
    """Clase que representa un triángulo."""
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        """Calcula el área del triángulo."""
        return 0.5 * self.base * self.altura