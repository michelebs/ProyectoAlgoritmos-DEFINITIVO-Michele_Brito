# Creación de la clase canción
class Cancion:
    def __init__(self, codigo, nombre,duracion, link, reproducciones, userslike):
        self.codigo = codigo
        self.nombre = nombre
        self.duracion = duracion
        self.link = link
        self.reproducciones = reproducciones
        self.userslike = userslike

# Función para la creación de una canción
def crear_cancion(cancion_data):
    cancion = Cancion(
        codigo=cancion_data['id'],
        nombre=cancion_data['name'],
        duracion=cancion_data['duration'],
        link=cancion_data['link'],
        reproducciones = 0,
        userslike=[]
    )
    return cancion