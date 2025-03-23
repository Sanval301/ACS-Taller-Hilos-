class Sequence:
    """Clase para generar secuencias numéricas."""
    
    def __init__(self, n1, n2):
        """
        Inicializa una secuencia entre dos números.
        
        Args:
            n1 (int): Número inicial
            n2 (int): Número final
        """
        if n1 >= n2:
            raise ValueError("n1 debe ser menor que n2")
        
        self.n1 = n1
        self.n2 = n2
        
    def generate_sequence(self):
        """
        Genera la secuencia compartida entre n1 y n2 (inclusive).
        
        Returns:
            list: Lista de números enteros entre n1 y n2
        """
        return list(range(self.n1, self.n2 + 1))
    
    def calculate_difference(self):
        """
        Calcula la diferencia entre n2 y n1.
        
        Returns:
            int: Resultado de n2 - n1
        """
        return self.n2 - self.n1
