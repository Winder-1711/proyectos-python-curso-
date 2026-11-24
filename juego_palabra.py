import random  # 👈 Esta línea le enseña a Python qué es 'random'

# Tu banco de palabras y configuraciones
BANCO_PALABRAS = {
    "PYTHON": "Lenguaje de programación versátil y muy popular.",
    "VARIABLE": "Espacio en memoria para almacenar un dato.",
    "FUNCION": "Bloque de código reutilizable definido con def.",
    "DICCIONARIO": "Estructura de datos basada en pares clave-valor.",
    "BUCLE": "Estructura para repetir instrucciones (como while o for).",
    "CODIGO": "Instrucciones escritas que la computadora ejecuta.",
} 

CONFIG_JUEGO = (6,)  # Intentos, Pistas 

def obtener_tablero(palabra, letras_adivinadas):
    tablero = []
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero.append(letra)
        else:
            tablero.append("_")
    return " ".join(tablero)

#Otra forma de hacerlo con comprensión de listas
#def obtener_tablero(palabra, letras_adivinadas):
    #return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])


#print(obtener_tablero("PYTHON", set()))  # Salida: "_ _ _ _ _ _"
#print(obtener_tablero("PYTHON", {"P", "O"}))  # Salida: "P _ _ _ O _"

def jugar():
    palabra_secreta = random.choice(list(BANCO_PALABRAS.keys()))
    pista = BANCO_PALABRAS[palabra_secreta]

    letras_adivinadas = set()
    letras_incorrectas = set() # Registro de letras falladas
    vidas = CONFIG_JUEGO[0]

    print("🎮 ¡BIENVENIDO A ADIVINA LA PALABRA!")
    print(f"\n💡 Pista: {pista}")

    while vidas > 0:
        print(f"\nTablero: {obtener_tablero(palabra_secreta, letras_adivinadas)}")
        print(f"❤️ Vidas restantes: {vidas}")
        if letras_incorrectas:
            print(f"❌ Letras descartadas: {', '.join(sorted(letras_incorrectas))}")
        intento = input("Ingresa una letra: ").strip().upper()

    # 1. Validación de entrada: una sola letra válida
        if len(intento) != 1 or not intento.isalpha():
            print("⚠️ Por favor, ingresa solo una letra válida.")
            continue

    # 2. Verificar si la letra ya fue usada
        if intento in letras_adivinadas or intento in letras_incorrectas:
            print(f"ℹ️ Ya habías probado con la letra '{intento}'. Intenta otra.")
            continue

    # 3. Lógica de acierto o fallo
        if intento in palabra_secreta:
            letras_adivinadas.add(intento)
            print(f"✅ ¡Bien hecho! La letra '{intento}' está en la palabra.")
        else:
            letras_incorrectas.add(intento)
            vidas -= 1
            print(f"❌ La letra '{intento}' no está en la palabra. Pierdes una vida.")

    # 4. Condición de victoria:
    # ¿Todas las letras de la palabra secreta ya están en letras_adivinadas?
        if set(palabra_secreta).issubset(letras_adivinadas):
            print(f"\n🎉 ¡FELICITACIONES! Adivinaste la palabra: {palabra_secreta}")
            return

# Si sale del bucle porque vidas llegó a 0, o se acaban las vidas
    print(f"\n💀 ¡Fin del juego! Te has quedado sin vidas.")
    print(f"La palabra secreta era: {palabra_secreta}")


# Iniciar el juego
jugar()
