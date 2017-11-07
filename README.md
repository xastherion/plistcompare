# plistcompare
Este Script tiene la finalidad de comparar listas de preferencias de la forma diff.

lo especial del script es su especificidad adaptada a los cambios en las listas de preferencias en las mac,
con la finalidad de ayudar a los administradores de macos a encontrar cambios despues de cambiar preferencias
a traves de los medios tradicionales.

Como funciona:

1.- Corres el script, asi él realizará una Screen de la carpeta de preferencias

2.- Haces el cambio en la configuracion que deseas p.e. fondo de pantalla

3.- Encuentras los archivos cambiados recientemente

4.- Comparas los cambios

5.- Puedes usar TM para retroceder en el Tiempo y obtener el archivo antiguo

Herramientas adicionales:


Junto a plistcompare he programado multi_command_executer.py que tiene la habilidad de escribir preferencias. No es un editor de preferencias especializado. Realmente es un simple "ejecutador de comandos" pero la idea no es ejecutar un comando cat o ls que son cortos he inolvidables, sino que es editar estas listas de preferencias que siempre hay que volver a editar, y que ademas a veces hay que modificar un poco. 

Cuando el Administrador tiene estas preferencias bien identificadas, puede agregarlas a la lista lista_cmd y apareceran como comandos por defecto en las entradas del programa.

Todavia tengo por objetivo, eliminar las funciones para cada comando, pues es mas lógico en un contador controle la cantidad de comandos y veces que la funcion se ejecuta, pero mis pocos conocimientos de python todavia no me lo han permitido.
