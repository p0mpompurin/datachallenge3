import string

class SistemaJerarquico():
    """
    Clase que representa un sistema jerárquico, que es un sistema estelar múltiple compuesto por N ≥ 2 estrellas.
    Los atributos principales de un sistema jerárquico son:
    
    Atributos:
    - estrellas: Una lista de estrellas que contiene (tipo lista).
    """
    
    def __init__(self):
        """
        Inicializa una instancia de la clase SistemaJerarquico.
        Crea una lista vacía para almacenar las estrellas del sistema jerárquico.
        """
        self.estrellas= []

    def agregar_estrella(self, estrella):
        """
        Agrega una estrella al sistema jerárquico.
        
        Parámetros:
        - estrella: La estrella a agregar al sistema jerárquico.
        """
        self.estrellas.append(estrella)
    
    def devolver_por_masa(self):
        """
        Devuelve la lista de estrellas ordenada por masa estelar.
        
        Retorna:
        - Una lista de estrellas ordenada por masa estelar.
        """
        return sorted(self.estrellas, key=lambda x: x._masa)
    
    def devolver_por_nombres(self):
        """
        Imprime los nombres de las estrellas seguidos de la lista ordenada de letras del alfabeto.
        
        Retorna:
        - Una lista de nombres de estrellas seguidos de la lista ordenada de letras del alfabeto.
        """
        nombres = []
        for i in range(len(self.estrellas)):
            # Se asume que el sistema jerarquico no tendra mas de 26 estrellas
            # Por lo que a cada nombre de la estrella correspondiente a la posicion i de la lista de estrellas, se le asigna una letra del abecedario.
            nombres.append(self.estrellas[i].nombre + " " + string.ascii_uppercase[i])
        return nombres