import os
import argparse
import math
from math import fabs

'''def gettopfile(filename)
    filename1=filename.split('.')[0]+'_top.txt'
    if not os.path.exists(filename1):
        result_file=open(filename1,'w')
    else:
        result_file=open(filename1,'r+')
        result_file.read()'''
    
     

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-c', action='store', required=True, dest='chain',
                    help='chain_break is the first ') 
    parser.add_argument('-r', action='store', required=True, dest='remove',
                    help='roma_moveable is the first ') 
    #parser.add_argument('-t', action='store', required=True, dest='deduce',
     #               help='threshold  is the first') 
    parser.add_argument('-f', action='store', required=True, dest='file',
                    help='file_name of design result')
    parser.add_argument('-f1', action='store', required=True, dest='pdbfile',
                    help='pdbfile_name of design result')
    inputs=parser.parse_args()
    

    text_file=os.getcwd()+'/'+inputs.file
    resultfile=os.getcwd()+'/'+inputs.pdbfile
    originalfile=open(text_file) 
    if not os.path.exists(resultfile):
        result_file=open(resultfile,'w')
    else:
        result_file=open(resultfile,'r+')
        result_file.read()
    scoffald_mut=0.0
    scoffald_WT=0.0
    chain_break=0.0
    rama_moveable=0.0
    name=1
    for line in originalfile.readlines():
        if 'Refined' in line and 'chainbreak_score' in line:
            theline=line.split()
            '''for i in xrange(len(theline)):
                print "%s:%s"% (str(i),theline[i])'''
            if float(inputs.chain)>=float(theline[31]) and float(inputs.remove)>=float(theline[34]):
                name=0
                chain_break=float(theline[31])
                rama_moveable=float(theline[34])               
        elif '# * Refined ES (with Ab)' in line and name==0:
            '''for i in xrange(len(theline)):
                print "%s:%s"%(str(i),theline[i])'''
            theline=line.split()
            scoffald_mut=float(theline[7])
            name=2
        elif '# Score12_WT_scaffold'in line and name==2:
            theline=line.split()
            scoffald_WT=float(theline[3])
            #if fabs(scoffald_mut-scoffald_WT)<float(inputs.deduce):
            result_file.write(str(inputs.file))
            result_file.write(':chainbreak_score:'+str(chain_break)+':rama_moveable:'+str(rama_moveable)+':MUT_scaffold:'+str(scoffald_mut)+':WT_scaffold:'+str(scoffald_WT))
            result_file.write('\n')
        else:
            continue
    originalfile.close()
    result_file.close()

if __name__=="__main__":
    print "begin detecting the the result of design"
    main()
    print "detect have done"
