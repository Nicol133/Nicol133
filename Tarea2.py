# Tarea 2 - Programación en Python para Mecatrónica
# Autor: Jimena Nicol Flores Prieto
# Fecha: 30/6/2025
# Universidad: Hispanoamericana
# Profesor: Alejandro Hernández Lobo
# Descripción: Programa para reemplazar caracteres en una cadena de texto de Rutaoriginal.txt

def reemplazar_caracteres(entrada, reemplazos):
    """Reemplaza caracteres en una cadena de texto según un diccionario de reemplazos."""
    for original, nuevo in reemplazos.items():
        entrada = entrada.replace(original, nuevo)
    return entrada

def main():
    # Leer el archivo de entrada
    with open('Rutaoriginal.txt', 'r', encoding='utf-8') as archivo:
        entrada = archivo.read()
    # Definir los caracteres a reemplazar
    reemplazos = {
        'a': '1',
        'e': '2',
        'i': '3',
        'o': '4',
        'u': '5',
        'A': '6',
        'E': '7',
        'I': '8',
        'O': '9',
        'U': '0'
    }
    # Reemplazar los caracteres
    entrada_reemplazada = reemplazar_caracteres(entrada, reemplazos)
    # Guardar el resultado en un nuevo archivo
    with open('condimentos_reemplazados.txt', 'w', encoding='utf-8') as archivo_salida:
        archivo_salida.write(entrada_reemplazada)
    print("Reemplazo completado. Archivo guardado como 'condimentos_reemplazados.txt'.")

if __name__ == "__main__":
    main()