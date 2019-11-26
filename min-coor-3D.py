# usage python min-coor.py 'Prefix' 'Time' 'Nfiles' 'tail_length'
#python min-coor.py ../3D-RG-Inter-Intra-C6 20 5 C6

import numpy as np
import sys,os   

prefix=sys.argv[1]
Time=sys.argv[2]
Nfiles=int(sys.argv[3])
tail_length=sys.argv[4]

# Removing existing file
if os.path.exists("./Config.xvg"):
    os.remove("./Config.xvg")
if os.path.exists("./min-coor.xvg"):
    os.remove("./min-coor.xvg")


f_config = open("Config.xvg","a")
f_min = open("min-coor.xvg","a")

# specifying the buffer in the bins
buf_in_RG=0.01 ; # (nm)
buf_in_COOR=0.2 ; # (number)
RG_fold=0.40
RG_unfold=0.80

# Template for .xvg file with multiple columns
f_config.write(' @ title "Energy of Configurations" \n')
f_config.write(' @ subtitle \"%s\" \n' % tail_length)
f_config.write(' @ xaxis label "Time (ns)" \n')
f_config.write(' @ yaxis label "Free Energy (kcal/mol)" \n')
f_config.write(' @ TYPE xy \n')
f_config.write(' @ view 0.15, 0.15, 1.00, 0.85 \n')
f_config.write(' @ legend on \n')
f_config.write(' @ legend box on \n')
f_config.write(' @ legend loctype view \n')
f_config.write(' @ legend 0.78, 0.8 \n')
f_config.write(' @ legend length 2 \n')
for i in range(0,4):
     j=i+1
     f_config.write(' @ s{} legend \"Config{}\N\" \n'.format(i,j))
# Template for .xvg file with multiple columns

f_min.write(' @ title "min-coor" \n')
f_min.write(' @ subtitle \"%s\" \n' % tail_length)
f_min.write(' @ xaxis label "Time (ns)" \n')
f_min.write(' @ yaxis label "Min-coordinate" \n')
f_min.write(' @ TYPE xy \n')
f_min.write(' @ view 0.15, 0.15, 1.00, 0.85 \n')
f_min.write(' @ legend on \n')
f_min.write(' @ legend box on \n')
f_min.write(' @ legend loctype view \n')
f_min.write(' @ legend 0.78, 0.8 \n')

# Modifying the 3D-free-output files
for i in range(0,Nfiles):
    filename=prefix+'.'+Time+'ns'+str(i)+'.dat'
    data = np.genfromtxt(filename,skip_header=13,usecols=[0,1,2,3])
    Nlines=data.shape[0]
    mod_file=prefix+'-Mod'+'.'+Time+'ns'+str(i)+'.dat'
    f=open(mod_file, "a")

    for i in range(0,Nlines):
      if (data[i,0] != 2.00000):
         np.savetxt(f,data[i,:],newline=' ')
         f.write("\n")
      else:
         np.savetxt(f,data[i,:],newline=' ')
         f.write("\n")
         f.write("\n")
    f.close()



for i in range(0,Nfiles):
    filename=prefix+'-Mod'+'.'+Time+'ns'+str(i)+'.dat'
    Nlines=data.shape[0]
    output_time=int(Time)*(i+1)
 
    for j in range(0,Nlines):
          if (data[j,3]==0.0000):
              f_min.write("{0:8.2f} {1:10.6f} {2:10.6f} {3:10.6f} {4:10.6f}\n".format(output_time,data[j,0],data[j,1],data[j,2]),data[j,3])
              

# Identifying Config 1 energy 
    COORD=np.array([])
    for j in range(0,Nlines):
         if ( (data[j,0] >= RG_fold-buf_in_RG ) and (data[j,0] <= RG_fold+buf_in_RG) and (data[j,1] >= 1-buf_in_COOR) and (data[j,1] <= 1+buf_in_COOR) and (data[j,2] >= 2-buf_in_COOR) and (data[j,2] <= 2+buf_in_COOR) ):
             COORD=np.append(COORD,data[j,3])

    energy=np.amin(COORD)
    f_config.write("{0:8.2f} {1:10.6f}".format(output_time,energy/4.184))

# Identifying Config 2 energy 
    COORD=np.array([])
    for j in range(0,Nlines):
         if ( (data[j,0] >= RG_fold-buf_in_RG ) and (data[j,0] <= RG_fold+buf_in_RG) and (data[j,1] >= 3-buf_in_COOR) and (data[j,1] <= 3+buf_in_COOR) and (data[j,2] >= 0-buf_in_COOR) and (data[j,2] <= 0+buf_in_COOR)  ):
             COORD=np.append(COORD,data[j,3])

    energy=np.amin(COORD)
    f_config.write("{0:10.6f}".format(energy/4.184))


# Identifying Config 3 energy 
    COORD=np.array([])
    for j in range(0,Nlines):
         if ( (data[j,0] >= RG_fold-buf_in_RG ) and (data[j,0] <= RG_fold+buf_in_RG) and(data[j,1] >= 2-buf_in_COOR) and (data[j,1] <= 2+buf_in_COOR) and(data[j,2] >= 1-buf_in_COOR) and (data[j,2] <= 1+buf_in_COOR)):
             COORD=np.append(COORD,data[j,3])

    energy=np.amin(COORD)
    f_config.write("{0:10.6f}".format(energy/4.184))


# Identifying Config 4 energy 
    COORD=np.array([])
    for j in range(0,Nlines):
         if ( (data[j,0] >= RG_unfold-buf_in_RG ) and (data[j,0] <= RG_unfold+buf_in_RG) and(data[j,1] >= 2-buf_in_COOR) and (data[j,1] <= 2+buf_in_COOR) and(data[j,2] >= 0-buf_in_COOR) and (data[j,2] <= 0+buf_in_COOR)):
             COORD=np.append(COORD,data[j,3])

    energy=np.amin(COORD)
    f_config.write("{0:10.6f}\n".format(energy/4.184))

f_min.close()
f_config.close()

exit()
