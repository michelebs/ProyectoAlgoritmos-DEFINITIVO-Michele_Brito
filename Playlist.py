# Traer información del otro archivo
from Cancion import Cancion, crear_cancion

# Creación de la clase playlist
class Playlist:
    def __init__(self,codigo,name, descripcion, creador, canciones, userslike):
        self.codigo = codigo
        self.name = name
        self.descripcion = descripcion
        self.creador = creador
        self.canciones = canciones
        self.userslike = userslike

# Función para la creación de una playlist
def crearPlaylist(playlist_data, usuarios, canciones):
    
    songList = []
    for track in playlist_data['tracks']:
        for cancion in canciones:
            if cancion.codigo == track:
                songList.append(cancion)
                break 
    playlist = Playlist(
        codigo=playlist_data['id'],
        name=playlist_data['name'],
        descripcion=playlist_data['description'],
        creador=playlist_data['creator'],
        canciones= songList,
        userslike = []
    )
    # Buscar el usuario correspondiente según el ID del creador
    for usuario in usuarios:
        if usuario.codigo == playlist.creador:
            usuario.savedPlaylists.append(playlist)
            break
    return playlist