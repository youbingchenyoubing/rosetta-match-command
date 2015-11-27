import os
import argparse

#usage python getmatch.py -r (rmsd) -clash (intra_clash) -clash1 (inter_clash) -f (file)




def main():
    import shutil
    parser=argparse.ArgumentParser()
    parser.add_argument('-r', action='store', required=True, dest='rmsd',
                    help='rmsd is the first ') 
    '''parser.add_argument('-r1', action='store', required=False, dest='rmsd',
                    help='rmsd is for S')i'''
    parser.add_argument('-clash', action='store', required=True, dest='intra_clash',
                    help='intra_clash is neeed') 
    parser.add_argument('-clash1', action='store', required=True, dest='inter_clash',
                    help='inter_clash is neeed') 
    parser.add_argument('-f', action='store', required=True, dest='text_file',
                    help='text_file is needed')
    inputs=parser.parse_args()
    text_file=os.getcwd()+'/'+inputs.text_file
    originalfile=open(text_file)
    dealfile=open(text_file+'_new','w')
    name=1
    for line in originalfile.readlines():
       # print line 
        theline=line.split()
        '''for i in theline:
            if i=='':
                theline.remove(i)'''
        '''for i in xrange(len(theline)):
            print "%s:%s"% (str(i),theline[i])'''
        if 'filename' in line:
            dealfile.write(line)
        elif '.pdb' in line:
            if 'S' in theline[2]:
               if float(inputs.rmsd)>float(theline[27]):
                   if float(inputs.intra_clash)>float(theline[31]):
                       if float(inputs.inter_clash)>float(theline[32]):
                           dealfile.write(line)
                           name=0
            elif 'C2N_' in theline[2]:
               if float(inputs.rmsd)>float(theline[28]):
                   if float(inputs.intra_clash)>float(theline[31]):
                       if float(inputs.inter_clash)>float(theline[32]):
                           dealfile.write(line)
                           name=0
            elif 'N2C_' in theline[2]:
               if float(inputs.rmsd)>float(theline[29]):
                   if float(inputs.intra_clash)>float(theline[31]):
                       if float(inputs.inter_clash)>float(theline[32]):
                           dealfile.write(line)
                           name=0
            '''elif 'E' in theline[2]:
               if float(inputs.rmsd)>float(theline[29]):
                   if float(inputs.intra_clash)>float(theline[31]):
                       if float(inputs.inter_clash)>float(theline[32]):
                           dealfile.write(line)'''
        elif '*' in line and name==0:
            #if float(inputs.rmsd)>float(theline[28]) or float(inputs.rmsd)>float(theline[29]):
               # if float(inputs.intra_clash)>float(theline[31]):
            dealfile.write(line)
            name=1

      
    originalfile.close()
    dealfile.close()
    shutil.move(text_file+'_new',text_file)
if __name__=="__main__":    
    print "begin translate waiting...."
    main()
    print "convert have done"
