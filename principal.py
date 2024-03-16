import requests
from Request import leerApi
from User import Usuario, crear_usuario, Musico, Escucha
from Album import Album, crear_album
from Playlist import Playlist, crearPlaylist
from Cancion import Cancion, crear_cancion

# URLs de los archivos JSON que contienen la información de usuarios, álbumes y listas de reproducción
urlPersonas = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json"
urlAlbums = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json"
urlPlaylists = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json"

# Menú Principal del programa

# Obtener los datos de los archivos JSON a través de una función leerApi
personasJSON = leerApi(urlPersonas)
albumsJSON = leerApi(urlAlbums)
playlistsJSON = leerApi(urlPlaylists)

# Listas para almacenar objetos de usuarios, músicos, álbumes, listas de reproducción, canciones y escuchas
Usuarios = []
Escuchas = []
Musicos = []
albums = []
playlists = []
songs = []

# Crear objetos de usuario a partir de los datos obtenidos del JSON y clasificarlos como oyentes o músicos
for datausuario in personasJSON:
    usuario = crear_usuario(datausuario)
    if usuario.type == 'listener':
        Usuarios.append(usuario)
        Escuchas.append(usuario)
    elif usuario.type == 'musician':
        Usuarios.append(usuario)
        Musicos.append(usuario)
    else:
        print("Error al crear el usuario")

# Crear objetos de álbum y agregar las canciones a la lista de canciones
for albumJSON in albumsJSON:
    album = crear_album(albumJSON, Musicos)

    albums.append(album)
    for track in album.tracks:
        songs.append(track)

# Crear objetos de lista de reproducción y asociarlas con usuarios y canciones correspondientes
for playlist in playlistsJSON:
    Newplaylist = crearPlaylist(playlist, Usuarios, songs)
    playlists.append(Newplaylist)

