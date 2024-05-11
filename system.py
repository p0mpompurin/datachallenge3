class SistemaPlanetario():
    """
    Clase que representa un sistema planetario, que es el conjunto de planetas que orbitan una estrella dada.
    
    Atributos:
    - estrella: El nombre de la estrella alrededor de la cual orbitan los planetas.
    - planetas: Una lista de objetos de la clase Planeta que representan los planetas en el sistema.
    """
    
    def __init__(self, estrella, planetas=[]):
        """
        Inicializa una instancia de la clase SistemaPlanetario.
        
        Parámetros:
        - estrella: El nombre de la estrella alrededor de la cual orbitan los planetas.
        - planetas: Una lista opcional de objetos de la clase Planeta que representan los planetas en el sistema.
                    Por defecto, se utiliza una lista vacía.
        """
        self.planetas = planetas
        self.estrella = estrella.nombre
    
    def numero_planetas(self):
        """
        Devuelve el número de planetas en el sistema.
        
        Retorna:
        - El número de planetas en el sistema (entero).
        """
        return len(self.planetas)
    
    def planetas_ordenados(self):
        """
        Devuelve la lista de planetas ordenada según su radio semimayor de la órbita.
        
        Retorna:
        - Una lista de cadenas que representan los planetas ordenados según su radio semimayor de la órbita.
          Si un planeta no tiene un radio semimayor definido, se indica en la cadena correspondiente.
        """
        lista_planetas = []
        planetas_ordenados = list(sorted(self.planetas, key=lambda x: x._a))
        for planeta in planetas_ordenados:
            if planeta._a != 0:
                lista_planetas.append(f"{planeta._nombre} con semieje mayor igual a {planeta._a}")
            else:
                lista_planetas.append(f"{planeta._nombre} no tiene semieje mayor definido")

        return lista_planetas