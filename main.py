
def main():
    while True:
        nombre = input("¿A quién quiere saludar? ('exit' para salir): ")
        if nombre.lower() == 'exit':
            print("¡Hasta luego!")
            break
        print(f"Hola {nombre}. ¡Encantado de conocerte!")

if __name__ == "__main__":
    main()
