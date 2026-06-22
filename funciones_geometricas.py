import math
def area_cuadrado(lado):
    """Calcula el área de un cuadrado dado el lado."""
    return lado ** 2
def area_circulo(radio):   
    """Calcula el área de un círculo dado el radio."""
    return math.pi * radio ** 2
def area_triangulo(base, altura):
    """Calcula el área de un triángulo dado la base y la altura."""
    return (base * altura) / 2
def area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dado la base y la altura."""
    return base * altura