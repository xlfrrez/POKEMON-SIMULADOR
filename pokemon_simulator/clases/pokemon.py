class Pokemon:
    cantidad_pokemon = 0

    def __init__(self, nombre, tipo, nivel=1, ataque=15, defensa=8, salud=100):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        self.salud_maxima = salud
        Pokemon.cantidad_pokemon += 1
        print(f"¡{self.nombre} ha sido creado! ")

    def __del__(self):
        print(f"{self.nombre} ha sido liberado")

    def entrenar(self, *estadisticas):
        """Sube de nivel y mejora una o mas estadisticas.
        Si no se indican estadisticas, mejora ataque, defensa y salud.
        """
        permitidas = {"ataque", "defensa", "salud"}
        if not estadisticas:
            estadisticas = ("ataque", "defensa", "salud")
        
        elegidas = []
        for estadistica in estadisticas:
            nombre_estadistica = str(estadistica).lower()
            if nombre_estadistica not in permitidas:
                print(f"Estadistica no valida: {estadistica}")
                print("Usa: ataque, defensa o salud.")
                return
            if nombre_estadistica not in elegidas:
                elegidas.append(nombre_estadistica)

        self.nivel += 1
        for estadistica in elegidas:
            if estadistica == "ataque":
                self.ataque += 5
            elif estadistica == "defensa":
                self.defensa += 3
            elif estadistica == "salud":
                self.salud_maxima += 10
                self.salud = min(self.salud + 10, self.salud_maxima)

        print(f"¡{self.nombre} subio al nivel {self.nivel}!")
        print("Estadisticas mejoradas: " + ", ".join(elegidas))

    def mostrar_info(self):
        print("\n--- Informacion del Pokemon ---")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Nivel: {self.nivel}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Salud: {self.salud}/{self.salud_maxima}")

    def atacar(self, objetivo):
        """Ataca a otro Pokemon; el daño minimo es 1."""
        if self.salud <= 0:
            print(f"{self.nombre} no puede atacar porque esta debilitado.")
            return

        if objetivo.salud <= 0:
            print(f"{objetivo.nombre} ya esta debilitado.")
            return

        dano = max(1, self.ataque - objetivo.defensa)
        objetivo.salud = max(0, objetivo.salud - dano)
        print(
            f"{self.nombre} ataco a {objetivo.nombre} "
            f"e hizo {dano} puntos de daño."
        )
        print(f"Salud restante de {objetivo.nombre}: {objetivo.salud}")

    def calcular_poder(self):
        """Calcula una puntuacion sencilla del poder total."""
        return self.ataque + self.defensa + self.salud

    @classmethod
    def total_pokemons(cls):
        """Muestra cuantos Pokemon estan registrados en el simulador."""
        print(f"Pokemon registrados: {cls.cantidad_pokemon}")
        return cls.cantidad_pokemon
