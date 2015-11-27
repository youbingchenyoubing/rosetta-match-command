#!/bin/bash
if [ ! -f "$3" ];then
echo "the file named $3 will be bulid autoly"
else
echo "there are already have a file named $3"
mv $3 $3_copy
echo "the previous file named $3 have a rename"
fi
#cd /home/rosetta/screentest
#loop=0
#loop1=1

for i in `ls *.multigraft.log`

do 
  #loop=expr $loop+1
  printf '%s\n' $i 
  python getdesign.py -c $1 -r $2 -f $i -f1 $3
done



python gettopdesign.py -f $3

echo "have counted done"


