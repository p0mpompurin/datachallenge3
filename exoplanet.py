import numpy as np

class PlanetaExoplanetario(Planeta):
    """
    Clase que representa un planeta exoplanetario, es decir, un planeta con una estrella anfitriona que no es el Sol.
    Hereda de la clase Planeta.
    """

    def metodo_descubrimiento(self, metodo):
        """
        Determina el método de primer descubrimiento del planeta exoplanetario, si por ”imagen directa”, ”velocidad radial” o ”transito”.

        Returns:
            str: El nombre del método de descubrimiento.

        """
        self.metodo_descubrimiento = metodo
        
        #Si el planeta es un tránsito, informa adicionalmente su parámetro de impacto 'b' :
        if self.metodo_descubrimiento == "Primary Transit":
            #Si el radio de la estrella es 0, no podemos calcular b, dado que se indefine.
            if (self._estrella_protegida)._radioestrella == 0:
                self.metodo_descubrimiento = "Transito, pero falta información para calcular el parámetro de impacto b"
                return self.metodo_descubrimiento
            #Si no es 0, entonces calculamos b
            else:
                b = self._a * np.cos(np.radians(self._i)) * (1 - self._e ** 2) / ((self._estrella_protegida)._radioestrella * (1 + self._e * np.sin(np.radians(self._w))))
                self.metodo_descubrimiento = f"Transito, con parámetro de impacto b: {b}"
                return self.metodo_descubrimiento
         
        #De no ser Tránsito, solamente devolvemos el nombre del método.
        elif self.metodo_descubrimiento == "Radial Velocity":
            self.metodo_descubrimiento = "Velocidad Radial"
            return self.metodo_descubrimiento
        
        elif self.metodo_descubrimiento == "Imaging":
            self.metodo_descubrimiento = "Imagen Directa"
            return self.metodo_descubrimiento
        
        else:
            self.metodo_descubrimiento = "Otro método"
            return self.metodo_descubrimiento
    
    def tatooine(self):
        """
        Determina si el planeta es similar a Tatooine, es decir, si orbita alrededor de una estrella binaria.

        Returns:
            str: Un mensaje indicando si el planeta es similar a Tatooine o no.
        """
        #Si el nombre indica más de una letra, en consecuencia, es similar a Tatooine, dado que esto nos indica que se encuentra orbitando 2 estrellas.
        if "A" and "B" in self._nombre:
            return "Es similar a Tatooine"
        #Si no, no es similar a Tatooine.
        else:
            return "No es similar a Tatooine, ya que solo cuenta con una estrella"