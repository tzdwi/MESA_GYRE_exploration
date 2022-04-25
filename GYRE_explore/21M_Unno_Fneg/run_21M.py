import os
from glob import glob
import numpy as np

if __name__ == "__main__":
    
    #profile_files = glob('../23M_mesa/LOGS_postrsg/profile*.data.GSM')
    profile_files = glob('../../21M_mesa/LOGS_postrsg/profile*.data.GSM') # Now running on pre-RSG profiles
    profile_nums = list(map(int,[s.split('/')[-1].split('.')[0].lstrip('profile') for s in profile_files]))

    profile_min_max = np.percentile(profile_nums,[0,100])
    
    #profiles = np.arange(*profile_min_max,15,dtype=int) 
    profiles = np.arange(*profile_min_max,5,dtype=int)
    
    for n in profiles:
        if f'summary_{n}.h5' in glob('summary*.h5'):
            print(f'already ran profile {n}')
            continue
        with open("postrsg_gyre_template.txt", "r") as text_file:
            gyre_file = text_file.readlines()
            for i,l in enumerate(gyre_file):
                gyre_file[i]=l.replace(r'PROF',str(n))
        with open("postrsg_gyre.in","w") as text_file:
            text_file.write(''.join(gyre_file))
            
        print(n)
            
        os.system('$GYRE_DIR/bin/gyre postrsg_gyre.in')