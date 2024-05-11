import numpy as np
import pandas as pd 
import string

def crear_estrella(data, nombre_estrella):
    """
    Crea una instancia de la clase Estrella a partir de los datos de una estrella y su nombre.

    Argumentos:
        data (DataFrame): DataFrame de pandas con los datos de una estrella.
        nombre (str): El nombre de la estrella.

    Return:
        Información de la estrella y si sus datos se encuentran en la base de datos o no.

    """
    for indice in range(len(data)):
        #Recorremos el indice de la base de datos y verificamos si el nombre de la estrella se encuentra en el nombre de la estrella o en los nombres alternativos.
        if nombre_estrella in data['star_name'][indice] or nombre_estrella in data['star_alternate_names'][indice]:
            #Calculamos el movimiento propio de la estrella.
            movimiento_propio = np.sqrt(data['ra'][indice]**2 + data['dec'][indice]**2)
            #Creamos una instancia de la clase Estrella con los datos de la estrella.
            estrella = Estrella(data['star_name'][indice], data['star_mass'][indice], data['star_radius'][indice], data['star_teff'][indice], data['star_distance'][indice], movimiento_propio)
           
            #Preparamos el mensaje que se imprimirá en la consola.
            print(f"\nLa estrella '{estrella.nombre}' tiene la siguiente información:")
            nombre_alternativo= data['star_alternate_names'][indice]
            info_estrella = {"nombre": estrella.nombre,"nombre alternativo":nombre_alternativo, "masa": estrella._masa, "radio": estrella._radioestrella, "temperatura superficial": estrella._teff, "distancia": estrella._distancia, "movimiento propio": estrella._movimientopropio}

            #Verificamos si alguno de los atributos de la estrella es igual a 0, en caso de serlo, se imprime un mensaje informando es debido a la falta información en la base de datos.
            for atributo, valor in info_estrella.items():
                if valor == 0:
                    print(f"El atributo '{atributo}' de la estrella '{estrella.nombre}' es igual a 0, por lo que falta su información en la base de datos")
            #Imprimimos la información de la estrella como un diccionario.
            print(info_estrella)
            #Imprimimos la luminosidad total y de la secuencia principal de la estrella.
            print( f"La luminosidad total de la estrella'{estrella.nombre}' es: {estrella.luminosidad_total()}")
            print( f"La luminosidad de la secuencia principal de la estrella'{estrella.nombre}' es: {estrella.luminosidad_secuencia_principal(l_sol = 3.828e26,m_sol = 1.9884e30)}")
            #Imprimimos un separador para que se vea mejor visualmente el print de la información de cada estrella.
            print("-----------------------------------------------------------------------------------------------------------------")
            return estrella
        #En caso de que la estrella no se encuentre en el indice actual, se continua con el siguiente.
        else:
            continue
    # Si el nombre de la estrella no se encuentra en la base de datos retornamos un mensaje informando que no se encuentra.
    print(f"\nLa estrella {nombre_estrella} no se encuentra en la base de datos\n-----------------------------------------------------------------------------------------------------------------")
    return None


def crear_sistema(data, estrella):
    """
    Crea un sistema planetario a partir del DataFrame con los datos de planetas exoplanetarios y el nombre de la estrella a la que orbita.

    Argumentos:
        data (DataFrame): DataFrame de pandas con los datos del planeta.
        estrella (Class): un objeto de la clase Estrella.

    Return:
        Información del sistema planetario, con respectivos métodos de clases, y si los datos se encuentran en la base de datos o no.
    """

    planetas = [] # Creamos una lista vacía donde iran los planetas para luego agregarla al sistema planetario.
    
