#!/bin/bash
DSTDIR="/tmp/confFiles"
SRCDIR="/etc"
####################################################################################################
# Crear un script que comprima con gzip sólo los archivos con extensión .conf en el directorio /etc#
####################################################################################################
# Limpiar el Workspace
rm -rf $DSTDIR
# Crear directorio destino en /tmp
mkdir -p $DSTDIR
clear
echo -e '[+] Copiando archivos \n'
# buscar recursivamente los archivos .conf en /etc y copiarlos al directorio temporal
find $SRCDIR -name '*.conf' -exec cp {} $DSTDIR \;
if [ $? -eq 0 ]; then
    echo -e "[+] Archivos copiados con exito.\n"
else
    echo -e "[-] Error.\n"
fi
echo -e "[+] Comprimiendo los archivos. "
cd $DSTDIR
find . -name '*.conf' -exec gzip --verbose {} \;

echo -e "\n [+] Saliendo...."
