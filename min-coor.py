# usage python min-coor.py 'Prefix' 'Time' 'Nfiles' 'tail_length'
#python min-coor.py ../2D-RG-Inter-C6 10 5 C6

import numpy as np
import sys,os   

prefix=sys.argv[1]
Time=sys.argv[2]
Nfiles=int(sys.argv[3])
tail_length=sys.argv[4]

f_config1 = open("Config1.xvg","a")
f_config2 = open("Config2.xvg","a")
f_config3 = open("Config3.xvg","a")
f_config4 = open("Config4.xvg","a")
f_min = open("min-coor.xvg","a")

# specifying the buffer in the bins
buf_in_RG=0.01 ; # (nm)
buf_in_COOR=0.2 ; # (number)
RG_fold=0.40
RG_unfold=0.80

# Template for .xvg file
f_config1.write(' @ title "Config1 Energy" \n')
f_config1.write(' @ subtitle \"%s\" \n' % tail_length)
f_config1.write(' @ xaxis label "Time (ns)" \n')
f_config1.write(' @ yaxis label "Free energy (kcal/mol)" \n')
f_config1.write(' @ TYPE xy \n')
f_config1.write(' @ view 0.15, 0.15, 1.00, 0.85 \n ')
f_config1.write(' @ legend on \n ')
f_config1.write(' @ legend box on \n ')
f_config1.write(' @ legend loctype view \n ')
f_config1.write(' @ legend 0.78, 0.8 \n ')
f_config1.write(' @ legend length 2 \n ')


f_config2.write(' @ title "Config2 Energy" \n')
f_config2.write(' @ subtitle \"%s\" \n' % tail_length)
f_config2.write(' @ xaxis label "Time (ns)" \n')
f_config2.write(' @ yaxis label "Free energy (kcal/mol)" \n')
f_config2.write(' @ TYPE xy \n')
f_config2.write(' @ view 0.15, 0.15, 1.00, 0.85 \n ')
f_config2.write(' @ legend on \n ')
f_config2.write(' @ legend box on \n ')
f_config2.write(' @ legend loctype view \n ')
f_config2.write(' @ legend 0.78, 0.8 \n ')


f_config3.write(' @ title "Config3 Energy" \n')
f_config3.write(' @ subtitle \"%s\" \n' % tail_length)
f_config3.write(' @ xaxis label "Time (ns)" \n')
f_config3.write(' @ yaxis label "Free energy (kcal/mol)" \n')
f_config3.write(' @ TYPE xy \n')
f_config3.write(' @ view 0.15, 0.15, 1.00, 0.85 \n ')
f_config3.write(' @ legend on \n ')
f_config3.write(' @ legend box on \n ')
f_config3.write(' @ legend loctype view \n ')
f_config3.write(' @ legend 0.78, 0.8 \n ')

f_config4.write(' @ title "Config4 Energy" \n')
f_config4.write(' @ subtitle \"%s\" \n' % tail_length)
f_config4.write(' @ xaxis label "Time (ns)" \n')
f_config4.write(' @ yaxis label "Free energy (kcal/mol)" \n')
f_config4.write(' @ TYPE xy \n')
f_config4.write(' @ view 0.15, 0.15, 1.00, 0.85 \n ')
f_config4.write(' @ legend on \n ')
f_config4.write(' @ legend box on \n ')
f_config4.write(' @ legend loctype view \n ')
f_config4.write(' @ legend 0.78, 0.8 \n ')

f_min.write(' @ title "min-coor" \n')
f_min.write(' @ subtitle \"%s\" \n' % tail_length)
f_min.write(' @ xaxis label "Time (ns)" \n')
f_min.write(' @ yaxis label "Min-coordinate" \n')
f_min.write(' @ TYPE xy \n')
f_min.write(' @ view 0.15, 0.15, 1.00, 0.85 \n ')
f_min.write(' @ legend on \n ')
f_min.write(' @ legend box on \n ')
f_min.write(' @ legend loctype view \n ')
f_min.write(' @ legend 0.78, 0.8 \n ')

for i in range(0,Nfiles):
    filename=prefix+'.'+Time+'ns'+str(i)+'.dat'
    data = np.genfromtxt(filename,skip_header=9,usecols=[0,1,2])
    Nlines=data.shape[0]
    output_time=int(Time)*(i+1)
 
    for j in range(0,Nlines):
          if (data[j,2]==0.0000):
              f_min.write("{0:8.2f} {1:10.6f} {2:10.6f} {3:10.6f}\n".format(output_time,data[j,0],data[j,1],data[j,2]))
              

# Identifying Config 1 energy 
    COORD=np.array([])
    for j in range(0,Nlines):
         if ( (data[j,0] >= RG_fold-buf_in_RG ) and (data[j,0] <= RG_fold+buf_in_RG) and(data[j,1] >= 1-buf_in_COOR) and (data[j,1] <= (1+buf_in_COOR))):
             COORD=np.append(COORD,data[j,2])

    energy=np.amin(COORD)
    f_config1.write("{0:8.2f} {1:10.6f}\n".format(output_time,energy/4.184))

# Identifying Config 2 energy 
    COORD=np.array([])
    for j in range(0,Nlines):
         if ( (data[j,0] >= RG_fold-buf_in_RG ) and (data[j,0] <= RG_fold+buf_in_RG) and(data[j,1] >= 3-buf_in_COOR) and (data[j,1] <= 3+buf_in_COOR)):
             COORD=np.append(COORD,data[j,2])

    energy=np.amin(COORD)
    f_config2.write("{0:8.2f} {1:10.6f}\n".format(output_time,energy/4.184))


# Identifying Config 3 energy 
    COORD=np.array([])
    for j in range(0,Nlines):
         if ( (data[j,0] >= RG_fold-buf_in_RG ) and (data[j,0] <= RG_fold+buf_in_RG) and(data[j,1] >= 2-buf_in_COOR) and (data[j,1] <= 2+buf_in_COOR)):
             COORD=np.append(COORD,data[j,2])

    energy=np.amin(COORD)
    f_config3.write("{0:8.2f} {1:10.6f}\n".format(output_time,energy/4.184))


# Identifying Config 4 energy 
    COORD=np.array([])
    for j in range(0,Nlines):
         if ( (data[j,0] >= RG_unfold-buf_in_RG ) and (data[j,0] <= RG_unfold+buf_in_RG) and(data[j,1] >= 2-buf_in_COOR) and (data[j,1] <= 2+buf_in_COOR)):
             COORD=np.append(COORD,data[j,2])

    energy=np.amin(COORD)
    f_config4.write("{0:8.2f} {1:10.6f}\n".format(output_time,energy/4.184))

f_min.close()
f_config1.close()
f_config2.close()
f_config3.close()
f_config4.close()

exit()
