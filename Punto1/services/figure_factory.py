from ..models.rectangle import Rectangle
from ..models.triangle import Triangle

class FigureFactory:
    """Factory Method para crear instancias de figuras geométricas."""
    
    @staticmethod
    def create_figure(figure_type, *args):
        """
        Crea una instancia de figura según el tipo especificado.
        
        Args:
            figure_type (str): Tipo de figura ('rectangle' o 'triangle')
            *args: Argumentos para la construcción de la figura
            
        Returns:
            Figure: Una instancia de la figura correspondiente
        """
        if figure_type.lower() == 'rectangle':
            return Rectangle(*args)
        elif figure_type.lower() == 'triangle':
            return Triangle(*args)
        else:
            raise ValueError(f"Tipo de figura no soportado: {figure_type}")