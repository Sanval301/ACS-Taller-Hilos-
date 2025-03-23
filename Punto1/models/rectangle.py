from .figure import Figure

class Rectangle(Figure):
    """Clase que representa un rectángulo."""
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura
