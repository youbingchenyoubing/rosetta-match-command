import os
import argparse
import math
from math import fabs
import sys
#import pdb  #debug python program , is equal to gdb


def partion(array,low,high,arrayfilename):
    mid=array[low]
    midfilename=arrayfilename[low]
    #pdb.set_trace()
    while low<high:
        while low<high and array[high]>=mid:
            high=high-1 
        array[low]=array[high]
        arrayfilename[low]=arrayfilename[high]
        while low<high and array[low]<=mid:
            low=low+1
        array[high]=array[low]
        arrayfilename[high]=arrayfilename[low]
    array[low]=mid
    arrayfilename[low]=midfilename
    return low
        
def quick_sort(array,low,high,arrayfilename):
    if low<high:
        mid=partion(array,low,high,arrayfilename)
        quick_sort(array,low,mid-1,arrayfilename)
        quick_sort(array,mid+1,high,arrayfilename)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-f', action='store', required=True, dest='file',
                    help='file_name of design result')
    
    inputs=parser.parse_args()
    
    topfile=os.getcwd()+'/'+inputs.file
    filename=[]
    filetop=[]

    result_top=open(topfile,'r') 
    for line in  result_top:
        line=line.strip('\n')
        print "%s"% str(line)
        line=line.split(':')
        filename.append(line[0])
        filetop.append(float(line[6]))
    result_top.close()
    print "%s" %filename
    quick_sort(filetop,0,len(filetop)-1,filename)
    result_top=open(topfile,'r+')
    result_top.read()
    result_top.write('\n')

    result_top.write('\n')
     
    result_top.write('\n')
    result_top.write('\n')
    result_top.write('top rank(below):')
    result_top.write('\n')
    for i in xrange(len(filetop)):
        result_top.write(str(filename[i])+':'+str(filetop[i]))
        result_top.write('\n')

    result_top.close()


if __name__=="__main__":
    main()
