# Traer información del otro archivo
from Cancion import crear_cancion, Cancion

# Creación de la clase album
class Album:
    def __init__(self, codigo, name, description, cover, realeseDate, genre, artist, tracks, userslike, totalReproducciones):
        self.codigo = codigo
        self.name = name
        self.description = description
        self.cover = cover
        self.realeseDate = realeseDate
        self.genre = genre
        self.artist = artist
        self.tracks = tracks
        self.userslike = userslike
        self.totalReproducciones = totalReproducciones

# Función para la creación de un album
def crear_album(album_data, musicos):

        
        canciones = []
        for cancion in album_data['tracklist']:
            song = crear_cancion(cancion)
            canciones.append(song)
        album = Album(
            codigo=album_data['id'],
            name=album_data['name'],
            description=album_data['description'],
            cover=album_data['cover'],
            realeseDate=album_data['published'],
            genre=album_data['genre'],
            artist=album_data['artist'],
            tracks=canciones,
            userslike = [],
            totalReproducciones=0
        )
        # Buscar el músico correspondiente según el ID del artista
        for musico in musicos:
            if musico.codigo == album.artist:
                musico.albums.append(album)
                break    

        return album
