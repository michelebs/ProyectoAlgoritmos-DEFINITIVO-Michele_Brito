# Creación de la clase usuario
class Usuario:
    def __init__(self,codigo, nombre, correo, Type):
        self.codigo = codigo
        self.nombre = nombre
        self.correo = correo
        self.type = Type
    
# Creación de las clases heredadas: escucha y músico
class Escucha(Usuario):
    def __init__(self,codigo, nombre, correo, Type, likedSongs, likedAlbums, savedPlaylists, likedMusicos):
        super().__init__(codigo, nombre, correo, Type)
        self.likedSongs = likedSongs
        self.likedAlbums = likedAlbums
        self.savedPlaylists = savedPlaylists
        self.likedMusicos = likedMusicos

class Musico(Usuario):
    def __init__(self,codigo, nombre, correo, Type, albums, Topsongs, TotalReproducciones, userslike):
        super().__init__(codigo , nombre, correo, Type)
        self.albums = albums
        self.Topsongs = Topsongs
        self.TotalReproducciones = TotalReproducciones
        self.userslike = userslike

# Función para la creación de un usuario
def crear_usuario(datausuario):
    if datausuario['type'] == 'listener':
        return Escucha(datausuario['id'],datausuario['name'], datausuario['email'], datausuario['type'], [], [], [],[])
    elif datausuario['type'] == 'musician':
        return Musico(datausuario['id'],datausuario['name'], datausuario['email'], datausuario['type'], [], [], 0, [])