# Función principal del programa
def main():
    print("------------BIENVENIDO AL SISTEMA DE METROFY----------------")
        
    while True:
        opcion = input('Selecciona 1 para entrar al sistema de gestión de usuarios\nSelecciona 2 para entrar al sistema de gestion musical\nSelecciona 3 para entrar a gestion de interacciones\nSelecciona 4 para la gestion de moderacion\nSelecciona 5 para salir\n')
        while not opcion == '1' and not opcion == '2' and not opcion == '3' and not opcion == '4' and not opcion == '5':
            print("Opcion invalida")
            opcion = input('Selecciona 1 para entrar al sistema de gestión de usuarios\nSelecciona 2 para entrar al sistema de gestion musical\nSelecciona 3 para entrar a gestion de interacciones\nSelecciona 4 para la gestion de indicadores (moderacion)\nSelecciona 5 para salir\n')
        if opcion == '1':
            print("Has seleccionado la gestion de usuarios\n")
            print("\n------------BIENVENIDO AL SISTEMA DE GESTION DE PERFILES----------------\n")
            while True:
                opcion = input("Presiona 1 para registrar nuevos usuarios\nPresiona 2 para buscar usuarios por el nombre\nPresiona 3 para actualizar tu informacion\nPresiona 4 para borrar tu informacion\nPresiona 5 para salir del modulo")
                while not opcion == '1' and not opcion == '2' and not opcion == '3' and not opcion == '4' and not opcion == '5':
                    print("Opcion invalida")
                    opcion = input("Presiona 1 para registrar nuevos usuarios\nPresiona 2 para buscar usuarios por el nombre\nPresiona 3 para actualizar tu informacion\nPresiona 4 para borrar tu informacion\nPresiona 5 para salir del modulo")
                if opcion == '1':
                    print("\nHas seleccionado la opcion de registrar nuevos usuarios\n")
                        
                    CI = input("Introduce la CI del usuario\n")
                    while not CI.isnumeric():
                        print("opcion invalida\n")
                        CI = input("Introduce la CI del usuario\n")
                    nombre = input("Introduce el nombre del nuevo usuario\n")
                    correo = input("\nIntroduce el correo del nuevo usuario\n")
                    tipo = input("\nIntroduce el tipo de usuario: 1 para Escucha, 2 para Musico\n")
                    while not tipo == '1' and not tipo == '2':
                        print("Opcion invalida")
                        tipo = input("\nIntroduce el tipo de usuario: 1 para Escucha, 2 para Musico\n")
                    if tipo == '1':
                        datausuario = {'id': CI ,'name': nombre, 'email': correo, 'type': 'listener'}
                        usuario = crear_usuario(datausuario)
                        Usuarios.append(usuario)
                        Escuchas.append(usuario)
                    elif tipo == '2':
                        datausuario = {'id': CI , 'name': nombre, 'email': correo, 'type': 'musician'}
                        usuario = crear_usuario(datausuario)
                        Musicos.append(usuario)
                        Usuarios.append(usuario)
                        
                    print("\nUsuario registrado con exito...\n")
                elif opcion == '2':
                    
                    print("\nHas seleccionado la opcion de buscar usuarios por el nombre\n")
                    for usuario in Usuarios:
                        print("\nNombre: " + usuario.nombre + "\n")
                    nombre = input("Introduce el nombre del usuario que deseas buscar\n")
                    for usuario in Usuarios:
                        if usuario.nombre == nombre:
                            print('\nAccediendo al perfil de: ' + usuario.nombre)
                            print('nombre: ' + usuario.nombre + 'correo: ' + usuario.correo + 'tipo :' + usuario.type + '\n')
                            if usuario.type == 'listener':
                                likedMusicos = ''
                                likedsongs= ''
                                likedalbums = ''
                                savedPlaylists = ''
                                for musico in usuario.likedMusicos:
                                    likedMusicos += musico.nombre + '\n'
                                for song in usuario.likedSongs:
                                    likedsongs += song.nombre + '\n'
                                for album in usuario.likedAlbums:
                                    likedalbums += album.name + '\n'
                                for playlist in usuario.savedPlaylists:
                                    savedPlaylists += playlist.name + '\n'
                                print('Artistas que le gustan: ' + likedMusicos + 'Canciones que le gustan: ' + likedsongs + '\n' + 'Albumes que le gustan: ' + likedalbums + '\n' + 'Playlist que ha guardado: ' + savedPlaylists + '\n')
                            elif usuario.type == 'musician':
                                albumsUser = ''
                                topSongs = ''
                                for album in usuario.albums:
                                    albumsUser += album.name + '\n'
                                for song in usuario.Topsongs:
                                    topSongs += song.name + '\n'
                                print('Albumes que ha creado: ' + albumsUser +  '\n' + 'Total de reproducciones: ' + str(usuario.TotalReproducciones) + '\n' + 'Canciones mas escuchadas: ' + topSongs + '\n')
                                listen = input('Presiona 1 para escuchar alguna cancion\nPresiona 2 si no quieres escuchar ninguna canción\n')
                                while not listen == '1' and not listen == '2':
                                    print("Opcion invalida")
                                    listen = input('Presiona 1 para escuchar alguna cancion\nPresiona 2 si no quieres escuchar ninguna canción\n')
                                if listen == '1':
                                    for album in usuario.albums:
                                        print("nombre album: " + album.name + '\n')
                                        for song in album.tracks:
                                            print('nombre cancion: ' + song.nombre + '\n')
                                        print()
                                    cancion = input('Introduce el nombre de la cancion que quieras escuchar\n')
                                    for album in usuario.albums:
                                        for song in album.tracks:
                                            if song.nombre == cancion:
                                                print('Reproduciendo: ' + song.nombre + '\n')
                                                song.reproducciones += 1
                                                usuario.TotalReproducciones += 1
                                                album.totalReproducciones += 1
                                                break
                            break
                elif opcion == '3':
                    print("\nHas seleccionado la opcion de actualizar tu informacion\n")
                    CI = input('Introduce tu codigo de usuario\n')
                    encontrado = False
                    for usuario in Usuarios:
                        if usuario.codigo == CI:
                            nombre = input("Introduce tu nombre\n")
                            correo = input("Introduce tu correo\n")
                            usuario.nombre = nombre
                            usuario.correo = correo
                            print('Informacion actualizada con exito\n')
                            encontrado = True
                            break

                    if encontrado == False:
                        print("No se ha conseguido el usuario\n")
                elif opcion == '4': 
                    print("\nHas seleccionado la opcion de borrar tu informacion\n")
                    CI = input('Introduce tu codigo de usuario\n')
                    encontrado =  False
                    for usuario in Usuarios:
                        if usuario.codigo == CI:
                            if usuario.type == 'listener':
                                Usuarios.remove(usuario)
                                Escuchas.remove(usuario)
                            elif usuario.type == 'musician':
                                Usuarios.remove(usuario)
                                Musicos.remove(usuario)

                            print('Usuario eliminado con exito\n')
                            encontrado = True
                            break
                    if encontrado == False:
                        print("No se ha conseguido el usuario\n")
                elif opcion == '5':
                    print("Saliendo del modulo de gestion de usuarios...\n")
                    break
        elif opcion == '2':
            print("Has seleccionado al  sistema de Gestion Musical\n")
            print("\nBIENVENIDO AL SISTEMA DE GESTION MUSICAL\n")
            while True:
                opcion = input("Presiona 1 para registrar un nuevo Album\nPresiona 2 para escuchar una cancion\nPresiona 3 para crear una playlist\nPresiona 4 para salir del modulo\n")
                while not opcion == '1' and not opcion == '2' and not opcion == '3' and not opcion == '4':
                    print("Opcion invalida")
                    opcion = input("Presiona 1 para registrar un nuevo Album\nPresiona 2 para escuchar una cancion\nPresiona 3 para crear una playlist\nPresiona 4 para salir del modulo\n")
                if opcion == '1':
                    CI = input("Introduce tu ID de musico\n")
                    encontrado = False
                    for musico in Musicos:
                        if musico.codigo == CI:
                            encontrado = True
                            codigo = input('Introduce el codigo del album\n')
                            nombre = input("Introduce el nombre del album\n")
                            fecha = input("Introduce la fecha de lanzamiento\n")
                            portada = input("Introduce el link de la portada del album\n")
                            descrip = input('Introduce el descripcion del album\n')
                            genero= input('Introduce el genero del album\n')
                            tracklist = []

                            while True:
                                codigo = input("Ingresa el codigo de la cancion\n")
                                cancion = input("Introduce el nombre de la cancion\n")
                                duracion = input("Introduce la duracion de la cancion\n")
                                link = input("Introduce el link de la cancion\n")
                                newsong = crear_cancion({'id': codigo, 'name': cancion, 'duration': duracion, 'link': link, 'reproducciones': 0})
                                tracklist.append(newsong)
                                opcion = input("Presiona 1 para agregar otra cancion\nPresiona 2 para aceptar\n")
                                while not opcion == '1' and not opcion == '2':
                                    print("Opcion invalida")
                                    opcion = input("Presiona 1 para agregar otra cancion\nPresiona 2 para aceptar\n")
                                if opcion == '2':
                                    break

                            newAlbum =  Album(codigo, nombre, descrip,  portada,  fecha,  genero, CI,  tracklist, [],0)
                            albums.append(newAlbum)
                            for musico in Musicos:
                                if musico.codigo == CI:
                                    musico.albums.append(newAlbum)
                                    break
                            print("Album creado con exito\n")
                            


                            break
                    if encontrado == False:
                        print("Musico no encontrado\n")
                elif opcion == '2':
                    print("Has seleccionado escuchar una cancion\n")
                    opcion = input("Selecciona 1 para buscar cancion por album o nombre\nSelecciona 2 si quieres ver las playlist disponibles\n")
                    while not opcion == '1' and not opcion == '2':
                        print("Opcion invalida")
                        opcion = input("Selecciona 1 para buscar cancion por album o nombre\nSelecciona 2 si quieres ver las playlist disponibles\n")
                    if opcion == '1':
                        opcion = input("Selecciona 1 para buscar por album\nSelecciona 2 para buscar por nombre\n")
                        while not opcion == '1' and not opcion == '2':
                            print("Opcion invalida")
                            opcion = input("Selecciona 1 para buscar por album\nSelecciona 2 para buscar por nombre\n")
                        if opcion == '1':
                            for album in albums:
                                print("Nombre: " + album.name + "\n")
                            nombre = input("Introduce el nombre del album\n")
                            for album in albums:
                                if album.name == nombre:
                                    for song in album.tracks:
                                        print("Nombre: " + song.nombre + "\n")
                                    cancion = input("Introduce el nombre de la cancion que quieres escuchar\n")
                                    for song in album.tracks:
                                        if song.nombre == cancion:
                                            print('Reproduciendo: ' + song.nombre + '\n')
                                            song.reproducciones += 1
                                            for musico in Musicos:
                                                if musico.codigo == album.artist:
                                                    musico.TotalReproducciones += 1
                                                    break
                                            break

                        elif opcion == '2':
                            for song in songs:
                                print("Nombre: " + song.nombre + "\n")
                            nombre = input("Introduce el nombre de la cancion que quieres escuchar\n")
                            for song in songs:
                                if song.nombre == nombre:
                                    print('Reproduciendo: ' + song.nombre + '\n')
                                    song.reproducciones += 1
                                    break
                    elif opcion == '2':
                        for playlist in playlists:
                            print("Nombre: " + playlist.name + "\n")
                        nombre = input("Introduce el nombre de la playlist que quieres escuchar\n")
                        for playlist in playlists:
                            if playlist.name == nombre:
                                for song in playlist.canciones:
                                    print("Nombre: " + song.nombre + "\n")
                                cancion = input("Introduce el nombre de la cancion que quieres escuchar\n")
                                for song in playlist.canciones:
                                    if song.nombre == cancion:
                                        print('Reproduciendo: ' + song.nombre + '\n')
                                        song.reproducciones += 1
                                        for musico in Musicos:
                                            if musico.codigo == album.artist:
                                                musico.TotalReproducciones += 1
                                                break
                                        break
                elif opcion == '3':
                    print("Has seleccionado la opcion de crear una playlist\n")
                    CI = input("Introduce tu ID de usuario\n")
                    encontrado = False
                    for escucha in Escuchas:
                        if CI == escucha.codigo:
                            encontrado = True
                            codigo = input("Introduce el codigo de la playlist\n")
                            nombrePl = input("Introduce el nombre de la playlist\n")
                            descrip = input("Introduce la descripcion de la playlist\n")
                            tracklist = []
                            while True:
                                opcion = input("Selecciona 1 para buscar canciones por Nombre\nSelecciona 2 para buscar canciones por artista\nSelecciona 3 para buscar canciones por album\nSelecciona 4 para buscar canciones por playlist\n")
                                while not opcion == '1' and not opcion == '2' and not opcion == '3' and not opcion == '4':
                                    print("Opcion invalida")
                                    opcion = input("Selecciona 1 para buscar canciones por Nombre\nSelecciona 2 para buscar canciones por artista\nSelecciona 3 para buscar canciones por album\nSelecciona 4 para buscar canciones por playlist\n")
                                if opcion == '1':
                                    for song in songs:
                                        print("Nombre: " + song.nombre + "\n")
                                    cancion = input("Introduce el nombre de la cancion que quieres agregar\n")
                                    for song in songs:
                                        if song.nombre == cancion:
                                            tracklist.append(song)
                                            break

                                elif opcion == '2':
                                    for musico in Musicos:
                                        print("Nombre: " + musico.nombre + "\n")
                                    nombre = input("Introduce el nombre del músico\n")
                                    musico_encontrado = False
                                    for musico in Musicos:
                                        if musico.nombre == nombre:
                                            musico_encontrado = True
                                            for album in musico.albums:
                                                for song in album.tracks:
                                                    print("Nombre: " + song.nombre + "\n")
                                                cancion = input("Introduce el nombre de la canción que quieres agregar\n")
                                                for song in album.tracks:
                                                    if song.nombre == cancion:
                                                        tracklist.append(song)
                                                        break
                                                break
                                            break
                                    if not musico_encontrado:
                                        print("No se encontró ningún músico con ese nombre.")
                                elif opcion == '3':
                                    for album in albums:
                                        print("Nombre: " + album.name + "\n")
                                    nombre = input("Introduce el nombre del album\n")
                                    album_encontrado = False
                                    for album in albums:
                                        if album.name == nombre:
                                            album_encontrado = True
                                            for song in album.tracks:
                                                print("Nombre: " + song.nombre + "\n")
                                            cancion = input("Introduce el nombre de la canción que quieres agregar\n")
                                            for song in album.tracks:
                                                if song.nombre == cancion:
                                                    tracklist.append(song)
                                                    break
                                            break
                                    if not album_encontrado:
                                        print("No se encontró ningún álbum con ese nombre.")
                                elif opcion == '4':
                                    for playlist in playlists:
                                        print("Nombre: " + playlist.name + "\n")
                                    nombre = input("Introduce el nombre de la playlist\n")
                                    playlist_encontrada = False
                                    for playlist in playlists:
                                        if playlist.name == nombre:
                                            playlist_encontrada = True
                                            for song in playlist.canciones:
                                                print("Nombre: " + song.nombre + "\n")
                                            cancion = input("Introduce el nombre de la canción que quieres agregar\n")
                                            for song in playlist.canciones:
                                                if song.nombre == cancion:
                                                    tracklist.append(song)
                                                    break
                                            break
                                    if not playlist_encontrada:
                                        print("No se encontró ninguna playlist con ese nombre.")
                                opcion = input("Presiona 1 para agregar otra cancion\nPresiona 2 para aceptar\n")
                                while not opcion == '1' and not opcion == '2':
                                    print("Opcion invalida")
                                    opcion = input("Presiona 1 para agregar otra cancion\nPresiona 2 para aceptar\n")
                                if opcion == '2':
                                        break
                            newPlaylist = Playlist(codigo, nombrePl, descrip, CI, tracklist, [])
                            playlists.append(newPlaylist)
                            for escucha in Escuchas:
                                if escucha.codigo == CI:
                                    escucha.savedPlaylists.append(newPlaylist)
                                    break
                            print("Playlist creada con exito\n")
                            break
                elif opcion == '4':
                    print("Saliendo del modulo de Gestion Musical\n")
                    break

        elif opcion == '3':
            print("Has seleccionado la gestion de interacciones\n")
            print("\nBIENVENIDO AL SISTEMA DE GESTION DE INTERACCIONES\n")
            CI = input('Ingresa tu codigo de Escucha')
            for user in Escuchas:
                if user.codigo == CI:
                    print('Bienvenido ' + user.nombre + '\n')
                    break
            opcion = input("Selecciona 1 para interactuar a un musico\nSelecciona 2 para interactuar con una cancion\nSelecciona 3 para interactuar con un album\nSelecciona 4 para interactuar con una playlist\nSelecciona 5 para salir del modulo\n")
            while not opcion == '1' and not opcion == '2' and not opcion == '3' and not opcion == '4' and not opcion == '5':
                print("Opcion invalida")
                opcion = input("Selecciona 1 para interactuar a un musico\nSelecciona 2 para interactuar con una cancion\nSelecciona 3 para interactuar con un album\nSelecciona 4 para interactuar con una playlist\nSelecciona 5 para salir del modulo\n")
            if opcion == '1':
                print("Has seleccionado interactuar con un musico\n")
                opcion = input ("Selecciona 1 para dar like\nSelecciona 2 para quitar un like\n")
                while not opcion == '1' and not opcion == '2':
                    print("Opcion invalida")
                    opcion = input ("Selecciona 1 para dar like\nSelecciona 2 para quitar un like\n")
                if opcion == '1':
                    for musico in Musicos:
                        print("Nombre: " + musico.nombre + "\n")
                    nombre = input("Introduce el nombre del musico\n")
                    for musico in Musicos:
                        if musico.nombre == nombre:
                            musico.userslike.append(CI)
                            user.likedMusicos.append(musico)
                            print("Like agregado con exito\n")
                            break
                elif opcion == '2':
                    for musico in user.likedMusicos:
                        print("Nombre: " + musico.nombre + "\n")
                    nombre = input("Introduce el nombre del musico\n")
                    encontrado = False
                    for musico in Musicos:
                        if musico.nombre == nombre:
                            encontrado = True
                            musico.userslike.remove(CI)
                            user.likedMusicos.remove(musico)
                            print("Like eliminado con exito\n")
                            break
                    if encontrado == False:
                        print("Musico no encontrado\n")

            elif opcion == '2':
                print("Has seleccionado interactuar con una cancion\n")
                opcion = input ("Selecciona 1 para dar like\nSelecciona 2 para quitar un like\n")
                while not opcion == '1' and not opcion == '2':
                    print("Opcion invalida")
                    opcion = input ("Selecciona 1 para dar like\nSelecciona 2 para quitar un like\n")
                if opcion == '1':
                    for song in songs:
                        print("Nombre: " + song.nombre + "\n")
                    nombre = input("Introduce el nombre de la cancion\n")
                    for song in songs:
                        if song.nombre == nombre:
                            song.userslike.append(CI)
                            user.likedSongs.append(song)
                            print("Like agregado con exito\n")
                            break
                elif opcion == '2':
                    for song in user.likedSongs:
                        print("Nombre: " + song.nombre + "\n")
                    nombre = input("Introduce el nombre de la cancion\n")
                    encontrado = False
                    for song in songs:
                        if song.nombre == nombre:
                            encontrado = True
                            song.userslike.remove(CI)
                            user.likedSongs.remove(song)
                            print("Like eliminado con exito\n")
                            break
                    if encontrado == False:
                        print("Cancion no encontrada\n")

            elif opcion == '3':
                print("Has seleccionado interactuar con un album\n")
                opcion = input ("Selecciona 1 para dar like\nSelecciona 2 para quitar un like\n")
                while not opcion == '1' and not opcion == '2':
                    print("Opcion invalida")
                    opcion = input ("Selecciona 1 para dar like\nSelecciona 2 para quitar un like\n")
                if opcion == '1':
                    for album in albums:
                        print("Nombre: " + album.name + "\n")
                    nombre = input("Introduce el nombre del album\n")
                    for album in albums:
                        if album.name == nombre:
                            album.userslike.append(CI)
                            user.likedAlbums.append(album)
                            print("Like agregado con exito\n")
                            break
                elif opcion == '2':
                    for album in user.likedAlbums:
                        print("Nombre: " + album.name + "\n")
                    nombre = input("Introduce el nombre del album\n")
                    encontrado = False
                    for album in albums:
                        if album.name == nombre:
                            encontrado = True
                            album.userslike.remove(CI)
                            user.likedAlbums.remove(album)
                            print("Like eliminado con exito\n")
                            break
                    if encontrado == False:
                        print("Album no encontrado\n")
            
            elif opcion == '4':
                print("Has seleccionado interactuar con una playlist\n")
                opcion = input ("Selecciona 1 para dar like\nSelecciona 2 para quitar un like\n")
                while not opcion == '1' and not opcion == '2':
                    print("Opcion invalida")
                    opcion = input ("Selecciona 1 para dar like\nSelecciona 2 para quitar un like\n")
                if opcion == '1':
                    for playlist in playlists:
                        print("Nombre: " + playlist.name + "\n")
                    nombre = input("Introduce el nombre de la playlist\n")
                    for playlist in playlists:
                        if playlist.name == nombre:
                            playlist.userslike.append(CI)
                            user.savedPlaylists.append(playlist)
                            print("Like agregado con exito\n")
                            break
                elif opcion == '2':
                    for playlist in user.savedPlaylists:
                        print("Nombre: " + playlist.name + "\n")
                    nombre = input("Introduce el nombre de la playlist\n")
                    encontrado = False
                    for playlist in playlists:
                        if playlist.name == nombre:
                            encontrado = True
                            playlist.userslike.remove(CI)
                            user.savedPlaylists.remove(playlist)
                            print("Like eliminado con exito\n")
                            break
                    if encontrado == False:
                        print("Playlist no encontrada\n")
            elif opcion == '5':
                print("Saliendo del Modulo de interacciones\n")
                break


            
        elif opcion == '4':
            print ("Has seleccionado la gestion de moderacion o indicadores\n")
            print("Bienvenido al modulo de Indicadores\n")

            opcion = input("Selecciona 1 para ver los 5 musicos con mas reproducciones\nSelecciona 2 para ver los 5 albumes con mas reproducciones\nSelecciona 3 para ver las 5 canciones con mas reproducciones\nSelecciona 4 para ver las 5 playlist con mas likes\nSelecciona 5 para salir\n")
            while not opcion == '1' and not opcion == '2' and not opcion == '3' and not opcion == '4' and not opcion == '5':
                print("Opcion invalida")
                opcion = input("Selecciona 1 para ver los 5 musicos con mas reproducciones\nSelecciona 2 para ver los 5 albumes con mas reproducciones\nSelecciona 3 para ver las 5 canciones con mas reproducciones\nSelecciona 4 para ver las 5 playlist con mas likes\nSelecciona 5 para salir\n")
            if opcion == '1': 
                print("Has seleccionado ver los 5 musicos con mas reproducciones\n")
                Musicos.sort(key=lambda musico: musico.TotalReproducciones, reverse=True)
                for i in range(5):
                    print("Nombre: " + Musicos[i].nombre + "Reproducciones: " + str(Musicos[i].TotalReproducciones) + "\n")

            elif opcion == '2':
                print("Has seleccionado ver los 5 albumes con mas reproducciones\n")

                albums.sort(key=lambda album: album.totalReproducciones, reverse=True)
                for i in range(5):
                    print("Nombre: " + albums[i].name + "Reproducciones: " + str(albums[i].totalReproducciones) + "\n")
            elif opcion == '3':
                print("Has seleccionado ver las 5 canciones con mas reproducciones\n")
                songs.sort(key=lambda song: song.reproducciones, reverse=True)
                for i in range(5):
                    print("Nombre: " + songs[i].nombre + "Reproducciones: " + str(songs[i].reproducciones) + "\n")
            elif opcion == '4':
                print("Has seleccionado ver las 5 playlist con mas likes\n")
                playlists.sort(key=lambda playlist: len(playlist.userslike), reverse=True)
                for i in range(5):
                    print("Nombre: " + playlists[i].name + "Likes: " + str(len(playlists[i].userslike)) + "\n")
            elif opcion == '5':
                print("Saliendo del modulo de indicadores\n")
                break
        elif opcion == '5':
            print ("ESPERAMOS VOLVER A VERTE PRONTO\n")
            break



                
# Ejecutar la función principal al correr el script
main()
