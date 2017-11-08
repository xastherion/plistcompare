# plistcompare
Este Script tiene la finalidad de comparar listas de preferencias de la forma diff.

lo especial del script es su especificidad adaptada a los cambios en las listas de preferencias en las mac,
con la finalidad de ayudar a los administradores de macos a encontrar cambios despues de cambiar preferencias
a traves de los medios tradicionales.

Como funciona:

1.- Corres el script, asi él realizará una Screen de la carpeta de preferencias

2.- Haces el cambio en la configuración que deseas p.e. fondo de pantalla

3.- Encuentras los archivos cambiados recientemente

4.- Comparas los cambios

5.- Puedes usar TM para retroceder en el Tiempo y obtener el archivo antiguo. O puedes copiar el archivo con otro nombre como .bak antes de cambiarlo

Herramientas adicionales:

Junto a plistcompare he programado multi_command_executer_dict.py que tiene la habilidad de escribir preferencias. No es un editor de preferencias especializado, sino que ealmente es un simple "ejecutador de comandos" pero la idea no es ejecutar un comando "cat" o "ls" que son cortos e inolvidables, sino que es editar listas de preferencias que siempre hay que volver a editar, y que ademas a veces hay que modificar un poco y que por lo general son largos comandos con direcciones. 

Cuando el Administrador tiene estas preferencias bien identificadas, puede agregarlas al diccionario "lista_cmd" y apareceran como comandos por defecto en las entradas del programa.

TO-DO´s:

- Todavía me falta implementar un archivo de comandos.txt para guardar los comandos separadamente del código. Para esto tengo casi listo el "file_command_executer.py" que ya lo hace, solo debo unirlo a este actual
- Crear una rutina que guarde un nuevo comando en el archivo de comandos, para no tener que estar cambiando el código. Aqui creo que alcanza un botoncito adicional en el programa principal que llame a una unica ventana con Entry y boton "Guardar"
- También es casi necesario una etiqueta (Label) que pueda explicar brevemente lo que hace el comando
- El multicommand es bien útil para manejar comandos aislados, y puede ejecutar también scripts con varios commandos. Pero esto puede resultar engorroso de acuerdo a variables de entorno o directorios donde se ejecuta el script. Quiero encontrar un camino fácil para esto. Uno puede ser la opcion "subir script" que permita almacenar el script objetivo en un contenedor único y accesible del programa. Otro (o ambos) podría ser un "Do it!" multilinia. Temporalmente se puede usar & && ó ; para concatenar comandos en una sola linea, claro que en cuanto los comandos sean muchos o muy largos se vuelve complicado.
