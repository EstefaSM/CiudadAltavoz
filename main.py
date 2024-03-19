bandas=[]
idAleatorio=0
programacionDiaUno = []
programacionDiaDos = []
programacionDiaTres = []

#CONSTRUYENDO LA INTERFAZ
print("*************************")
print("****🤘🏻ALTAVOZ ES TU VOZ🤘🏻****")
print("*************************")

opcion=100
while(opcion!=6):
    print("1. Registrar banda📝")
    print("2. Buscar información de bandas🔎")
    print("3. Ver programación de bandas👀")
    print("4. Modificar información de bandas📝")
    print("5. Eliminar una banda❌")
    print("6. Salir🥺")

    opcion=int(input("Digita una opción: "))

    if opcion==1:
        banda={}
        idAleatorio+=1
        if idAleatorio>100:
            print("Se ha alcanzado el límite de bandas participantes 💔")
        #CREANDO DATOS DEL DICCIONARIO
        banda["id"]=idAleatorio
        banda["nombre"]=input("Nombre de la banda: ")
        banda["genero"]=input("Género: ")
        banda["clasificacion"]=input("Clasificación: ")
        while True:
            try:
                minutos = int(input("Tiempo que tocará la banda(en minutos, máximo 60): "))
                if 0 < minutos <= 60:
                    break
                else:
                    print("El tiempo debe ser un valor entre 1 y 60 minutos.")
            except ValueError:
                print("Ingresa un número válido.")
        
        # Formatear el tiempo como "HH:MM"
        horas = minutos // 60
        minutos = minutos % 60
        formatoTiempo = f"{horas:02d}:{minutos:02d}"
        banda["tiempo"] = formatoTiempo
        banda["costo"]=int(input("Costo: $"))
        
        bandas.append(banda)
        print(f"***La banda {banda['nombre']} se ha agregado con éxito.***")

    elif opcion==2:
        bandaBuscada=input("Digita el nombre de la banda que estás buscando: ")
        bandaEncontrada = []
        for bandaAuxiliar in bandas:
            if bandaAuxiliar["nombre"].lower() == bandaBuscada.lower():
                bandaEncontrada.append(bandaAuxiliar)
        
        if bandaEncontrada:
            for bandaEncontrada in bandaEncontrada:
                print(f"Nombre: {bandaEncontrada['nombre']}")
                print(f"Género: {bandaEncontrada['genero']}")
                print(f"Clasificación: {bandaEncontrada['clasificacion']}")
                print(f"Tiempo que tocará: {bandaEncontrada['tiempo']}")
        else:
            print("¡Ups! No encontramos bandas con ese nombre, inténtalo de nuevo.")

    elif opcion == 3:
        for banda in bandas:
            genero = banda["genero"].lower()
            if "rock" in genero or "punk" in genero or "metal" in genero:
                programacionDiaUno.append(banda)
            elif "ska" in genero or "reggae" in genero or "pop" in genero or "indie" in genero:
                programacionDiaDos.append(banda)
            elif "rap" in genero or "techno" in genero or "electrónica" in genero:
                programacionDiaTres.append(banda)

        print("PROGRAMACIÓN DEL DÍA 1: ROCK | METAL | PUNK:")
        for banda in programacionDiaUno:
            print(f"Nombre: {banda['nombre']}")
            print(f"Género: {banda['genero']}")
            print(f"Clasificación: {banda['clasificacion']}")
            print(f"Tiempo que tocará: {banda['tiempo']}")
            print()
        
        print("\nPROGRAMACIÓN DEL DÍA 2: REGGAE | POP | SKA | INDIE:")
        for banda in programacionDiaDos:
            print(f"Nombre: {banda['nombre']}")
            print(f"Género: {banda['genero']}")
            print(f"Clasificación: {banda['clasificacion']}")
            print(f"Tiempo que tocará: {banda['tiempo']}")
            print()
        
        print("\nPROGRAMACIÓN DEL DÍA 3: ROCK | METAL | PUNK:")
        for banda in programacionDiaTres:
            print(f"Nombre: {banda['nombre']}")
            print(f"Género: {banda['genero']}")
            print(f"Clasificación: {banda['clasificacion']}")
            print(f"Tiempo que tocará: {banda['tiempo']}")
            print()

    elif opcion == 4:
        print("Listado de bandas:")
        for posicion, banda in enumerate(bandas):
            print(f"{posicion + 1}.{banda['nombre']}")

        posicionBanda = int(input("Selecciona el número de la banda a modificar: ")) - 1
        if posicionBanda < 0 or posicionBanda >= len(bandas):
            print("Número de banda inválido.")
        else:
            bandaSeleccionada = bandas[posicionBanda]

            print("\nInformación actual de la banda:")
            print(f"1. Nombre: {bandaSeleccionada['nombre']}")
            print(f"2. Género: {bandaSeleccionada['genero']}")
            print(f"3. Clasificación: {bandaSeleccionada['clasificacion']}")
            print(f"4. Tiempo que tocará: {bandaSeleccionada['tiempo']}")
            print(f"5. Costo: {bandaSeleccionada['costo']}")
            
            modificar = int(input("Selecciona el número del campo a modificar: "))
            if modificar < 1 or modificar > 5:
                print("Número de campo inválido.")
            else:
                valorNuevo = input("Ingresa el nuevo valor: ")

                if modificar == 1:
                    bandaSeleccionada['nombre'] = valorNuevo
                elif modificar == 2:
                    bandaSeleccionada['genero'] = valorNuevo
                elif modificar == 3:
                    bandaSeleccionada['clasificacion'] = valorNuevo
                elif modificar == 4:
                    bandaSeleccionada['tiempo'] = valorNuevo
                elif modificar == 5:
                    bandaSeleccionada['costo'] = valorNuevo

                confirmarModificacion = input("¿Deseas confirmar la modificación? (Si/No): ").lower()
                if confirmarModificacion == 'Si':
                    print("Banda modificada exitosamente.")
                elif confirmarModificacion == 'No':
                    print("Modificación cancelada.")
                else:
                    print("Entrada inválida. Por favor, ingresa 'Si' o 'No'.")

    elif opcion == 5:
        print("Listado de bandas:")
        for posicion, banda in enumerate(bandas):
            print(f"{posicion + 1}. {banda['nombre']}")
        posicionBanda = int(input("Selecciona el número de la banda a eliminar: ")) - 1
        if posicionBanda < 0 or posicionBanda >= len(bandas):
            print("Número de banda inválido.")
        else:
            bandaEliminada = bandas.pop(posicionBanda)
            print(f"Banda '{bandaEliminada['nombre']}' eliminada correctamente.")

    elif opcion == 6:
        pass