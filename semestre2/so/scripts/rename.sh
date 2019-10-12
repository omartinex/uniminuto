#!/bin/bash
WORKDIR='/tmp/txtfiles'

# Borrar y crear workdir
rm -rf $WORKDIR
mkdir $WORKDIR

# Crear archivos temporales con extensión txt
echo -e '[+] Creando archivos temporales. \n'
for i in {1..10}
do                                               
    tempfile -s .txt -d $WORKDIR > /dev/null
done
clear
# 
echo -e '\n[+] Buscando arhivos con x o X en el nombre. \n'
cd $WORKDIR
find . -regex '.*[xX].*.txt' 

echo -e '\n[+] Renombrando arhivos a md.'

for f in `find . -regex '.*[xX].*.txt'`; do 
    mv -- "$f" "${f%.txt}.md"
done

echo -e '\n[+] Archivos .md en el directorio:'
ls -1 $WORKDIR/*.md
echo -e ""
