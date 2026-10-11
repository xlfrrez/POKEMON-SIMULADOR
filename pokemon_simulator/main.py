from clases.pokemon import Pokemon

pokemones = []


def buscar_pokemon(nombre):
    """Busca un Pokemon por nombre y devuelve el objeto o None."""
    for pokemon in pokemones:
        if pokemon.nombre.lower() == nombre.lower():
            return pokemon
    return None


def capturar_pokemon():
    print("\n--- Capturar Pokemon ---")
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("El nombre no puede quedar vacio.")
        return

    if buscar_pokemon(nombre):
        print("Ya existe un Pokemon con ese nombre.")
        return

    tipo = input("Tipo: ").strip()
    if not tipo:
        print("El tipo no puede quedar vacio.")
        return
    
    pokemon = Pokemon(nombre, tipo)
    pokemones.append(pokemon)
    print(f"¡{nombre} fue agregado al equipo!")


def seleccionar_pokemon(mensaje="Escribe el nombre del Pokemon: "):
    nombre = input(mensaje).strip()
    pokemon = buscar_pokemon(nombre)
    if pokemon is None:
        print("No se encontro ese Pokemon.")
    return pokemon


def entrenar_pokemon():
    pokemon = seleccionar_pokemon("¿Que Pokemon quieres entrenar? ")
    if pokemon is None:
        return

    print("1. Mejorar todas las estadisticas")
    print("2. Mejorar una estadistica")
    print("3. Mejorar dos estadisticas")
    opcion = input("Elige una opcion: ").strip()

    if opcion == "1":
        pokemon.entrenar()
    elif opcion == "2":
        estadistica = input("Cual (ataque, defensa, salud): ").strip().lower()
        pokemon.entrenar(estadistica)
    elif opcion == "3":
        primera = input("Primera (ataque, defensa, salud): ").strip().lower()
        segunda = input("Segunda (ataque, defensa, salud): ").strip().lower()
        pokemon.entrenar(primera, segunda)
    else:
        print("Opcion no valida.")


def mostrar_pokemones():
    if not pokemones:
        print("Todavia no has capturado ningun Pokemon.")
        return

    for pokemon in pokemones:
        pokemon.mostrar_info()
        print(f"Poder total: {pokemon.calcular_poder()}")


def combatir():
    if len(pokemones) < 2:
        print("Necesitas al menos dos Pokemon para combatir.")
        return

    print("Pokemon disponibles:")
    for pokemon in pokemones:
        print(f"- {pokemon.nombre} (salud: {pokemon.salud})")

    atacante = seleccionar_pokemon("¿Quien va a atacar? ")
    if atacante is None:
        return

    objetivo = seleccionar_pokemon("¿A quién va a atacar? ")
    if objetivo is None:
        return

    if atacante is objetivo:
        print("Un Pokemon no puede atacarse a si mismo.")
        return

    atacante.atacar(objetivo)


def liberar_pokemon():
    pokemon = seleccionar_pokemon("¿Que Pokemon quieres liberar? ")
    if pokemon is None:
        return

    nombre = pokemon.nombre
    pokemones.remove(pokemon)
    # Se actualiza el contador de la clase al retirar el Pokémon del equipo.
    Pokemon.cantidad_pokemon = max(0, Pokemon.cantidad_pokemon - 1)
    print(f"{nombre} fue retirado del equipo.")


def menu():
    while True:
        print("\n========== SIMULADOR POKEMON ==========")
        print("1. Capturar Pokemon")
        print("2. Entrenar Pokemon")
        print("3. Ver informacion de todos")
        print("4. Combatir")
        print("5. Calcular total de Pokemon")
        print("6. Liberar Pokemon")
        print("0. Salir")

        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            capturar_pokemon()
        elif opcion == "2":
            entrenar_pokemon()
        elif opcion == "3":
            mostrar_pokemones()
        elif opcion == "4":
            combatir()
        elif opcion == "5":
            Pokemon.total_pokemons()
        elif opcion == "6":
            liberar_pokemon()
        elif opcion == "0":
            print("¡Gracias por usar el simulador Pokemon!")
            break
        else:
            print("Opcion no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