#Recorremos toda la data para encontrar los planetas que orbitan la estrella con el nombre ingresado en la función.
    for indice in range(len(data)):
        #Si encontramos un planeta que orbita la estrella con el nombre dado, creamos una instancia de la clase PlanetaExoplanetario y la agregamos a la lista de planetas.
        if data['star_name'][indice] == estrella.nombre or data['star_alternate_names'][indice] == estrella.nombre:
            exoplaneta = PlanetaExoplanetario(data['name'][indice], estrella, data['mass'][indice], data['radius'][indice], data['semi_major_axis'][indice], data['inclination'][indice], data['eccentricity'][indice], data['omega'][indice])
            #Identificamos el método de descubrimiento del planeta
            exoplaneta.metodo_descubrimiento((data['detection_type'][indice]))
            planetas.append(exoplaneta)

    #Si no encontramos planetas que orbiten la estrella con el nombre dado, retornamos un mensaje indicando que no hay planetas o que la estrella no se encuentra en la base de datos.
    if len(planetas) == 0:
        print(f"\nLa estrella {estrella.nombre} no tiene planetas, o no se encuentra en la base de datos")
        return None
    #Si encontramos planetas que orbiten la estrella con el nombre dado, creamos una instancia de la clase SistemaPlanetario, e imprimimos la información del sistema planetario.
    else:
        sistema = SistemaPlanetario(estrella, planetas)

        print(f"\nEl sistema planetario de la estrella '{sistema.estrella}' tiene la siguiente información:")
        print(f"Nombre del sistema: {sistema.estrella}")
        print(f"Número de planetas en el sistema: {sistema.numero_planetas()}")
        print(f"Lista de planetas en el sistema:")
        #Recorremos la lista de planetas del sistema para imprimir la información de cada planeta.
        for planeta in sistema.planetas:
            periodo= planeta.periodo_rotacion_kepleriana(g = 6.67430e-11)
            #Si el periodo de rotación kepleriano es igual a 0, significa que no hay datos suficientes para calcular el periodo.
            if periodo == 0:
                print(f"    *{planeta._nombre} sin datos suficientes para calcular el periodo")
                print(f"        *{planeta.tatooine()}")
                # Imprimimos el método de descubrimiento de cada planeta.
                print(f"        *Metodo decubrimiento: {planeta.metodo_descubrimiento}")
            #Si el periodo de rotación kepleriano es distinto de 0, imprimimos el periodo de rotación kepleriano, si el planeta es similar a Tatooine y el método de descubrimiento.
            else:
                print(f"    *{planeta._nombre} con periodo de rotación kepleriano igual a {periodo}")
                print(f"        *{planeta.tatooine()}")
                # Imprimimos el método de descubrimiento de cada planeta.
                print(f"        *Metodo decubrimiento: {planeta.metodo_descubrimiento}")
        #Imprimimos la lista de planetas ordenada según su radio semimayor de la órbita.
        print(f"Lista de planetas ordenados según su radio semimayor de la órbita:\n {sistema.planetas_ordenados()}")
        #Retornamos el sistema planetario.
        return sistema



#Declaración de constantes
l_sol = 3.828e26  # Luminosidad del Sol [Watts]
m_sol = 1.9884e30  # Masa del Sol [KG]
g = 6.67430e-11  # Constante de gravitación universal [m^3/kg/s^2]

#Lectura de datos
data = pd.read_csv("exoplanets.csv")

#Limpieza de datos:
data_limpio = data.fillna(0) #Eliminación de datos Nan y rellenar con 0 para evitar errores
data_limpio['star_name'] = data_limpio['star_name'].replace(0, '0') #Reemplazo de 0 por '0' para evitar errores, ya que los nombres son str
data_limpio['star_alternate_names'] = data_limpio['star_alternate_names'].replace(0, '0') #Lo mismo para alternate_names

#Creamos las instancias de cada estrella.

estrella_HR8799 = crear_estrella(data_limpio, "HR 8799")
estrella_HD202206 = crear_estrella(data_limpio, "HD 202206 ")
estrella_TRAPPIST1 = crear_estrella(data_limpio, "TRAPPIST-1")
estrella_TOI1338 = crear_estrella(data_limpio, "TOI-1338")
estrella_HD188753 = crear_estrella(data_limpio, "HD 188753")
estrella_Kepler451 = crear_estrella(data_limpio, "Kepler-451")
estrella_Kepler16 = crear_estrella(data_limpio, "Kepler-16 ")

sistema_HR8799 = crear_sistema(data_limpio, estrella_HR8799)

sistema_HD202206 = crear_sistema(data_limpio, estrella_HD202206)

sistema_TRAPPIST1 = crear_sistema(data_limpio, estrella_TRAPPIST1)

sistema_TOI1338 = crear_sistema(data_limpio, estrella_TOI1338)

sistema_Kepler451 = crear_sistema(data_limpio, estrella_Kepler451)

sistema_Kepler16 = crear_sistema(data_limpio, estrella_Kepler16)

#Utilizando 2 sistemas planetarios, los uniremos para crear a mano un sistema jerárquico.
#Creamos la instancia de la clase SistemaJerarquico
sistema_jerarquico = SistemaJerarquico()
#Añadimos al sistema las 2 estrellas que conforman el sistema jerárquico.
sistema_jerarquico.agregar_estrella(estrella_Kepler16)
sistema_jerarquico.agregar_estrella(estrella_Kepler451)
sistema_jerarquico.agregar_estrella(estrella_Kepler16)

#Imprimimos la lista de estrellas ordenadas por masa.
print(f"Lista de estrellas del sistema ordenadas por masa:\n {[estrella.nombre for estrella in sistema_jerarquico.devolver_por_masa()]}")

#Imprimimos los nombres de las estrellas seguidos de la lista ordenada de letras del abecedario.
print(f"Nombres de las estrellas del sistema ordenadas según las letras del abecedario:\n {sistema_jerarquico.devolver_por_nombres()}")
