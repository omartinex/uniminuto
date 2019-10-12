#!/bin/bash
echo -e "****************************************************************"
echo -e "*			Menú de opciones			*"
echo -e "****************************************************************"

echo -e "1. Comprimir con gzip sólo los archivos con extensión '.conf' en el directorio '/etc'"
echo -e "2. Cambiar extensión de los ficheros que contengan una x en su nombre de .txt a .md"
echo -e "3. Copiar todos los archivos (no directorios) en '/etc' a una carpeta creada en el directorio /home"
echo -e "4. Nombres y Apellidos "
echo -e "5. Salir" 

echo -e "Digite el número de la opción que desea: "
read OPTION

case $OPTION in
     1)
          sudo ./gzipConfFiles.sh 
          ;;
     2)
	  ./rename.sh
          ;;
     3)
	  ./copyFiles.sh
          ;;
     4)
	  ./nombre.sh
          ;;
     5)
	  exit
          ;;
     *)
          echo "Debe digitar el número de la opción."
	  exit
          ;;
esac
