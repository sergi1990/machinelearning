import modulofichero

nombre_fichero ='fichero1.txt'
fichero = modulofichero.fichero(nombre_fichero)
    
texto ="sta es la primera fila del fichero.\nEsta sera la segunda fila"
fichero.grabar_fichero(texto)

texto ="\n este es un texto incluido"
fichero.incluir_fichero(texto)

texto_leido = fichero.leer_fichero()
print (texto_leido)