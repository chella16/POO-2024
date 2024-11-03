def imprimir_archivos(archivos, nivel=0):
    for archivo in archivos:
        print(" " * (nivel * 4) + archivo["nombre"])  # Imprime el nombre del archivo con indentación
        if "subarchivos" in archivo:  # Si el archivo tiene subarchivos, llama recursivamente a la función
            imprimir_archivos(archivo["subarchivos"], nivel + 1)

# Ejemplo de lista de archivos en formato de árbol
archivos = [
    {"nombre": "archivo1.txt"},
    {"nombre": "carpeta1", "subarchivos": [
        {"nombre": "archivo2.txt"},
        {"nombre": "archivo3.txt"},
        {"nombre": "carpeta2", "subarchivos": [
            {"nombre": "archivo4.txt"},
            {"nombre": "archivo5.txt"},
        ]}
    ]},
    {"nombre": "archivo6.txt"}
]

imprimir_archivos(archivos)
