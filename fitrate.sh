#!/bin/bash
cd /home/rosetta/pdbID
for file_a in `ls *.pdb`
do
   
  cd /home/rosetta/pdbID
  echo  $file_a >"${file_a%%.*}"
  cd /home/rosetta/screentest
  ./commond2FX7 ${file_a%%.*}
  if [ $? -eq 0 ];then
  echo "$file_a OK" 
  else 
  echo "rm $file_a">>removePDB
  echo "rm ${file_a%%.*}">>removePDB
fi
done 
